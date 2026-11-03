---
content_hash: 31a93c2ad30f5bb46faaeaad923b9c7f1d848ca0b86dca7c3ba402bb3a08d11d
fetched_at: '2026-06-29T00:09:09.079342+00:00'
page_id: '392495321'
product: rm
source: tdn-rm
title: 3344016 FISCAL01-5961 DT - Período de Apuração - Encerramento do periodo de
  apuração do ICMS
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=392495321
version: 1
---

# Encerramento do período de apuração do ICMS com DIFAL

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Serviços |
| **Módulo:** | Totvs Gestão Fiscal |
| **Função:** | Encerramento de Período de Apuração |
| **Situação/Requisito:** | Ao encerrar o período de apuração de ICMS o sistema retorno erro abaixo:  Erro no encerramento do(s) período(s): Período Filial 1 - Tributo ICMS - 01/06/2018 - 30/06/2018:  Erro na Apuração dos Valores de Diferencial de Alíquota. Erro: A coluna 'CODCOLIGADA, IDPER, CODETD' está restrita a conter valores exclusivos. O valor '1, 6398, SP' já existe. |
| **Solução/Implementação:** | - Na escrituração de lançamentos fiscais quando informado cliente fornecedor no movimento e este for o destinatário final da mercadoria será considerado a UF do Histórico do cliente fornecedor do movimento e não a UF atual do cliente fornecedor.  - Foi removida a consistência de natureza fiscal do lançamento quando o movimento é escriturado.  - Foi incluído consistência no lançamento fiscal para verificar se o mesmo está vinculado a lançamento de Outros débitos e créditos. |
