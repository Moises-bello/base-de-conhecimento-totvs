---
article_id: 37637542846871
category: Financeiro - Contas a Receber
content_hash: 42025cfb8948a00c86ae890796f7f272fa7c6385556b35062e44fb625ce96d36
fetched_at: '2026-06-28T22:38:12.526861+00:00'
product: protheus
section_id: 1500001539421
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGAFIN - Help: NAOPRINCIP'
type: support-article
updated_at: '2026-01-13T12:48:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37637542846871-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-Help-NAOPRINCIP
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37637583353367) Tempo aproximado para leitura: **00:05 min**  
  
**Ocorrência**  
Ao excluir um registro, é apresentado o help:naoprincip.  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro  
  
**Causa**  
Ao tentar excluir diretamente o título de abatimento, o sistema não permitirá a operação e apresentará a seguinte mensagem:

**NAOPRINCIP**  
“**PROBLEMA:** Este título está agregado a outro título, portanto não poderá ser baixado individualmente.  
**SOLUÇÃO:** Para baixar este título, escolha o título principal.”  
  
**Solução**  
Os títulos de abatimento, identificados pelo símbolo “-” (como **IN-**, **IS-**, **CF-**, entre outros), estão sempre vinculados a um **título principal** (por exemplo, **NF**, **FT**, **BOL**, etc.). Dessa forma, não é possível incluí-los sem a existência prévia de um título principal, tampouco efetuar sua baixa antes que o título principal seja devidamente baixado.

**Saiba mais**

[Títulos tipo PI- (PIS), CF-(Cofins), CS-(CSLL)](https://tdn-homolog.totvs.com/pages/releaseview.action?pageId=52199579)
