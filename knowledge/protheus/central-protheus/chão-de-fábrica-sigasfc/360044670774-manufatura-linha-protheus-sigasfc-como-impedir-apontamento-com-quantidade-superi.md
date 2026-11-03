---
article_id: 360044670774
category: Chão de Fábrica (SIGASFC)
content_hash: 6aca9b117029f357f92b0d639854282e17162609142d06e2421b5f2016740bfe
fetched_at: '2026-06-28T22:42:49.803441+00:00'
product: protheus
section_id: 360005696234
source: central-protheus
title: Manufatura - Linha Protheus - SIGASFC - Como impedir apontamento com quantidade
  superior a que foi apontada em operação anterior
type: support-article
updated_at: '2022-04-01T14:06:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044670774-Manufatura-Linha-Protheus-SIGASFC-Como-impedir-apontamento-com-quantidade-superior-a-que-foi-apontada-em-opera%C3%A7%C3%A3o-anterior
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:00:30 min**  
**Dúvida**Como impedir apontamento com quantidade superior a que foi apontada em operação anterior?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Chão de Fábrica (SIGASFC) - Versão 12   
  
**Solução**Para essa validação o **SIGASFC - Chão de Fábrica** faz uso do mesmo parâmetro do **SIGAPCP - Planejamento e Controle da Produção**.  
Verifique no **F12** do **MATA681 - Apontamento de Produção Mod2**, do **SIGAPCP** o conteúdo do parâmetro **Verifica Saldo Operação Anterior?** altere o conteúdo desse parâmetro para **Produção + Perda** ou **Produção - Perda**, conforme a sua necessidade.
