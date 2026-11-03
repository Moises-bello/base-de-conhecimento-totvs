---
article_id: 21581642198295
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: 04b732a690131c3a0c3727490c8cf2ba1464448278e72b3eeb6b28f4bc8a6e84
fetched_at: '2026-06-28T22:42:09.186994+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - GNREWS - Erro
  de validação 220 -"Descrição: Período de apuração não informado!"'
type: support-article
updated_at: '2024-02-26T10:46:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21581642198295-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-GNREWS-Erro-de-valida%C3%A7%C3%A3o-220-Descri%C3%A7%C3%A3o-Per%C3%ADodo-de-apura%C3%A7%C3%A3o-n%C3%A3o-informado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21581636868375) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**Ao transmitir a **GNRE WS** pela rotina **FISA095**, ocorre o erro de validação:

**220 -"Descrição: Período de apuração não informado!**

*Print* erro

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21581636868631)  
**Ambiente**  
Cross Segmentos - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Causa**Conteúdo vazio ou incorreto no campo **F6\_REF** da guia de recolhimento (**Tabela SF6**).  
  
**Solução**É preciso preencher no campo **F6\_REF** um código de referência para o guia de recolhimento **MATA960** com uma das opções abaixo:

*Print*:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21581642182551)
