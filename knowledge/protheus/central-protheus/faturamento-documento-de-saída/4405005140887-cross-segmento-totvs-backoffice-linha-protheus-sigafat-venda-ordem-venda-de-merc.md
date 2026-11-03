---
article_id: 4405005140887
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: 6af8c5d9798e789af697ad3de7a280dbfde9d97f960223719d577c8fde272ece
fetched_at: '2026-06-28T22:38:43.928830+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Venda Ordem
  (Venda de mercadoria adquirida, Remessa Simbólica e Remessa por conta e ordem de
  terceiros)
type: support-article
updated_at: '2021-11-25T11:13:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4405005140887-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Venda-Ordem-Venda-de-mercadoria-adquirida-Remessa-Simb%C3%B3lica-e-Remessa-por-conta-e-ordem-de-terceiros
---

**Dúvida**

Como incluir uma Venda Ordem ( Venda de mercadoria adquirida, Remessa Simbólica e Remessa por conta e ordem de terceiros)

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões.  
  
**Solução**

O processo de venda a ordem deve ser realizado em  notas distintas e não existe uma forma automatizada  no sistema.  
  
1) Faturamento (CFOP 6120 - **Venda de mercadoria adquirida ou recebida de terceiros entregue ao destinatário pelo vendedor remetente, em venda à ordem)**  
TES   
Gera duplicata = Sim  
Atualiza estoque= Não (para que não fique com estoque negativo)  
Demais configurações de impostos (avaliar com fiscal)  
  
2) Nota fiscal de remessa para entrega (**Remessa Simbólica) - Após entrada na mercadoria - Recebimento Petrobrás**  
TES  
Gera duplicata =Não   
Atualiza Estoque= Sim   
Demais configurações de impostos (avaliar com fiscal)

Obs: Caso necessário informar o número da  nota de saída do faturamento (primeira nota) preencher o campo de informações complementares no pedido de venda (C5\_MENNOTA).

3) Nota fiscal conta e ordem **(Remessa por conta e ordem de terceiros)**  
TES  
Gera duplicata =Não   
Atualiza Estoque= Não   
Demais configurações de impostos (avaliar com fiscal)  
Obs: Caso necessário informar o número da  nota de saída do faturamento (primeira nota) preencher o campo de informações complementares no pedido de venda (C5\_MENNOTA).  
  
Documentação informações complementares.   
[Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Como gerar informações na TAG infCpl ou infAdFisco no XML e no DANFE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024950773--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Como-gerar-informa%C3%A7%C3%B5es-na-TAG-infCpl-ou-infAdFisco-no-XML-e-no-DANFE?source=search)
