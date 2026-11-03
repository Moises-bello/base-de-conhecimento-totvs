---
content_hash: 6360171d5d2054ec28986fe9e7f8487742ac572dc17c22f5db93c7a08970900a
fetched_at: '2026-06-29T00:10:47.906802+00:00'
page_id: '561064833'
product: rm
source: tdn-rm
title: Registro 9000
type: documentation
url: https://tdn.totvs.com/display/LRM/Registro+9000
version: 2
---

Controle e Encerramento do Arquivo Digital.

BLOCO9lefttrue90009000 (nível 1)

**Apuração do Total do Arquivo**

Este registro totaliza Os campos de apuração dos valores a ressarcir, a recuperar ou a complementar informados nos registros totalizadores 1200, 1300, 1400 e 1500.

| Nº | Campo | Descrição | Origem dos Dados |
| --- | --- | --- | --- |
| X01 | REG | Registro 9000 | Texto fixo contendo 9000 |
| X02 | REG1200\_ICMSST\_RECUPERAR\_RESSARCIR | Valor a recuperar ou a ressarcir nas saídas para consumidor final | Resultado positivo da diferença da somatória dos valores declarados no campo F07 [APUR\_ICMSST\_RECUPERAR\_RESSARCIR] pela somatória dos valores declarados no campo F08 [APUR\_ICMSST\_COMPLEMENTAR] de todos os registros 1200 [Totalizador das saidas para consumidor final]  Observação: Preencher com zero quando o resultado da equação X02=∑[F07]-∑[F08] for negativo |
| X03 | REG1200\_ICMSST\_COMPLEMENTAR | Valor a complementar nas saídas para consumidor final | Resultado negativo da diferença da somatória dos valores declarados no campo F07 [APUR\_ICMSST\_RECUPERAR\_RESSARCIR] pela somatória dos valores declarados no campo F08 [APUR\_ICMSST\_COMPLEMENTAR] de todos os registros 1200 [Totalizador das saidas para consumidor final].  Observação: Preencher com zero quando o resultado da equação X03=∑[F07]-∑[F08] for positivo |
| X04 | REG1300\_ICMSST\_RECUPERAR\_RESSARCIR | Valor a recuperar ou a ressarcir nas saídas para outros estados | Somatória dos valores declarados no campo H06 [APUR\_ICMSST\_RECUPERAR\_RESSARCIR] de todos os registros 1300 (Totalizador das saídas para outros estados) |
| X05 | REG1400\_ICMSST\_RECUPERAR\_RESSARCIR | Valor a recuperar ou a ressarcir nas saidas de que trata o art. 119 | Somatória dos valores declarados no campo J05 [APUR\_ICMSST\_RECUPERAR\_RESSARCIR] de todos os registros 1400 (Totalizador das saídas que trata o art. 119) |
| X06 | REG1500\_ICMSST\_RECUPERAR\_RESSARCIR | Valor a recuperar ou a ressarcir nas saídas destinadas a contribuinte do Simples Nacional | Somatória dos valores declarados no campo L04 [APUR\_ICMSST\_RECUPERAR\_RESSARCIR] de todos os registros 1500 (Totalizador das saídas para contribuinte do Simples Nacional) |
| X07 | REG9000\_FECOP\_RESSARCIR | Valor a ressarcir do FECOP | Resultado positivo da somatória dos valores declarados nos campos F09 [APUR\_FECOP\_RESSARCIR] dos registros 1200 e H07 [APUR\_FECOP\_RESSARCIR] dos registros 1300 menos a somatória dos valores declarados no campo F10 [APUR\_FECOP\_COMPLEMENTAR] dos registros 1200.  Observação: Preencher com zero quando o resultado da equação X07=∑[F09]+∑[H07]-∑[F10] for negativo |
| X08 | REG9000\_FECOP\_COMPLEMENTAR | Valor a complementar do FECOP | Resultado negativo da somatória dos valores declarados nos campos F09 [APUR\_FECOP\_RESSARCIR] dos registros 1200 e H07 [APUR\_FECOP\_RESSARCIR] dos registros 1300 menos a somatória dos valores declarados no campo F10 [APUR\_FECOP\_COMPLEMENTAR] dos registros 1200.  Observação: Preencher com zero quando o resultado da equação X08=∑[F09]+∑[H07]-∑[F10] for positivo |

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
]]>
