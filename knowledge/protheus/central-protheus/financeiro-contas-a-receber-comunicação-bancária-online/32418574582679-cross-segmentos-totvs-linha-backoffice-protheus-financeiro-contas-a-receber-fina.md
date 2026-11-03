---
article_id: 32418574582679
category: Financeiro - Contas a Receber - Comunicação Bancária Online
content_hash: 06a9e42c6e0a2bf075ca27e2d86e3f9c1cce0caa7ffc770510e19104791e00c5
fetched_at: '2026-06-28T22:37:49.278175+00:00'
product: protheus
section_id: 26656227629847
source: central-protheus
title: Cross Segmentos - TOTVS Linha Backoffice Protheus - Financeiro - Contas a Receber
  - FINA713 - Boleto baixando no banco após data de vencimento
type: support-article
updated_at: '2025-06-12T12:42:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/32418574582679-Cross-Segmentos-TOTVS-Linha-Backoffice-Protheus-Financeiro-Contas-a-Receber-FINA713-Boleto-baixando-no-banco-ap%C3%B3s-data-de-vencimento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32418574571287) Tempo aproximado para leitura: **00:10:00 min****Ocorrência**Ao realizar uma **transmissão de títulos via API (FINA713)** e o cliente da empresa não efetuar o pagamento até o vencimento do boleto, o banco está efetuando baixa do boleto, impossibilitando o pagamento após o vencimento.  
**Ambiente**Cross Segmentos - TOTVS Linha Backoffice Protheus - Financeiro - A partir da release 12.1.2310

**Causa**Este cenário ocorre devido o campo **EE\_DIASREC (Dias para recebimento)** estar vazio na configuração de **Parâmetros de Bancos (FINA130)**, com isso é enviado a data limite de pagamento do boleto até o vencimento.   
  
**Solução**Acessar os **Parâmetros de Bancos (FINA130)** - Aba: **Outros**  
Localizar o campo **EE\_DIASREC** e adicionar dias para recebimento

Exemplo: 365  
Após o vencimento do boleto no Internet Banking, o cliente pode efetuar o pagamento deste boleto em até 365 dias   
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32418574571671)

**Saiba mais**  
**[Contas a receber (Comunicação bancária online)](https://tdn.totvs.com/pages/releaseview.action?pageId=612548392)**
