---
article_id: 35831414262423
category: Escrita Fiscal - Configurador de Tributos
content_hash: 693141b06a9819392a5afcaa103d6723e18e6ceafe06a882206ad2eb520574f1
fetched_at: '2026-06-28T22:39:17.234162+00:00'
product: protheus
section_id: 26791332087191
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - Como configurar
  o cBenef de redução de base no Fisa170?
type: support-article
updated_at: '2026-06-12T19:28:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35831414262423-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-FIS-Como-configurar-o-cBenef-de-redu%C3%A7%C3%A3o-de-base-no-Fisa170
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35831414233751) Tempo aproximado para leitura: 00:05**min**  
  
**Dúvida**  
Como configurar o cBenef de redução de base no Fisa170?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**

Segue abaixo um exemplo de configuração e pode ser usado para qualquer estado.

Configuração da redução de base

[Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - Como configurar a redução de base do ICMS no fisa170?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/35829525876503-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-FIS-Como-configurar-a-redu%C3%A7%C3%A3o-de-base-do-ICMS-no-fisa170)

MV\_estado = SC

Código do cBenef = SC820003

O código pode ser inserido de forma manual ou importado através do U\_IMPSPED

[CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Como importa a TABELA52 no Protheus para tratamento da tag cBenef](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047771974-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-importa-a-TABELA52-no-Protheus-para-tratamento-da-tag-cBenef)

Na rotina Fisa156 - verificar

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35831398005015)

Não pode ter data fim - não aplica o cBenef

Configurador

Cadastro da mensagem

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35831414236951)

Regra Ajuste de Lançamento - tabela52

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35831398005911)![](https://centraldeatendimento.totvs.com/hc/article_attachments/35831414242071)![](https://centraldeatendimento.totvs.com/hc/article_attachments/35831398007319)

Visualização da tabela no pedido de Vendas

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35831414246167)![](https://centraldeatendimento.totvs.com/hc/article_attachments/35831398008983)

Os dados são gravados na CDV

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35831414247831)
