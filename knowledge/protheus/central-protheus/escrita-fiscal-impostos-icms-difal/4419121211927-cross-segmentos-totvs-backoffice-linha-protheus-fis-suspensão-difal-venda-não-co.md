---
article_id: 4419121211927
category: Escrita Fiscal - Impostos - ICMS - Difal
content_hash: 36fa756ad122042518a160222c121716216e6fbc78d24daca8c357619abda635
fetched_at: '2026-06-28T22:39:19.318656+00:00'
product: protheus
section_id: 1500001549902
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Suspensão Difal -
  Venda Não Contribuinte - LC 190/2022
type: support-article
updated_at: '2022-01-17T20:13:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4419121211927-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Suspens%C3%A3o-Difal-Venda-N%C3%A3o-Contribuinte-LC-190-2022
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **HH:MM:SS min** **Dúvida**Qual tratamento no Protheus para Suspensão do Difal - Venda para Não Contribuinte -  conforme LC 190/2022?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**

Para adequar o sistema, quando se tratar de operação interestadual a não contribuinte ou consumidor final, não mais será definida a alíquota do ICMS próprio baseada simplesmente na tabela de alíquotas do ICMS. O sistema passa a verificar se haverá o calculo do DIFAL observando também o campo da TES **F4\_DIFAL (Calc. Difal).** Lembrando também que quando há a configuração do campo de **Calc.Difal**o campo **F4\_COMPL (Calc.Dif.Icm)** também deve ser configurado corretamente.

Assim, quando esses campos estiverem definidos como **"Não"**, o sistema aplicará  sobre o ICMS próprio a alíquota interna da UF de origem.

Sendo assim, para não calcular o Difal será necessário configurar na TES:

Calcula ICMS = Sim

L. Fiscal ICMS = Diferente de Não

Calc Dif ICM = Não

Calc Difal = Não

**Importante**

É importante ressaltar que aquilo que, em certos casos, pode depender do calculo do DIFAL, como por exemplo os fundos de combate e erradicação da pobreza, devem ter suas configurações revisadas.

Para os casos em que é necessário calcular **Fundo de Combate e Erradicação da Pobreza (FECP)**, o sistema disponibiliza na Rotina **UF x UF (FISA080)**campos para configuração do calculo. Assim, após aplicar o patch desta solução, é possível configurar para que as operações interestaduais sem calculo de DIFAL a consumidor final e ou não contribuinte efetuem o calculo do **FECP**.

Para tanto, na aba **FECP**da Rotina **UF x UF (FISA080)**configure pelo menos os seguintes campos:

* Aliq. Fecp **(CFC\_ALQFCP)**
* Alq. Fcp. Ori **(CFC\_ALFCPO)**

**![](https://tdn.totvs.com/download/attachments/658424127/image2022-1-8_13-34-9.png?version=1&modificationDate=1641659649127&api=v2)**

**Parecer Consultoria Tributária - Totvs:**

<https://www.totvs.com/blog/fiscal-clientes/mudancas-para-2022/>
