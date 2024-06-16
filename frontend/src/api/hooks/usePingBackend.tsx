import { API_HOST } from "@/shared/env";
import { useQuery } from "react-query";

export const usePingBackend = () => {
  return useQuery("ping", async () => {
    const res = (await fetch(API_HOST + "/healthcheck").then((res) =>
      res.json(),
    )) as { status: boolean };

    return Boolean(res.status);
  });
};
