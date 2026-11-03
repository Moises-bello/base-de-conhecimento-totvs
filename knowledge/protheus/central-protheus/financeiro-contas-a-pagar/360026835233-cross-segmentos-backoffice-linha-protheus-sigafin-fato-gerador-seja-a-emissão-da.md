---
article_id: 360026835233
category: Financeiro - Contas a Pagar
content_hash: 4c8dcb74926a4cb75e90d4f523d0c297a823d178f2db21bbb5a6a1c50cfab730
fetched_at: '2026-06-28T22:38:08.520335+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Fato gerador seja a
  emissão da NF
type: support-article
updated_at: '2024-08-19T13:26:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026835233-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Fato-gerador-seja-a-emiss%C3%A3o-da-NF
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25703887396887)**Tempo aproximado para leitura: **00:03:00 min****Dúvida**Como configurar o sistema para que o fato gerador seja a emissão da NF e não seu pagamento?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões

**Solução**O sistema trata de acordo com legislação, o cálculo de vencimentos de impostos (**PCC**) a partir da data de vencimento do título principal considera o vencimento como pagamento, já que o fato gerador do **PCC** é o pagamento.   
É possível ajustar o cálculo da data de vencimento de impostos de acordo com sua regra de negócio utilizando o ponto de entrada **F050MDVC**, no módulo **Financeiro**.

**Importante:**  
Se as informações acima não atenderem sua regra de negócio na implementação no produto padrão, poderá nos encaminhar a legislação que define que o cálculo de vencimento de impostos deve considerar a emissão do título e não seu vencimento, sendo assim podemos compartilhar este ticket para nossa consultoria tributária avaliar a solicitação. 

**Saiba Mais**  
[F050MDVC - Cálculo da data de vencimento de impostos](http://tdn.totvs.com/pages/releaseview.action?pageId=6070892)

[Fatos geradores dos tributos considerados no Extrator financeiro para o TAF](https://tdn.totvs.com/pages/releaseview.action?pageId=737543501)
