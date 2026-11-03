---
article_id: 360018568632
category: PCO - Cubos
content_hash: 28ca7a3bfa4711bf2ebe6d983787b756bb689517277a45d2c8c35a32b092886c
fetched_at: '2026-06-28T22:37:11.544932+00:00'
product: protheus
section_id: 1500001550862
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGAPCO - PCOA300 Help: PCOA300CB
  - Cubo XX inconsistente, favor reprocessar.'
type: support-article
updated_at: '2023-11-21T13:02:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018568632-Cross-Segmento-Backoffice-Linha-Protheus-SIGAPCO-PCOA300-Help-PCOA300CB-Cubo-XX-inconsistente-favor-reprocessar
---

**Dúvida**Help: PCOA300CB - Cubo XX inconsistente, favor reprocessar.

**Ambiente**Protheus – SIGAPCO – A partir da versão 11.80  
  
   
**Solução**

Caso seja Reprocessado os Saldos do Cubo através da Rotina PCOA300 e seja apresentado a mensagem:

**Help: PCOA300CB - Cubo XX inconsistente, favor reprocessar**

Por gentileza tente realizar o seguinte procedimento:

1º Será necessário considerar todos os lançamentos existentes da Tabela AKD dentro do período, para tanto será necessário executar a seguinte Query (via SQL) para identificar este período:

**SELECT MIN(AKD\_DATA), MAX(AKD\_DATA) FROM AKD010 WHERE AKD\_STATUS = '1' AND D\_E\_L\_E\_T\_ = ' '**

Obs: O resultado desta Query apresentará a Data Mínima e Máxima de Lançamento dentro da Tabela ADK - Lançamentos

2º A partir desta Data será necessário informar as mesmas dentro dos parâmetros: Data de ? / Data Até ? (parâmetros da Rotina PCOA300)

Obs: Recomenda-se também reprocessar: **Tipos de Saldo = Todos**

**Tipos de Saldo Base = (conteúdo em branco)**

3º Ao finalizar o reprocessamento, será apresentado a seguinte mensagem: **Verificado Saldos das contas analíticas e os cubos foram processados com Sucesso.**

**Importante**

|  |
| --- |
| Importante: É necessário ter as Stored Procedures: p11\_12.sps e p11\_13.sps + Fonte: PCOXSLD devidamente atualizados (conforme última versão disponível em Download no Portal do Cliente Totvs) |
