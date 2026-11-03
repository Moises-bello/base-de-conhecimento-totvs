---
article_id: 360036918633
category: Escrita Fiscal - Impostos - ICMS - Difal
content_hash: 68b20b7f246a782423c96dae26122921038469107b9cff768e1b5494fda03c51
fetched_at: '2026-06-28T22:39:19.300527+00:00'
product: protheus
section_id: 1500001549902
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Qual a configuração
  para o calculo do DIFAL por dentro para Nota Fiscal de Entrada?
type: support-article
updated_at: '2024-01-18T12:55:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036918633-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Qual-a-configura%C3%A7%C3%A3o-para-o-calculo-do-DIFAL-por-dentro-para-Nota-Fiscal-de-Entrada
---

**Dúvida**Qual a configuração para o calculo do DIFAL por dentro para Nota Fiscal de Entrada?  
  
**Ambiente**  
Microsiga Protheus – Livros Fiscais – A partir da versão 11.80  
  
**Solução**

Cálculo de base dupla na entrada:

**TES:**

Calcula ICMS = SIM  
Livro de ICMS= Isento ou Outros  
Calc.Dif.ICM = SIM  
Calc.Difal = Vazio ou Não (Este campo é somente para as notas de saída)

Exemplo 01:

Parâmetros

MV\_BASDENT "Informe o estado da sua filial do Protheus que esta fazendo a entrada"  
MV\_CMPALIQ = .F.

Sua Filial do Protheus que esta fazendo a entrada é de SP  
MV\_ESTADO = SP  
MV\_BASDENT = SP  
MV\_CMPALIQ = .F.

Exemplo:  
Valor de Mercadoria – R$ 1.000,00  
ICMS interestadual (Próprio)  ICMS – 1.000,00 \* 12 = 120,00  
DIFAL (ICMS Complementar) DIF – 1.073,17 \* 18 = 73,17

Memoria de calculo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9565393094679)

No Protheus será apresentado da seguinte maneira:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9350073673623)

A base do ICMS complementar fiscal na aba Livro Fiscal no campo Base.Destin

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9350128369047)

Exemplo 02:

Parâmetros

MV\_BASDENT "Informe o estado da sua filial do Protheus que esta fazendo a entrada"  
MV\_CMPALIQ = .T.

Sua Filial do Protheus que esta fazendo a entrada é de SP  
MV\_ESTADO = SP  
MV\_BASDENT = SP  
MV\_CMPALIQ = .T.

Exemplo:  
Valor de Mercadoria = R$ 1.000,00  
ICMS Próprio= 1.000,00 \* 12% = 120,00  
Base de cálculo de Difal = R$ 1.000,00 - ICMS Próprio / 0,82 (alíquota interna Destino) = 1.073,17  
Valor Difal = 1.073,17 \* 6%= 64,39

Memoria de calculo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20669075656983)

No Protheus será apresentado da seguinte maneira:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20669075676055)

A base do ICMS complementar fiscal na aba Livro Fiscal no campo Base.Destin

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20669075684119)

 Informações adicionais:

<https://tdn.totvs.com/pages/releaseview.action?pageId=699815598>

<https://tdn.totvs.com/pages/releaseview.action?pageId=223162116>
