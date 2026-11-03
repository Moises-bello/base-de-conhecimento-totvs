---
article_id: 360034776874
category: NFe - Nota Fiscal Eletrônica
content_hash: 27dc89fda703127b7f855b893240cd573d4366d66ec828086550e890bcdc043e
fetched_at: '2026-06-28T22:40:05.209733+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 627  Rejeição:
  O valor do ICMS desonerado deve ser informado'
type: support-article
updated_at: '2025-06-12T14:54:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034776874-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-627-Rejei%C3%A7%C3%A3o-O-valor-do-ICMS-desonerado-deve-ser-informado
---

**Dúvida**Como solucionar a rejeição 627 Rejeição: O valor do ICMS desonerado deve ser informado ?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.  
  
**Solução**

1- Caso a UF de transmissão não valide a rejeição 934 retire do **TES o motivo de desoneração.**

* Deixe o campo no**TES** na Aba **Outros**F4\_MOTICM  **Mot. Desone. em branco:**

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17461674298647)

2- Exclua a nota e gere novamente.

3- Caso sua **UF de transmissão valide a rejeição 934,** ao informar a situação tributária do ICMS **20, 30, 40, 41, 50, 70 ou 90,**se  informada a TAG  **motDesICMS**será necessário informar **vICMSDeson com valor.**

A situação tributária do ICMS é cadastrada no **TES** no campo **Sit. trib. ICMS** **(F4\_SITTRIB)**

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17461674320791)

4- Verifique se realmente foi utilizada a situação tributária do ICMS corretacaso esteja  será necessário informar as TAGS **vICMSDeson**e **motDesICMS.**

Para isso preencha no**TES** na Aba **Outros**o campo F4\_MOTICM  **Mot. Desone.**

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17461674298647)

5 - Após isso exclua a nota e gere novamente.

* **Saiba mais:**
* Conforme a nota técnica 2016.002\_v\_1.61 podem ser utilizados o seguintes **motivos de desoneração**para cada**CST:**

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17461674333463)

**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17461674336791)**

**![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17461674350871)**

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17461649229207)

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17461674374551)

**Importante:**

Para atender a Resolução 13 da Sefaz do RJ deverá configurar conforme o link abaixo:

[MP - FIS - Configuração para o cálculo do ICMS Desonerado Resolução SEFAZ 13/2019 RJ](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360030959773)

Além disso, há o Parâmetro **MV\_DESONRJ** conforme o print e o link abaixo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360060892833)

[Pacote de correções - Gravação da tabela CD2](https://tdn.totvs.com/pages/releaseview.action?pageId=518467133)

* **Exemplo ICMS 20 com Motivo 9 e redução de ICMS:**

**No TES:**

* Campo Agrega valor (F4\_AGREG = S)
* Campo Motivo de desoneração (F4\_MOTICMS = 9)
* Campo Sit. trib. ICM (F4\_SITTRIB = 20)
* Campo Calcula ICMS (F4\_ICM= S)
* Campo Red. do ICMS (F4\_BASEICM= preenchido)

Nesta configuração o valor ICMS desonerado  **NÃO** **é** **descontado** do valor total da nota.

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17461674380951)**

**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17461649263255)**

**No TES:**

* Campo Agrega valor (F4\_AGREG = D)
* Campo Motivo de desoneração (F4\_MOTICMS = 9)
* Campo Sit. trib. ICM (F4\_SITTRIB = 20)
* Campo Calcula ICMS (F4\_ICM= S)
* Campo Red. do ICMS (F4\_BASEICM= preenchido)

Nesta configuração o valor ICMS desonerado é **descontado** do valor total da nota.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17461649267095)

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17461649282711)

* **Exemplo ICMS 30 :**

**No TES:**

* Campo Agrega valor (F4\_AGREG = S)
* Campo Motivo de desoneração (F4\_MOTICMS = 9)
* Campo Sit. trib. ICM (F4\_SITTRIB = 30)
* Campo Calcula ICMS (F4\_ICM= S)

Nesta configuração o valor ICMS desonerado  **NÃO** **é** **descontado** do valor total da nota.

**No TES:**

* Campo Agrega valor (F4\_AGREG = D)
* Campo Motivo de desoneração (F4\_MOTICMS = 9)
* Campo Sit. trib. ICM (F4\_SITTRIB = 30)
* Campo Calcula ICMS (F4\_ICM= S)

Nesta configuração o valor ICMS desonerado é **descontado** do valor total da nota.

* **Exemplo ICMS 40 com Motivo 9:**

**No TES:**

* Campo Agrega valor (F4\_AGREG = D)
* Campo Motivo de desoneração (F4\_MOTICMS = 9)
* Campo Sit. trib. ICM (F4\_SITTRIB = 40)
* Campo Calcula ICMS (F4\_ICM= S)

