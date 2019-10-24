FROM kennethreitz/pipenv

RUN apt-get update && apt-get -y install cron vim

COPY . /app
RUN chmod 755 /app/main.py

# Copy cron_file file to the cron.d directory
COPY cron_file /etc/cron.d/cron_file

# Give execution rights on the cron job
RUN chmod 0644 /etc/cron.d/cron_file

# Apply cron job
RUN crontab /etc/cron.d/cron_file

# !!!
# Setting the environment variables
ENV env_var this_is_a_var

RUN printenv > /etc/environment

# Run the command on container startup
CMD ["cron", "-f"]
