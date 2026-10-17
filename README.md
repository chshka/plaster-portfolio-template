# 白石膏浮雕个人网站 · 开源示例模板

这是可部署的纯静态示例站，使用原创程序花叶浮雕、通用资料与两张本地 SVG 作品示例图。背景上的“示例背景”可在首页修改或删除。

HTML + CSS + 原生 JavaScript / WebGL，无后端、数据库、运行时npm依赖、外部CDN和构建步骤。

## 在 Netlify 导入

导入这个仓库的 `main` 分支。Base directory 留空、Build command 留空、Publish directory 填 **`site`**。根目录 `netlify.toml` 已配置发布目录。[详细步骤](docs/NETLIFY.md)。

## 本地预览

在仓库根目录运行：

```sh
python -m http.server 8080 --bind 127.0.0.1 --directory site
```

打开 http://127.0.0.1:8080/ 。Python仅用于本地预览；线上只需静态文件托管。直接双击 index.html 会受浏览器 file:// 模块/模型访问限制，完整特效须通过 HTTP/HTTPS。

## 文件结构

```text
site/
  index.html
  css/style.css
  js/main.js
  js/gallery-assets.js
  js/loading-screen.js
  js/relief-background.js
  js/relief-flow.js
  js/relief-model.js
  js/relief-surface.js
  js/relief-text.js
  assets/
netlify.toml
docs/NETLIFY.md
```

## 修改资料和素材

- 修改 `site/index.html` 的姓名、介绍、邮箱、导航和项目说明。
- 修改 `site/css/style.css` 调整字体和布局。
- `site/js/gallery-assets.js` 声明图片、高度图和GLB的对应关系。资源URL相对于首页，而JavaScript模块import相对于模块所在目录。
- `site/js/relief-flow.js` 控制白石膏光照、流场、扩散和动态高度。
- `site/js/relief-text.js` 使用独立手动流场扰动文字；自动动画仅作用于背景。
- 可暂停动态；系统减少动态效果设置有效。WebGL失败时保留可读正文和备用图。

## 建站技能关联

`relief-portfolio` 是用于指导AI建站、准备素材与验证的技能包；本仓库是可以直接托管的网页项目。网页运行不要求安装该技能。技能仓库：[`chshka/relief-portfolio`](https://github.com/chshka/relief-portfolio)。安装与使用方法见技能仓库 README，另见 [关联说明](docs/SKILL.md)。

## 实现与限制

动态浮雕使用高度网格、实时法线和柔和遮蔽近似，并非原参考网站的完整复刻。GLB读取器只支持应用变换、嵌入BIN、无压缩三角网格，任意外部glTF应使用成熟加载器。

现代浏览器需要支持 ES Modules 与 WebGL；手机性能取决于设备。验证覆盖桌面及手机模拟，真实手机帧率尚未验证。免费托管额度以平台当前套餐为准。

## 示例资源与许可

- 示例浮雕由 `tools/generate_sample_relief.py` 的数学函数生成，未使用个人角色模型或第三方网站资源。
- `site/assets/sample-height.png`：线性高度；`sample-relief.glb`：实际三角网格；`sample-relief.png`：备用渲染图。
- `sample-emblem.svg` 与 `project-sample-01.svg`、`project-sample-02.svg` 均为原创几何占位图，可直接替换。
- 制作脚本需 Blender Python；访客和静态托管不需要Blender。可用 `blender --background --factory-startup --python tools/generate_sample_relief.py` 重生成素材。
- 源码与上述程序示例资源采用 MIT 许可。加入自己的照片或模型后，请自行标注这些素材的授权。
- 默认示例邮箱 `hello@example.com` 仅作占位。
