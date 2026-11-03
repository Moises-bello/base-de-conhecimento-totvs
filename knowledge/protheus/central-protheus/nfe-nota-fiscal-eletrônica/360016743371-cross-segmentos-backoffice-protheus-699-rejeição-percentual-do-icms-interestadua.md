---
article_id: 360016743371
category: NFe - Nota Fiscal Eletrônica
content_hash: b26a969c54ff816b646bee2da02d0bd122421358f088558c917a380a1e02dadd
fetched_at: '2026-06-28T22:40:03.042229+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus -  699 Rejeição : Percentual do ICMS
  Interestadual para a UF de destino difere do previsto para o ano da Data de Emissão'
type: support-article
updated_at: '2025-08-11T21:38:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016743371-Cross-Segmentos-Backoffice-Protheus-699-Rejei%C3%A7%C3%A3o-Percentual-do-ICMS-Interestadual-para-a-UF-de-destino-difere-do-previsto-para-o-ano-da-Data-de-Emiss%C3%A3o
---

**Dúvida**Como corrigir a rejeição 699 : Percentual do ICMS Interestadual para a UF de destino difere do previsto para o ano da Data de Emissão ?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.

**Solução**   
1.  Preencher no TES o campo **Calcula ICMS "F4\_ICM" = S - Sim**

![CALCU_ICMS_SIM.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/17495588419863)

2. **Preencher no TES** o campo **Calc.Dif.ICM** (F4\_COMPL) = SIM

![CALCU_DIF_ICM.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/17495608623383)

3. Para isso **preencher no TES** o campo **Calc.Difal** (F4\_DIFAL) = SIM

![CALCU_DIF_ICM.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/17495588438423)

4. Acessar o módulo **Configurador (SIGACFG)**, em seguida em **Ambiente /****Cadastros / Parâmetros** clicar em **editar****MV\_PPDIFAL**={{2016,40,60},{2017,60,40},{2018,80,20},{2019,100,0},{2020,100,0},{2021,100,0},{2022,100,0},{2023,100,0},{2024,100,0},{2025,100,0}}

![MV_PPDIFAL.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/17495608635799)

5. Após isso, exclua a nota e gere novamente.

6. Preencher como consumidor final, altere **no pedido de vendas** o campo **C5\_TIPOCLI  "Tipo Cliente"****diferente de** **F - Cons. Final**

![CONSUMIDOR_FINAL.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/17495608643607)

7. Após isso, exclua a nota e gere novamente.

8. Caso seja **Contribuinte o destinatário** preencha a inscrição estadual no campo  Ins. Estad. **"A1\_INSCR"**

![Ins._Estad..gif](https://centraldeatendimento.totvs.com/hc/article_attachments/17495588458519)​

9. Preencha o campo Destaca IE **"A1\_IENCONT"**   em branco

![destaca_IE_em_branco.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/17495608655767)

10. Preencha o campo Contribuinte **"A1\_CONTRIB"**  1- Sim

![contrib_sim.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/17495608666775)

11. Após isso, exclua a nota e gere novamente.

12. Caso seja I**sento o destinatário** deixe em branco ou Preencha com literal Isento o campo de inscrição estadual no campo  Ins. Estad. **"A1\_INSCR"**

​![inscr_ISENTO.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/17495608670615)

13. Preencha o campo Destaca IE **"A1\_IECONT"**  em branco

![destaca_IE_em_branco.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/17495608655767)

14. Preencha o campo Contribuinte **"A1\_CONTRIB"**  1- Sim

![contrib_sim.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/17495608666775)

15. Após isso, exclua a nota e gere novamente.

* **Importante:**

Além disso, em alguns casos mesmo com o percentual correto a nota de não contribuinte, consumidor final e operação interestadual ao retornar uma nota do ano anterior pode ser gerada como ***FINNFE = 1*** desde que CFOP esteja Anexo XIII.04 caso não esteja apenas os CFOPS de finalidade de devolução.

Nestas situações a ***tag pICMSInterPart*** será gerada com o percentual relativo ao ano de emissão da NF-e referenciada.

**Conforme a FAQ do TDN:** <http://tdn.totvs.com.br/pages/releaseview.action?pageId=224104756>

 Nos casos específicos de retorno de mercadoria obrigatoriamente deverá ser utilizada as CFOP ´s expressas no Anexo XIII.04.

E para devolução informar os CFOPS que constam na tabela da nota técnica 2013.005\_v\_1.22 na página 130 pela sefaz com finalidade igual 4.

O Anexo XIII.04 consta na nota técnica ***2015.003\_ v\_1.94 página 22.*** (Baixe no site da Sefaz).

* **Saiba mais:**

Ao fazer nota de devolução, se houver mais de uma nota referenciada essas notas precisam ser do mesmo ano, caso sejam de anos diferentes será necessário fazer a devolução separada para autorização.

**O conteúdo das TAGS serão retirados dos campos:**

* Grupo ICMSUFDEST x Campos CD2:

Tag **vBCUFDest** -> **CD2\_BC**

Tag **pFCPUFDest** -> **CD2\_PFCP**

Tag **pICMSUFDest** -> **CD2\_ALIQ**

Tag **pICMSInter** -> **CD2\_ADIF**

Tag **pICMSInterPart** -> **CD2\_PDDES - conforme parâmetro MV\_PPDIFAL**

Tag **vFCPUFDest** -> **CD2\_VFCP**

Tag **vICMSUFDest** -> **CD2\_VDDES**

Tag **vICMSUFRemet** -> **CD2\_VLTRIB**

* **Conforme o Exemplo abaixo:**

<pICMSInterPart>40.0000</pICMSInterPart> → 2016

<pICMSInterPart>60.0000</pICMSInterPart> → 2017

<pICMSInterPart>80.0000</pICMSInterPart> → 2018

<pICMSInterPart>100.0000</pICMSInterPart> → 2019 **( E os anos posteriores)**
