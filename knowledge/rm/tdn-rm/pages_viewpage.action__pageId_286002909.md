---
content_hash: a44037c4138fca8d3afa40feccf2873b7103e45f6e7d945a885a2c271754d7a4
fetched_at: '2026-06-29T00:08:38.961912+00:00'
page_id: '286002909'
product: rm
source: tdn-rm
title: 1140341 MATESTCNTFTOF01-462 DT Cancelamento de Solicitação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=286002909
version: 98
---

# CANCELAMENTO DE SOLICITAÇÃO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Construção e Projetos. |
| **Módulo:** | TOTVS Gestão de Estoque, Compras e Faturamento. |
| **Função:** | Cancelamento de OS e Cancelamento de Solicitação. |
| **Situação/Requisito:** | Ao Cancelar uma Ordem de Serviço no Manutenção de Ativos (SigaMNT) a Solicitação de Armazém associada a esta Ordem de Serviço não foi encontrada no BackOffice, impedindo o Cancelamento da OS. Este caso ocorreu porque o parâmetro MV\_NGMNTAS estava configurado no Protheus com valor 1 que significa Aglutinar Solicitações de Armazém para mesma Ordem de Serviço. Nesta situação a tag RequestInternalId da mensagem CancelRequest vem com o valor da chave com base na SA e o adapter do RM estava considerando o valor da chave do Item da SA. |
| **Solução/Implementação:** | O adapter de Cancelamento de Solicitação - CancelRequest\_1.000 foi ajustado para considerar as opções referentes ao parâmetro do Protheus MV\_NGMNTAS - Aglutina Solicitação de Armazém para mesma Ordem de Serviço (1=Sim / 2 = Não). Ao receber a mensagem CancelRequest, o adapter irá buscar na tabela De-Para o registro com base na informação enviada. Caso não encontre registro pela tabela Item de Movimento, será pesquisado pela tabela de Movimento. Caso não encontre será apresentada mensagem "Erro ao cancelar requisição: Requisição informada não foi encontrada no BackOffice." |
| **Conversores e Parâmetros:** | Para atualizar o adapter no RM realize os seguintes passos:   1. Acesse RM \ Integração \ Integração \ Mensagem Única \ Integrações. Selecione a integração de Identificador 1001 e abra o anexo Mapeamento de Entidades. Edite o registro CANCELREQUEST, acesse o link do evento e clique em excluir. 2. No anexo Mapeamento de Entidades exclua o registro CANCELREQUEST. 3. Acesse Ferramentas \ Configurar, avance até a etapa Projetos de Integração. Selecione o item TOTVS Manutenção de Ativos x BackOffice RM e execute o processo para atualizar o adapter CancelRequest. |
| **Tickets relacionados:** | 1140341. |
| **Requisito:** | Integração Manutenção de Ativos x BackOffice RM. |

divs
