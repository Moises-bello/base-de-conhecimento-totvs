---
content_hash: 0553ac03744b7994cae4ea04304cf49deaf8744d8821b0ebb44ace8c075533cb
fetched_at: '2026-06-29T00:08:38.568184+00:00'
page_id: '285670541'
product: rm
source: tdn-rm
title: DT Vínculo de Produto na Tela de Condições Contratuais em Anexo Restrições
  do Contrato
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=285670541
version: 3
---

# Vínculo de produto na tela de condições contratuais em anexo restrições do contrato

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Restrições de Contrato | SauCondContratProibido | | Exceção à restrição de contrato | SauCondContratExcecao | |
| **Requisito****:** | SAUHRM02-1106 |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL Server® e Oracle® |
| **Sistema(s) Operacional(is):** | Windows® |

## Descrição

Em Condições Contratuais, para restringir um item o sistema deverá ter como base o Código do Produto (CODPRD) e não código(ESPECIFICO). Atualmente a referencia é o código especifico, isso gera retrabalho nas restrições quando este código muda.

## Procedimento para Utilização

1. Acesse **Cadastros/Faturamento/Condições Contratuais com Convênio**.
2. Selecione um registro e clique em **Anexos/Restrições de Contrato**.
3. Edite um registro de restrição contratual ou crie um novo.
4. Ao selecionar o tipo MATMED, o código salvo na seção Faixa será o CODPRD e não mais o código específico.
5. Novamente na tela de **Condições Contratuais**, selecione um registro e clique em **Anexos/Exceções à Restrição Contratual**.
6. Ao editar ou criar um novo registro, o código salvo será também o CODPRD e não mais o código específico do produto.
7. As rotinas e validações do sistema passarão a considerar o CODPRD para as restrições contratuais.
