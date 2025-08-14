# Phase 5 — Patient Records Hub (New Pillar)

**Objective**  
Introduce a minimal safe vault for patient records.

## Scope — IN
- Schema & API: `vault_documents`, RBAC, audit log
- Storage: Supabase Storage or S3 (signed URLs, object ACLs)
- Security: encryption at rest, short-lived tokens, least privilege, redaction in logs
- Consent UX: upload, share/revoke

## Exit Criteria
- Privacy checklist passes
- Access control verified by tests (only permitted roles can read)
