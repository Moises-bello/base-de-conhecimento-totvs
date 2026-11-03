---
article_id: 29988705874583
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 34f3ab4794840eb425c1524a2612c61e37fa61362ac844a59a8cd0ea4ae7a91c
fetched_at: '2026-06-28T22:38:33.044984+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Help "O campo do arquivo
  não existe no dicionário." na atualização de dicionário
type: support-article
updated_at: '2026-06-22T17:20:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/29988705874583-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Help-O-campo-do-arquivo-n%C3%A3o-existe-no-dicion%C3%A1rio-na-atualiza%C3%A7%C3%A3o-de-dicion%C3%A1rio
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29988690006935) Tempo aproximado para leitura: 00**:02:00 min** **Dúvida**Help "O campo do arquivo não existe no dicionário." na atualização de dicionário, como resolver?  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões  
  
**Solução**

Esse erro ocorre quando o campo está presente fisicamente na tabela do banco de dados, mas não está registrado no dicionário de campos (**SX3**).

Exemplo: O campo existe na tabela SA1 (A1\_CONTPOR), mas não existe no dicionário (X3\_CAMPO = 'A1\_CONTPOR')

1 - **Campo não cadastrado no SX3:** Caso não houve registro no dicionário de campos (SX3), o campo precisa ser incluído;

2 - **Inconsistência na SX2 (Dicionário de Tabelas) por filial:**

Em alguns casos, o erro pode ocorrer porque a **SX2 referencia a tabela para uma filial específica**, mas os campos correspondentes **não estão registrados no SX3 para essa mesma filial**.

É necessário verificar se os registros da SX2 e SX3 estão alinhados para todas as filiais envolvidas.

**Observação importante:** Caso utilize customizações, orientamos que contate seu analista in loco para realizar a manutenção, ou a Equipe TOTVS Hub via orçamento.

Dúvidas sobre a avaliação, contate a Equipe Protheus Framework.
