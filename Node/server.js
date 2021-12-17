const http = require('http');

const hostname = 'localhost';
const port = 8000;
const queue = [];

const server = http.createServer(async (req, res) => {
    const buffers = [];

    for await (const chunk of req) {
        buffers.push(chunk);
    }
    const data = Buffer.concat(buffers).toString();

    if (req.method === 'POST') {
        console.log(`Body: ${data}`);
        if (queue.length < 5) {
            queue.push(data);
        }
        else {
            queue.shift();
            queue.push(data);
        }
        res.statusCode = 200;
        res.setHeader('Content-Type', 'text/plain');
        res.end("Данные успешно записаны");
    }
    if (req.method === 'GET') {
        let message = "";
        for (let i = 0; i < queue.length; i++)
            message += queue[i] + "  ";
        res.statusCode = 200;
        res.setHeader('Content-Type', 'text/plain');
        res.end(message);
    }

});

server.listen(port, hostname, () => {
    console.log(`Server running at http://${hostname}:${port}/`);
  });