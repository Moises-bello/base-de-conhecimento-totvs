---
article_id: 360015878231
category: Financeiro - Compensação Contas a Pagar
content_hash: 362c45e6bb2859df333a5637beed5884d0b61f0a7aa0ea0d732e36b468543e5b
fetched_at: '2026-06-28T22:37:33.653034+00:00'
product: protheus
section_id: 35057559197335
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA340 - Compensação
  títulos TX com títulos de Adiantamento
type: support-article
updated_at: '2026-01-21T17:02:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015878231-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA340-Compensa%C3%A7%C3%A3o-t%C3%ADtulos-TX-com-t%C3%ADtulos-de-Adiantamento
---

**Dúvida**  
É possível compensar um título do tipo TX com um adiantamento do tipo PA?

**Ambiente**  
Microsiga Protheus - Financeiro - FINA340 - Todas as versões  
  
  
**Solução:**  
Os Títulos do Tipo **TX** referem-se a impostos, por esse motivo, somente podem ser compensados com títulos do tipo **TXA**.

Para a compensação dos TX com TXA, é necessário ajustar o parâmetro **“Compensa Títulos?”**, acessível pela tecla **F12** do teclado, selecionando a opção **"****Impostos"**.

Em situações de compensação entre títulos comuns, como **NF** com **PA**, a opção correta é "**Normais"**, evitando, assim, a geração do help **NOTITCOMP**.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360084042693)  
  
Não é possível realizar a compensação de títulos do tipo **TX** (Impostos) com títulos que não sejam do tipo **TXA**.

**Saiba mais**

[Cross Segmento - Backoffice Linha Protheus - SIGAFIN - Geração de impostos para pagamento antecipado e compensação de adiantamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019956692-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-Gera%C3%A7%C3%A3o-de-impostos-para-pagamento-antecipado-e-compensa%C3%A7%C3%A3o-de-adiantamento)

[Cross Segmento - Backoffice Linha Protheus - FINA080 - TXA baixado porém com saldo em aberto](https://centraldeatendimento.totvs.com/hc/pt-br/articles/37673439117335-Cross-Segmento-Backoffice-Linha-Protheus-FINA080-TXA-baixado-por%C3%A9m-com-saldo-em-aberto)
