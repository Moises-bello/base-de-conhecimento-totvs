---
content_hash: da2528aadbfda8bfa41227e15f48ea3369b4d197af266333f580805b6c8e264a
fetched_at: '2026-06-29T00:09:00.879858+00:00'
page_id: '370607544'
product: rm
source: tdn-rm
title: 3013306 MATESTCNTFTOF01-2442 DT Rastreabilidade de Movimentos - OS
type: documentation
url: https://tdn.totvs.com/display/LRM/3013306+MATESTCNTFTOF01-2442+DT+Rastreabilidade+de+Movimentos+-+OS
version: 3
---

# MOVIMENTOS RELACIONADOS A ORDEM DE SERVIÇO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Construção e Projetos. |
| **Módulo:** | Manutenção. |
| **Função:** | Movimentos Relacionados a OS. |
| **Situação/Requisito:** | Ao acessar a opção de Movimentos Relacionados pelo RMOfficina, alterar uma informação na capa do Movimento o sistema apresenta a seguinte mensagem "*O registro "XX" do detalhe "Ordem de Serviço" possui o campo "1º Identificador" obrigatório. Favor verificar este detalhe*."  A mensagem é apresentada, pois os dados de Ordem de Serviço são carregados para os movimentos que não são de Ordem de Serviço. |
| **Solução/Implementação:** | Ao acessar a opção de Movimentos Relacionados pelo RMOfficina e alterar uma informação na capa do Movimento não será apresentado a mensagem citada. A mensagem será apresentada somente para os movimentos de Ordem de Serviço quando não for informado o 1º Identificador do objeto de manutenção. |
| **Conversores e Parâmetros:** | Não se aplica. |
| **Tickets relacionados:** | Não se aplica. |
| **Requisito:** | MovMovimentoAction; MntMovRelationAction |
| **Documento de Referência:** | <https://tdn.totvs.com/display/public/LRM/O.S.+Normal> |
| **Pacote:** | Informe o [linkdopacote] |
