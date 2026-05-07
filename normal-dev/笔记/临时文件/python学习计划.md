

## 📚 完整Python Web开发学习路线

### 第一阶段：Python核心基础强化（2-3周）
> 你已有基础语法知识，此阶段快速过一遍文档，重点查漏补缺

| 模块 | 核心内容 | 推荐文档 |
|------|----------|----------|
| 数据结构 | 列表/字典/集合/元组的方法与高级用法 | [Python官方数据结构文档](https://docs.python.org/3/tutorial/datastructures.html) |
| 函数进阶 | 参数类型(`*args`/`**kwargs`)、作用域、闭包 | [Python官方函数定义文档](https://docs.python.org/3/tutorial/controlflow.html#defining-functions) |
| 面向对象 | 类、继承、魔术方法、属性装饰器 | [Python官方类文档](https://docs.python.org/3/tutorial/classes.html) |
| 异常处理 | try/except/finally、自定义异常、上下文管理器 | [Python官方异常文档](https://docs.python.org/3/tutorial/errors.html) |
| 迭代器与生成器 | yield、迭代协议、生成器表达式 | [Python官方迭代器文档](https://docs.python.org/3/tutorial/classes.html#iterators) |
| 装饰器 | 函数装饰器、类装饰器、functools.wraps | [Python官方装饰器PEP318](https://peps.python.org/pep-0318/) |

**动手练习：** 每学完一个模块，在本地写代码验证，不依赖视频教程，直接啃文档中的例子。


### 第二阶段：Web开发前置知识（2-3周）
> Web开发运行在互联网之上，必须先理解底层协议

| 模块 | 核心内容 | 推荐文档/资源 |
|------|----------|---------------|
| HTTP协议 | 请求/响应模型、方法(GET/POST/PUT/DELETE)、状态码、Header、Cookie | [MDN HTTP文档](https://developer.mozilla.org/docs/Web/HTTP) |
| URL与路由 | URL结构、查询参数、路径参数、RESTful设计 | [MDN URI文档](https://developer.mozilla.org/docs/Glossary/URI) |
| JSON/XML | 数据序列化与反序列化 | Python内置`json`模块文档 |
| 网络基础 | TCP/IP、端口、Socket编程概念 | [Python socket文档](https://docs.python.org/3/library/socket.html) |
| 前端基础 | HTML/CSS/JavaScript基本认知（能看懂即可） | [MDN Web入门](https://developer.mozilla.org/docs/Learn/Getting_started_with_the_web) |
| 数据库基础 | SQL语言、关系型数据库概念 | [SQLite官方文档](https://www.sqlite.org/docs.html) 入门 |

**重点：** 这一阶段的核心是弄懂"浏览器输入URL后发生了什么"，这会让你后续学习框架时事半功倍。


### 第三阶段：数据库与ORM（2-3周）

| 模块 | 核心内容 | 推荐文档 |
|------|----------|----------|
| SQL深入 | 表设计、索引、外键、JOIN查询、聚合函数 | [SQLite SQL文档](https://www.sqlite.org/lang.html) |
| SQLAlchemy Core | 引擎、连接池、元数据、表反射、SQL表达式 | [SQLAlchemy Core文档](https://docs.sqlalchemy.org/en/20/core/) |
| SQLAlchemy ORM | 模型定义、关系映射、会话管理、查询构建 | [SQLAlchemy ORM文档](https://docs.sqlalchemy.org/en/20/orm/) |
| Alembic | 数据库迁移管理 | [Alembic官方文档](https://alembic.sqlalchemy.org/) |
| PostgreSQL | 安装配置、psycopg2驱动、JSON字段、全文搜索 | [PostgreSQL官方文档](https://www.postgresql.org/docs/) |

**实战练习：**
1. 用SQLAlchemy设计一个博客系统的数据模型（用户、文章、评论、标签）
2. 用Alembic管理表结构的变更


### 第四阶段：首个Web框架——Flask入门（3-4周）
> **Flask是最适合文档学习的框架**，核心非常精简，完全可以通过阅读官方文档掌握

| 模块 | 核心内容 | 推荐文档 |
|------|----------|----------|
| Flask核心 | 应用工厂、路由、请求/响应对象、视图函数 | [Flask官方快速入门](https://flask.palletsprojects.com/en/stable/quickstart/) |
| 模板渲染 | Jinja2模板语法、模板继承、过滤器、宏 | [Jinja2文档](https://jinja.palletsprojects.com/) |
| 表单处理 | WTForms、CSRF保护、验证器 | [WTForms文档](https://wtforms.readthedocs.io/) |
| 数据库集成 | Flask-SQLAlchemy扩展 | [Flask-SQLAlchemy文档](https://flask-sqlalchemy.palletsprojects.com/) |
| 用户认证 | Flask-Login、session管理、密码哈希 | [Flask-Login文档](https://flask-login.readthedocs.io/) |
| 测试 | pytest、Flask测试客户端、fixture | [Flask测试文档](https://flask.palletsprojects.com/en/stable/testing/) |
| 部署 | Gunicorn、环境变量、生产配置 | [Flask部署文档](https://flask.palletsprojects.com/en/stable/deploying/) |

**学习方法：**
- 完整阅读Flask官方教程（Tutorial），它一步步带你构建一个博客应用
- 然后将这个博客改造为自己的项目（如记账应用、Todo List）


### 第五阶段：全栈框架——Django（4-6周）
> Django"大而全"，文档极其完善，是学习企业级Web开发的最佳选择

| 模块 | 核心内容 | 推荐文档 |
|------|----------|----------|
| Django入门 | 项目结构、MTV模式、URL分发、设置文件 | [Django官方教程](https://docs.djangoproject.com/en/stable/intro/tutorial01/)（7个part） |
| 模型层 | ORM、查询集、关联、聚合、自定义管理器 | [Django模型文档](https://docs.djangoproject.com/en/stable/topics/db/models/) |
| 视图层 | 函数视图、类视图、通用视图、Mixins | [Django视图文档](https://docs.djangoproject.com/en/stable/topics/http/views/) |
| 模板层 | DTL语法、模板标签、自定义标签与过滤器 | [Django模板文档](https://docs.djangoproject.com/en/stable/topics/templates/) |
| 表单 | Form API、ModelForm、验证、Widgets | [Django表单文档](https://docs.djangoproject.com/en/stable/topics/forms/) |
| 用户认证 | 内置User模型、权限、登录/注册/密码重置 | [Django认证文档](https://docs.djangoproject.com/en/stable/topics/auth/) |
| Admin后台 | 自定义ModelAdmin、内联、搜索/过滤 | [Django Admin文档](https://docs.djangoproject.com/en/stable/ref/contrib/admin/) |
| 中间件 | 请求/响应处理链、自定义中间件 | [Django中间件文档](https://docs.djangoproject.com/en/stable/topics/http/middleware/) |
| 信号 | 内置信号、自定义信号、解耦设计 | [Django信号文档](https://docs.djangoproject.com/en/stable/topics/signals/) |
| 测试 | TestCase、Client、覆盖度 | [Django测试文档](https://docs.djangoproject.com/en/stable/topics/testing/) |
| 部署 | WSGI/ASGI、静态文件、安全清单 | [Django部署文档](https://docs.djangoproject.com/en/stable/howto/deployment/) |

**学习方法：**
1. 先完整跟做官方7个part的Polls教程
2. 再完整阅读"Topics"类别下的所有文档
3. 构建一个复杂项目（如电商后台、社交平台）巩固


### 第六阶段：现代异步框架——FastAPI（3-4周）
> 现代化、高性能、自动生成API文档，2024-2025年最热门的Python Web框架

| 模块 | 核心内容 | 推荐文档 |
|------|----------|----------|
| FastAPI核心 | 路径操作、查询参数、请求体、类型提示 | [FastAPI官方教程](https://fastapi.tiangolo.com/tutorial/) |
| Pydantic | 数据验证、模型定义、配置管理 | [Pydantic v2文档](https://docs.pydantic.dev/latest/) |
| 依赖注入 | Depends、可复用的依赖、全局依赖 | [FastAPI依赖文档](https://fastapi.tiangolo.com/tutorial/dependencies/) |
| 数据库 | SQLAlchemy异步、async/await模式 | [FastAPI SQL文档](https://fastapi.tiangolo.com/tutorial/sql-databases/) |
| 认证 | OAuth2、JWT、API Key | [FastAPI安全文档](https://fastapi.tiangolo.com/tutorial/security/) |
| 中间件与CORS | 自定义中间件、跨域配置 | [FastAPI中间件文档](https://fastapi.tiangolo.com/tutorial/middleware/) |
| 后台任务 | BackgroundTasks、Celery集成 | [FastAPI后台任务文档](https://fastapi.tiangolo.com/tutorial/background-tasks/) |
| 测试 | TestClient、异步测试、mock | [FastAPI测试文档](https://fastapi.tiangolo.com/tutorial/testing/) |
| WebSocket | 实时通信、连接管理 | [FastAPI WebSocket文档](https://fastapi.tiangolo.com/advanced/websockets/) |

**学习方法：**
- FastAPI的文档是业界公认的最佳文档之一，直接从头到尾阅读Tutorial部分
- 将之前在Flask或Django中的项目用FastAPI重写一遍


### 第七阶段：工程化与专家技能（持续学习）

| 模块 | 核心内容 | 推荐文档 |
|------|----------|----------|
| 异步编程 | asyncio、事件循环、协程、任务 | [Python asyncio文档](https://docs.python.org/3/library/asyncio.html) |
| 缓存 | Redis使用、缓存策略、缓存失效 | [redis-py文档](https://redis-py.readthedocs.io/) |
| 消息队列 | Celery、RabbitMQ/Redis作为broker | [Celery文档](https://docs.celeryq.dev/) |
| Docker | 容器化、Dockerfile、docker-compose | [Docker官方文档](https://docs.docker.com/) |
| Web服务器 | Nginx反向代理、Gunicorn配置 | [Nginx文档](https://nginx.org/en/docs/)、[Gunicorn文档](https://docs.gunicorn.org/) |
| CI/CD | GitHub Actions、自动化测试与部署 | [GitHub Actions文档](https://docs.github.com/en/actions) |
| 安全 | OWASP Top 10、SQL注入防范、XSS/CSRF防护 | [OWASP文档](https://owasp.org/) |
| 性能优化 | 数据库查询优化、缓存策略、性能分析 | Django/Flask各自性能文档 |
| 系统设计 | REST API设计规范、微服务架构基础 | [OpenAPI规范](https://spec.openapis.org/oas/latest.html) |
| 源码阅读 | 阅读Flask/Django/FastAPI核心源码 | GitHub仓库源码 |


## 🎯 推荐学习节奏

```
月份1-2：  Python核心强化 + HTTP/数据库基础
月份3-4：  SQLAlchemy + Flask完整学习 + 小项目
月份5-6：  Django深度学习 + 中型项目
月份7-8：  FastAPI + 异步编程 + API项目
月份9-12： 工程化技能(Docker/Celery/Redis/Nginx) + 综合大项目 + 源码阅读
```

## 📖 文档学习的最佳实践

1. **先读Tutorial再读Reference：** 框架文档通常分为Tutorial（教程）和Reference（参考），先跟教程走一遍，再精读参考文档
2. **边读边写代码：** 每个代码示例都要亲自敲一遍，不要复制粘贴
3. **阅读源码：** 当文档不够清晰时，直接跳入框架源码（Flask的源码非常易读）
4. **做好笔记：** 用Markdown记录关键概念和你的理解
5. **构建项目：** 每学完一个框架，构建一个完整的项目来巩固

## 🏗️ 推荐项目清单

| 阶段 | 项目 | 技术栈 |
|------|------|--------|
| 基础 | 个人博客 | Flask + SQLite + Jinja2 |
| 中级 | 任务管理后台 | Django + PostgreSQL + Redis |
| 进阶 | RESTful API服务 | FastAPI + SQLAlchemy + JWT |
| 专家 | 微服务电商系统 | Django/FastAPI + Docker + Celery + Nginx |
。