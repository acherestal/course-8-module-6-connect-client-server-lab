const API_BASE = "http://localhost:5000";

const list = document.querySelector("#event-list");
const form = document.querySelector("#event-form");
const titleInput = document.querySelector("#title");
const statusEl = document.querySelector("#status");

function setStatus(msg) {
  statusEl.textContent = msg;
}

function renderEvent(event) {
  const li = document.createElement("li");
  li.textContent = `${event.id}. ${event.title}`;
  list.appendChild(li);
}

function loadEvents() {
  list.innerHTML = "";
  setStatus("Loading events...");

  fetch(`${API_BASE}/events`)
    .then((r) => r.json())
    .then((events) => {
      events.forEach(renderEvent);
      setStatus("");
    })
    .catch(() => setStatus("Could not load events. Is the server running?"));
}

form.addEventListener("submit", (e) => {
  e.preventDefault();
  const title = titleInput.value.trim();
  if (!title) return;

  fetch(`${API_BASE}/events`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ title }),
  })
    .then(async (r) => {
      const data = await r.json();
      if (!r.ok) throw new Error(data.error || "Error");
      return data;
    })
    .then((newEvent) => {
      renderEvent(newEvent);
      titleInput.value = "";
      setStatus("Event added!");
      setTimeout(() => setStatus(""), 800);
    })
    .catch((err) => setStatus(err.message));
});

loadEvents();
