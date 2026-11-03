---
article_id: 14196322451735
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: c8e0531b05b949653882beb7f458c5782abf43ce46c33028eb14429aaacfceef
fetched_at: '2026-06-28T22:42:03.591769+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Sped Fiscal
  - Como gerar os registros E500/E510/E520 no Sped Fiscal?
type: support-article
updated_at: '2023-04-27T19:56:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/14196322451735-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Sped-Fiscal-Como-gerar-os-registros-E500-E510-E520-no-Sped-Fiscal
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **02:00 min** **Dúvida**Como gerar os registros **E500/E510/E520** no **Sped Fiscal**?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**Os registros **E500- Período da apuração do IPI, E510 - Consolidação dos valores do IPI por CFOP e código de tributação do IPI e  E520 – Apuração do IPI** referem-se ao período de apuração do **IPI** atual e é gerado com base nos dados da **Apuração do IPI**, rotina **MATA952** do **Protheus**.

Para que seja considerada corretamente no **Sped Fiscal**, é preciso rodar a apuração antes da geração do arquivo e as perguntas na *wizard* de geração da apuração precisam estar conforme abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14195379511703)

Na*wizard* de geração do **Sped Fiscal**, a pergunta **Livro** e **Tipo de Atividade** devem estar conforme abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14195385284119)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14195386959383)

**Importante:**

Sempre verificar se Apuração e **Sped Fiscal** estão sendo gerados para a mesma filial.
