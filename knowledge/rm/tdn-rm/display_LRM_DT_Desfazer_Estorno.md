---
content_hash: 39b73f063bd788e6c121d70e046649b2b1e15afd7645e34c19628c074d2a8166
fetched_at: '2026-06-29T00:06:04.353703+00:00'
page_id: '200908883'
product: rm
source: tdn-rm
title: DT_Desfazer_Estorno
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_Desfazer_Estorno
version: 10
---

# Desfazer Estorno

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | Faturamento |
| **Rotina:** | |  | | --- | | **Nome Técnico** | | Lançamentos na conta do paciente | |
| **Requisito (ISSUE):** | PCREQ-6796 |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL e Oracle |
| **Sistema(s) operacional(is):** | Windows |
| **Versões/Release:** | 12.1.7 |

## Descrição

A funcionalidade de desfazer o estorno está vinculada diretamente a realização do estorno. Para que seja possível uma ação de desfazer um estorno, anteriormente deverá ser feito uma ação de estorno.

A validação de desfazer estorno deve ser semelhante a do estorno, sendo uma funcionalidade oposta à outra, isto a função de desfazer o estorno é voltar ao estado anterior da realização do estorno. Fazendo com que todos os valores e quantidades possam voltar a seu estado inicial anterior a realização do estorno.

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de atualizações da versão 12.1.7

1. Aplique o patch do chamado e execute uma vez a rotina*"Lançamento da conta do paciente"*.

## Procedimento para Utilização

1. Acesse o menu Faturamento /Particular e Convênios /Lançamentos na conta do paciente.
2. Selecione um atendimento com lançamentos.
3. Selecione alguns registros na grid com a tecla CTRL e clique no botão Estorno.
4. O perfil do usuário deve estar configurado para habilitar o botão de "Reverter Estorno indevido".
5. Selecione os registro estornados e clique no botão de **Reverter Estorno** indevido.
6. Os registros serão ativados novamente.
