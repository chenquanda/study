# Maven 环境安装与配置操作文档
## 📌 前置准备
**必须先安装 JDK 环境**，Maven 依赖于 Java 运行。
*   打开命令提示符（CMD），输入 `java -version`。
*   如果能正确显示 Java 版本号（建议 JDK 8 或 JDK 11 及以上），则说明已具备条件；如果提示“不是内部或外部命令”，请先安装 JDK 并配置环境变量。
---
## 第一步：下载 Maven 安装包
1. 访问 Maven 官方下载页面：[https://maven.apache.org/download.cgi](https://maven.apache.org/download.cgi)
2. 找到 **Files** 区域，下载 **Binary zip archive** （例如：`apache-maven-3.9.6-bin.zip`）。
   *(注：不要下载 Source zip archive，那是源码，不需要编译)*
---
## 第二步：解压并安装
Maven 是“绿色免安装”软件，解压即安装。
1. 找到下载好的 `.zip` 压缩包。
2. **建议解压路径**：将其解压到一个**没有中文、没有空格、没有特殊字符**的目录下。
   * ❌ 错误示例：`D:\我的软件\apache-maven-3.9.6`
   * ✅ 正确示例：`D:\Develop\apache-maven-3.9.6`
3. 解压后，打开该文件夹，确认内部结构如下（重点确认有 `bin`、`conf`、`boot` 等文件夹）：
   ```text
   D:\Develop\apache-maven-3.9.6
   ├── bin/
   ├── boot/
   ├── conf/
   ├── lib/
   └── README.txt
   ```
---
## 第三步：配置系统环境变量
1. **打开环境变量设置**：
   * 右键点击桌面上的“此电脑” -> 选择“属性”。
   * 点击右侧或底部的“高级系统设置”。
   * 在弹出的窗口中，点击下方的 **“环境变量”** 按钮。
2. **新建 MAVEN_HOME 变量**：
   * 在“系统变量”区域，点击 **“新建”**。
   * 变量名：`MAVEN_HOME`
   * 变量值：填入你的 Maven 解压路径（例如 `D:\Develop\apache-maven-3.9.6`）
   * 点击“确定”。
3. **编辑 Path 变量**：
   * 在“系统变量”中找到名为 `Path` 的变量，双击打开（或选中后点击“编辑”）。
   * 点击 **“新建”**，输入：`%MAVEN_HOME%\bin`
   * 点击“确定”，然后一路点击“确定”关闭所有环境变量窗口。
---
## 第四步：验证安装是否成功
1. 打开一个新的 **命令提示符（CMD）** 窗口。（**注意：** 必须是重新打开一个新的，之前打开的 CMD 不会刷新环境变量）
2. 输入以下命令并回车：
   ```cmd
   mvn -v
   ```
3. 如果配置正确，将会输出 Maven 的版本号、Java 版本及操作系统信息，类似如下内容：
   ```text
   Apache Maven 3.9.6 (bc0240f3c744dd6b6ec2920b3cd08dcc295161ae)
   Maven home: D:\Develop\apache-maven-3.9.6
   Java version: 1.8.0_361, vendor: Oracle Corporation, runtime: C:\Program Files\Java\jdk1.8.0_361\jre
   ...
   ```
---
## 第五步：（强烈建议）修改 Maven 配置与本地仓库路径
默认情况下，Maven 下载的依赖包会存放在 `C:\Users\你的用户名\.m2\repository`，随着时间推移会占用大量 C 盘空间。建议将其转移到其他盘。
1. 进入 Maven 解压目录下的 `conf` 文件夹（例如：`D:\Develop\apache-maven-3.9.6\conf`）。
2. 用记事本或 VS Code 打开 `settings.xml` 文件。
3. **修改本地仓库路径**：
   找到大约第 53 行的注释掉的 `<localRepository>` 标签，在它下方添加一行：
   ```xml
   <!-- 配置本地仓库路径，路径可以自己定 -->
   <localRepository>D:\Develop\maven_repository</localRepository>
   ```
4. **配置阿里云镜像（加速下载）**：
   找到 `<mirrors>` 标签（大约在 146 行），在 `<mirrors>` 和 `</mirrors>` 之间插入以下配置：
   
   ```xml
   <mirror>
       <id>aliyunmaven</id>
       <mirrorOf>*</mirrorOf>
       <name>阿里云公共仓库</name>
       <url>https://maven.aliyun.com/repository/public</url>
   </mirror>
   ```
5. 保存并关闭 `settings.xml` 文件。
---
## 第六步：在 IDEA 中配置 Maven
如果你使用 IntelliJ IDEA 进行开发，需要将 IDEA 关联到我们刚刚安装的 Maven：
1. 打开 IDEA，点击 `File` -> `Settings` (Mac 系统为 `IntelliJ IDEA` -> `Preferences`)。
2. 在左侧菜单找到 `Build, Execution, Deployment` -> `Build Tools` -> `Maven`。
3. **Maven home path**：点击右侧文件夹图标，选择你刚才解压的 Maven 目录（`D:\Develop\apache-maven-3.9.6`）。
4. **User settings file**：勾选 Override，然后选择刚才修改过的 `settings.xml` 文件（`D:\Develop\apache-maven-3.9.6\conf\settings.xml`）。
5. **Local repository**：勾选 Override，它会自动读取你在 `settings.xml` 中配置的路径（`D:\Develop\maven_repository`）。
6. 点击 `Apply` 和 `OK`。
---
## 附：macOS / Linux 系统简略步骤
1. 下载压缩包或使用 Homebrew：`brew install maven`
2. 解压到 `/usr/local/` 下：`tar -zxvf apache-maven-3.9.6-bin.tar.gz -C /usr/local/`
3. 编辑环境变量文件：`vim ~/.zshrc` （或 `~/.bash_profile`）
4. 在文件末尾追加：
   ```bash
   export MAVEN_HOME=/usr/local/apache-maven-3.9.6
   export PATH=$MAVEN_HOME/bin:$PATH
   ```
5. 刷新配置：`source ~/.zshrc`
6. 后续修改 `settings.xml` 和配置 IDEA 的步骤与 Windows 完全一致。
