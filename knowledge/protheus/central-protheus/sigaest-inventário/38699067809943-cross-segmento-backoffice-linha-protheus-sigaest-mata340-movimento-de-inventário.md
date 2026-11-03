---
article_id: 38699067809943
category: SIGAEST - INVENTÁRIO
content_hash: f4acaceffbfd48a8048883ae12a3b18ef27a84bab0633981e974b14bad05e31e
fetched_at: '2026-06-28T22:38:50.372695+00:00'
product: protheus
section_id: 1500001538961
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA340 - Movimento
  de inventário não aparece no kardex mesmo com status "Processado"
type: support-article
updated_at: '2026-03-02T12:38:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38699067809943-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA340-Movimento-de-invent%C3%A1rio-n%C3%A3o-aparece-no-kardex-mesmo-com-status-Processado
---

Se o movimento de inventário não aparece no Kardex mesmo com status "Processado", isso ocorre porque, ao digitar uma quantidade igual ao saldo atual do produto, nenhuma movimentação é registrada, já que não há diferença a ser ajustada, não gerando lançamentos nos relatórios.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38699067801495) Tempo aproximado para leitura: **00:01:00 min**  
  
**Dúvida**  
Movimento de inventário não aparece no kardex mesmo com status "Processado"  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**  
O processamento do inventário, realiza as movimentações internas DE0/RE0(MATA241) para atingir a quantidade que foi digitada na rotina de digitação MATA270, a partir da quantidade que você possui no saldo atual(B2\_QATU). Ou seja, se realizar uma digitação informando uma quantidade **igual** à quantidade que possui no seu **Saldo Atual(B2\_QATU)**, ao processar o inventário referente a essa digitação, ele não irá efetuar nenhuma movimentação e por esse motivo não irá registrar nada nos relatórios de movimentações.

Ex:

* Prod01 - B2\_QATU =10. Digitação de inventário - Quantidade B7\_QUANT = 10. Nenhuma movimentação será realizada e não haverá registro desse inventário. Status= 2 -Processado.
* Prod01 - B2\_QATU =10. Digitação de inventário - Quantidade B7\_QUANT = 15. Movimentação registrada no Kardex - DE0 = 5. Status= 2 -Processado.
* Prod01 - B2\_QATU =10. Digitação de inventário - Quantidade B7\_QUANT = 5. Movimentação registrada no Kardex - RE0 = 5. Status= 2 -Processado.

**Saiba mais:**

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA340 - Processo padrão para Inventariar produtos no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049739614-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA340-Processo-padr%C3%A3o-para-Inventariar-produtos-no-Estoque)

[*Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como realizar o estorno (exclusão) de movimento de Inventário?*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4402384407063)

[*SIGAEST - MILE importação de arquivo da tabela SB7 (Digitação do inventário)*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/10573324218007-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MILE-importa%C3%A7%C3%A3o-de-arquivo-da-tabela-SB7-Digita%C3%A7%C3%A3o-do-invent%C3%A1rio-)
