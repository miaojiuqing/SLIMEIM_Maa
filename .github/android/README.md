# Android APK 打包说明

对齐 `overflow65537/MAA_Punish` / `miaojiuqing/MAA_bbb` 的写法：CI 用
[Aliothmoon/MaaFwApp](https://github.com/Aliothmoon/MaaFwApp)（固定 commit）把我们
的 Project Interface 资源 + Python agent 打成 APK，放在 GitHub Release 里，
并在正式版时上传到 MirrorChyan。

## 产物

| 项 | 值 |
|---|---|
| workflow job | `install.yml` → `android`（名称 `Build Android APK`） |
| artifact | `MaaSLIMEIM-android` |
| 文件名 | `MaaSLIMEIM-android-<tag>.apk`（没有签名 secrets 时是 `-debug.apk`） |
| 包名 | `com.maafw.mq.slm`（`patch_maafwapp.py` 的 base + `pi-profile.yaml` 的 `app.id`） |
| 版本 | 由 `meta` job 算出的 tag，写进 APK 内 `interface.json` 的 `version` |

只有 `refs/tags/v*` 触发的正式版才会进 Release；分支/PR 只产出 artifact。

## 需要配置的 Repository secrets

| Secret | 内容 |
|---|---|
| `ANDROID_KEYSTORE_BASE64` | keystore 文件的 base64（**单行**） |
| `ANDROID_KEYSTORE_PASSWORD` | store password |
| `ANDROID_KEY_ALIAS` | 别名 |
| `ANDROID_KEY_PASSWORD` | key password（PKCS12 下必须与 store 相同） |
| `ANDROID_MIRRORCHYANUPLOADTOKEN` | MirrorChyan 上传 token（与桌面端那个可能不是同一个） |

行为：**一个都没配** → 走 `assembleDebug`，文件名带 `-debug`；**只配了 1~3 个** →
直接失败（故意的，防止"以为签了其实没签"）；**4 个都配** → 解码到
`$RUNNER_TEMP/android-release.jks`、走 `assembleRelease`。

签名步骤里有一段前置校验（`keytool -list` 验密码 + 验别名），
把 AGP 那种 `KeytoolException: ... EOFException` 的模糊报错提前成 2 秒的明确归因。

## 生成 keystore

```powershell
# 本机若无 JDK，可用 Android Studio / PyCharm 自带的 jbr
$keytool = "<...>\jbr\bin\keytool.exe"
$pw = "<自己定的密码>"

& $keytool -genkeypair -v `
  -keystore "D:\vscode\keys\slimeim-release.jks" `
  -alias slm -keyalg RSA -keysize 4096 -validity 10000 `
  -storetype PKCS12 -storepass $pw -keypass $pw `
  -dname "CN=SLIMEIM_Maa, OU=SLIMEIM_Maa, O=miaojiuqing, L=Fuzhou, ST=Fujian, C=CN"

# 自检：大小应 4KB 上下，前 4 字节是 30 82（PKCS12）
& $keytool -list -keystore "D:\vscode\keys\slimeim-release.jks" -storepass $pw

# base64 必须单行；不要用 certutil -encode（它会加头尾和换行）
[Convert]::ToBase64String([IO.File]::ReadAllBytes("D:\vscode\keys\slimeim-release.jks")) |
  Set-Content -NoNewline -Encoding ascii "D:\vscode\keys\slimeim-release.jks.b64"
```

坑：

- 别把**密码文本**存成 `.jks` 文件（AGP 会报 `java.io.EOFException`），keystore 一定 4KB 上下；
- PKCS12 下 store 密码 = key 密码，想区分就得用 `-storetype JKS`；
- 别名要和 `ANDROID_KEY_ALIAS` 逐字一致（区分大小写）；
- base64 要单行，粘贴 secret 前先清空旧值；
- **keystore 一旦发过版就永远不能换**（换了老用户必须卸载重装），离线备份两份；
- debug 与 release 的 `applicationId` 相同、只有签名不同，先装了 debug 包再装 release 包会签名冲突，定好包名后统一用 release 包测试。

## MirrorChyan

`android_mirrorchyan` job 只在「正式版 + 用的是 release 签名 + 配了 rid」时运行，
把 APK 以 `os: android` 传到 `ANDROID_RID`。

`ANDROID_RID` 定义在 `install.yml` 顶部的 workflow `env` 里，当前值 **`SLIMEIM_Maa_exec`**
（MirrorChyan 后台给的安卓 rid，与桌面端的 `SLIMEIM_Maa` 是两个不同的资源）：

- 打包时会把 APK 内 `interface.json` 的 `mirrorchyan_rid` 改成它 —— MaaFwApp 的更新检查
  读的是 PI 里的 rid、请求固定带 `os=android` 且要求返回 APK 链接，不改的话 app 会去查
  桌面 rid 从而拿不到 android 包；
- 留空时不会改 rid，且上传 job 自动跳过（写死前先确认后台确实有这个 rid）。

上传用的 token 是 secret `ANDROID_MIRRORCHYANUPLOADTOKEN`（与桌面端的
`MirrorChyanUploadToken` 不是同一个，别填错）。

桌面端（`mirrorchyan_release.yml`、`mirrorchyan_release_note.yml`）用的仍是
`SLIMEIM_Maa` + `MirrorChyanUploadToken`，不要动；Android 的 PI 资源 zip 已经不再发布
（`install` 矩阵与 `mirrorchyan_release.yml` 里的 `android` 都去掉了，由 APK 取代）。

## 本地模拟

`.github/android/pi-profile.yaml` 是 MaaFwApp 的打包配方，CI 里直接由 MaaFwApp 读取；
只有 CI 环境（Android SDK + Gradle）才能真正出 APK，本地不必复现。
