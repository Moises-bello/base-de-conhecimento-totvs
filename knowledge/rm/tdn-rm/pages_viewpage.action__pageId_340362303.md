---
content_hash: cd815608f36a1d1ab3fdebaef4694edfd3bebbbb11c8bd0d58bbdbbfc4d916ac
fetched_at: '2026-06-29T00:08:52.400532+00:00'
page_id: '340362303'
product: rm
source: tdn-rm
title: DT Geração da Prévia de Valores dos Lançamentos Financeiro
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=340362303
version: 17
---

# Prévia de Valores dos Lançamentos Financeiro

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Gestão Educacional |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Gerar / Excluir Prévia de Valores do Lançamento | Gerar / Excluir Prévia de Valores do Lançamento | | Visualização dos Valores da Prévia | Visualização dos Valores da Prévia | | Excluir Prévia dos Valores do Lançamento | Excluir Prévia dos Valores do Lançamento | | Cubo da Prévia do Faturamento Financeiro | Cubo da Prévia do Faturamento Financeiro | | Cubo da Prévia das Bolsas do Faturamento Financeiro | Cubo da Prévia das Bolsas do Faturamento Financeiro |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | |  |  | |  |  | |
| **Cadastros Iniciais:** |  |
| **Parâmetro(s):** |  |
| **Ponto de Entrada:** |  |
| **Tickets relacionados** |  |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** |  |
| **País(es):** |  |
| **Banco(s) de Dados:** |  |
| **Tabelas Utilizadas:** |  |
| **Sistema(s) Operacional(is):** |  |

## Descrição

Para eventuais conferências ou previsão de receita referentes a valores financeiros o usuário, anteriormente, só conseguia estas informações após a geração dos lançamentos financeiros ou através da simulação da parcela individualmente por aluno.

Disponibilizamos a possibilidade do usuário gerar prévias dos valores correspondentes aos lançamentos financeiros com objetivo de facilitar a conferência dos valores que irão compor o lançamento financeiro ou até mesmo prever a receita.

A geração destas prévias serão armazenadas no banco de dados e estarão disponíveis para ser consultadas através do módulo TOTVS Gestão Educacional e no módulo TOTVS Inteligência de Negócios através dos cubos criados para importação.

Toda a geração dos valores de prévia serão baseadas nas configurações das parcelas, bolsas e descontos.

## Procedimento para Implantação

Para utilizar os recursos referentes à geração da prévia é importante conceder no perfil do usuário as devidas permissões.

## Procedimento para Utilização

* **Gerar / Excluir Prévia de Valores do Lançamento**

Processo responsável em gerar a prévia dos valores do lançamento conforme os filtros aplicados.

O processo poderá ser acessado em:

O processo de geração dos valores de prévia é semelhante ao processo de geração de lançamento, porem a saída final é uma prévia dos valores que deverão compor o lançamento financeiro futuramente.

**Opção: Tipo de execução**

**Gerar prévia:** o processo será executado no modo de geração da prévia, ou seja, o sistema vai realizar a simulação da geração de lançamentos e gravar os valores conforme as informações do processo.

**Excluir prévia:** o processo será executado no modo de exclusão, ou seja, o sistema vai excluir as prévias já processadas conforme as informações do processo.

O usuário poderá executar a exclusão da prévia somente se tiver permissão habilitada no perfil, caso contrário o processo apresentará uma mensagem bloqueando a execução da exclusão.

**Opção “Considerar nos cálculos da prévia o desconto por antecipação ”:**

Com esta opção marcada ao realizar o cálculo do valor liquido para a parcela o sistema vai considerar o desconto por antecipação parametrizado. Na prévia será possível identificar se os valores foram processados levando em consideração o desconto por antecipação ou não.

* **Visualização dos Valores da Prévia**

Todos os valores processados para a prévia poderão ser consultados em:

Serão apresentados todos os valores processados pelo processo de geração da prévia.

Como facilitador foram disponibilizadas várias informações que poderão auxiliar nos filtros e análises dos dados, tais como: período letivo, curso, turno, matriz aplicada, habilitação, serviço, usuário que processou.

Foi disponibilizado o anexo de detalhamento dos valores de prévia das bolsas.

As informações referentes aos valores de prévia ficarão armazenados nas tabelas SPREVIALAN e SPREVIABOLSALAN

Também será possível excluir uma prévia pela visualização, para isto acesse o menu de processo e clique em “Excluir Prévia dos Valores do Lançamento”.

