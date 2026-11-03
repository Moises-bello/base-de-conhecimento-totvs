---
content_hash: 89efd74879879d1893747caa40fee1ccc42df9d8d86b2a0864c65be8c23e197b
fetched_at: '2026-06-29T00:10:22.632087+00:00'
page_id: '497927565'
product: rm
source: tdn-rm
title: Interface de Provisão Por Centro de Custo (PLR - 13° Salário - Férias)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=497927565
version: 12
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | RH |
| Módulo: | Folha de Pagamento |
| Função: | Possibilitar a visualização de Provisões (PLR, 13º Salário e Férias) por Centro de Custo |
| Requisito/Story/Issue | [1- FOPROTINAS01-8716](http://jiraproducao.totvs.com.br/browse/FOPROTINAS01-8716)  [2- FOPROTINAS01-8713](http://jiraproducao.totvs.com.br/browse/FOPROTINAS01-8713)  [3- FOPROTINAS01-8712](http://jiraproducao.totvs.com.br/browse/FOPROTINAS01-8712) |

## **02. SITUAÇÃO/REQUISITO**

Criação de uma interface para visualização das provisões de férias, 13° Salário e PLR, por centro de custo.

## **03. SOLUÇÃO**

Foram criados novos campos para o valor de provisão de PLR e mestres detalhes para exibição dos históricos por centro de custo. Localizados em:

"Funcionários >> Anexos >> Histórico >> Histórico de Provisão".

**PLR (Normal)**

**PLR (Centro de Custo)**

**Férias (Centro de Custo)**

**13° Salário (Centro de Custo)**

## **04. RESTRIÇÕES**

  As informações de provisão por centro de custo somente são exibidas se o parâmetro: "Contabilização de provisões acumuladas por centro de custo", estiver **marcado**.

     

* É obrigatório que o cliente vincule uma fórmula no parametrizador, para que a provisão por centro de custo de PLR seja gerada corretamente. É muito importante que após ser vinculada a fórmula a mesma **não** deve ser retirada do parametrizador, qualquer alteração que seja necessário deve ser realizada diretamente no texto da fórmula. Caso a fórmula seja retirada do parametrizador ou se o seu código for modificado o comportamento da interface será comprometido.
* Para que um registro de PLR seja visualizado é necessário que neste mesmo mês tenha sido gerada uma provisão de férias e/ou décimo terceiro.
* Se for editado um registro de férias por centro de custo e alterado algum campo que faz parte da chave primária da tabela, o registro correspondente de décimo terceiro desta tabela (caso haja), também será modificado. O mesmo ocorre para alterações nos registros de décimo terceiro. Caso a alteração ocorra de forma simultânea, o primeiro registro a ser alterado será o de férias, e o de 13° Salário será o segundo. Exemplo: Existe um registro na tabela com as seguintes informações: Mês, Ano,Código de Centro de Custo iguais, e valor de provisão de férias e valor de provisão de décimo terceiro diferentes, ambos tratam-se do mesmo registro exibidos em grids diferentes. Supondo que se realize uma alteração na grid de férias e altere o mês e simultaneamente altere na grid de 13° o valor. O sistema irá alterar primeiro o que se refere a férias, modificando consequente o registro de 13° também, pois o campo mês é chave. Quando o sistema tentar realizar a alteração de valor no décimo terceiro, não será efetivada pois o sistema irá buscar pela chave antiga.  É importante alterar registros chaves da tabela de forma separada.
* Não é permitido inserir um registro por centro de custo sem que haja um registro de provisão normal associado.
* Não é permitido incluir um registro com mês e ano posterior ao selecionado na visão.

## **5. OUTROS DOCUMENTOS**

<http://tdn.totvs.com/pages/releaseview.action?pageId=393357522>
