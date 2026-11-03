---
content_hash: 04fedcf2e3e06bdbec0275f67c3543c7376f140d4172c147b6f7c45b2b672aa7
fetched_at: '2026-06-29T00:10:35.485462+00:00'
page_id: '529307056'
product: rm
source: tdn-rm
title: DEDUINTEGRACOES-6436 DT Detalhamento do cálculo da bolsa do aluno
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=529307056
version: 14
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Educacional |
| Módulo: | TOTVS Educacional |
| Função: | Geração de lançamento |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : |  |

## **02. SITUAÇÃO/REQUISITO**

Após a geração do lançamento financeiro é necessário identificar quais informações foram consideradas para calcular o valor da bolsa.

## **03. SOLUÇÃO**

Durante a geração do lançamento financeiro do aluno iremos gravar na tabela **SBOLSALAN** as informações que foram consideradas no cálculo da bolsa.

Tais como:

| Campo | Descrição |
| --- | --- |
| TIPODESC | Tipo de desconto concedido pela bolsa (P = Percentual / V = Valor) |
| DESCONTO | Desconto concedido para a bolsa |
| ORDEMBOLSA | Ordem de aplicação da bolsa |
| VALORORIGINALPARCELA | Valor original da parcela vinculada a bolsa |
| VALORDESCONTOPARCELA | Valor de desconto de parcela |
| VLRDESCONTOANTEAPLICADO | Valor de desconto por antecipação considerado, e que dependendo da parametrização poderá impactar no cálculo da bolsa |
| VALORBASECALCULO | Valor base do cálculo para aplicar o desconto da bolsa |
| TIPOBOLSA | Tipo de bolsa ( S = Somar bolsa / C = Cascata / M = Maior Bolsa) |
| ORDEMAPLICDESCANTECIPACAO | Indica a incidência e ordem de aplicação do desconto por antecipação (A = Antes / D = Depois) |
| AFETABASECALCULO | Indica se o valor calculado para a bolsa irá afetar a base de cálculo no cálculo das próximas bolsa ( nos caso da classificação do tipo cascata ) |
| INCONDICIONAL | Indica se a bolsa é condicional ( S = Sim / N = Não) |
| TETOVALOR | Indica se foi considerado algum teto de valor ( valor máximo para a bolsa ) |

Importante

**=>** O TOTVS Educacional possibilita ao cliente definir no cadastro da bolsa uma fórmula que será responsável em retornar o percentual de desconto da bolsa que deverá ser aplicado para o aluno, pois em alguns cenário de clientes considerando regras especificas no momento da geração do lançamento o percentual da bolsa pode ser diferente do percentual definido no cadastro da bolsa do aluno.

Quando este cenário ocorrer o TOTVS Educacional irá identificar campo “EXECUTOUFORMULA” da tabela SBOLSALAN e no campo “PERCENTCALCFORMULA” será gravado o percentual de desconto processado pela fórmula.

Com isso ressaltamos que no campo “DESCONTO” será gravado o valor que estava definido no cadastro da bolsa do aluno, desta forma conseguimos manter a rastreabilidade das informações.

**=>** Quando o tipo de desconto da bolsa for igual a "Valor" ressaltamos que os campos "VLRDESCONTOANTEAPLICADO", VALORBASECALCULO não terão informações, pois o valor da bolsa já esta definido e não haverá incidência de cálculo.

As informações que serão gravadas serão baseados nos dados de parametrização do TOTVS Educacional e do cadastro da bolsa do aluno conforme o exato momento da geração do lançamento financeiro, desta forma caso o registro do cadastro de bolsa do aluno ou parametrização do sistema sejam alterados posteriormente será possível pelo detalhamento do cálculo identificar quais parametrizações foram consideradas quando a bolsa foi processada.

## **Desconto por Antecipação**

No momento da geração do lançamento financeiro em que o desconto por antecipação é processado para um contrato que contenha bolsa condicional, é gravado na tabela **SBOLSALANDESCPONTUAL** as bolsas ( bolsa condicional ) conforme cada vencimento do desconto por antecipação que foi apurado, ou seja, gravamos uma projeção do valor da bolsa para cada vencimento do desconto por antecipação.

Com isso realizamos evoluímos também para que a tabela **SBOLSALANDESCPONTUAL** passe a gravar mais duas informações:

| Campo | Descrição |
| --- | --- |
| VLRDESCONTOANTECIPACAO | Valor do desconto por antecipação para o vencimento |
| VALORBASECALCULO | Valor base de cálculo utilizado para calcular o valor da bolsa |

Informação

Conforme parametrização o valor da bolsa condicional a ser concedida para o aluno poderá ser alterado em função do desconto por antecipação aplicado no momento da baixa do lançamento financeiro.

Isso irá ocorrer quando o parâmetro “Mantém fórmula default para valor opcional” estiver marcado, pois neste caso o valor da bolsa condicional será calculado pela fórmula parametrizada.

Lembramos que o valor do desconto por antecipação impactará no cálculo da bolsa somente ser fórmula que calcula o valor da bolsa condicional estiver utilizado a função “**VLRBOLSALANDESCANTPORDTBAIXA(‘’)**”.

Observação:

O parâmetro “Mantém fórmula default para valor opcional” está disponível em Educacional | Integração | Financeiro | Educacional | Fin. Vlrs. Opcionais/Integração.

## **Visualização do Cálculo da Bolsa do Lançamento**

Com objetivo de auxiliar na conferência das informações processadas pelo o cálculo da bolsa do lançamento disponibilizamos a visão de dados “Cálculo da Bolsa do Lançamento” que demonstra todas as informações do cálculo da bolsa.

Esta visão poderá ser acessada através do anexo do contrato ou através do anexo da parcela

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
