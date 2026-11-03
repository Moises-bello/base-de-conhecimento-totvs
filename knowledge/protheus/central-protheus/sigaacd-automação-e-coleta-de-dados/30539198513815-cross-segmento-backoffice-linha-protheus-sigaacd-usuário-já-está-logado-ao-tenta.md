---
article_id: 30539198513815
category: SIGAACD - Automação e Coleta de Dados
content_hash: 15bd83d528d78469eaae9d53bd2044110548a2bcea209bc6c1cdc89f1f2a2a9f
fetched_at: '2026-06-28T22:39:11.066901+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAACD  - "Usuário já está
  logado" ao tentar fazer múltiplo login
type: support-article
updated_at: '2025-03-12T12:45:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/30539198513815-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Usu%C3%A1rio-j%C3%A1-est%C3%A1-logado-ao-tentar-fazer-m%C3%BAltiplo-login
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30539198449943) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Ao efetuar múltiplo login no Coletor de Dados é apresentada a mensagem da imagem abaixo. O que fazer para resolver?

![036e82db-dc84-4441-b821-e976eea14ca5.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/30539198456599)  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Automação e Coleta de Dados - Todas as versões.  
  
**Solução**Para solucionar a mensagem, basta deixar o parâmetro MV\_ACDUSER (Habilita a validação para verificar se o usuário já esta logado) = .F.

Quando ele  está = .T., ele acaba validando que o usuário já está logado e apresenta a mensagem na tela. Com o parâmetro = .F. ele não valida e permite o acesso.

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Automação e Coleta de Dados*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550002-SIGAACD-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados)
