---
article_id: 360025687693
category: NFe - Nota Fiscal Eletrônica
content_hash: a64525868745019124363ab699268e51cd6e86e8771399a543276186454d32fe
fetched_at: '2026-06-28T22:40:05.521704+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 934  Rejeição :
  Não informado valor do ICMS desonerado ou o Motivo de desoneração'
type: support-article
updated_at: '2024-05-22T15:02:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025687693-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-934-Rejei%C3%A7%C3%A3o-N%C3%A3o-informado-valor-do-ICMS-desonerado-ou-o-Motivo-de-desonera%C3%A7%C3%A3o
---

**Dúvida**Como corrigir a rejeição abaixo:

934 Rejeição : Não informado valor do ICMS desonerado ou o Motivo de desoneração ?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**

1 - Ao informar a situação tributária do ICMS **20, 30, 40, 41, 50, 70 ou 90,**se  informada a TAG  **motDesICMS**será necessário informar **vICMSDeson com valor.**

A situação tributária do ICMS é cadastrada no **TES** no campo **Sit. trib. ICMS** **(F4\_SITTRIB)**

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360041920134)

2- Verifique se realmente foi utilizada a situação tributária do ICMS corretacaso esteja  será necessário informar as TAGS **vICMSDeson**e **motDesICMS.**

Para isso preencha no**TES** na Aba **Outros**o campo F4\_MOTICM  **Mot. Desone.**

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360042764713)

3 - Além disso, realize as configurações abaixo:

* **Exemplo ICMS 20 com Motivo 9 e redução de ICMS:**

**No TES:**

* Campo Agrega valor (F4\_AGREG = S)
* Campo Motivo de desoneração (F4\_MOTICMS = 9)
* Campo Sit. trib. ICM (F4\_SITTRIB = 20)
* Campo Calcula ICMS (F4\_ICM= S)
* Campo Red. do ICMS (F4\_BASEICM= preenchido)

Nessa configuração o valor ICMS desonerado  **NÃO** **é** **descontado** do valor total da nota.

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360043567113)**

**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360042729334)**

**No TES:**

* Campo Agrega valor (F4\_AGREG = D)
* Campo Motivo de desoneração (F4\_MOTICMS = 9)
* Campo Sit. trib. ICM (F4\_SITTRIB = 20)
* Campo Calcula ICMS (F4\_ICM= S)
* Campo Red. do ICMS (F4\_BASEICM= preenchido)

Nessa configuração o valor ICMS desonerado é **descontado** do valor total da nota.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360042814094)

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360042814274)

* **Exemplo ICMS 30 :**

**No TES:**

* Campo Agrega valor (F4\_AGREG = S)
* Campo Motivo de desoneração (F4\_MOTICMS = 9)
* Campo Sit. trib. ICM (F4\_SITTRIB = 30)
* Campo Calcula ICMS (F4\_ICM= S)

Nessa configuração o valor ICMS desonerado  **NÃO** **é** **descontado** do valor total da nota.

**No TES:**

* Campo Agrega valor (F4\_AGREG = D)
* Campo Motivo de desoneração (F4\_MOTICMS = 9)
* Campo Sit. trib. ICM (F4\_SITTRIB = 30)
* Campo Calcula ICMS (F4\_ICM= S)

Nessa configuração o valor ICMS desonerado é **descontado** do valor total da nota.

* **Exemplo ICMS 40 com Motivo 9:**

**No TES:**

* Campo Agrega valor (F4\_AGREG = D)
* Campo Motivo de desoneração (F4\_MOTICMS = 9)
* Campo Sit. trib. ICM (F4\_SITTRIB = 40)
* Campo Calcula ICMS (F4\_ICM= S)

Nessa configuração o valor ICMS desonerado é **descontado** do valor total da nota.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360042513594)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360042513674)

**No TES:**

* Campo Agrega valor (F4\_AGREG = S)
* Campo Motivo de desoneração (F4\_MOTICMS = 9)
* Campo Sit. trib. ICM (F4\_SITTRIB = 40)
* Campo Calcula ICMS (F4\_ICM= S)

Nessa configuração o valor ICMS desonerado  **NÃO** **é** **descontado** do valor total da nota.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360042523114)

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360042523214)

* **Exemplo ICMS 50 com Motivo 9:**

**No TES:**

* Campo Agrega valor (F4\_AGREG = S)
* Campo Motivo de desoneração (F4\_MOTICMS = 9)
* Campo Sit. trib. ICM (F4\_SITTRIB = 50)
* Campo Calcula ICMS (F4\_ICM= S)