Serão excluídas todas as prévias selecionadas na visão.

| Atenção  Sempre que houver alteração de valores de parcelas, bolsas e descontos ou para os casos em que a parcela é calculada por crédito e houver alteração na matriz curricular a prévia ficará desatualizada, sendo necessário executar o processo de geração novamente. |
| --- |

* **Importação dos Cubos**

Foram disponibilizados 2 cubos para a visualização de dados consolidados da prévia. Para que eles sejam importados é necessário que o usuário tenha um perfil com permissões na funcionalidade de Cubos no TOTVS Inteligência de Negócios. Também é necessário que o perfil do usuário tenha permissão de importação na categoria de cubos na qual o Cubo será importado.

**Verificação da categoria do cubo:**

**Importação dos Cubos:**

Para cada um dos cubos será necessário realizar a importação conforme os passos abaixo:

Selecionar o cubo desejado no diretório de Objetos Gerenciais dentro da instalação do CorporeRM.

Selecionar os checkboxes do cubo adicionado, informa as coligadas para as quais o cubo será importado, selecionar uma categoria na qual o perfil do usuário tenha permissão para importar cubos e executar a importação.

Cubos importados na base.

* **Visualização dos cubos:**

Para visualizar os cubos pela primeira vez é necessário que ele seja atualizado, o que pode ser feito via processo ou via duplo clique nele.

A atualização dos cubos é importante para que se trabalhe com dados atualizados, uma vez que os cubos não trabalham em cima da base de dados padrão, eles trabalham sobre dados processados e consolidados pelo processo de atualização do cubo.

Na primeira vez que acessar os cubos será necessário organizar as colunas disponíveis nele da forma que preferir, e ao término dessa configuração salvá-la, para que quando o mesmo usuário acessá-lo novamente não seja necessário montá-lo novamente.

O cubo vai propiciar uma visão dinâmica dos dados consolidados, sendo possível agrupá-los por diversos agrupadores e em tempo de visualização poderá incluir, excluir e reordenar agrupadores e dados de valores.

**EDUCUB0004 - Prévia Faturamento Financeiro**

Cubo onde é possível visualizar agrupados os dados das prévias de lançamentos financeiros, onde é possível agrupar desde uma parcela/cota até o período letivo (dentre diversos níveis de agrupamentos).

Como sugestão de agrupamentos pode ser feito o seguinte arranjo (dentre vários outros possíveis):

* Área de registros (Onde estarão os dados a que serão agrupados):
  + Período Letivo, Serviço, Curso, Aluno, Contrato, Parcela e Cota.
* Área de dados (Onde estarão os valores):
  + Valor Líquido, Valor Original, Valor Desconto, Valor de Bolsas Condicionais, Valor de Bolsas Incondicionais, Valor de Crédito Retroativo e Valor de Desconto por Antecipação.

O cubo ficará desta forma após ser organizado segundo a sugestão acima:

A atualização deste cubo é baseada na coligada, filial e nível de ensino logado pelo usuário por  em consulta SQL . Para visualizar as informações de outra coligada, filial ou ensino superior basta alterar uma dessas informações no contexto do sistema. E atualizar os dados no cubo. Recomenda que antes de mudar as informações no contexto para outra coligada, filial ou nível de ensino realizar uma exportação das informações atuais no cubo.

**EDUCUB0005 - Prévia das Bolsas do Faturamento Financeiro**

Cubo onde é possível visualizar agrupados os dados das bolsas das prévias de lançamentos financeiros, onde é possível agrupar desde alguns atributos de bolsa até o período letivo (dentre diversos níveis de agrupamentos).

Como sugestão de agrupamentos pode ser feito o seguinte arranjo (dentre vários outros possíveis):

* Área de registros (Onde estarão os dados a que serão agrupados):
  + Período Letivo, Serviço, Curso, Aluno, Contrato, Parcela, Cota, Tipo de Sacado, Sacado, Bolsa, FIES e Bolsa Condicional.
* Área de dados (Onde estarão os valores):
  + Valor da Prévia da Bolsa.

O cubo ficará desta forma após ser organizado segundo a sugestão acima:

A atualização deste cubo é baseada na coligada, filial e nível de ensino logado pelo usuário por  em consulta SQL . Para visualizar as informações de outra coligada, filial ou ensino superior basta alterar uma dessas informações no contexto do sistema. E atualizar os dados no cubo. Recomenda que antes de mudar as informações no contexto para outra coligada, filial ou nível de ensino realizar uma exportação das informações atuais no cubo.
