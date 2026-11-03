---
article_id: 4409540998679
category: NFe - Nota Fiscal Eletrônica
content_hash: 067f262c7028361b4eba1862abc90169bcb04fb219f8ca0cd09e95842d7b5be0
fetched_at: '2026-06-28T22:40:05.320978+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 816 Rejeição: Valor
  do ICMS Interestadual para UF do Remetente difere do calculado'
type: support-article
updated_at: '2025-06-18T14:48:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409540998679-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-816-Rejei%C3%A7%C3%A3o-Valor-do-ICMS-Interestadual-para-UF-do-Remetente-difere-do-calculado
---

**Dúvida**Como solucionar a rejeição 816 Rejeição: Valor do ICMS Interestadual para UF do Remetente difere do calculado ?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.

**Solução**Sistema grava base do Difal com frete quando parâmetro: **MV\_DEVTOT = .F. apresenta a Rejeição 815,** quando é nota de devolução com frete.

Foi liberado o pacote de correção da**ISSUE: DSERFISE-2086**

Protheus 12.1.2310: <https://suporte.totvs.com/portal/p/10098/download?e=1124963>

Protheus 12.1.2410 <https://suporte.totvs.com/portal/p/10098/download?e=1171486>

Ao fazer nota de **operação interestadual, para consumidor final e não contribuinte** a Sefaz espera que Se CST de **ICMS = 00** e informado o grupo **ICMSUFDest** Valor do ICMS Interestadual para UF do Remetente **(tag: vICMSUFRemet)** difere de: **((vBCUFDest \* pICMSUFDest) - (vBC \* pICMSInter)) – vICMSUFDest (\*4)**   
  
**Observação 1:** Se o resultado do cálculo for menor que zero deverá ser informado o valor “0.00”.

**Observação 2:** Se existir benefício fiscal de redução de base de cálculo no destino, o valor da base de cálculo no ICMS de destino (vBCUFDest) deverá ser informado considerando esse benefício.

* **Conforme o exemplo :**

![com_difal.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/32896732089367)

* Verifique se o sistema está **atualizado conforme o link abaixo:**

[Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Nota técnica 2020.005](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052495714)

1.  Preencher no TES o campo **Calcula ICMS "F4\_ICM" = S - Sim**

![CALCU_ICMS_SIM.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/32896732093847)

2. **Preencher no TES** o campo **Calc.Dif.ICM** (F4\_COMPL) = SIM

![CALCU_DIF_ICM.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/32896732095511)

3. Para isso **preencher no TES** o campo **Calc.Difal** (F4\_DIFAL) = SIM

![CALCU_DIF_ICM.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/32896705327895)

4. Acessar o módulo **Configurador (SIGACFG)**, em seguida em **Ambiente /****Cadastros / Parâmetros** clicar em **editar****MV\_PPDIFAL**={{2016,40,60},{2017,60,40},{2018,80,20},{2019,100,0},{2020,100,0},{2021,100,0},{2022,100,0},{2023,100,0}}

![MV_PPDIFAL.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/32896705328791)

5. Após isso, exclua a nota e gere novamente.

6. Preencher como consumidor final, altere **no pedido de vendas** o campo **C5\_TIPOCLI  "Tipo Cliente"** **diferente de** **F - Cons. Final**

![CONSUMIDOR_FINAL.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/32896705332375)

7. Após isso, exclua a nota e gere novamente.

8. Caso seja **Contribuinte o destinatário** preencha a inscrição estadual no campo  Ins. Estad. **"A1\_INSCR"**

![Ins._Estad..gif](https://centraldeatendimento.totvs.com/hc/article_attachments/32896732105751)​

9. Preencha o campo Destaca IE **"A1\_IENCONT"**   em branco

![destaca_IE_em_branco.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/32896705338519)

10. Preencha o campo Contribuinte **"A1\_CONTRIB"**  1- Sim

![contrib_sim.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/32896705339543)

11. Após isso, exclua a nota e gere novamente.

12. Caso seja I**sento o destinatário** deixe em branco ou Preencha com literal Isento o campo de inscrição estadual no campo  Ins. Estad. **"A1\_INSCR"**

​![inscr_ISENTO.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/32896732112919)

13. Preencha o campo Destaca IE **"A1\_IECONT"**  em branco

![destaca_IE_em_branco.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/32896705338519)

14. Preencha o campo Contribuinte **"A1\_CONTRIB"**  1- Sim

![contrib_sim.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/32896705339543)

15. Após isso, exclua a nota e gere novamente.

16. Caso a situação tributária da nota não seja **00 - tributado integralmente altere no TES**Sit. trib. ICM "F4\_SITTRIB" diferente de 00:

![F4_SITTRIB.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/32896732115223)

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

* **Validação da Sefaz:**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4410982231831)

* Saiba mais:

**Exceção : O prazo previsto para a Nota Técnica 2020.005 v1.21**

* Ambiente de Homologação:**20/10/2021**
* **Ambiente de Produção:25/10/2021**
