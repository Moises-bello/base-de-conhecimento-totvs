---
content_hash: b407280740d3b98f89b0cba664aee039f9351f9736aa11951bb44850dc5d189c
fetched_at: '2026-06-29T00:10:20.257952+00:00'
page_id: '490335926'
product: rm
source: tdn-rm
title: DT Parâmetro de Utiliza PERT
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=490335926
version: 3
---

i

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | *RM* |
| Segmento: | *Construção e Projetos.* |
| Módulo: | **Gestão de Obras e Projetos*.* |
| Função: | Não utilizar PERT |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | [TOPORCAPLAN001-7392](http://jiraproducao.totvs.com.br/browse/TOPORCAPLAN001-7392) |

## **02. SITUAÇÃO/REQUISITO**

Foi levantada a necessidade da utilização do TOP Mobile sem a utilização do PERT.

Para tal, será utilizado o parâmetro "Utiliza PERT" para que o mesmo identifique os projetos em que o PERT realmente não será utilizado.

## **03. SOLUÇÃO**

Ao desmarcar a opção "Utiliza PERT", o sistema passará a não exibir o menu do PERT, nem as opções de Sincronismo com o Project. Também será removido o processo de Exportar PERT para o Cronograma.

Para que o TOP Mobile utilize as datas do cronograma para a sua programação, no cálculo do cronograma serão preenchidos os campos de data de Data Início e Fim Programados da tarefa com as datas do cronograma.

Quando o parâmetro de mobilidade "Atualizar o PERT / Cronograma automaticamente ao sincronizar e ao salvar o apontamento de Avanço Físico" estiver marcado e o projeto não utilizar PERT, será salvo no cronograma realizado o percentual do apontamento do item da folha tarefa. Este percentual sempre irá para o primeiro período aberto.
