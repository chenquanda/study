# Demo - 多语言学习项目

> 个人学习 Java / Python / Go / C++ 的代码仓库，包含各语言子项目和笔记。

## 项目结构

```
demo/
├── java/          # Java 学习项目
├── python/        # Python 学习项目（uv 管理）
├── go/            # Go 学习项目（Go Modules）
├── cpp/           # C/C++ 学习项目
└── 笔记/          # 学习笔记
    └── git/       # Git 相关笔记
```

## 环境要求

| 工具 | 版本 | 说明 |
|------|------|------|
| Git | >= 2.40 | 版本控制 |
| Python | 3.11+ | python/ 子项目 |
| uv | 最新版 | Python 包管理（替代 pip/venv） |
| Go | >= 1.22 | go/ 子项目 |
| Java (JDK) | >= 17 | java/ 子项目（按需安装） |
| C/C++ 编译器 | GCC/MSVC/Clang | cpp/ 子项目（按需安装） |

## 新电脑环境搭建

### 1. 安装 Git 并配置 SSH

```bash
# 安装 Git 后，生成 SSH 密钥
ssh-keygen -t ed25519 -C "你的邮箱@example.com"

# 查看公钥，添加到 GitHub → Settings → SSH and GPG keys
cat ~/.ssh/id_ed25519.pub

# 测试连接
ssh -T git@github.com
```

### 2. 克隆项目

```bash
git clone git@github.com:你的用户名/demo.git
cd demo
```

### 3. Python 环境搭建

```bash
# 安装 uv（Windows PowerShell）
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

# 进入 python 目录
cd python

# 创建虚拟环境并安装依赖
uv sync

# 运行
uv run main.py
```

> **注意**：`uv sync` 会根据 `pyproject.toml` 自动创建 `.venv/` 和安装依赖。
> `uv.lock` 和 `.python-version` 已在 `.gitignore` 中忽略，无需关心。

### 4. Go 环境搭建

```bash
# 安装 Go：https://go.dev/dl/
# 安装后验证
go version

# Go Modules 会自动下载依赖
cd go/test
go run .
```

> **注意**：`go/bin/` 和 `go/pkg/` 是本地缓存目录，已通过 `.gitignore` 忽略。
> 每个子项目的 `go.mod` 和 `go.sum` 已纳入版本控制，换电脑后 `go mod download` 即可恢复依赖。

### 5. Java 环境搭建

```bash
# 安装 JDK 17+：https://adoptium.net/
# 验证
java -version
javac -version

# 构建（如果用 Maven）
cd java/xxx
mvn clean install

# 构建（如果用 Gradle）
cd java/xxx
./gradlew build        # Linux/Mac
gradlew.bat build      # Windows
```

### 6. C/C++ 环境搭建

```bash
# Windows: 安装 Visual Studio Build Tools 或 MinGW
# Mac: xcode-select --install
# Linux: sudo apt install build-essential

# 验证
gcc --version
```

## 注意事项

### 关于 .gitignore

根目录的 `.gitignore` 覆盖所有子项目，已包含：
- Python、Java/Maven/Gradle、Go、C/C++、Node.js、Rust 的忽略规则
- 数据科学相关的大文件（数据集、模型权重等）
- 各类 IDE 配置（IDEA、VSCode、GoLand 等）
- 操作系统临时文件

如果某个子项目有特殊忽略需求，可以在子项目目录下再添加 `.gitignore`。

### 关于 uv（Python 包管理）

| 命令 | 说明 |
|------|------|
| `uv init` | 初始化新项目 |
| `uv add <包名>` | 添加依赖（自动更新 pyproject.toml） |
| `uv remove <包名>` | 移除依赖 |
| `uv sync` | 同步安装所有依赖 |
| `uv run <脚本>` | 在虚拟环境中运行 |
| `uv python list` | 查看可用 Python 版本 |
| `uv python install 3.12` | 安装指定 Python 版本 |

### 关于 Go Modules

| 命令 | 说明 |
|------|------|
| `go mod init <模块名>` | 初始化新模块 |
| `go get <包@版本>` | 添加依赖 |
| `go mod tidy` | 清理未使用的依赖 |
| `go mod download` | 下载所有依赖到本地缓存 |

### 关于 Git 操作

日常流程：`git pull` → 修改代码 → `git add .` → `git commit -m "说明"` → `git push`

详细笔记见 [笔记/git/Git-项目初始化与推送.md](笔记/git/Git-项目初始化与推送.md)
