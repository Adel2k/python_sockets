
# 🔌 Python Sockets

A simple Python script demonstrating basic socket programming. This project includes a server and a client that communicate over TCP/IP.

---

## 📁 Repository Contents

- `server.py`: Script to start the server.
- `client.py`: Script to start the client.

---

## ⚙️ Requirements

- Python 3.x

No external libraries are required.

---

## 🚀 Usage

### 1. Start the Server

Run the server script to start listening for incoming connections:

```bash
python server.py
````

The server will start and wait for a client to connect.

### 2. Start the Client

In a separate terminal, run the client script to connect to the server:

```bash
python client.py
```

The client will connect to the server and send a message.

---

## 🛠️ How It Works

* The **server** creates a socket, binds it to a host and port, and listens for incoming connections.
* The **client** creates a socket and connects to the server's host and port.
* Upon connection, the client sends a message to the server.
* The server receives the message and prints it.

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 👤 Author

**Adeline Eminian**

* GitHub: [@Adel2k](https://github.com/Adel2k)
* LinkedIn: [Adeline Eminian](https://www.linkedin.com/in/adeline-eminian-24adel)

---

## 📌 Disclaimer

This script is intended for educational purposes to demonstrate basic socket programming concepts. Use responsibly and ensure compliance with all applicable laws and regulations.

