import { Chat } from "./components/chat";

export default function App() {
  return (
    <main className="mx-auto flex max-w-lg flex-col gap-6 p-4">
      <div className="flex flex-col">
        <h1 className="text-5xl font-bold tracking-tight">sailor 🏴‍☠️</h1>
        <h2 className="mt-2 text-xl tracking-tight">
          A profanity filtering API in Python using regular expressions and
          FastAPI.
        </h2>
      </div>
      <Chat />
    </main>
  );
}
