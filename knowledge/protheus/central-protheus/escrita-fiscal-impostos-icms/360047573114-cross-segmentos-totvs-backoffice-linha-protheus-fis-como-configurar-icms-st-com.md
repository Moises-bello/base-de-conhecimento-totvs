---
article_id: 360047573114
category: Escrita Fiscal - Impostos - ICMS
content_hash: 53c2a0ec5cd45a187cef14fa936ead2f8c7cb479a919a9d10a5b01e5136f31a4
fetched_at: '2026-06-28T22:39:24.166386+00:00'
product: protheus
section_id: 1500001549842
source: central-protheus
title: 'CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Como configurar
  ICMS ST com base dupla? '
type: support-article
updated_at: '2022-06-22T12:26:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047573114-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-configurar-ICMS-ST-com-base-dupla
---

**Dúvida**Como configurar ICMS ST com base dupla ?

**Ambiente**Protheus - Fiscal – A partir da versão 11.80  
  
**Solução**Realizado implementação para que seja utilizada base dupla no cálculo de ST para quando a mercadoria for destinada a uso/consumo.

**Parametro**

MV\_UFBDST

Informe os estados que devem ter base dupla de ST. Válido apenas quando a venda for destinada a consumo e entre estados distintos.

Exemplo : SP/RS/PR

Ao realizar um Pedido ou Nota Fiscal aonde o destino seja Consumo e o estado de destino esteja contido no parâmetro MV\_UFBDST.

É valido apenas para vendas interestaduais.

**IPI na Base (F4\_INCIDE):** Este campo permite informar se valor de IPI incide na base de ICMS. Para o exemplo a seguir o IPI entrou na base de cálculo do ICMS, desta forma pode ser definido como "Consumidor Final" ou como **"Sim".**

 **Marg. Solid. (F4\_MKPSOL):** Indica qual a forma de considerar a aplicação da margem de lucro do ICMS retido, permitindo sobrepor as configurações normais das situações

onde a margem será aplicada. No exemplo a seguir não utilizamos o MVA no cálculo, desta forma o campo deve estar como **NUNCA.**

**IPI Bs.ICMST (F4\_SOMAIPI):** Indica se valor do IPI irá compor a base do ICMS-ST. No exemplo a seguir o IPI foi considerado nos cálculos, desta forma o campo deve estar como **1-Sim.**

**Mat.Consumo (F4\_CONSUMO):**1-Sim

**Calc.Dif.Icm (F4\_COMPL):** S - Sim

 

**Tipo Cliente:** Consumo Final

Exemplo de cálculo:

Valor da operação: R$ 1.000,00;

Alíquota de IPI (5%): R$ 50,00  
MVA = 40%, (Não aplicar MVA, considerando apenas diferença entre alíquota interna e interestadual)  
Alíquota ICMS interna de 12%;  
ICMS destacado no documento de aquisição interestadual (1.050 x 0,12) = R$ 126,00;  
Cálculo da exclusão do ICMS operação interestadual da BC = (R$ 1.050,00) - (R$ 126,00)  
Valor da operação sem o ICMS operação interestadual = R$ 924,00  
BC do ICMS diferencial de alíquota considerando-se alíquota interna de 18% (924,00 / 0,82) = R$ 1.126,83  
Cálculo do ICMS diferencial de alíquota, considerando a BC e alíquota interna do estado destino - BC com alíquota de origem (1.126,83 x 18%) - (1050,00 x 12%) = R$ 76,83 Base de cálculo do ICMS substituição tributária (R$ 924,00 / 0,82) = R$ 1.126,83;  
Cálculo do ICMS ST devido: R$ 1.126,83 x 18% = (R$ 202,83) - (R$ 126,00) = R$ 76,83;   "Para chegar neste valor de 76,83 sua TES deve estar com o campo **Ded.ICM.ST (F4\_ICMSTMT)** = 1-SIM"  
ICMS ST devido = R$ 76,83.  
Total da nota fiscal (a+b+l) = R$ 1.126,83

**![](https://tdn.totvs.com/download/attachments/238029250/image2019-11-28_12-9-16.png?version=1&modificationDate=1574953755980&api=v2)**
