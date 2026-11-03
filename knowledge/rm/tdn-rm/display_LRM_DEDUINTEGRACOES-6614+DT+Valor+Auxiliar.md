---
content_hash: 263b44ab168e8d7c2ad959bb3affd2da75216eb45bb77bb152efed51dd2ebee4
fetched_at: '2026-06-29T00:10:35.381428+00:00'
page_id: '528914247'
product: rm
source: tdn-rm
title: DEDUINTEGRACOES-6614 DT Valor Auxiliar
type: documentation
url: https://tdn.totvs.com/display/LRM/DEDUINTEGRACOES-6614+DT+Valor+Auxiliar
version: 21
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Educacional |
| Módulo: | TOTVS Educacional |
| Função: | Cadastro |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DEDUINTEGRACOES-6614](https://jiraproducao.totvs.com.br/browse/DEDUINTEGRACOES-6614) |

## **02. SITUAÇÃO/REQUISITO**

Diante de alguns cenário apresentados pelos cliente surgiu a necessidade de controlar de forma paralela e especifica valores relacionados ao processamento das bolsas e descontos por antecipação calculados durante geração do lançamento financeiro do aluno.

## **03. SOLUÇÃO**

Foi implementado no TOTVS Educacional o recurso do “Valor Auxiliar”.

O “Valor Auxiliar” possibilita ao cliente que tem alguma particularidade definir no TOTVS Educacional valores auxiliares que terão o objetivo de armazenar valores provenientes de regras especificas e que estão relacionadas a bolsa ou desconto por antecipação.

**Como funciona:**

Deverá ser cadastrado o valor auxiliar definindo as seguintes informações:

|  |  |
| --- | --- |
| Código | Código do valor auxilia.  Este campo é alfanumérico, neste caso pode ser utilizando números e letras na composição do código. |
| Descrição | Descrição do valor auxiliar |
| Valor auxiliar utilizado em | Indica onde o valor auxiliar será utilizado.   * Bolsa * Desconto por antecipação |
| Ordem de processamento | Indica a ordem de processamento do valor auxiliar na geração do lançamento financeiro ATENÇÃO A ordem de processamento do valor auxiliar deverá ser definida quando houver dependência entre os valores auxiliares, por exemplo: Temos o valor auxiliar “A” e “B”, porém a fórmula que irá processar o valor auxiliar “B” leva em consideração nos cálculos o valor auxiliar “A”, neste caso a ordem de processamento deverá ser: Valor auxiliar “A” ordem = 1 Valor auxiliar “B” ordem = 2 Caso não haja dependência entre os valores auxiliares o campo “Ordem de processamento” poderá ser igual 0. |
| Visível a todas coligadas | Indica se o valor auxiliar será global, ou seja, visível a todas as coligadas |
| Visualizar o valor auxiliar no detalhamento de cálculo da parcela | Indica se o valor auxiliar cadastrado será apresentado no detalhamento do cálculo da parcela. |
| Inativo | Indica que o valor auxiliar está inativo |
| Válido até | Indica até qual data o valor auxiliar é válido (esta informação deverá ser preenchida somente se o valor auxiliar for inativado) Observação Estando o valor auxiliar inativo o mesmo será processado para todas as parcelas em que a data de vencimento seja inferior ao campo "**Válido até**"  **Exemplo:**   * Contrato A tem:   + As parcelas:     - 1: Data de vencimento até 31/01/2020     - 2: Data de vencimento até 28/02/2020     - 3: Data de vencimento até 31/03/2020   + As bolsas para todas as parcelas:     - Bolsa Condicional A     - Bolsa Condicional B vinculada ao item de desconto Z2 ( indica que essa bolsa é válida até o segundo vencimento).     - Bolsa Incondicional C   + O desconto por antecipação Z com os itens de desconto:     - Item de desconto Z1 até o dia 05 fixo com 11,08%     - Item de desconto Z2 até o dia 10 fixo com 5,74%     - Item de desconto Z3 até o dia 20 fixo com 2,91%     - Item de desconto Z4 até o dia 31 fixo com 0% * Os valores auxiliares cadastrados são:   + Valor auxiliar 1 com a fórmula VAUX1 utilizados em bolsa   + Valor auxiliar 2 com a fórmula VAUX2 utilizados em bolsa ( **inativo e válido até 31/01/2020** )   + Valor auxiliar 3 com a fórmula VAUX3 utilizados em desconto por antecipação   Na geração do lançamento financeiro para as parcelas do contrato são gerados os seguintes valores auxiliares para as bolsas e para o desconto por antecipação:   * Parcela 1:   + Será gerado todos dos valores auxiliares para as bolsas e para o desconto por antecipação. * Parcela 2:   + Será gerado o valor auxiliar 1 para bolsa e o valor auxiliar 3 para o desconto por antecipação.   + O valor auxiliar 2 não será gerado, pois a data de vencimento da parcela é 28/02/2020 é inferior a data de validade do valor auxiliar ( até 31/01/2020 ). * Parcela 3:   + Será gerado o valor auxiliar 1 para bolsa e o valor auxiliar 3 para o desconto por antecipação.   + O valor auxiliar 2 não será gerado, pois a data de vencimento da parcela é 31/03/2020 é inferior a data de validade do valor auxiliar ( até 31/01/2020 ). |
| Fórmulas para processamento do valor | Tem o objetivo de ter a fórmula que será processada para obter o conteúdo do valor auxiliar OBSERVAÇÃO As fórmulas podem ser informadas por coligada caso o campo "Visível a todas coligadas" estiver marcado, caso contrário a fórmula a ser informada deverá ser da coligada que pertence o valor auxiliar.  Lembrando que é permitido somente uma única fórmula por coligada.  O contexto para o processamento das fórmulas deverá ser do desconto por antecipação visíveis pelo anexo "**Descontos por antecipação da parcela**" na visão de parcela, ou dar bolsa do lançamento visíveis pelo anexo "**Cálculo da Bolsa do Lançamento**" na visão do contrato ou na visão de parcela do contrato. Fórmula Recomendamos consultar o [documento](https://tdn.totvs.com/pages/viewpage.action?pageId=532035637)que descreve sobre as funções de fórmula que poderão ser utilizadas na construção das fórmulas que serão utilizadas no processamento dos valores auxiliares. |

**Exemplo:**

Ao gerar o lançamento financeiro, durante o cálculo da bolsa ou desconto por antecipação para o aluno o sistema irá identificar o valor auxiliar cadastro e executará a fórmula associada, o valor retornado será armazenando no banco de dados.

Importante:

Serão gravados somente os valores auxiliares que forem maior que zero.

Para consultar como os valores auxiliares serão gravados e processados recomendamos acessar os documentos técnico abaixo:

[Documento técnico - Cálculo dos Valores Auxiliares para Bolsas](https://tdn.totvs.com/pages/viewpage.action?pageId=535038478)

[Documento técnico - Cálculo dos Valores Auxiliares para Desconto por Antecipação](https://tdn.totvs.com/pages/viewpage.action?pageId=536713436)

**É importante ressaltar que o valor processado no “Valor Auxiliar” não impacta de forma nenhuma nos valores processados para o lançamento financeiro ou cálculo dos valores da parcela. O “Valor Auxiliar” tem objetivo apenas de processar e guardar informações em paralelo para que posteriormente possa ser consultada.IMPORTANTE!**

div.theme-default .ia-splitter #main {
margin-left: 0px;
}
.ia-fixed-sidebar, .ia-splitter-left {
display: none;
}
#main {
padding-left: 10px;
padding-right: 10px;
overflow-x: hidden;
}
.aui-header-primary .aui-nav, .aui-page-panel {
margin-left: 0px !important;
}
.aui-header-primary .aui-nav {
margin-left: 0px !important;
}
.aui-tabs.horizontal-tabs>.tabs-menu>.menu-item.active-tab a::after {
background: #FF9900; !important
}
.menu-item.active-tab {
border-bottom: none !important;
}
]]>
