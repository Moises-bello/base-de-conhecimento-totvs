---
content_hash: e7a1f9b471fb42bf40854e9ad86e6c4f351733e138c29dc2caa4fe3c37cca2a7
fetched_at: '2026-06-29T00:08:53.055096+00:00'
page_id: '342308354'
product: rm
source: tdn-rm
title: DT Avanço Físico afeta Medição de Contrato
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=342308354
version: 3
---

# AVANÇO FÍSICO AFETA MEDIÇÃO DE CONTRATO

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | ***RM*** |
| **Segmento:** | ***Construção e Projetos*** |
| **Módulo:** | ****Gestão de Obras e Projetos**** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Mobilidade* | *Mobilidade* | | *Contratos* | *Contratos* |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | **Apontamento de Avanço Físico** | **Apontamento de Avanço Físico** | | *Edição de Apontamentos* | *Edição de Apontamentos* | | *Validar Apontamentos* | *Validar Apontamentos* | | *Atualizar Pert* | *Atualizar Pert* | | *Medição de Itens de Contrato* | *Medição de Itens de Contrato* | |
| **Cadastros Iniciais:** | *Projeto, Tarefa, Folha Tarefa, Contratos, Períodos de Contrato* |
| **Parâmetro(s):** | *Não se aplica* |
| **Ponto de Entrada:** | *Não se aplica* |
| **Tickets relacionados** | *Não se aplica* |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | *TOPORCAPLAN-2794* |
| **País(es):** | *Brasil* |
| **Banco(s) de Dados:** | *SQL Server e Oracle* |
| **Tabelas Utilizadas:** | *Não se aplica* |
| **Sistema(s) Operacional(is):** | *Windows, Android, iOS* |

## Descrição

Apontamentos de Avanço Físico realizados no módulo de Mobilidade podem afetar diretamente a medição de itens de contrato.

## Procedimento para Utilização

A partir do APP Minha Obra é possível criar/alterar medições de itens de contrato através dos apontamentos de Avanço Físico dos itens da Folha Tarefa, sendo via coletor ou apontamento manual. Para que essa incidência ocorra, é necessário vincular o contrato desejado ao item associado à folha tarefa, porém é necessário considerar algumas premissas:

* A tarefa deve ser definida antes do contrato;
* As datas início e fim do contrato devem fazer interseção com as datas início e fim da folha tarefa;
* A tarefa selecionada deve estar associada ao contrato;
* Ao salvar a associação do contrato ao item, caso o parâmetro de medição acima de 100% estiver diferente de SEMPRE PERMITIR, será verificado se a quantidade planejada do item da folha é maior que a quantidade do saldo do item no contrato, o que não deve ser permitido.

No processo de Validar Apontamento de Avanço Físico o parâmetro de medição acima de 100% também é verificado e se estiver diferente de SEMPRE PERMITIR, e a quantidade apontada do item da folha for maior que a quantidade do saldo do item nocontrato, um alerta será exibido, não permitindo a execução.

No processo de Atualizar PERT o parâmetro de medição acima de 100% também é verificado e se estiver diferente de SEMPRE PERMITIR, e a quantidade apontada do item da folha for maior que a quantidade do saldo do item no contrato, um alerta será exibido, não permitindo a execução. Caso as validações estejam aprovadas, a quantidade apontada do item será incorporada à medição do item no contrato, no respectivo período que corresponde à DATA DE APONTAMENTO do item da folha. Se o período do contrato estiver liberado, a medição não será inserida e o erro deverá ser exposto.

Na tela de medição de itens, nos períodos do contrato, é possível consultar os apontamentos que influenciaram na medição do item corrente, basta selecionar o item no grid e clicar no botão .
