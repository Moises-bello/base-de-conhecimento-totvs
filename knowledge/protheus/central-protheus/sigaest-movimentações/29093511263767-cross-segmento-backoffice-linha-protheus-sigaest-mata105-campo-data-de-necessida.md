---
article_id: 29093511263767
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 20b3e35bf56342074a43ce0e3cb0ced57e9cfef4d886568baa5250ad552f3df0
fetched_at: '2026-06-28T22:38:55.672431+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA105 - Campo Data
  de Necessidade não está vindo preenchida. O que fazer?
type: support-article
updated_at: '2025-03-12T12:26:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/29093511263767-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA105-Campo-Data-de-Necessidade-n%C3%A3o-est%C3%A1-vindo-preenchida-O-que-fazer
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29093544942231) Tempo aproximado para leitura: **00:01:37 min** **Dúvida**Campo "data necessidade" da rotina MATA105 não está vindo preenchida. Como corrigir?  
  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**O campo Necessidade (CP\_DATPRF) no padrão precisa do Inicializador Padrão com a função DDATABASE para assumir o preenchimento inicial da data. Basta deixar o campo Inicializador Padrão do campo no Dicionário de Dados com a função conforme exemplo abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29093544946583)

Desta forma, ao abrir a rotina ele trará automaticamente a Data da Necessidade

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29093544954263)

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Movimentações no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)
