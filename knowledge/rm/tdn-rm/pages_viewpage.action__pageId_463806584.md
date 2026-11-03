---
content_hash: d4d8d4acf3fc1b916225ef70dfd43a9dd73a198d0a383d2b15b45b0bb19bf6c6
fetched_at: '2026-06-29T00:10:15.108708+00:00'
page_id: '463806584'
product: rm
source: tdn-rm
title: 5045667 FISCAL01-8061 DT Falha na escrituração ao encontrar período do tributo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=463806584
version: 1
---

# Falha ao encontrar o período entre meses distintos

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Serviços |
| **Módulo:** | TOTVS Gestão Fiscal |
| **Função:** | Escrituração |
| **Situação/Requisito:** | Ao realizar a escrituração de lançamentos, é apresentado o seguinte erro informando período de apuração fechado ou inexistente para o tributo, porém o período do tributo existe e está aberto.  Erros no Serviço de Inclusão de Lançamentos  ---------------------------------------------------------------------------------  Erro na Inclusão do Registro:  Filial 1 - Documento 000046463 - Série 000 - Data 21/01/2019:  Período de Apuração do(s) Tributo(s) <NOME DO TRIBUTO> não está aberto para movimentação.  --------------------------------------------------------------------------------- |
| **Solução/Implementação:** | O período de apuração foi configurado da seguinte forma:              O lote de escrituração possui período inicial de 01/01/2019 a 31/01/2019:            Os movimentos deste lote estão compreendidos no período de 21/01/2019 a 28/01/2019.     O movimento que não estava sendo escriturado, possui data de lançamento do dia 28/01/2019:                O erro ocorria por que o sistema buscava os períodos com data de início menor do que 21/01/2019 e data de fim maior que 28/01/2019 OU data de início maior que 01/01/2019 e data de fim menor que 31/01/2019. Desta forma, só encontrava o seguinte período:      Pois o período de 27/01/2019 a 02/02/2019 extravasa o mês. Ao passo que o lançamento em questão não está neste período. Por isso o erro.  A solução foi buscar os períodos com data de início entre 21/01/2019 e 28/01/2019 OU data de fim entre 21/01/2019 e 28/01/2019 OU data de início maior que 01/01/2019 e data de fim menor que 31/01/2019. |
