---
content_hash: 3c864f37a42fe65869bd1091f7291a85937a986af808c21d769e64a48200b68b
fetched_at: '2026-06-29T00:06:25.484714+00:00'
page_id: '224397677'
product: rm
source: tdn-rm
title: DT_Transferencia_de_candidatos_entre_coligadas
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_Transferencia_de_candidatos_entre_coligadas
version: 1
---

# TRANSFERÊNCIA DE CANDIDATOS ENTRE COLIGADAS

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | **TOTVS Folha de Pagamento** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Rescisão* | *Funcionário* | |
| **Versão/Release:** | *12.1.4* |

## Descrição

No módulo de Transferência de funcionários, o flag “**Ignorar cópia de faixa/nível salarial do histórico de função quando não existirem na coligada de destino**”, tem como objetivo possibilitar a cópia do histórico de funções quando na coligada destino não houver a tabela, faixa e níveis salariais associados as funções do funcionário.

## Procedimento para Utilização

Para que o usuário tenha acesso a transferência é preciso demitir o funcionário. Acesse **Folha de Pagamento / Funcionário**, selecione o funcionário e clique no ícone “Rescisão”

Em “Aviso Prévio” informe o tipo de demissão

Na aba “Rescisão” informe os campos “Motivo de Demissão” e “Motivo de Mudança” e as datas, que precisam ser preenchidas de acordo com a data do envelope de pagamento do funcionário. Salve. Obs.: Para consultar o envelope de pagamento, selecione um funcionário e clique no ícone “Envelope”

Concluída a demissão do funcionário. O próximo passo é transferir o funcionário para a coligada destino, para isto clique em “Transferir Funcionário” e será direcionado para a tela “Parâmetros de Transferência”.

Nesta tela é preciso informar a coligada destino no campo “Nova Coligada” e marcar o flag “Transfere histórico” para habilitar a marcação do flag “Ignorar cópia de faixa/nível salarial do histórico de função quando não existirem na coligada de destino”

Logo após, preencha os Dados de Transferência e execute a próxima tela.

Depois da execução ter sido concluída, verificar se o funcionário foi transferido e se as informações do histórico de função foram copiadas para a coligada destino. Para isto, acione a coligada de destino e acesse o cadastro do Funcionário Anexos / Históricos / Histórico de Função.

Observe abaixo que o histórico de função do funcionário foi copiado na coligada destino
