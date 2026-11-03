---
article_id: 11955550948119
category: Chão de Fábrica (SIGASFC)
content_hash: 7cf7578fe139b64d26970e6a7c0b37ce3a36aa8acca2fa274d11079771d69547
fetched_at: '2026-06-28T22:42:49.851977+00:00'
product: protheus
section_id: 360005696234
source: central-protheus
title: 'Manufatura - Linha Protheus - SIGASFC - HELP: Período informado para produção
  é inválido. Data inicial do apontamento deve ser dia útil'
type: support-article
updated_at: '2023-02-24T13:13:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11955550948119-Manufatura-Linha-Protheus-SIGASFC-HELP-Per%C3%ADodo-informado-para-produ%C3%A7%C3%A3o-%C3%A9-inv%C3%A1lido-Data-inicial-do-apontamento-deve-ser-dia-%C3%BAtil
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:04 min****Ocorrência**Ao tentar incluir um apontamento de produção através das rotinas **SFCA316 - Apontamento de Produção Modelo 2** é apresentada a mensagem **SFCA314 Período informado para Produção é Inválido. Data inicial de apontamento deve ser dia útil.**

**![Imagem1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11955467392151)**

**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Chão de Fábrica (SIGASFC) - Versão 12  
  
**Causa**A data inicial do apontamento não é dia útil, de acordo com o calendário do centro de trabalho, da área de produção ou do parâmetro **MV\_SFCCDCL - Calendário Genérico SFC**   
  
**Solução**Para solucionar essa dúvida, realize os seguintes passos:  
1. Acesse a rotina **SFCA002 - Máquinas**, e consulte a máquina que está apontando, veja o centro de trabalho informado no campo **CYB\_CDCETR - Centro de Trabalho**;  
2. Acesse a rotina **SFCA001 - Centro de Trabalho**, consulte o centro de trabalho identificado no passo anterior e veja se há calendário especificado para ele no campo **CYL\_CDCL - Calendário**;  
3. Se possuir calendário, acesse a rotina **SFCA013 - Calendário Genérico**, consulte esse calendário, e veja se a data indicada na mensagem e que está tentando apontar é dia útil;  
4. Se não possuir calendário, veja se o centro de trabalho possui área de produção indicada no campo **CYI\_CDARPO - Área de Produção**;  
5. Se tiver área de produção indicada, acesse a rotina **SFCA007 - Área de produção**, consulte essa área de produção e veja se há calendário especificado no campo **CYA\_CDCL - Calendário**;  
6. Se existir calendário especificado, acesse a rotina **SFCA013**, consulte esse calendário e veja se a data indicada na mensagem e que está apontando é dia útil;  
7. Se o centro de trabalho e a área de produção não tiverem calendário especificado, consulte o calendário do parâmetro **MV\_SFCCDCL**;  
8. Acesse a rotina **SFCA013**, veja se esse calendário existe e se é dia útil.
