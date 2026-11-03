---
article_id: 360027639592
category: Escrita Fiscal - Impostos - ICMS
content_hash: 7166f6100dcafa59e80f6148f8587ee7d410cafa6fc95c7e41875f6150cd5f0c
fetched_at: '2026-06-28T22:39:23.967871+00:00'
product: protheus
section_id: 1500001549842
source: central-protheus
title: ' CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Como configurar
  o ICMS Diferido?'
type: support-article
updated_at: '2024-05-09T13:11:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027639592--CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-configurar-o-ICMS-Diferido
---

**Dúvida**

Como configurar o ICMS diferido ?

**Ambiente**

Protheus - Fiscal - A partir da versão 12

**Solução**

Configurações necessárias:

**Calcula ICMS (F4\_ICM):** Definido como SIM.

**ICMS Diferido (F4\_ICMSDIF):**

1-O ICMS é calculado e diferido.

2=Não há calculo do ICMS diferido.

3=O ICMS é calculo e reduzido.

4=O ICMS é calculado, reduzido do ICMS a recolher e somado ao total do título e da nota fiscal (Incentivo Fiscal).

5=Diferimento com ST Diferimento do ICMS é calculado mas não é reduzido do ICMS. Deve ser utilizado exceção fiscal para reduzir alíquota do ICMS Próprio conforme percentual de diferimento. Este tratamento é utilizado quando nota possuir ICMS com diferido e ICMS ST sem diferimento.

6=Deduz NF e Duplicata;

7=Ded. ICMS BC. Composta

**Perc. ICM DIF (F4\_PICMDIF) :** Informar o Percentual de Diferimento

**CST** = 51

Exemplos de configurações no boletim:

<https://tdn.totvs.com/pages/releaseview.action?pageId=654111155>

**Informações Importantes:**Os campos F4\_ICMSDIF e F4\_PICMDIF  precisam ser configurados corretamente de acordo com a necessidade.

**Atenção:**Quando definido como 100% no campo **F4\_PICMDIF**significa que haverá o diferimento total do ICMS, caso seja informado um valor diferente de 100 o cálculo será realizado de acordo com o Percentual informado).

Referente o diferimento, são gravados os campos abaixo: 

**FT\_VOPDIF**  
É o valor total do ICMS antes do diferimento.

**FT\_ICMSDIF**É o valor do ICMS Diferido

**FT\_VALICM**

É o valor do ICMS após diferimento.

Verificação do calculo:

**O XML faz o seguinte cálculo para levar o percentual do diferimento:**

FT\_ICMSDIF / FT\_VOPDIF \* 100

Após a NT 005 serão gravados os campos

CD2\_VFCPDI - Valor do FECP Diferido

CD2\_VFCPEF - Valor do FECP Efetivo

* O campo CD2\_VFCP fica responsável por gerar a tag <vFCP>, onde é gravado o Valor do ICMS relativo ao Fundo de Combate à Pobreza (FCP), considerando o valor do FCP Efetivo + o valor do FCP Diferido, ou seja, o valor total do FCP desconsiderando o possível valor diferido.
* O campo CD2\_VFCPDI fará a geração da tag <vFCPDif>, onde é gravado o Valor do ICMS relativo ao Fundo de Combate à Pobreza (FCP) diferido.
* Já o campo CD2\_VFCPEF fará a geração da tag <vFCPEfet>, onde é gravado o Valor do ICMS relativo ao Fundo de Combate à Pobreza (FCP) efetivo, ou seja, o valor total de FCP - o valor diferido de FCP.
