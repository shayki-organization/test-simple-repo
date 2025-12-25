# API Documentation

## Overview

Simple test repository

## Base URL

```
https://api.example.com/v1
```

## Authentication

All API requests require authentication using a Bearer token:

```
Authorization: Bearer <your-token>
```

## Endpoints

### Health Check

```
GET /health
```

Returns the health status of the service.

**Response:**
```json
{
  "status": "healthy",
  "version": "1.0.0"
}
```

### List Resources

```
GET /api/v1/resources
```

Returns a list of all resources.

**Query Parameters:**
- `limit` (optional): Maximum number of results (default: 100)
- `offset` (optional): Pagination offset (default: 0)

**Response:**
```json
{
  "data": [...],
  "total": 100,
  "limit": 100,
  "offset": 0
}
```

### Get Resource

```
GET /api/v1/resources/{id}
```

Returns a specific resource by ID.

**Response:**
```json
{
  "id": "123",
  "name": "Example",
  "created_at": "2024-01-01T00:00:00Z"
}
```

### Create Resource

```
POST /api/v1/resources
```

Creates a new resource.

**Request Body:**
```json
{
  "name": "New Resource",
  "description": "Optional description"
}
```

**Response:**
```json
{
  "id": "124",
  "name": "New Resource",
  "created_at": "2024-01-01T00:00:00Z"
}
```

## Error Handling

All errors follow this format:

```json
{
  "error": {
    "code": "ERROR_CODE",
    "message": "Human-readable error message"
  }
}
```

### Common Error Codes

| Code | HTTP Status | Description |
|------|-------------|-------------|
| `NOT_FOUND` | 404 | Resource not found |
| `UNAUTHORIZED` | 401 | Invalid or missing authentication |
| `FORBIDDEN` | 403 | Insufficient permissions |
| `VALIDATION_ERROR` | 400 | Invalid request data |
| `INTERNAL_ERROR` | 500 | Server error |

## Rate Limiting

API requests are limited to 1000 requests per hour per API key.

Rate limit headers are included in all responses:
- `X-RateLimit-Limit`: Maximum requests per hour
- `X-RateLimit-Remaining`: Remaining requests
- `X-RateLimit-Reset`: Unix timestamp when limit resets
