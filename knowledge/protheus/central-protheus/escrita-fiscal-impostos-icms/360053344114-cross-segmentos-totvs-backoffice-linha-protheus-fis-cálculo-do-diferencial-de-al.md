---
article_id: 360053344114
category: Escrita Fiscal - Impostos - ICMS
content_hash: a2052b93abe01a5747429a55e7919699dda375824252d907756d8ac69cab11ed
fetched_at: '2026-06-28T22:39:23.977336+00:00'
product: protheus
section_id: 1500001549842
source: central-protheus
title: ' CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Cálculo do diferencial
  de alíquota ICMS ST no RJ para notas fiscais de entrada - Base Dupla'
type: support-article
updated_at: '2024-06-20T18:21:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053344114--CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-C%C3%A1lculo-do-diferencial-de-al%C3%ADquota-ICMS-ST-no-RJ-para-notas-fiscais-de-entrada-Base-Dupla
---

**Dúvida**Qual a configuração para o cálculo do diferencial de alíquota ST no RJ conforme a formula **"ICMS ST DIFAL = [(V oper - ICMS origem) / (1 - ALQ interna)] x ALQ interna - (V oper x ALQ interestadual)**

**Ambiente**Microsiga Protheus - a partir da versão 12

**Solução**

Informe no**Cadastro do Produto** ou da**Exceção Fiscal** o percentual de **ICMS-ST (MVA)** estabelecido por norma legal, caso não exista, informe um percentual fictício (por exemplo 0,01) somente para possibilitar o cálculo pelo diferencial:

**TES**

Calcula ICMS (F4\_ICM) = SIM

L. FISC. ICMS (F4\_LFICM) = TRIBUTADO

DIF. ALIQ. (F4\_COMPL) = NÃO

MATL CONSUMO (F4\_CONSUMO) = SIM

AGREGA SOLID. (F4\_INCSOL) = SIM

MARG. SOLID. (F4\_MKPSOL) = NUNCA (Indica que o sistema deve ignorar o MVA preenchido no produto ou exceção fiscal)

Ded.ICM.ST (F4\_ICMSSTMT)= SIM

**Fornecedor:**  
  
O **FORNECEDOR** deve ser de um Estado diferente do emitente (MV\_ESTADO).

**Parâmetros:**

Configurar o parâmetro **MV\_UFBDST**com o estado da sua empresa.  
  
**MV\_UFBDST:**  
Informe os estados que devem ter base dupla de ST. Valido apenas quando a venda for destinada a consumo e entre estados distintos.   
  
**Para que o cálculo NÃO fique em desacordo com o cenário esperado, será necessário NÃO preencher a UF no MV\_BASDSSE.**

**MV\_BASDSSE:  
Define UFs que terão cálculo da base do destino em operações de Saída para Port. SEFAZ SE 367/2016; Art. 22 e 23.**

**Para o cálculo do FECP ST :**

O FECP deverá ser configurado pela rotina FISA080- UFXUF:

UF Origem - Informe o estado de origem  
UF Destino - Informe o estado de destino  
Aliq FECP - Informe % do FECP

**TES:**

Isen FECP = Não

Importante - Operações com Substituição Tributária

Para que o FCP-ST seja calculado corretamente é obrigatório o uso de um CST de Substituição Tributária: 10, 30 ou 70. Esta regra é válida para todos os estados, em operações de entrada e saída.

***Exemplo do cálculo demonstrado no Manual de Substituição Tributária pág. 9.***

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360090958053/mceclip0.png)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360090957133/mceclip1.png)

**Informações adicionais:**

FIS0060\_BASE\_DUPLA\_ST\_CONSUMO

<https://tdn.totvs.com/display/public/PROT/FIS0060_BASE_DUPLA_ST_CONSUMO>

UF x UF (FISA080)

<http://tdn.totvs.com/display/PROT/FIS0058_UF_X_UF_CFC>

Tratamento dos Fundos Estaduais de Combate à Pobreza

<http://tdn.totvs.com/pages/releaseview.action?pageId=287056662>

Link do parecer elaborado pela Consultoria de Segmentos da TOTVS  - Convênio ICMS 142/18

<https://tdn.totvs.com.br/pages/releaseview.action?pageId=450143442>

Manual de Substituição Tributária RJ

<http://www.fazenda.rj.gov.br/sefaz/content/conn/UCMServer/path/Contribution%20Folders/site_fazenda/informacao/icms/substituicao_trib/Manual%20ST%20v3-27-03-2016%20editado.pdf?lve>
