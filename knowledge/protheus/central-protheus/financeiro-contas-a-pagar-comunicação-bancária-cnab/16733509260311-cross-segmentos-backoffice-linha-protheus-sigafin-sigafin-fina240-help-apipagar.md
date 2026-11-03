---
article_id: 16733509260311
category: Financeiro - Contas a Pagar - Comunicação Bancária CNAB
content_hash: e2d99490e272a7c4cd7ffc1f226f51041162be5c63811fc0b96c0e5cc255aef1
fetched_at: '2026-06-28T22:37:56.439415+00:00'
product: protheus
section_id: 1500001550622
source: central-protheus
title: 'Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - SIGAFIN - FINA240
  - Help: APIPAGAR - Modelo não possui registro online de pagamentos'
type: support-article
updated_at: '2024-08-22T20:00:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/16733509260311-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-SIGAFIN-FINA240-Help-APIPAGAR-Modelo-n%C3%A3o-possui-registro-online-de-pagamentos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16733533838743) Tempo aproximado para leitura: **00:10:00 min****Ocorrência**No Modulo Financeiro, ao tentar cadastrar o borderô para boletos de pagamentos online, ocorre o **HELP:** **APIPAGAR - Modelo informado não possui registro online de pagamentos para o banco selecionado  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/16733413217431)**

**Ambiente**Cross Segmentos - Totvs BackOffice (Linha Protheus) - Financeiro - A partir da release 12.1.33

**Causa**Esse incidente ocorre, pois o modelo selecionado para pagamento não é valido para a transmissão de títulos online via API   
  
**Solução**Utilizar os modelos de pagamentos (**Tabela genérica 58 do SX5**) homologados para transmissão: 

* 30 - Transmissão de pagamento dos boletos gerados
* 31 - Transmissão de pagamento dos boletos gerados
* 01 - Transmissão de transferência entre contas
* 03 - Transmissão de transferência entre contas
* 41 - Transmissão de transferência entre contas
* 43 - Transmissão de transferência entre contas
* 13 - Transmissão de pagamentos de GUIA com código de barras
* 16 - Transmissão de pagamentos da DARF
* 18 - Transmissão de pagamentos da DARF
* 17 - Transmissão de pagamentos da GPS
* 45 - Transferencias via PIX

**Saiba mais:**  
[Modelo de borderô para geração de CNAB por segmentos.](https://tdn.totvs.com/pages/releaseview.action?pageId=233743712)  
[Banco do Brasil - Configuração pagamentos - FINA710](https://tdn.totvs.com/pages/releaseview.action?pageId=734394173)  
[Contas a pagar (Comunicação bancária online)](https://tdn.totvs.com/pages/releaseview.action?pageId=734394071)

##
