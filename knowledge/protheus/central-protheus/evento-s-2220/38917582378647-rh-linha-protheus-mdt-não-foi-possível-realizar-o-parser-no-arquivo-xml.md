---
article_id: 38917582378647
category: Evento S-2220
content_hash: b5cee995c1496c7d4ec291edd8d8b56264ca83a09ce00e7be13b03e1d11da63a
fetched_at: '2026-06-28T22:45:25.553545+00:00'
product: protheus
section_id: 8260535758103
source: central-protheus
title: RH - Linha Protheus - MDT - Não foi possível realizar o Parser no arquivo XML
type: support-article
updated_at: '2026-03-09T20:50:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38917582378647-RH-Linha-Protheus-MDT-N%C3%A3o-foi-poss%C3%ADvel-realizar-o-Parser-no-arquivo-XML
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38917599151383) Tempo aproximado para leitura: **HH:MM:SS min**  
  
**Ocorrência**  
Ao integrar os eventos S-2210, S-2220, S-2221 ou S-2240 do módulo SIGAMDT ao SIGATAF, o sistema apresenta o erro: Não foi possível realizar o Parser no arquivo XML

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38917597530135)

**Ambiente**  
TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as versões  
  
  
**Solução**  
Verifique nas rotinas que compõem o evento a ser integrado se há alguma palavra com caracteres especiais, como ponto e vírgula (;) ou aspas, bem como acentuações.

Caso haja acentuações ou caracteres especiais, remova-os e realize a integração do evento novamente.

**Saiba Mais**  
[Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)
