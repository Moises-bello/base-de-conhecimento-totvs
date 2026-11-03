---
article_id: 360004425292
category: License Sever Virtual
content_hash: c2fdb3af1fa7f54727e7620e62886b2d48996d01409f0cbc4ed871e8cbf3c143
fetched_at: '2026-06-28T22:42:20.063621+00:00'
product: protheus
section_id: 360000075428
source: central-protheus
title: 'Framework - Linha Protheus - Mensagem de erro: Host não encontrado'
type: support-article
updated_at: '2026-01-27T17:26:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004425292-Framework-Linha-Protheus-Mensagem-de-erro-Host-n%C3%A3o-encontrado
---

**Dúvida**  
O que fazer quando aparecer a mensagem Falha ao transmitir os dados para a TOTVS. TOTVS License Server - Host não encontrado?  
  
**Ambiente**  
Protheus - LSVirtual - Todas as versões  
  
**Solução**  
Realize o procedimento abaixo.  
  
1. Abra o arquivo **appserver.ini** no diretório .../bin/appserver/ do License Server Virtual;  
  
2. Altere a configuração da seção **SSLConfigure**  
[SSLConfigure]  
SSL2=1  
SSL3=1  
TLS1=1  
  
3. **Salve** o arquivo e **reinicie o serviço** do License Server Virtual.
