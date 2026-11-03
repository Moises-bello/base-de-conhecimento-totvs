---
article_id: 9942920525719
category: NFe - Nota Fiscal Eletrônica
content_hash: 0bc30eff2e2f6ae39da56dfd3c278b2c5133e38f03c09654dec6e676a6177fd8
fetched_at: '2026-06-28T22:40:05.425843+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 876 Rejeição Operação
  interestadual para Consumidor Final e valor do FCP informado em campo diferente
  de vFCPUFDest
type: support-article
updated_at: '2025-06-23T11:53:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9942920525719-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-876-Rejei%C3%A7%C3%A3o-Opera%C3%A7%C3%A3o-interestadual-para-Consumidor-Final-e-valor-do-FCP-informado-em-campo-diferente-de-vFCPUFDest
---

**Dúvida**Como solucionar a rejeição 876 Rejeição Operação interestadual para Consumidor Final e valor do FCP informado em campo diferente de vFCPUFDest  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - Todas as versões

Cross Segmentos - TSS - a partir da versão 12

**Solução**

Conforme e **NT - Nota Técnica****2016/002**, essa rejeição ocorre quando é Operação interestadual *tag* **idDest**=**2** para Consumidor Final *tag* **indFinal**=**1**, não contribuinte *tag* **indIEDest**=**9** e informado o valor do **FCP - Fundo de Combate à Pobreza***tag* **vFCP**.

* **Conforme o exemplo :**

![com_difal.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/32986127728535)

1.  Preencher no TES o campo **Calcula ICMS "F4\_ICM" = S - Sim**

![CALCU_ICMS_SIM.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/32986127729175)

2. **Preencher no TES** o campo **Calc.Dif.ICM** (F4\_COMPL) = SIM

![CALCU_DIF_ICM.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/32986127729559)

3. Para isso **preencher no TES** o campo **Calc.Difal** (F4\_DIFAL) = SIM

![CALCU_DIF_ICM.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/32986127730071)

4. Acessar o módulo **Configurador (SIGACFG)**, em seguida em **Ambiente /****Cadastros / Parâmetros** clicar em **editar****MV\_PPDIFAL**={{2016,40,60},{2017,60,40},{2018,80,20},{2019,100,0},{2020,100,0},{2021,100,0},{2022,100,0},{2023,100,0}}

![MV_PPDIFAL.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/32986127739799)

5. Após isso, exclua a nota e gere novamente.

6. Preencher como consumidor final, altere **no pedido de vendas** o campo **C5\_TIPOCLI  "Tipo Cliente"****diferente de** **F - Cons. Final**

![CONSUMIDOR_FINAL.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/32986127740055)

7. Após isso, exclua a nota e gere novamente.

8. Caso seja **Contribuinte o destinatário** preencha a inscrição estadual no campo  Ins. Estad. **"A1\_INSCR"**

![Ins._Estad..gif](https://centraldeatendimento.totvs.com/hc/article_attachments/32986127740311)​

9. Preencha o campo Destaca IE **"A1\_IENCONT"**   em branco

![destaca_IE_em_branco.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/32986151617815)

10. Preencha o campo Contribuinte **"A1\_CONTRIB"**  1- Sim

![contrib_sim.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/32986151623191)

11. Após isso, exclua a nota e gere novamente.

12. Caso seja I**sento o destinatário** deixe em branco ou Preencha com literal Isento o campo de inscrição estadual no campo  Ins. Estad. **"A1\_INSCR"**

​![inscr_ISENTO.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/32986127741335)

13. Preencha o campo Destaca IE **"A1\_IECONT"**  em branco

![destaca_IE_em_branco.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/32986151617815)

14. Preencha o campo Contribuinte **"A1\_CONTRIB"**  1- Sim

![contrib_sim.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/32986151623191)

15. Após isso, exclua a nota e gere novamente.

16. Caso a situação tributária da nota não seja **00 - tributado integralmente altere no TES**Sit. trib. ICM "F4\_SITTRIB" diferente de 00:

![F4_SITTRIB.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/12379648643351)

17. Após isso, exclua a nota e gere novamente.

* **Saiba mais:**

**O conteúdo das TAGS serão retirados dos campos:**

* Grupo ICMSUFDEST x Campos CD2:

Tag **vBCUFDest** -> **CD2\_BC**

Tag **pFCPUFDest** -> **CD2\_PFCP**

Tag **pICMSUFDest** -> **CD2\_ALIQ**

Tag **pICMSInter** -> **CD2\_ADIF**

Tag **pICMSInterPart** -> **CD2\_PDDES**

Tag **vFCPUFDest** -> **CD2\_VFCP**

Tag **vICMSUFDest** -> **CD2\_VDDES**

Tag **vICMSUFRemet** -> **CD2\_VLTRIB**

* ***Validação da Sefaz:***

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9942838259351)
