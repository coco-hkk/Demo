/**
 * 二维码实验服务端
 */

const http = require("http");
const fs = require("fs");

const server = http.createServer();


server.on("request", (request, response) => {
    const url = decodeURIComponent(request.url);
    console.log(url)
    const regex0 = new RegExp("^/info");

    if (regex0.test(url)) {
        if (request.method === "GET") {
            // 读取 html 文件
            const html = fs.readFileSync('./index.html')
            response.writeHead(200, {
                "Content-Type": "text/html; charset=UTF-8",
            });
            response.end(html);
        }
    }
});

server.listen(8888);
