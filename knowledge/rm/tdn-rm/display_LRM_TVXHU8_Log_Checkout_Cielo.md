---
content_hash: 2c75287128fb52ccb051c21b21152369ae385827a8a5da45a6f2924f4ba7aa4f
fetched_at: '2026-06-29T00:08:19.309658+00:00'
page_id: '267780584'
product: rm
source: tdn-rm
title: TVXHU8_Log_Checkout_Cielo
type: documentation
url: https://tdn.totvs.com/display/LRM/TVXHU8_Log_Checkout_Cielo
version: 111
---

# Baixa Pagamento Cartão de Crédito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Gestão Financeira* |
| **Função:** | *Baixa Pagamento Cartão de Crédito* |
| **Situação/Requisito:** | *Ao efetuar um pagamento com cartão de crédito (Checkout Cielo), a baixa não ocorre e não é apresentada mensagem nenhuma o porquê o lançamento não foi baixado* |
| **Solução/Implementação:** | *Disponibilizar a gravação de arquivo de log, contendo a mensagem caso ocorra algum problema após Cielo chamar as rotina de notificação e mudança de status* |
| **Conversores e Parâmetros:** | *Parâmetro:* *"Gravar arquivo de log quando ocorrer erro no processamento de notificação e mudança de status" em "Parametrizador | Contas a Receber | Baixa | Cartão de Crédito/Débito | Configurações Gerais 2/2"* |
| **Chamados relacionados:** | *TVTOLR.* |
| **Requisito (ISSUE):** | PCREQ-8625 |

divs
