---
article_id: 36147453667095
category: Escrita Fiscal - Reforma Tributaria - CBS e IBS
content_hash: 3823969fff176ac389d7748c1270074d6831c5917d8ba5d1c4fa66d9c82ef4a8
fetched_at: '2026-06-28T22:39:15.684514+00:00'
product: protheus
section_id: 33305945453079
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - Como calcular IBS/CBS
  cClasstrib 000001 na venda Hibrida ?
type: support-article
updated_at: '2025-11-07T17:33:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36147453667095-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-FIS-Como-calcular-IBS-CBS-cClasstrib-000001-na-venda-Hibrida
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36147440916503) Tempo aproximado para leitura: 00:10 **min**  
  
**Dúvida**  
Como calcular IBS/CBS cClasstrib 000001 na venda Hibrida ?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - a partir da versão 12.1.2310  
  
**Solução**

Nesse exemplo vamos trabalhar com a forma Hibrida de calculo, sendo ICMS, PIS e COFINS pelo TES e IBS/CBS pelo Configurador de tributos 

<https://tdn.totvs.com/pages/releaseview.action?pageId=955482625>

**Exemplo de Calculo**

Mercadoria = 1000,00

Base de calculo do ICMS = 1000,00\*18% = 180,00

Base do PIS/COFINS = 820,00

PIS 1,65% = 13,53

COFINS 7,6% = 62,32

TES

CFOP = 5102

Calcula ICMS = sim

L fiscal ICMS = tributado

CST = 00

PIS/COF = ambos

Cred PIS/COF = debita

CST PIS= 01

CST COF= 01

Base de calculo do IBS/CBS = 1000,00-180,00-13,53-62,32 = 744,15

CBS - 744,15\*0,90= 6,70

IBS - 744,15\*0,10= 0,74

Parecer da Consultoria

<https://tdn.totvs.com/pages/releaseview.action?pageId=980989292>

Carga Inicial do IBS/CBS

OBS.: Os cadastros incluídos na **Regra de Cálculo - Documentos Fiscais** pela funcionalidade de **Carga Regras de Cálculo CBS/IBS** apresentarão a **Vigência Inicial (F2B\_VIGINI)** para 01/01/2026 e a **Vigência Final (F2B\_VIGFIM)** para 31/12/2026 e o **Status (F2B\_STATUS)** será **"Em Teste".**

Para inicio dos testes precisam ser alterados Vigência Inicial para 01/10/2025 e Status para Aprovado

ID tributos

CBSFED

IBSEST

Regra de Base de calculo do IBS/CBS

Base de Cálculo:

* **Cód. Regra (F27\_CODIGO)**: TB0001
* **Descrição (F27\_DESC)**: BASE DE CALCULO: CBS FED/IBS EST
* **Valor Origem (F27\_VALORI)**: 11 - Formula Manual
* Fórmula: ( O:VAL\_MERCADORIA + O:FRETE + O:SEGURO + O:DESPESAS + O:VAL\_II ) - ( O:DESCONTO + O:VAL\_PS2 + O:VAL\_CF2 + O:VAL\_ICMS + O:VAL\_DIFAL + O:VAL\_FECP + O:VAL\_FCPDIF + O:VAL\_ISS )

Alíquota:

* **Cód. Regra (F28\_CODIGO)**: TA0001
* **Descrição (F28\_DESC)**: ALÍQUOTA 0.9%
* **Valor Origem (F28\_VALORI)**: 04 - Alíquota Informada Manualmente
* **Tp. Alíquota (F28\_TPALIQ)**: 1 - Percentual
* **Alíquota (F28\_ALIQ)**: 0,90

* **Cód. Regra (F28\_CODIGO)**: TA0002
* **Descrição (F28\_DESC)**: ALÍQUOTA 0.1%
* **Valor Origem (F28\_VALORI)**: 04 - Alíquota Informada Manualmente
* **Tp. Alíquota (F28\_TPALIQ)**: 1 - Percentual
* **Alíquota (F28\_ALIQ)**: 0,10

**Na importação o sistema não cria a regra de escrituração, deve ser configurada**

Regra de Escrituração

Tabela cClasstrib atualizada , conforme instrução

[CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Como importar a tabela cClassTrib-IBS/CBS no Configurador de Tributos?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/34662420522391-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-importar-a-tabela-cClassTrib-IBS-CBS-no-Configurador-de-Tributos)

cClasstrib = 000001

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36147440918167)

Regra de Calculo Documentos Fiscais CBS

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36147440920343)![](https://centraldeatendimento.totvs.com/hc/article_attachments/36147440920727)

Regra de Calculo Documentos Fiscais IBS

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36147453619607)

Perfis os mesmos

Pedido de Vendas

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36147453621399)

Gravação na CJ3 e F2D

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36147440931735)![](https://centraldeatendimento.totvs.com/hc/article_attachments/36147440936599)
