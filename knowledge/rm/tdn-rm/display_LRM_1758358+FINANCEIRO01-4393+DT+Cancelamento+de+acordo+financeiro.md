---
content_hash: 2e68ed4e0b4df61664d93b1165388382214ca57aaa3128f4652b31381ae41e0e
fetched_at: '2026-06-29T00:08:48.889450+00:00'
page_id: '329028553'
product: rm
source: tdn-rm
title: 1758358 FINANCEIRO01-4393 DT Cancelamento de acordo financeiro
type: documentation
url: https://tdn.totvs.com/display/LRM/1758358+FINANCEIRO01-4393+DT+Cancelamento+de+acordo+financeiro
version: 87
---

# CANCELAMENTO DE ACORDO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Gestão Financeira |
| **Função:** | Cancelamento de acordo |
| **Situação/Requisito:** | Gera-se um Acordo para o cliente, agrupando alguns lançamentos e inserindo nesta negociação um valor de acréscimo qualquer. Por algum motivo, foi necessário gerar um novo Acordo deste título já negociado anteriormente. A operação é realizada com sucesso, mas por algum motivo será necessário cancelar esta segunda negociação. Ao cancelar o segundo Acordo, o sistema está zerando o valor de acréscimo do primeiro Acordo e na aba Valores a subpasta Acordo não é mais exibida. |
| **Solução/Implementação:** | Otimizado o processo de cancelamento de acordo para verificar se deve ser atualizado os valores de acordo no lançamento de origem. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |

divs
