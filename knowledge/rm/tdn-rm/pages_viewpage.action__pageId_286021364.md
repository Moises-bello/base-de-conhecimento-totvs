---
content_hash: ce69dc5df077b00d0b1cebb28b56b56e50745308df8ed055bd187ff65a41e748
fetched_at: '2026-06-29T00:08:39.438651+00:00'
page_id: '286021364'
product: rm
source: tdn-rm
title: 1172612 DT Validação de faixa etária na inscrição do portal
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=286021364
version: 105
---

# Validação de faixa etária para pessoas sob sua responsabilidade

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | Processo Seletivo |
| **Função:** | Validação de faixa etária na inscrição do portal |
| **Situação/Requisito:** | Ao logar com um responsável com um endereço de uma área ofertada específica que possuía limite de faixa etária, a validação era realizada com a data de nascimento do responsável no momento do carregamento da página, informando que a data de nascimento não está dentro da faixa etária determinada pela área de interesse, e após isso, redirecionava o usuário para outra página, não possibilitando o usuário inscrever outra pessoa de sua responsabilidade. |
| **Solução/Implementação:** | Foi adicionado uma nova opção na tela de inscrição quando a pessoa possui outras pessoas sob sua responsabilidade. Desta forma, o usuário precisa informar previamente se a inscrição a ser realizada é para ele próprio ou para alguém de sua responsabilidade. Através dessa seleção é que será feita a validação da data de nascimento com a faixa etária nos processos seletivos que existem controle de Faixa etária.  Caso o próprio responsável, ou alguém de sua responsabilidade que ele tenha selecionado não esteja dentro da faixa etária determinada, irá aparecer uma mensagem logo abaixo das opções informando que a data de nascimento não está dentro do período estabelecido. Juntamente com isso, o botão de finalizar inscrição estará desabilitado.  Se o usuário selecionar outra área de interesse que não possua o controle de faixa etária, ou selecione outra pessoa que esteja dentro da faixa etária, esta mensagem será ocultada e o botão de Finalizar inscrição poderá ser habilitado novamente caso as demais opções estejam definidas corretamente. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A |

divs
