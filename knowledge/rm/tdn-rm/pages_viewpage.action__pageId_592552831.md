---
content_hash: dbd95ed8a30508a57e2b1ff61440ee32af078555440841787ce909bd077ecaef
fetched_at: '2026-06-29T00:10:56.694380+00:00'
page_id: '592552831'
product: rm
source: tdn-rm
title: Ajuda Compensatória Mensal – Lei nº 14.020, de 6 de julho de 2020
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=592552831
version: 16
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS Folha de Pagamento |
| Linha de Produto: | RM |
| Versões | * 12.1.2302.257 ou superior * 12.1.2306.216 ou superior * 12.1.2310.148 ou superior |

## **02. SITUAÇÃO/REQUISITO**

O pagamento, pelo empregador, de Ajuda Compensatória mensal, em decorrência da redução proporcional de jornada de trabalho e de salário ou da suspensão temporária de contrato de trabalho tem natureza indenizatória e NÃO integra a base de cálculo do imposto sobre a renda retido na fonte ou da declaração de ajuste anual do imposto sobre a renda da pessoa física, conforme estabelece o art. 9º da Lei nº 14.020, de 6 de Julho de 2020, que dispõe sobre o Programa Emergencial de Manutenção do Emprego e da Renda como medida complementar aplicável durante o estado de calamidade pública reconhecido pelo Decreto Legislativo nº 6, de 20 de março de 2020, e da emergência de saúde pública de importância internacional decorrente do coronavírus.

O rendimento pago como Ajuda Compensatória não integrará o salário devido pelo empregador na hipótese de redução proporcional de jornada de trabalho e de salário e deverá ser informado separadamente no campo 'Outros (especificar)' da subficha 'Rendimentos Isentos' do beneficiário do declarante como especificação da rubrica no campo descrição.

Na hipótese do beneficiário ter recebido mais de uma rubrica referente a rendimentos isentos que devam ser informadas no campo 'Outros (especificar)', o declarante poderá informar cada uma, detalhadamente, na ficha 'Informações Complementares - comprovante de rendimentos'.

## **03. SOLUÇÃO**

Informar o evento de pagamento de Ajuda Compensatória Mensal dentro da aba 'Campo 4 - Rend. Isentos e não Tribut.' sub aba 'Outros (especificar) - Campo 5/Linha8'. Esta aba fica localizada dentro dos parâmetros da coligada, conforme a imagem abaixo:

Passo 01, Passo 02, Passo 03, Passo 04passo1,passo2,passo3,passo4yespasso1

Evento Lançado na ficha Financeira nas competências abaixo:

nopasso2

Informado o evento na aba 'Campo 4 - Rend. Isentos e não Tribut.' sub aba 'Outros (especificar) - Campo 5/Linha8:

nopasso3

Gerando o Informe de Rendimentos, o evento sai da Linha 07 - Outros: Outros (especificar) - Campo 5/ linha 8, campo 4 - RENDIMENTOS ISENTOS E NÃO TRIBUTÁVEIS:

nopasso4

Na DIRF em arquivo o mesmo é enviado para o registro RIO - Rendimentos Isentos Anuais – Outros:

No Programa da DIRF 2021, o mesmo retorna no respectivo campo:

## **04. DEMAIS INFORMAÇÕES**

falseDica

Para que no Informe de Rendimentos o campo 'Outros (especificar) - Campo 5/Linha8', retorne com a informação referente a ajuda compensatória mensal, basta editar o nome do campo na tabela dinâmica INT41, conforme exemplo abaixo.

Alterando o nome do registro 9, da tabela dinâmica INT41:

No processo de geração da DIRF/Informe de Rendimentos, na aba 'Campo 4 - Rend. Isentos e não Tribut.' a sub aba será retornada com a descrição alterada:

Ao gerar o Informe de rendimentos, o campo será retornado com Descrição:

falseObservação

1. Mesmo alterando a descrição do campo 'Outros (especificar) - Campo 5/Linha8', na DIRF em arquivo o rendimento isento continua sendo informado no registro RIO - Rendimentos Isentos Anuais – Outros

**Conforme orientação da Lei nº 14.020, o rendimento pago como Ajuda Compensatória Mensal, tem natureza indenizatória, não devendo integrar na Base de Cálculo de Imposto de Renda. Desta Forma, este evento NÃO deve incidir em IRRF (IRRF, IRRF Férias, IRRF 13º). IMPORTANTE!**

## **05. ASSUNTOS RELACIONADOS**

* Para detalhar no programa da DIRF 2021 as informações complementares detalhando cada rubrica que compõe o campo 'Outros especificar', deverá fazer de forma manual, editando o respectivo campo no programa da Receita. Assim, ao gerar o Comprovante de Rendimentos pelo programa da Receita, irá descriminar cada rubrica:

Exemplo:

Comprovante de Rendimentos gerado no programa da Receita Federal:

* No Gerador de Informe de Rendimento do Produto Folha de Pagamento, poderá incluir Fórmulas de Mensagem para descriminar os valores:

Exemplo:

Informando a Fórmula de Mensagem:

Ao gerar o Informe de Rendimentos do produto, a mensagem foi retornada no campo Informações complementares:

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
