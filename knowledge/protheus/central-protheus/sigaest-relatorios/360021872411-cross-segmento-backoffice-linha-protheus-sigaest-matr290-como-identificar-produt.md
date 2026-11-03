---
article_id: 360021872411
category: SIGAEST - RELATORIOS
content_hash: a98506ff10a87359fe8c61ac5bba46d8ddee9aa99d4c3b0be4a2f3bf2e690b2c
fetched_at: '2026-06-28T22:39:05.972625+00:00'
product: protheus
section_id: 1500001538841
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATR290 - Como identificar
  produtos obsoletos (Sem movimento) no estoque?
type: support-article
updated_at: '2025-03-12T12:23:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021872411-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATR290-Como-identificar-produtos-obsoletos-Sem-movimento-no-estoque
---

**Dúvida**

Como identificar produtos com obsolescência, ou seja, que estejam **sem movimentos** em determinado período?  
  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

É possível identificar produtos obsoletos (sem movimentos) pelo relatório **Análise de Estoques (MATR290)** permite que o usuário verificar seus produtos com obsoletos (sem movimentos) no parâmetro "**Lst só prod.obsolet ?"** **= Sim** e o parâmetro "**Dt.Limite p/obsolt ?"** Indicar a partir de qual período deseja que exiba os produtos que não foram movimentados.

**Exemplo como parametrizar o relatório para essa análise, dessa forma abaixo,** demonstra **apenas** os produtos que **não tiveram movimentos desde 31/12/2023:**

Data Atual = 30/09/2024

**Lst so prod.obsolet ?** = Sim

**Dt.Limite p/obsolt ?** = 31/12/2023

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26756246824471)

**Saiba mais:**

*[Análise de Estoques - MATR290](http://tdn.totvs.com/pages/viewpage.action?pageId=348295976)*

*[Clique aqui e veja mais artigos sobre Relatórios no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360012224673-SIGAEST-RELATORIOS)*

[SIGAEST - Identificar quando ocorreu a última Saída ou último movimento de um produto no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/articles/11569381611287-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Identificar-quando-ocorreu-a-%C3%BAltima-Sa%C3%ADda-ou-%C3%BAltimo-movimento-de-um-produto-no-Estoque)
