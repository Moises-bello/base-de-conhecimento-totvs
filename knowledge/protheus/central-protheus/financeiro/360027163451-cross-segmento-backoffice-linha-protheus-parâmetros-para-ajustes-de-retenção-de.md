---
article_id: 360027163451
category: Financeiro
content_hash: a61fe0dbd4aea16ead537ad1ea14efdc58b889df7231f7cea7374f5efc2e0124
fetched_at: '2026-06-28T22:38:00.812010+00:00'
product: protheus
section_id: 1500001550522
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - Parâmetros para ajustes de Retenção
  de PCC no Módulo (06) Financeiro
type: support-article
updated_at: '2025-10-31T20:34:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027163451-Cross-Segmento-Backoffice-Linha-Protheus-Par%C3%A2metros-para-ajustes-de-Reten%C3%A7%C3%A3o-de-PCC-no-M%C3%B3dulo-06-Financeiro
---

**Dúvida**  
Quais ajustes são necessários para configurar a retenção de PCC no Módulo (06) FINANCEIRO?  
  
**Ambiente**Cross Segmento - BackOffice Linha Protheus – Financeiro – A partir da versão 11.80  
  
**Solução**Parametrização para retenção de Imposto PIS  / COFINS  / CSLL  ( PCC )

**NATUREZA**  
**Calcula PIS** (ED\_CALCPIS) = **Sim**

**Percentual de PIS** (ED\_PERCPIS) = **Informe a alíquota**

**Calcula COFINS** (ED\_CALCCOF) = **Sim**

**Percentual de COFINS** (ED\_PERCCOF) = **Informe a alíquota**

**Calcula CSLL** (ED\_CALCCSL) = **Sim**

**Percentual de CSLL** (ED\_PERCCSL) = **Informe a alíquota**

**FORNECEDOR**  
**Rec. PIS** (A2\_RECPIS) = **Não**

**Rec. COFINS** (A2\_RECCOFI) = **Não**

**Rec. CSLL** (A2\_RECCSLL) = **Não**

**CLIENTE**  
**Rec. PIS** (A1\_RECPIS) = **Sim**

**Rec. COFINS** (A1\_RECCOFI) = **Sim**

**Rec. CSLL** (A1\_RECCSLL) = **Sim**

**Modo de abatimento do imposto** (A1\_ABATIMP) = **Cálculo do sistema**

Parâmetros referentes à retenção **PIS**/**COFINS**/**CSLL** - **Lei 10.925**  
  
**MV\_RF10925**: Data de referência inicial, para que os novos procedimentos quanto à retenção de PIS/COFINS/CSLL sejam aplicados) = 26/07/04.

**MV\_VL10925**: Valor máximo de pagamentos no período para dispensa da retenção de PIS/COFINS/CSLL = 5000.

**MV\_RT10925**: Modo padrão de operação do Sistema quanto à retenção de PIS/COFINS/CSLL. (1=Calculado p/sistema, 2=Efetua Retenção sempre - 3=Não efetua retenção) = 1.

**MV\_AC10925**: Controle de permissão para que o usuário altere o modo de retenção na janela cálculo de retenção - 1=Permite alteração - 2= Não permite alteração = 1.

**MV\_AB10925**: Modo de retenção do PIS,COFINS e CSLL p/ C.Receber 1=Verif.retenção pelo valor da nota emitida - 2=Verif.retenção p/soma notas emitidas no período = 2.

**MV\_MT10925**: Verifica base de retenção pelo total ou apenas pelos títulos que retiveram impostos.1=Todos 2=Somente os que retiveram PIS etc = 1.

**MV\_BX10925** (Entrada): Define o momento do tratamento da retenção dos impostos PIS COFINS e CSLL. 1= Na Baixa ou 2 = Na Emissão.

**MV\_BR10925** (Saída): Define o momento do tratamento da retenção dos impostos PIS COFINS e CSLL. 1= Na Baixa ou 2 = Na Emissão.

**MV\_BP10925** (Saída) :Define se deve considerar no valor de pagamento, o valor bruto da baixa parcial ou o valor liquido considerando os impostos.(1=Vl Bruto/2=Vl Liquido)

**MV\_BS10925**: Indica se o cálculo da retenção será sobre a base do PIS/COFINS/CSLL ou pelo valor total da duplicata. 1=Valor da base; 2=Valor total = 2

**MV\_LJ10925**: Considerar para verificação de valores de retenção os valores de todas as lojas do cliente. Opções: 1 = Loja atual ou 2 = Todas as lojas = 2.

**MV\_VRETPIS**: Valor mínimo para dispensa de retenção de PIS = 0.00.

**MV\_VRETCOF**: Valor mínimo para dispensa de retenção de COFINS = 0.00.

**MV\_VRETCSL**: Valor mínimo para dispensa de retenção de CSLL = 0.00.

**MV\_PISNAT**: Natureza para títulos referentes ao PIS = PIS.

**MV\_COFINS**: Natureza para títulos referentes a COFINS = COFINS.

**MV\_CSLL**: Natureza de Título de Pagamento de CSLL = CSLL.

**MV\_AG10925:** indica se os impostos do PCC serão aglutinados em um título apenas quando ocorrerem os três impostos num mesmo título. 1=Aglutina ou 2=Não Aglutina = 2.

**Observação**

Após a alteração dos parâmetros de rateio, somente os novos registros serão considerados.

**MV\_RATPIS:** rateio do imposto na entrada - T. (Default) para ratear os impostos ou .F. colocar o valor integral apenas na primeira parcela.

**MV\_RATCOF**: rateio do imposto na entrada - .T. (Default) para ratear os impostos ou .F. colocar o valor integral apenas na primeira parcela.

**MV\_RATCSLL**: rateio do imposto na entrada - .T. (Default) para ratear os impostos ou .F. colocar o valor integral apenas na primeira parcela.

**I****mportante:**  
Os parâmetros referentes à Lei 10.925 devem permanecer conforme sugerido acima.

Parâmetros referentes à retenção **PIS**/**COFINS**/**CSLL** - **Lei 13.137 - Nova Lei**

Adequação do *Protheus* para atender as alterações de regras de cálculo do **PIS**, **Cofins** e **CSLL** de acordo com a Lei 13137/15 | Lei nº 13.137, de 19 de junho de 2015 vigente a partir do dia 22/06/2015.

**MV\_VL13137**: Define o valor mínimo para retenção do Pis/Cofins/Csll de acordo com a Lei 13.137 = 10.00.

**MV\_VCPCCP**: Qual a data que será considerada para a cumulatividade do PCC na Emissão. 1= Emissão, 2=Venc.Real, 3=Dt Contab.

**MV\_VCPCCR**: Qual a data que será considerada para a cumulatividade do PCC na Emissão. 1=Emissão, 2=Venc.Real, 3=Dt Contab.  
  
O parâmetro **MV\_BX10925 e MV\_BR10925** não deve ser alterado, uma vez que, no momento da implantação do ***Protheus***, foi definido como a empresa irá tratar o imposto.

**Saiba mais**[Adequação da Lei 13.137 – Novas regras para Pis, Cofins, CSLL](http://tdn.totvs.com/pages/viewpage.action?pageId=192092055)

[DOC0023\_Apuração\_ de\_PIS\_COFINS](http://tdn.totvs.com/pages/viewpage.action?pageId=6076810)

[MP - FIS - Como gerar um único título para retenção de PIS/COFINS/CSLL na entrada da NF?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500000831461)
