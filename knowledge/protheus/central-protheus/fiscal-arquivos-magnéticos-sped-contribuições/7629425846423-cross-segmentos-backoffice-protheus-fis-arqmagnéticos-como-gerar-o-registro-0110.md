---
article_id: 7629425846423
category: Fiscal Arquivos Magnéticos - SPED Contribuições
content_hash: f11a2149ce62b3921b4fa8985d2327b0ccf8c20043cb81fc9660735818c4cb7c
fetched_at: '2026-06-28T22:42:04.956405+00:00'
product: protheus
section_id: 1500001535081
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Como gerar o
  Registro 0110 do EFD Contribuições.
type: support-article
updated_at: '2022-08-31T11:54:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7629425846423-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Como-gerar-o-Registro-0110-do-EFD-Contribui%C3%A7%C3%B5es
---

**Dúvida**Como gerar o Registro **0110** do **EFD Contribuições**?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões.  
  
**Solução**O registro **0110** do **EFD Contribuições**, informa os Regimes de Apuração da Contribuição Social e de Apropriação de Crédito e tem objetivo de informar qual é o tipo de regime de incidência a que se submete a pessoa jurídica (exclusivamente **não cumulativo**, exclusivamente **cumulativo** ou **ambos os regimes**).

Este Registro é gerado, através das informações obtidas nas perguntas da *Wizard* do **processamento da Apuração** e **geração do arquivo txt**, onde é informado o **Tipo de Regime**.  
  
Informações dos campos do **Registro 0110**.  
  
**Campo 02 - COD\_INC\_TRIB**   
**Código indicador da incidência tributária no período**:   
**1** – Escrituração de operações com incidência exclusivamente no regime não-cumulativo;   
**2** – Escrituração de operações com incidência exclusivamente no regime cumulativo;   
**3** – Escrituração de operações com incidência nos regimes não-cumulativo e cumulativo.  
**Pergunta 06** (**Regime PIS/COFINS:?**) do **processamento da Apuração**  
**Pergunta 08** (**Regime PIS/COFINS:?**) da **geração do arquivo txt**

**Campo 03 - IND\_APRO\_CRED**   
**Código indicador de método de apropriação de créditos comuns**, no caso de incidência no **regime não-cumulativo** (**COD\_INC\_TRIB = 1 ou 3**):   
1 – **Método de Apropriação Direta**. O parâmetro **MV\_RATPROP** precisa estar **= T**  
2 – **Método de Rateio Proporcional** (Receita Bruta). O parâmetro **MV\_RATPROP** precisa estar **= F ou em branco**  
  
Importante:

O parâmetro **MV\_RATPROP**, desabilita o cálculo do **crédito PIS/COFINS** feito por **Rateio Proporcional**.   
O parâmetro **MV\_RATPROP =** **T** -> **Desabilita**. **Apropriação direta**, nesse caso **não gera o registro 0111**, para calcular a **proporcionalidade das receitas**, pois a **proporcionalidade do rateio** é indicada diretamente no parâmetro **MV\_PERCAPD**.  
O parâmetro **MV\_RATPROP = F ou em branco** -> Mantém **cálculo por rateio**. Nesse caso os valores para o rateio **serão considerados através do registro 0111**.  
  
**Campo 04 - COD\_TIPO\_CONT**   
**Código indicador do Tipo de Contribuição Apurada no Período**   
1 – Apuração da Contribuição Exclusivamente a Alíquota Básica   
2 – Apuração da Contribuição a Alíquotas Específicas (Diferenciadas e/ou por Unidade de Medida de Produto)  
**Pergunta 15 (Tipo Contribuição) wizard geração arquivo EFD Contribuições.** **Importante:**Foi **removida a opção Método de Apropriação de Créditos comuns**, pois como o ERP **trata somente apropriação por Rateio Proporcional**, o arquivo é gerado com a **opção 2 no campo 04 COD\_TIPO\_CONT, do registro 0110**. Então a opção utilizada é somente o Rateio.

**Campo 05 - IND\_REG\_CUM**   
**Código indicador do critério de escrituração e apuração adotado**, no caso de incidência exclusivamente no **regime cumulativo** (**COD\_INC\_TRIB = 2**), pela pessoa jurídica submetida ao regime de tributação com base no **Lucro Presumido**:   
1 – **Regime de Caixa** - **Escrituração consolidada** (**Registro F500**);   
2 – **Regime de Competência** - **Escrituração consolidada** (**Registro F550**);   
9 – **Regime de Competência** - **Escrituração detalhada, com base nos registros dos Blocos “A”, “C”, “D” e “F”**.  
  
**Importante:**Quando o regime for exclusivamente **Cumulativo**, este registro terá um novo campo, **05-IND\_REG\_CUM**, indicando se o Contribuinte optará pelo **Regime de Caixa**, **Competência consolidada**, ou **Competência detalhada**.

Link registro **0111**:  
  
[Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - EFD Contribuições Registro 0111](https://centraldeatendimento.totvs.com/hc/pt-br/articles/8549061841431-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-EFD-Contribui%C3%A7%C3%B5es-Registro-0111?source=search)

Link Registro **F500:**

<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018411671-MP-FIS-EFD-CONTRIBUI%C3%87%C3%95ES-Como-gerar-o-registro-F500-F525-e-1900?source=search>

Link Registro **F550:**  
<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020733952-MP-FIS-EFD-CONTRIBUI%C3%87%C3%95ES-Como-gerar-o-registro-F550-e-1900?source=search>
