import { CornerDownLeftIcon } from "lucide-react";
import { useState } from "react";
import useSWRMutation from "swr/mutation";

import {
  InputGroup,
  InputGroupAddon,
  InputGroupButton,
  InputGroupText,
  InputGroupTextarea,
} from "@/components/ui/input-group";
import { censorFetcher } from "@/lib/fetchers";
import { formatDate, randomPirateName } from "@/lib/utils";

type Message = {
  id: string;
  name: string;
  content: string;
  date: Date;
};

function useChat() {
  const [input, setInput] = useState("");
  const [messages, setMessages] = useState<Message[]>([
    {
      id: crypto.randomUUID(),
      name: randomPirateName(),
      content: "Watch the language, scallywag!",
      date: new Date(),
    },
    {
      id: crypto.randomUUID(),
      name: randomPirateName(),
      content: "Where'd you put me **** treasure?!",
      date: new Date(),
    },
    {
      id: crypto.randomUUID(),
      name: randomPirateName(),
      content: "Arrr matey!",
      date: new Date(),
    },
  ]);

  const { trigger, isMutating } = useSWRMutation(
    "http://0.0.0.0:8000/censor",
    censorFetcher,
    {
      onSuccess: (data) => {
        const message: Message = {
          id: crypto.randomUUID(),
          name: randomPirateName(),
          content: data,
          date: new Date(),
        };

        setMessages((previous) => [message, ...previous]);
        setInput("");
      },
    },
  );

  return {
    messages,
    input,
    setInput,
    send: () => trigger(input.trim()),
    isLoading: isMutating,
    disabled: isMutating || input.trim().length === 0,
  };
}

export function Chat() {
  const { messages, input, setInput, send, disabled } = useChat();

  return (
    <div className="w-full space-y-3">
      <InputGroup className="w-full">
        <InputGroupTextarea
          className="text-base!"
          placeholder="Try it out!"
          value={input}
          onChange={(event) => setInput(event.target.value)}
          onKeyDown={(event) => {
            if (event.key === "Enter" && !event.shiftKey) {
              event.preventDefault();
              if (!disabled) send();
            }
          }}
        />
        <InputGroupAddon align="block-end" className="px-3 pt-0! pb-2">
          <InputGroupText className="text-sm">
            {280 - input.length} characters left
          </InputGroupText>
          <InputGroupButton
            size="icon-sm"
            className="ml-auto size-6"
            onClick={() => send()}
            disabled={disabled}
          >
            <CornerDownLeftIcon />
          </InputGroupButton>
        </InputGroupAddon>
      </InputGroup>
      <ul className="flex w-full flex-col gap-3">
        {messages.map(({ id, name, content, date }) => (
          <li key={id}>
            <article className="flex gap-2 rounded-md border p-3">
              <img
                className="size-10 rounded-full border"
                src={`https://deno-avatar.deno.dev/avatar/${name}.svg`}
                alt={`${name}'s avatar`}
              />
              <div>
                <span>
                  <span className="font-semibold">{name}</span>
                  <span className="text-muted-foreground">
                    {" "}
                    · {formatDate(date)}
                  </span>
                </span>
                <p className="whitespace-pre-line">{content}</p>
              </div>
            </article>
          </li>
        ))}
      </ul>
    </div>
  );
}
