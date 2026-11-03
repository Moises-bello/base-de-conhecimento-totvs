---
article_id: 21580903143959
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: 2d05c95ad9f8b0b57b679141e964d1f15dbd48df1ab7b1cd95904ab47aee77f2
fetched_at: '2026-06-28T22:42:09.190491+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - GNREWS - Erro
  de validação 244 -"Descrição: Receita não informada!"'
type: support-article
updated_at: '2024-02-26T16:49:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21580903143959-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-GNREWS-Erro-de-valida%C3%A7%C3%A3o-244-Descri%C3%A7%C3%A3o-Receita-n%C3%A3o-informada
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21580903121431) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**Ao transmitir a **GNRE WS** pela rotina **FISA095** acontece erro de validação:

**244 -"Descrição: Receita não informada!"**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21580903123607)  
**Ambiente**  
Cross Segmentos - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Causa**Conteúdo vazio ou incorreto no campo **F6\_CODREC** da guia de recolhimento .  
  
**Solução**Preencha no campo **F6\_CODREC** um código de receita valido para **UF,** segundo indica o manual de preenchimento no **Portal GNRE**:  
  
<https://www.gnre.pe.gov.br:444/gnre/portal/automacao.jsp>

Exemplo*:*

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21580929523991)