Nessa configuração o valor ICMS desonerado  **NÃO** **é** **descontado** do valor total da nota.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045517873)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045517993)

* **Exemplo ICMS 70 com Motivo 9 e redução de ICMS:**

**No TES:**

* Campo Agrega valor (F4\_AGREG = S)
* Campo Motivo de desoneração (F4\_MOTICMS = 9)
* Campo Sit. trib. ICM (F4\_SITTRIB = 20)
* Campo Calcula ICMS (F4\_ICM= S)
* Campo Red. do ICMS (F4\_BASEICM= preenchido)

Se a **redução for no ICMS-ST**

* Campo Red. do ICMS (F4\_BSICMS-St)

Nessa configuração o valor ICMS desonerado  **NÃO** **é** **descontado** do valor total da nota.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045668973)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045669173)

**No TES:**

* Campo Agrega valor (F4\_AGREG = D)
* Campo Motivo de desoneração (F4\_MOTICMS = 9)
* Campo Sit. trib. ICM (F4\_SITTRIB = 70)
* Campo Calcula ICMS (F4\_ICM= S)
* Campo Red. do ICMS (F4\_BASEICM= preenchido)

Se a **redução for no ICMS-ST**

* Campo Red. do ICMS (F4\_BSICMS-St)

Nessa configuração o valor ICMS desonerado  **NÃO** **é** **descontado** do valor total da nota.

Nessa configuração o valor ICMS desonerado é **descontado** do valor total da nota.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045672033)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360044810454)

* **Exemplo ICMS 90 com Motivo 9:**

**No TES:**

* Campo Agrega valor (F4\_AGREG = D)
* Campo Motivo de desoneração (F4\_MOTICMS = 9)
* Campo Sit. trib. ICM (F4\_SITTRIB = 90)
* Campo Calcula ICMS (F4\_ICM= S)

Nessa configuração o valor ICMS desonerado é **descontado** do valor total da nota.

**No TES:**

* Campo Agrega valor (F4\_AGREG = S)
* Campo Motivo de desoneração (F4\_MOTICMS = 9)
* Campo Sit. trib. ICM (F4\_SITTRIB = 90)
* Campo Calcula ICMS (F4\_ICM= S)

Nessa configuração o valor ICMS desonerado  **NÃO** **é** **descontado** do valor total da nota.

* **Como configurar ICMS 40 com Motivo de desoneração 8 Órgão Público:**

Ao gerar nota para empresa Orgão Público (campo A1\_TPESSOA = EP)  
  
• Campo Agrega Valor (F4\_AGREG = “D”) – Indica que deve descontar o valor do imposto do valor contábil.   
• Campo Cálculo ICMS (F4\_ICM = “Sim”) – Indica que haverá o cálculo do ICMS.   
• Campo L.Fiscal ICMS (F4\_LFICM =”Isento”) – Indica que será escriturado como Isento.   
• Campo Sit.Trib.ICMS (F4\_SITTRIB =”40”) – Indica que Isento.   
• Campo Mot.Desone. (F4\_MOTICMS=8)

4 - Após isso, exclua a nota e gere novamente.

* **Saiba mais:**

* Conforme a nota técnica 2016.002\_v\_1.61 podem ser utilizados o seguintes **motivos de desoneração** para cada **CST:**

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360042526454)

**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360043371093)**

**![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360043372173)**

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360043372453)

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360042527894)

**Importante:**

Para atender a Resolução 13 da Sefaz do RJ deverá configurar conforme o link abaixo:

[MP - FIS - Configuração para o cálculo do ICMS Desonerado Resolução SEFAZ 13/2019 RJ](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360030959773)

Além disso, há o Parâmetro **MV\_DESONRJ** conforme o print e o link abaixo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17462365705495)

<https://tdn.totvs.com/pages/releaseview.action?pageId=518467133>

**Importante:**

Caso seja nota de **SUFRAMA** realizar as configurações abaixo:

[CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Como configurar o sistema para calcular SUFRAMA?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034294253)

**Obs: Para nota de suframa deve sempre usar o motivo da desoneração F4\_MOTICMS= 7 (suframa) e sempre haverá o abatimento da tag vICMSDeson do total da nota.**

* Para nota de **Suframa** será considerado:

Na linha da tabelas **CD2** o campo **CD2\_IMP= ZFM** será levado o valor do campo **CD2\_DESCZF**

* **Validação da Sefaz:**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360044289974)

**Importante:**

Caso o grupo do **ICMS 90** não tenha valor o XML será gerado conforme exemplo abaixo sem valor do ICMS desonerado ou o Motivo de desoneração **para atender a Exceção**:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360047872433)
