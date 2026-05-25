import { useState } from "react"

function App() {

  const [message, setMessage] = useState("")
  const [messages, setMessages] = useState([])

  const API_URL = import.meta.env.VITE_API_URL

  async function sendMessage() {

    if (!message) return

    const res = await fetch(
      `${API_URL}/support/`,
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
          message
        })
      }
    )

    

    const data = await res.json()

    setMessages([
      ...messages,
      {
        user: message,
        ai: data.response
      }
    ])

    setMessage("")
  }

  return (
    <div className="min-h-screen bg-gray-100 p-10">

      <div className="max-w-2xl mx-auto bg-white p-6 rounded-xl shadow">

        <h1 className="text-3xl font-bold mb-6">
          AI Support Agent
        </h1>

        <div className="space-y-4 mb-6">

          {messages.map((m, i) => (
            <div
              key={i}
              className="border p-3 rounded"
            >
              <p>
                <b>User:</b> {m.user}
              </p>

              <p className="mt-2">
                <b>AI:</b> {m.ai}
              </p>
            </div>
          ))}

        </div>

        <div className="flex gap-2">

          <input
            className="border p-2 flex-1 rounded"
            value={message}
            onChange={(e) =>
              setMessage(e.target.value)
            }
            placeholder="Ask support..."
          />

          <button
            onClick={sendMessage}
            className="bg-black text-white px-4 rounded"
          >
            Send
          </button>

        </div>

      </div>

    </div>
  )
}

export default App