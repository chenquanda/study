
## 一、Java（SpringBoot 为主）

### 必装（一次性搞定基础环境）
1. **Extension Pack for Java（微软官方）**
   - 包含：Language Support for Java、Debugger for Java、Maven for Java、Test Runner for Java、Project Manager for Java、IntelliCode
   - 作用：代码补全、语法检查、调试、Maven 管理、项目结构管理


2. **Spring Boot Extension Pack（VMware 官方）**
   - 包含：Spring Boot Tools、Spring Initializr、Spring Boot Dashboard
   - 作用：一键生成 SpringBoot 项目、Bean/路由跳转、实时应用信息、启停/调试仪表盘


### 强烈推荐
3. **Lombok Annotations Support**
   - 识别 `@Data/@Slf4j` 等，消除“未定义方法”报错


4. **XML Language Support by Red Hat**
   - MyBatis XML、Spring 配置文件高亮与校验

5. **SonarLint**
   - 实时代码质量/安全检查，减少 bug 和坏味道

6. **GitLens**
   - 行级 Git 历史、作者、提交信息，追溯代码变更


---

## 二、Go 开发

### 必装
1. **Go（Google 官方，golang.go）**
   - 语法高亮、智能补全（gopls）、代码导航、调试（Delve）、测试、格式化


### 强烈推荐
2. **Error Lens**
   - 错误直接显示在行尾，不用切 Problems 面板

3. **Golang Postfix Completion**
   - `err.if` → `if err != nil`；`slice.for` → range 循环，省大量模板代码

4. **Paste JSON as Code**
   - 复制 JSON → 右键生成带 tag 的 Go struct，非常方便

5. **Code Runner**
   - 一键运行当前 Go 文件/脚本，无需配置 launch.json

---

## 三、Python（FastAPI 为主）

### 必装
1. **Python（微软官方，ms-python.python）**
   - 解释器选择、虚拟环境、调试、Lint、基础补全


2. **Pylance（微软官方，ms-python.vscode-pylance）**
   - 比默认语言服务器更快、更准；**强类型检查**（特别适合 FastAPI 类型注解）、智能补全、参数提示


3. **FastAPI（FastAPI Labs 官方）**
   - 侧边栏展示所有路由、一键跳转、搜索路由、CodeLens 导航、部署与日志


### 强烈推荐
4. **FastAPI Snippets**
   - 快速插入 `@app.get/post/put/delete`、`Depends`、`HTTPException` 等模板

5. **REST Client**
   - 写 `.http` 文件直接测试 FastAPI 接口，不用 Postman

6. **Black Formatter**
   - 保存时自动格式化代码，统一团队风格

7. **Flake8**
   - 实时代码检查，配合 Black 做“格式化+质量”双保障

8. **Poetry Integration**
   - 可视化管理依赖，自动识别虚拟环境

---

## 四、通用全栈辅助（三类开发都建议装）
- **GitLens**：行级 Git 信息，谁改的、何时改
- **Error Lens**：所有语言错误行内显示
- **Code Runner**：一键运行多种语言脚本
- **Docker**：容器化项目管理（三类项目都常用）


---
