import { AlertCircleIcon } from "lucide-react";
import useSWR from "swr";

import { Chat } from "./components/chat";
import { Alert, AlertDescription, AlertTitle } from "./components/ui/alert";
import { baseUrl } from "./lib/constants";
import { healthFetcher } from "./lib/fetchers";

function OutageAlert() {
  return (
    <Alert variant="destructive">
      <AlertCircleIcon />
      <AlertTitle>Sailor is experiencing technical difficulties.</AlertTitle>
      <AlertDescription>
        Our API is currently not responding, so this demonstration may not
        function correctly. Please try again later.
      </AlertDescription>
    </Alert>
  );
}

export default function App() {
  const { data: healthy, error } = useSWR(baseUrl + "/health", healthFetcher);

  return (
    <main className="mx-auto flex max-w-lg flex-col gap-6 p-4">
      <div className="flex flex-col gap-2">
        <h1 className="text-5xl font-bold tracking-tight">sailor 🏴‍☠️</h1>
        <p className="text-xl tracking-tight">
          A profanity filtering API in Python using regular expressions and
          FastAPI.
        </p>
        <ul>
          <li>
            <span className="font-medium">GitHub:</span>{" "}
            <a
              className="text-blue-500 underline underline-offset-2"
              href="https://github.com/nicholasdly/sailor"
              target="_blank"
              rel="noopener noreferrer"
            >
              github.com/nicholasdly/sailor
            </a>
          </li>
          <li>
            <span className="font-medium">Documentation:</span>{" "}
            <a
              className="text-blue-500 underline underline-offset-2"
              href={baseUrl + "/docs"}
              target="_blank"
              rel="noopener noreferrer"
            >
              {baseUrl.split("://")[1] + "/docs"}
            </a>
          </li>
        </ul>
      </div>
      {(error || !healthy) && <OutageAlert />}
      <Chat />
    </main>
  );
}
