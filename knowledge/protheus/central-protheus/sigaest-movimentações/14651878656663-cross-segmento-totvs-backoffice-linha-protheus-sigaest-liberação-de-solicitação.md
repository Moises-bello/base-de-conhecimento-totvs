---
article_id: 14651878656663
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 14400144987d1b1e6eba3cf4a863c0c88ffced73b23a13936f9c170560991fd5
fetched_at: '2026-06-28T22:38:58.502653+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAEST - Liberação de
  Solicitação ao Armazém (MATA107)
type: support-article
updated_at: '2024-11-04T12:57:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/14651878656663-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEST-Libera%C3%A7%C3%A3o-de-Solicita%C3%A7%C3%A3o-ao-Armaz%C3%A9m-MATA107
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26488350137367) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Como utilizar o controle de Liberação de Solicitação ao Armazém?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAEST - Todas as versões.  
  
**Solução**Para utilização dessa rotina, será necessário configurar os parâmetros:

* MV\_APROVSA = .T.
* MV\_APRSAEC = .F.

Após essa alteração, é necessário configurar o usuário solicitante na rotina Cadastro de Solicitante (MATA084), preenchendo o campo "Quantidade" (AI\_QUANT).

Quando a solicitação ao armazém cadastrada for de quantidade inferior à definida no campo "Quantidade" (AI\_QUANT), não haverá bloqueio.

Ao incluir uma solicitação ao armazém de quantidade superior à informada no campo "Quantidade" (AI\_QUANT), a mesma será gerada com o status "Em aprovação". Para ser aprovada, é necessário acessar a rotina Liberação de Solicitação (MATA107).

Após alteração dos parâmetros:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/14651685978135)  
   
Ao abrir a rotina "Liberação de Solicitação" (MATA107):   
![](https://centraldeatendimento.totvs.com/hc/article_attachments/14651709001751)

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Movimentações no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)*