Nesta configuração o valor ICMS desonerado é **descontado** do valor total da nota.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17461674434711)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17461674439959)

**No TES:**

* Campo Agrega valor (F4\_AGREG = S)
* Campo Motivo de desoneração (F4\_MOTICMS = 9)
* Campo Sit. trib. ICM (F4\_SITTRIB = 40)
* Campo Calcula ICMS (F4\_ICM= S)

Nesta configuração o valor ICMS desonerado  **NÃO** **é** **descontado** do valor total da nota.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17461649325463)

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17461674460567)

* **Exemplo ICMS 50 com Motivo 9:**

**No TES:**

* Campo Agrega valor (F4\_AGREG = S)
* Campo Motivo de desoneração (F4\_MOTICMS = 9)
* Campo Sit. trib. ICM (F4\_SITTRIB = 50)
* Campo Calcula ICMS (F4\_ICM= S)

Nesta configuração o valor ICMS desonerado  **NÃO** **é** **descontado** do valor total da nota.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17461649344023)

* **Exemplo ICMS 70 com Motivo 9 e redução de ICMS:**

**No TES:**

* Campo Agrega valor (F4\_AGREG = S)
* Campo Motivo de desoneração (F4\_MOTICMS = 9)
* Campo Sit. trib. ICM (F4\_SITTRIB = 20)
* Campo Calcula ICMS (F4\_ICM= S)
* Campo Red. do ICMS (F4\_BASEICM= preenchido)

Se a **redução for no ICMS-ST**

* Campo Red. do ICMS (F4\_BSICMS-St)

Nesta configuração o valor ICMS desonerado  **NÃO** **é** **descontado** do valor total da nota.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17461649346967)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17461649382935)

**No TES:**

* Campo Agrega valor (F4\_AGREG = D)
* Campo Motivo de desoneração (F4\_MOTICMS = 9)
* Campo Sit. trib. ICM (F4\_SITTRIB = 70)
* Campo Calcula ICMS (F4\_ICM= S)
* Campo Red. do ICMS (F4\_BASEICM= preenchido)

Se a **redução for no ICMS-ST**

* Campo Red. do ICMS (F4\_BSICMS-St)

Nesta configuração o valor ICMS desonerado  **NÃO** **é** **descontado** do valor total da nota.

Nesta configuração o valor ICMS desonerado é **descontado** do valor total da nota.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17461649387415)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17461649399703)

* **Exemplo ICMS 90 com Motivo 9:**

**No TES:**

* Campo Agrega valor (F4\_AGREG = D)
* Campo Motivo de desoneração (F4\_MOTICMS = 9)
* Campo Sit. trib. ICM (F4\_SITTRIB = 90)
* Campo Calcula ICMS (F4\_ICM= S)

Nesta configuração o valor ICMS desonerado é **descontado** do valor total da nota.

**No TES:**

* Campo Agrega valor (F4\_AGREG = S)
* Campo Motivo de desoneração (F4\_MOTICMS = 9)
* Campo Sit. trib. ICM (F4\_SITTRIB = 90)
* Campo Calcula ICMS (F4\_ICM= S)

Nesta configuração o valor ICMS desonerado  **NÃO** **é** **descontado** do valor total da nota.

* **Como configurar ICMS 40 com Motivo de desoneração 8 Órgão Público:**

Ao gerar nota para empresa Orgão Público (campo A1\_TPESSOA = EP)  
  
• Campo Agrega Valor (F4\_AGREG = “D”) – Indica que deve descontar o valor do imposto do valor contábil.   
• Campo Cálculo ICMS (F4\_ICM = “Sim”) – Indica que haverá o cálculo do ICMS.   
• Campo L.Fiscal ICMS (F4\_LFICM =”Isento”) – Indica que será escriturado como Isento.   
• Campo Sit.Trib.ICMS (F4\_SITTRIB =”40”) – Indica que Isento.   
• Campo Mot.Desone. (F4\_MOTICMS=8)

**Importante:**

Caso seja nota de **SUFRAMA**realizar as configurações abaixo:

[CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Como configurar o sistema para calcular SUFRAMA?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034294253)

* Para nota de **Suframa** será considerado:

Na linha da tabelas **CD2** o campo **CD2\_IMP= ZFM** será levado o valor do campo **CD2\_DESCZF**

**Importante:**

* **Caso a UF de transmissão de nota não valide a rejeição 934 e a empresa não deseje gerar no xml valor desonerado e motivo de desoneração.**

[MP-NFE- 934- Rejeição: Não informado valor do ICMS desonerado ou o Motivo de desoneração](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025687693)

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17461674534935)

* **Validação da Sefaz:**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045224774)
