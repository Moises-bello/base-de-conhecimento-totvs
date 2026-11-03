---
article_id: 4409534620823
category: NFe - Nota Fiscal Eletrônica
content_hash: 953a1dd4cda8ae0a45360d5c40b1a3c6547dca1a149be76e2b756adc36bbe91c
fetched_at: '2026-06-28T22:40:03.282531+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos -  815 Rejeição:
  Valor do ICMS Interestadual para UF de Destino difere do calculado'
type: support-article
updated_at: '2026-04-02T19:53:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409534620823-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-815-Rejei%C3%A7%C3%A3o-Valor-do-ICMS-Interestadual-para-UF-de-Destino-difere-do-calculado
---

**Dúvida**Como solucionar a Rejeição 815 : Valor do ICMS Interestadual para UF de Destino difere do calculado ?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.

**Solução**

Ao fazer nota de **operação interestadual, para consumidor final e não contribuinte** a Sefaz espera que Se CST de **ICMS = 00** e informado o grupo **ICMSUFDest Valor do ICMS Interestadual para UF de Destino (tag: vICMSUFDest) difere de: ((vBCUFDest \* pICMSUFDest) - (vBC \* pICMSInter)) \* pICMSInterPart (\*4)**

**Observação 1:** Se o resultado do cálculo for menor que zero deverá ser informado o valor “0.00”.

**Observação 2:** Se existir benefício fiscal no destino, o valor da base de cálculo no ICMS de destino (vBCUFDest) deverá ser informado considerando esse benefício.

* **Conforme o exemplo :**

![com_difal.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/4409527832727)

* Verifique se o sistema está **atualizado conforme o link abaixo:**

[Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Nota técnica 2020.005](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052495714)

1.  Preencher no TES o campo **Calcula ICMS "F4\_ICM" = S - Sim**

![CALCU_ICMS_SIM.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/12262982868631)

2. **Preencher no TES** o campo **Calc.Dif.ICM** (F4\_COMPL) = SIM

![CALCU_DIF_ICM.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/12218305885719)

3. Para isso **preencher no TES** o campo **Calc.Difal** (F4\_DIFAL) = SIM

![CALCU_DIF_ICM.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/12219848276247)

4. Acessar o módulo **Configurador (SIGACFG)**, em seguida em **Ambiente /****Cadastros / Parâmetros** clicar em **editar****MV\_PPDIFAL**={{2016,40,60},{2017,60,40},{2018,80,20},{2019,100,0},{2020,100,0},{2021,100,0},{2022,100,0},{2023,100,0}}

![MV_PPDIFAL.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/12262451550871)

5. Após isso, exclua a nota e gere novamente.

6. Preencher como consumidor final, altere **no pedido de vendas** o campo **C5\_TIPOCLI  "Tipo Cliente"** **diferente de** **F - Cons. Final**

![CONSUMIDOR_FINAL.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/12262489971223)

7. Após isso, exclua a nota e gere novamente.

8. Caso seja **Contribuinte o destinatário** preencha a inscrição estadual no campo  Ins. Estad. **"A1\_INSCR"**

![Ins._Estad..gif](https://centraldeatendimento.totvs.com/hc/article_attachments/12262654101015)​

9. Preencha o campo Destaca IE **"A1\_IENCONT"**   em branco

![destaca_IE_em_branco.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/12262877763991)

10. Preencha o campo Contribuinte **"A1\_CONTRIB"**  1- Sim

![contrib_sim.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/12262677860247)

11. Após isso, exclua a nota e gere novamente.

12. Caso seja I**sento o destinatário** deixe em branco ou Preencha com literal Isento o campo de inscrição estadual no campo  Ins. Estad. **"A1\_INSCR"**

​![inscr_ISENTO.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/12262960898199)

13. Preencha o campo Destaca IE **"A1\_IECONT"**  em branco

![destaca_IE_em_branco.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/12262877763991)

14. Preencha o campo Contribuinte **"A1\_CONTRIB"**  1- Sim

![contrib_sim.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/12262677860247)

15. Após isso, exclua a nota e gere novamente.

16. Caso a situação tributária da nota não seja **00 - tributado integralmente altere no TES**Sit. trib. ICM "F4\_SITTRIB" diferente de 00:

![F4_SITTRIB.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/12262979926551)

17. Após isso, exclua a nota e gere novamente.

* **Saiba mais:**

**O conteúdo das TAGS serão retirados dos campos:**

* Grupo ICMSUFDEST x Campos CD2 da linha **CD2\_IMP = CMP:**

Tag **vBCUFDest** -> **CD2\_BC**

Tag **pFCPUFDest** -> **CD2\_PFCP**

Tag **pICMSUFDest** -> **CD2\_ALIQ**

Tag **pICMSInter** -> **CD2\_ADIF**

Tag **pICMSInterPart** -> **CD2\_PDDES**

Tag **vFCPUFDest** -> **CD2\_VFCP**

Tag **vICMSUFDest** -> **CD2\_VDDES**

Tag **vICMSUFRemet** -> **CD2\_VLTRIB**

* **Validação da Sefaz:**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4410974638359)

* **Saiba mais:**

**[Parecer da Consultoria](https://tdn.totvs.com/pages/releaseview.action?pageId=643728649)**
