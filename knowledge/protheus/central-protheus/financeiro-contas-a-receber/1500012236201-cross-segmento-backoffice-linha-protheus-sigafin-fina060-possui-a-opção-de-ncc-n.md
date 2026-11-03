---
article_id: 1500012236201
category: Financeiro - Contas a Receber
content_hash: 6e94ee5733ec62c4bd2f251c7523082a2fc66c1b97f08ba7ab4099ad042649ec
fetched_at: '2026-06-28T22:38:12.789918+00:00'
product: protheus
section_id: 1500001539421
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINA060- Possui a opção
  de NCC (Nota de Crédito Cliente) para pagamento via CNAB
type: support-article
updated_at: '2021-05-26T19:44:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500012236201-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA060-Possui-a-op%C3%A7%C3%A3o-de-NCC-Nota-de-Cr%C3%A9dito-Cliente-para-pagamento-via-CNAB
---

**Dúvida**Possui a opção de incluir uma NCC (Nota de Crédito Cliente) para pagamento via CNAB?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Solução**A rotina do CNAB foi criado para efetuar pagamento, dessa forma a mesma poderá efetuar apenas transferências ou depósitos, além dos pagamentos normais, não contemplados pelo padrão NCC.  
  
Para envio de títulos para o CNAB, é necessário criação de Borderôs, porém, não é possível pelo padrão criar borderôs com títulos do tipo **NCC** e **RA**, pois no sistema é entendido que esse valor já foi recebido ou existe um crédito e não faz sentido enviar uma informação para o banco pedindo recebimento de algo que foi recebido por meio destes registros.  
  
Abaixo segue o material da Rotina de Borderôs, para ver os detalhes:  
  
**Saiba Mais**<https://tdn.totvs.com/pages/releaseview.action?pageId=271405699>
