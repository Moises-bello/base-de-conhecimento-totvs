---
content_hash: e57debaac8487d4269e880642b21ee849d0bebcfa38f75be3daa284c59ae1370
fetched_at: '2026-06-29T00:10:47.446633+00:00'
page_id: '557333203'
product: rm
source: tdn-rm
title: DT - Devolução e Descarte de EPI/EPC
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=557333203
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS RH |
| Linha de Produto: | DistribuiçãoConstrução ProjetosLinha RM |
| Segmento: | RH |
| Módulo: | Segurança e Saúde Ocupacional |
| Função: | Fornecimento Automático de EPI/EPC |
| Ticket: | N/A |
| Requisito/Story/Issue (informe o requisito relacionado) : | RHU01-11123: Devolução e Descarte de EPI/EPC |

## **02. SITUAÇÃO/REQUISITO**

Na operação de descartes/devoluções, o sistema não facilita na tomada de decisão no momento de devolver/descartar um EPI, ou seja, fica aberto para que o usuário realize a devolução/descarte por completo de todos os itens ativos no cadastro do funcionário o que pode causar descartes/devoluções indevidas.

## **03. SOLUÇÃO**

Para solucionar este problema foram criadas dois campos novos um no passo de **Seleção de Parâmetros** e outro no passo de definição da **Ação**.

Na tela de **Seleção de Parâmetros** foi acrescentado o campo **Aceito sugestão na ação**este campo só fica visível para a Devolução, Descarte e Cancelamento e sempre irá aparecer marcado dando a opção para o usuário desmarca-lo caso queira.

Caso o campo seja desmarcado, no passo de definir as Ações das EPIS/EPCs a coluna **Ação** ficará em branco obrigando o usuário a preenche-la ou unitariamente ou utilizando a opção de Setar itens selecionados. Não será possível passar para a próxima etapa até todos os itens estarem preenchidos. Caso ele esteja marcado o sistema se comportará da maneira normal.

Por ultimo nesta Tela da Ação o campo **Confirmo a realização da validação das ações configuradas**foi incluído para que o usuário o marque após o preenchimento e validação das ações.  Este parâmetro está presente em todos os tipos de fornecimento.  Só será possível passar para a próxima etapa quando este campo estiver marcado.
