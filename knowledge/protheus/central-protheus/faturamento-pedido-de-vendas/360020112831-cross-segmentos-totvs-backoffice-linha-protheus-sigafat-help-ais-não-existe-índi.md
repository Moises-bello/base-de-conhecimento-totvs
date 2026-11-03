---
article_id: 360020112831
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 14b0c4c094356a3eaa648f07846819d358a47448c72db448910486ba97302922
fetched_at: '2026-06-28T22:38:41.148077+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: 'Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - HELP: AIS:
  Não existe índice para esse alias no SINDEX'
type: support-article
updated_at: '2021-09-17T20:31:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020112831-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-HELP-AIS-N%C3%A3o-existe-%C3%ADndice-para-esse-alias-no-SINDEX
---

**Ocorrência**

Ao incluir um pedido de venda gera o HELP: **AIS: Não existe índice para esse alias no SINDEX**

**Ambiente**

Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - a partir da release 12.1.17.  
  
**Causa**

A tabela AIS trata-se de uma das novas tabelas de tratamento **REINF**, referente a aposentadoria Especial, o erro somente ocorre por que não existe o índice da Tabela no dicionário.  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
1. Baixar o SDFBRA do Reinf para atualização do dicionário;  
2. Após extrair na pasta system Load, rodar UPDDISTR para criação da tabela e índices;  
3. Reiniciar o sistema e  realizar o processo.

**Obs**: Caso o Ambiente esteja desatualizado, é necessário aplicar o ultimo pacote de atualizações do REINF (Data superior à Abril/2018).

Maiores detalhes sobre a Tabela acesse o documento técnico: **[DT Aposentadoria Especial - Faturamento](https://tdn.totvs.com/x/pOQgFQ)**
