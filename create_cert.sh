docker-compose run --rm --entrypoint "certbot certonly --webroot -w /var/www/certbot --email admin_dti@lendik.com  -d admin.lendik.com --rsa-key-size 4096 --agree-tos  --force-renewal" certbot
