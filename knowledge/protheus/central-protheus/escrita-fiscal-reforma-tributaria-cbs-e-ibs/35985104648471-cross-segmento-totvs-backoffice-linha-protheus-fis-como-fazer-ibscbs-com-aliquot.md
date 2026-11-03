---
article_id: 35985104648471
category: Escrita Fiscal - Reforma Tributaria - CBS e IBS
content_hash: ec9b55ab14db9d853209ee4c0509bd68f78d05de4e3a3f7884513aa37eabd378
fetched_at: '2026-06-28T22:39:15.735789+00:00'
product: protheus
section_id: 33305945453079
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - Como fazer IBS/CBS
  com aliquota reduzida?
type: support-article
updated_at: '2025-11-17T21:29:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35985104648471-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-FIS-Como-fazer-IBS-CBS-com-aliquota-reduzida
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35985097817239) Tempo aproximado para leitura: 00:10**min**  
  
**Dúvida**  
Como fazer IBS/CBS com aliquota reduzida?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**

A Reforma Tributária, instituída pela Emenda Constitucional nº 132/2023 e regulamentada pela Lei Complementar nº 214/2025, prevê a redução de 60% na alíquota de IBS e CBS para setores específicos, como saúde, educação, medicamentos e produtos agropecuários. 

Segue um exemplo

Valor da mercadoria = 1000,00

redução da aliquota de 60%

Aliquota IBS = 0,10

Aliquota CBS = 0,90

Nesse exemplo vamos trabalhar com a forma Hibrida de calculo, sendo ICMS, PIS e COFINS pelo TES e IBS/CBS pelo Configurador de tributos 

OBS.:Os cadastros incluídos na **Regra de Cálculo - Documentos Fiscais** pela funcionalidade de **Carga Regras de Cálculo CBS/IBS** apresentarão a **Vigência Inicial (F2B\_VIGINI)** para 01/01/2026 e a **Vigência Final (F2B\_VIGFIM)** para 31/12/2026 e o **Status (F2B\_STATUS)** será **"Em Teste".**

Para inicio dos testes precisam ser alterados Vigencia Inicial para 01/10/2025 e Status para Aprovado

ID tributos

CBSFED

IBSEST

Regra de Base de calculo do IBS/CBS

Base de Cálculo:

* **Cód. Regra (F27\_CODIGO)**: TB0001
* **Descrição (F27\_DESC)**: BASE DE CALCULO: CBS FED/IBS EST
* **Valor Origem (F27\_VALORI)**: 11 - Formula Manual
* Fórmula: ( O:VAL\_MERCADORIA + O:FRETE + O:SEGURO + O:DESPESAS + O:VAL\_II ) - ( O:DESCONTO + O:VAL\_PS2 + O:VAL\_CF2 + O:VAL\_ICMS + O:VAL\_DIFAL + O:VAL\_FECP + O:VAL\_FCPDIF + O:VAL\_ISS )

Regra de Aliquota = CBS

Alíquota:

* **Cód. Regra (F28\_CODIGO)**: TA0001
* **Descrição (F28\_DESC)**: ALÍQUOTA 0.9%
* **Valor Origem (F28\_VALORI)**: 04 - Aliquota Informada Manualmente
* **Tp. Alíquota (F28\_TPALIQ)**: 1 - Percentual
* **Alíquota (F28\_ALIQ)**: 0,90
* Redução da aliquota = 60%

  ![](https://centraldeatendimento.totvs.com/hc/article_attachments/35985097818135)

Regra de Aliquota = IBS

* **Cód. Regra (F28\_CODIGO)**: TA0002
* **Descrição (F28\_DESC)**: ALÍQUOTA 0.1%
* **Valor Origem (F28\_VALORI)**: 04 - Aliquota Informada Manualmente
* **Tp. Alíquota (F28\_TPALIQ)**: 1 - Percentual
* **Alíquota (F28\_ALIQ)**: 0,10
* Redução da aliquota = 60%

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35985097818647)

Regra de Escrituração IBS/CBS

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35985097818903)

Regra de Calculo Documentos fiscais - CBS

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35985104637207)![](https://centraldeatendimento.totvs.com/hc/article_attachments/35985097822615)

Regra de Calculo Documentos Fiscais - IBS

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35985097823127)![](https://centraldeatendimento.totvs.com/hc/article_attachments/35985097823639)

Pedido de Vendas

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35985097824791)

Gravação na Cj3 e F2D

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35985097825687)![](https://centraldeatendimento.totvs.com/hc/article_attachments/35985097826327)
