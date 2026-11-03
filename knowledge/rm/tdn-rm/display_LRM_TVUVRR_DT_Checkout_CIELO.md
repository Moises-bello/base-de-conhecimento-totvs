---
content_hash: ad36b840a58965930f955e67d9c14ac9edbf173ee5e633f1707d31ecd5e33b5a
fetched_at: '2026-06-29T00:08:20.199770+00:00'
page_id: '268571625'
product: rm
source: tdn-rm
title: TVUVRR_DT_Checkout_CIELO
type: documentation
url: https://tdn.totvs.com/display/LRM/TVUVRR_DT_Checkout_CIELO
version: 111
---

# NOME DO REQUISITO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Gestão Financeira* |
| **Função:** | *Baixa Pagamento Cartão de Crédito* |
| **Situação/Requisito:** | *Ao efetuar um pagamento com cartão de crédito (Checkout Cielo), ocorre a mensagem de erro "[Customer.Identity] deve conter apenas números". Esse erro ocorre devido a mascara do CPF ou telefone do responsável financeiro do aluno quando é enviado para CIELO* |
| **Solução/Implementação:** | No momento de enviar o CPF e o telefone do responsável financeiro do aluno para a Cielo, a mascara do CPF será removida onde apenas os números deverão ser enviados |
| **Conversores e Parâmetros:** | N/A |
| **Chamados relacionados:** | *TVUVRR*  *XTJXYF* |
| **Requisito (ISSUE):** | PCREQ-8625 |

divs
