---
article_id: 33675439757335
category: Escrita Fiscal - Configurador de Tributos
content_hash: 7e4394c11d093e04bec5683ffb54e3075f917428002c05a20a4160adb02f4bf2
fetched_at: '2026-06-28T22:39:18.426792+00:00'
product: protheus
section_id: 26791332087191
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS – FISA170 – Como calcular
  o ISS utilizando o Configurador de Tributos para notas de entrada e saída?
type: support-article
updated_at: '2025-11-14T22:21:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/33675439757335-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-FISA170-Como-calcular-o-ISS-utilizando-o-Configurador-de-Tributos-para-notas-de-entrada-e-sa%C3%ADda
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33675423018647) Tempo aproximado para leitura: **00:10:00 min**  
  
**Dúvida**  
Como calcular ISS para pessoa jurídica utilizando o Configurador de Tributos (FISA170) para notas de entrada ou saída?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - a partir da versão 12.1.2310.  
  
**Solução**  
Segue abaixo os cadastros que devem ser criados no Configurador de Tributos para a geração do cálculo do ISS.

Segue exemplo de cadastros:

**1)** FISA170 - **Regras Fiscais** > Perfis > **Perfil do Produto**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33675423018775)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33675423019287)

**2)** FISA170 - **Regras Fiscais** > Perfis > **Perfil de Operação**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33675439745047)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33675439745431)

Obs.: Com relação ao Código de Serviço utilizado para esta operação, o mesmo deverá constar não só no Produto (campo B1\_CODISS), mas também na aba Código de Serviço do Perfil Tributário de Operação juntamente com o CFOP que será utilizado na nota.

**3)** FISA170 - **Regras Fiscais** > Perfis > **Perfil de Participante**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33675423019799)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33675423019927)

**4)** FISA170 - **Regras Fiscais** > Regras de Cálculo Documento Fiscal > **Regra de Base de Cálculo**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33675423020055)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33675439745943)

**5)** FISA170 - **Regras Fiscais** > Regras de Cálculo Documento Fiscal >**Regra de Alíquota**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33675439746199)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33675423020311)

**6)** FISA170 - **Regras Fiscais** > Regras de Cálculo Documento Fiscal > **Regra de Escrituração**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33675423020567)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33675423020823)

**7)** FISA170 - **Regras Fiscais** > Regras de Cálculo - Documentos Fiscais> **Regra de Cálculo - Documentos Fiscais**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33675439749271)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33675439749783)![](https://centraldeatendimento.totvs.com/hc/article_attachments/33675423021719)![](https://centraldeatendimento.totvs.com/hc/article_attachments/33675439751063)

**7)** Inclusão da Nota pelo Faturamento – Pedido de Venda no valor de R$ 1.000,00 com imposto de ISS no valor de R$ 50,00.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33675423023127)

8) Inclusão da Nota pelo Compras - Documento de Entrada no valor de R$ 1.000,00 com imposto de ISS no valor de R$ 50,00.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33675439751959)

**OBS:** para geração dos títulos do ISS no Contas a Pagar ou Contas a Receber, deve ser vinculado uma Regra Financeira na **Regra de Cálculo - Documentos Fiscais.**

[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FISA170 - Como gerar o imposto ISS com a regra financeira?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/32635165245847-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FISA170-Como-gerar-o-imposto-ISS-com-a-regra-financeira)

[CFGTRIB - Configurador de Tributos](https://tdn.totvs.com/display/public/PROT/CFGTRIB+-+Configurador+de+Tributos+-+12.1.22.10)

[Configurador de Tributos - Regras Financeiras](https://tdn.totvs.com/display/public/PROT/Configurador+de+Tributos+-+Regras+Financeiras#01-01)

[CFGTRIB - Código de Serviço ISS por Perfil de Operação](https://tdn.totvs.com/pages/releaseview.action?pageId=883676152)

[CFGTRIB - Cálculos no Configurador de Tributos](https://tdn.totvs.com/pages/viewpage.action?pageId=676039354)
