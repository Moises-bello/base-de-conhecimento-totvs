---
content_hash: b1e80daaf9f59a93e64de1f88ce0bd65982cd2d1ed7de4cd99033be92072c193
fetched_at: '2026-06-29T00:09:08.274450+00:00'
page_id: '385864019'
product: rm
source: tdn-rm
title: 661097 PORTALMOBILE01-563 DT Rematrícula online sem gerar lançamentos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=385864019
version: 1
---

# Rematrícula online sem gerar lançamentos

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | Portal Educacional |
| **Função:** | Matrícula Online |
| **Situação/Requisito:** | O sistema está associando a impressão do contrato financeiro, com o processo de geração de lançamentos na Matricula Online. Ou seja, os lançamentos são gerados através da matrícula online apenas se o cliente marcar a opção de imprimir o contrato financeiro nos parâmetros do sistema. |
| **Solução/Implementação:** | A rotina de matrícula online foi alterada para os seguintes cenários:    1) Parâmetro [Educacional > RM Portal > Matrícula > Contrato Financeiro > Disponível para impressão] marcado:    1.1) contrato existente    1.1.1) caso tenha alterado o plano de pagamento o contrato será atualizado com o novo plano de pagamento; 1.1.2) os campos [data de assinatura] e [assinado] da tabela de contrato serão atualizados. 1.1.3) se parametrizado [Educacional > RM Portal > Matrícula > Gerar lançamento > Gerar lançamentos] marcado será gerado o lançamento.    1.2) caso não tenha contrato será gerado um novo   1.1.1) os campos [data de assinatura] e [assinado] da tabela de contrato serão atualizados. 1.1.2) se parametrizado [Gerar lançamentos] marcado será gerado o lançamento.    2) Parâmetro [Disponível para impressão] DESmarcado:    1.1) contrato existente    1.1.1) o contrato não será atualizado 1.1.2) se parametrizado [Gerar lançamentos] marcado será gerado o lançamento.    1.2) caso não tenha contrato não será criado devido o parâmetro [Disponível para impressão] consequentemente também não será gerado lançamento. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A |
| **Documento de Referência:** | N/A |
