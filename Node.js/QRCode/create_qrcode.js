// 安装二维码图片库
const QRCode = require("qrcode");
const fs = require("fs");


/**
 * 生成二维码图片，并保存为 qrcode.png
 */
QRCode.toDataURL("http://192.168.0.150:8888/info", (err, url) => {
  if (err) throw err;
  let base64Data = url.replace(/^data:image\/png;base64,/, "");
  fs.writeFileSync("qrcode.png", Buffer.from(base64Data, "base64"));
});
