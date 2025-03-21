# Этап сборки
FROM node:18-alpine as builder
WORKDIR /app
COPY package*.json ./
RUN npm install --legacy-peer-deps  # Если есть проблемы с зависимостями
COPY . .
RUN npm run build

# Этап production
FROM nginx:1.23-alpine
COPY --from=builder /app/build /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf
