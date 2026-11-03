---
article_id: 11918677012375
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: e8f732796bbd451cc66bae78422760a6903c6f77cdad3ab26e34e05190a7cbab
fetched_at: '2026-06-28T22:42:02.370863+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - Sped Fiscal
  - Por que o registro C170 não é gerado para nota de saída ou com formulário próprio?
type: support-article
updated_at: '2023-01-25T12:56:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11918677012375-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Sped-Fiscal-Por-que-o-registro-C170-n%C3%A3o-%C3%A9-gerado-para-nota-de-sa%C3%ADda-ou-com-formul%C3%A1rio-pr%C3%B3prio
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura:**00:02:00 min** **Dúvida**Por que o registro **C170 - Itens do Documento Fiscal** não é gerado para nota de saída ou com formulário próprio?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**Para as notas de emissão própria, o **Protheus** não gera o  registro **C170**, se respaldando no trecho abaixo retirado do guia prático do **Sped Fiscal**.

![](https://totvssuporte.zendesk.com/attachments/token/JnvuqxB5wSCFLLcOYeDaAhqeW/?name=inline1104469486.png)

Dessa forma, para notas em questão  somente é gerado o registro **C170** quando acompanhar os registros **C176, C177**(**Ressarcimento de ICMS-ST**), portanto para notas sem ressarcimento não é gerado o registro **C170**.  
  
Para nos certificarmos de que estávamos interpretando corretamente a observação, realizamos um teste incluindo o registro **C170** em uma nota fiscal de emissão própria (tanto de entrada, quanto de saída) e o validador **do Sped Fiscal** apresentou a seguinte mensagem: **"Não é possível gerar registro analítico de Nota Fiscal Eletrônica de emissão própria."**  
  
Sendo assim, concluímos que de fato não é possível gerar o registro **C170** para notas fiscais de emissão própria sejam entradas ou saídas.  
  
![](https://totvssuporte.zendesk.com/attachments/token/smMjRyPlQM7fA014XH1ZQMNE5/?name=inline2017575632.png)  
  
![](https://totvssuporte.zendesk.com/attachments/token/DDpseYXORPIWRlaRo6mPYRLwH/?name=inline-384245778.png)
