FROM node:18-alpine as builder

ARG VITE_API_HOST
ENV VITE_API_HOST=$VITE_API_HOST
ARG VITE_SHA
ENV VITE_SHA=$VITE_SHA

COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build


FROM nginx:alpine as production-build
COPY nginx/nginx.conf /etc/nginx/nginx.conf

RUN rm -rf /usr/share/nginx/html/*

COPY --from=builder /dist /usr/share/nginx/html/frontend-app

EXPOSE 8080

CMD ["nginx", "-g", "daemon off;"]