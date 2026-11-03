---
content_hash: 74c802646fb596b58dfe5454053f4d13144d7b1add57301a7f1dcc5dd6680fce
fetched_at: '2026-06-29T00:10:15.939243+00:00'
page_id: '465390115'
product: rm
source: tdn-rm
title: DT - Envio de crachá na integração com TSA/Suricato
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=465390115
version: 2
---

# Envio de crachá na integração com TSA/Suricato

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | RH |
| **Módulo:** | Automação de Ponto |
| **Função:** | Integração |
| **Situação/Requisito:** | Enviar o número de crachá do funcionário na integração com o TSA/Suricato. |
| **Solução/Implementação:** | Foi criada a funcionalidade de envio do número do crachá no webservice RM. O envio dessa informação será feito juntamente com as demais informações do funcionário quando este for enviado para o TSA/Suricato. O envio do crachá será disparado a partir do Chronus quando for realizada qualquer alteração no cadastro de funcionário, ao vincular incluir, alterar ou excluir um crachá através da tela de crachás associados, e também pela tela de anexo do funcionário. Para que o crachá seja enviado, ele deverá estar ativo e ser do tipo Funcionário, Provisório ou Treinamento. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | PONTO01-6410 |
| **Requisito:** | N/A |
| **Documento de Referência:** | N/A |
| **Pacote:** | N/A |
