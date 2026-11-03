---
content_hash: 05b7c12b54d28849440ffc6533e070b79d60e3c3d79b7d3ca8de475348001fd1
fetched_at: '2026-06-29T00:08:05.221766+00:00'
page_id: '235587807'
product: rm
source: tdn-rm
title: TUNSTH_DT_Baixa_Cancelamento_da_Baixa
type: documentation
url: https://tdn.totvs.com/display/LRM/TUNSTH_DT_Baixa_Cancelamento_da_Baixa
version: 111
---

# Baixa - Cancelamento da Baixa

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Gestão Financeira* |
| **Função:** | Baixa - Cancelamento da Baixa |
| **Situação/Requisito:** | Cancelamento de baixa de lançamentos agrupados com 2 formas de pagamento     Ao realizar a baixa de lançamentos agrupados com 2 meios de pagamento (dinheiro e cartão) em seguida cancelar a baixa somente de 1 lançamento o sistema irá deixar o outro lançamento parcialmente baixado. Ao verificar o extrato de caixa do lançamento parcialmente baixado nota-se que possui 2 extratos sendo que 1 e do meio de pagamento dinheiro e outro do meio de pagamento cartao que está cancelado. E ao verifcar na aba dados adicionais o meio de pagamento do extrato de caixa, nota-se que não e apresentado qual o meio de pagamento do extrato referente as baixas (1 extrato do meio pag. dinheiro e 1 extrato do meio de pag. catão que foi cancelado a baixa).     O erro ocorre somente quando o lançamento e baixado agrupado e com uma forma de pagamento com tipo primitivo Dinheiro. |
| **Solução/Implementação:** | Otimização no processo de cancelamento de baixas do lançamento para não gerar extratos de caixa para lançamentos cancelados. |
| **Conversores e Parâmetros:** | *Informe os conversores/parâmetros.* |
| **Chamados relacionados:** | *Informe o(s) chamado(s) relacionado(s).* |
| **Requisito (ISSUE):** | FIN000041 |

divs
