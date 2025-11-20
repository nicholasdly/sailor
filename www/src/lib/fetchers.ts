export async function censor(
  url: string,
  { arg }: { arg: string },
): Promise<string> {
  const response = await fetch(url, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message: arg }),
  });

  if (!response.ok) throw new Error(`HTTP error! Status: ${response.status}`);

  return await response.json();
}
