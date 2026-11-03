---
content_hash: 70668b0ea43ad415c7ee0e3caebd43d28bdcc9c7c9026c210b1d117ee989e49e
fetched_at: '2026-06-29T00:08:35.941443+00:00'
page_id: '283384285'
product: rm
source: tdn-rm
title: 717361 FOPROTINAS01-580 DT Erro ao Acessar Cadastro de Sindicatos
type: documentation
url: https://tdn.totvs.com/display/LRM/717361+FOPROTINAS01-580+DT+Erro+ao+Acessar+Cadastro+de+Sindicatos
version: 109
---

# CADASTRO DE SINDICATOS

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Folha de Pagamento |
| **Função:** | Cadastro de Sindicatos |
| **Situação/Requisito:** | Ao tentar incluir ou editar um registro de sindicato no sistema, é apresentada a seguinte mensagem: "Valor não pode ser nulo. Nome do parâmetro: value". A mensagem é mostrada pela existência de um registro de País sem Descrição na base de dados, que era lido e, ao tentar incluí-lo na listagem  de países para cadastrar o endereço do sindicato, era disparada a mensagem. |
| **Solução/Implementação:** | Ao recuperar um País sem descrição da base de dados, será inserido o código do país seguido de " - Sem Desc" na listagem de países. |
| **Tickets relacionados:** | 717361 |

divs
