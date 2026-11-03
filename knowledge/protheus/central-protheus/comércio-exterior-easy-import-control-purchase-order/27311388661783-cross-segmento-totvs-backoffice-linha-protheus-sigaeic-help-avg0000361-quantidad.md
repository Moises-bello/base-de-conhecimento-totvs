---
article_id: 27311388661783
category: Comércio Exterior - Easy Import Control - Purchase - Order
content_hash: 0759f04ead14b8160155af0e40ab1b1f474818a13690f949258f80b916f114aa
fetched_at: '2026-06-28T22:39:41.265525+00:00'
product: protheus
section_id: 1500001538481
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - HELP AVG0000361
  - Quantidade maior que o Saldo da Solicitação.
type: support-article
updated_at: '2024-10-30T12:03:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/27311388661783-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-HELP-AVG0000361-Quantidade-maior-que-o-Saldo-da-Solicita%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27311364474647) Tempo aproximado para leitura: **00:02:00min** **Dúvida**Como corrigir o **Help:** "**AVG0000361**" - Quantidade maior que o Saldo da Solicitação?  
  
**Problema:** Quantidade maior que o Saldo da Solicitação.  
**Solução:** Verifique o saldo da quantidade na solicitação.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/27311364477591)

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Easy Import Control - a partir da versão 12  
  
**Solução**Neste caso, será necessário validar a quantidade de itens dentro da rotina de Solicitação de Importação (EICSI400) que está sendo consumida pela Purchase Order (EICPO400) em questão.  
Salientamos que a mensagem será apresentada caso a PO tente consumir uma quantidade maior que o Saldo disponível do item dentro da SI.  
  
**Saiba Mais:** **[Purchase Order](https://tdn.totvs.com/display/public/PROT/Purchase+Order+-+EICPO400)**
