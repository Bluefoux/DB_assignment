FROM mysql:8.0.35

# Create directory for initialization scripts
RUN mkdir -p /docker-entrypoint-initdb.d

# Copy SQL script for creating tables
COPY sql_data/tables.sql /docker-entrypoint-initdb.d/

# Set permissions
RUN chown -R mysql:root /docker-entrypoint-initdb.d
RUN chmod -R 750 /docker-entrypoint-initdb.d

# Additional configurations if needed

# EXPOSE 3306
