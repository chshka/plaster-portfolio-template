# 导入 Netlify

1. 在 Netlify 选择导入现有项目（Import an existing project），连接 GitHub。
2. 授权目标仓库。私有仓库也需要授予 Netlify 访问权限。
3. 选择仓库与 main 分支。Framework preset 选择 Other / 无框架。
4. Base directory 留空，Build command 留空，Publish directory 填 `site`。
5. 点击发布。根目录 netlify.toml 已声明 publish = "site"。
6. 打开平台提供的 HTTPS 链接，测试加载页、浮雕、导航、邮箱与手机滚动。
7. 后续推送 main 可由已连接的 Netlify 自动触发部署。

无需环境变量、数据库、后端或 npm install。完整网页依赖 HTTP/HTTPS 加载 ES Modules 和 GLB，不支持双击 file:// 运行全部特效。

仓库私有只限制源码访问；Netlify 生成的网站是否公开由 Netlify 的站点设置决定。

配置依据：[Netlify 官方文档](https://docs.netlify.com/build/configure-builds/file-based-configuration/)。托管额度按平台当前套餐为准。
