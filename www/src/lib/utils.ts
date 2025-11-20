import { type ClassValue, clsx } from "clsx";
import { twMerge } from "tailwind-merge";

import { pirates } from "./constants";

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs));
}

export function randomPirateName() {
  return pirates[Math.floor(Math.random() * pirates.length)];
}

export function formatDate(date: Date) {
  return Intl.DateTimeFormat("en-US", {
    month: "short",
    day: "numeric",
  }).format(date);
}
