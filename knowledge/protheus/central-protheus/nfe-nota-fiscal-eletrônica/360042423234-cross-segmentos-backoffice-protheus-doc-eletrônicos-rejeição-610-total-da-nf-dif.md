---
article_id: 360042423234
category: NFe - Nota Fiscal Eletrônica
content_hash: 98fe4bfc3dd4bf397c45ea437f446be7ec095a01993a5778fc49fcdaa9edf638
fetched_at: '2026-06-28T22:40:07.188506+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Rejeição: 610 Total
  da NF difere do somatório dos Valores compõe o valor Total da NF para nota de Suframa'
type: support-article
updated_at: '2024-09-16T21:54:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360042423234-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Rejei%C3%A7%C3%A3o-610-Total-da-NF-difere-do-somat%C3%B3rio-dos-Valores-comp%C3%B5e-o-valor-Total-da-NF-para-nota-de-Suframa
---

**Dúvida**

Como solucionar a rejeição abaixo:

Rejeição: 610 Total da NF difere do somatório dos Valores compõe o valor Total da NF ?

**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos

Cross Segmentos - TSS

**Solução**

O valor da TAG **vNF** deve bater com os valores levados no bloco **ICMSTOT** subtraindo e somando de acordo com o esperado pela regra de sua totalizadora.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26415366829207)

Caso o valor que não tenha destacado no XML seja o valor do **ICMS, PIS ou Cofins de Suframa** que foi calculado no sistema:

Desde a versão **3.10 da NFe** na qual foi criada a **TAG Vicmsdeson** o valor da desoneração do Suframa de ICMS é destacado **Vicmsdeson** e o PIS e Cofins é opcional destacar na **Vdesc.**

* **Exemplo do XML gerado:**

**![](https://totvssuporte.zendesk.com/attachments/token/cgei53KTwaru917WgO5cfoNnH/?name=inline2052551793.png)**

**Para Suframa é gravado o conteúdo na tabela SD2:**

* **Para o ICMS, Pis e Cofins** = D2\_DESCZFR
* **Para o Pis =**D2\_DESCZFP
* **Para o Confins =** D2\_DESCZFC

Sendo assim, fazer as verificações abaixo:

Para gerar a **TAG vICMSDeson** para Suframa é necessário verificar se o grupo da situação tributária na nota técnica  contempla as **TAGs vICMSDeson e motDesICMS  = 7**.

1- Conforme o **Manual da Sefaz para o ICMS a situação tributária = 40, 41 e 50**a situação tributaria do ICMS e cadastrada **no TES no campo Sit. trib. ICMS (F4\_SITTRIB)**

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17529796608791)

2- Preencher no TES os campos **F4\_MOTICMS= 7 (motivo de desoneração)**

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17529796616471)

3- A situação tributária do **Pis** campo no **TES Sit. trib. Pis (F4\_CSTPIS) e do Cofins** campo **Sit. trib. Cof (F4\_CSTCOF)  deve ser 06.**

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360079020713)**

4- Para **ICMS-ST**a situação tributaria do ICMS deve ser **30**preencher **no TES no campo Sit. trib. ICMS (F4\_SITTRIB)**

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17529796608791)

5- Preencher na TES os campos**F4\_MOTICMS= 7 (motivo de desoneração)**

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17529796616471)

6- Após alteração no TES a nota deve ser sempre excluída e se for utilizar o mesmo pedido é necessário digitar novamente o TES no pedido para que a situação tributária seja atualizada.

**Saiba mais:**

Se houver apenas cálculo de **Pis e Cofins** poderá utilizar **outras situações tributárias**, mas apenas se houver só cálculo de Pis e Cofins **sem ICMS suframa**. Nesse caso **não pode ser preenchido** o motivo de desoneração na TES.

* Caso seja nota de **SUFRAMA**realizar as configurações abaixo:

[CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Como configurar o sistema para calcular SUFRAMA?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034294253)

* **Importante:**

Caso o **Pis e o Cofins** não possa ser destacado na **TAG Vdesc** utilizar o parâmetro do link abaixo:  
  
[MP - NFE - Parâmetro MV\_NFLEIZF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021778932)

* **Saiba mais:**

**Caso** a empresa seja emitente **do Simples Nacional:**

Até o momento a Sefaz não disponibilizou nenhum **grupo de CSOSN** que possa ser **desonerado o valor** do Suframa, por esse motivo causa a **rejeição 610** nesse caso o **imposto não pode ser calculado** no sistema.  
  
Para o **Simples nacional** o sistema calcula o Suframa, porém não levamos para o XML, pois não há nenhum grupo do **CSOSN** que tenha a **TAG Vicmsdeson.**  
  
Sendo assim, para que não cause a rejeição o suframa **não pode** ser calculado.  
  
Verifique com a Sefaz se esse desconto pode ser na TAG ***vDESC*** ou direto no valor do Produto.  
  
Caso seja na ***Vdesc*** poderá utilizar os campos de desconto no cadastro de produto.
