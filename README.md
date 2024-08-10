# MyPass: Secure Password Manager
![MyPass Logo](https://github.com/user-attachments/assets/a07ce89e-1f24-495a-b18b-8e76dc318e80)

MyPass is a robust, user-friendly password manager designed to simplify and secure your digital life. With end-to-end encryption and intuitive vault management, MyPass ensures your sensitive information remains protected while being easily accessible to you.

## Features

- **Secure Encryption**: AES-256 encryption for all stored passwords
- **Intuitive Vault System**: Organize your passwords into custom vaults
- **Password Generator**: Create strong, unique passwords with ease
- **Two-Factor Authentication**: Add an extra layer of security to your MyPass account
- **Password Health Check**: Identify weak or reused passwords

## Tech Stack

- **Backend**: Python with Flask
- **Database**: MySQL with SQLAlchemy ORM
- **Frontend**: React (Web)
- **API**: RESTful API with JWT authentication
- **Encryption**: AES-256 in GCM mode, PBKDF2 for key derivation

## API Documentation

Detailed API documentation can be found in the [API.md](./api/API.md) file.

## Security

Security is our top priority. Here's an overview of our security measures:

- End-to-end encryption ensures your data is encrypted before it leaves your device
- Master Password is never stored, not even in hashed form
- Unique salt for each user to prevent rainbow table attacks
- Key derivation using PBKDF2 with 100,000 iterations
- All communications are over HTTPS
- Regular security audits and penetration testing


---

MyPass: One Key for Your Digital Life

