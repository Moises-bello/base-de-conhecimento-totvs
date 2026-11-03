---
article_id: 360021282772
category: Ativo Fixo - Baixa e Baixa de Adiantamento
content_hash: 5c8b177a046e2b9ddcbe53bf63ff42c07961638a76d0b8fce8de632211a9c4d8
fetched_at: '2026-06-28T22:41:55.560509+00:00'
product: protheus
section_id: 1500001535901
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAATF - Cancelamento da baixa
  do ativo imobilizado e MV_ATFVLNF
type: support-article
updated_at: '2023-11-20T16:20:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021282772-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-Cancelamento-da-baixa-do-ativo-imobilizado-e-MV-ATFVLNF
---

**Dúvida**No cancelamento da baixa de um ativo, qual a validação feita na nota fiscal na tabela SF2  
   
 **Ambiente**Protheus – Ativo Fixo – A partir da versão 12  
  
   
**Solução**

O parâmetro só terá validade caso a nota fiscal tenha sido gerada pelo ativo fixo, no item abaixo em destaque informando "SIM". E com isso será gerado uma nota fiscal na tabela SF2.

![](https://totvssuporte.zendesk.com/attachments/token/ThXlkapfuAOUZnca76D13nXPS/?name=inline-634824779.png)​Caso esteja como NÃO e mesmo assim o numero da nota fiscal, a título de informação, seja informado no momento da baixa, mesmo com o parâmetro MV\_ATFVLNF=.T., não será feito nenhuma verificação na SF2 no momento do cancelamento da baixa.
