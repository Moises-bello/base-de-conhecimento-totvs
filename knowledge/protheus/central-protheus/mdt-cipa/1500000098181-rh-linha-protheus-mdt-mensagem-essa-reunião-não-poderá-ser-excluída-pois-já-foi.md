---
article_id: 1500000098181
category: MDT - CIPA
content_hash: f130eaee5fb19da8d5b80694e1072814ccc846bb0bef7acfee44706f37e4a56e
fetched_at: '2026-06-28T22:44:23.309459+00:00'
product: protheus
section_id: 360012070553
source: central-protheus
title: RH - Linha Protheus - MDT - Mensagem "Essa reunião não poderá ser excluída,
  pois já foi realizada". Ao tentar excluir uma Agenda CIPA (MDTA665) no SIGAMDT
type: support-article
updated_at: '2025-10-03T19:05:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500000098181-RH-Linha-Protheus-MDT-Mensagem-Essa-reuni%C3%A3o-n%C3%A3o-poder%C3%A1-ser-exclu%C3%ADda-pois-j%C3%A1-foi-realizada-Ao-tentar-excluir-uma-Agenda-CIPA-MDTA665-no-SIGAMDT
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25674180174999)**Tempo aproximado para leitura: **00:02:00 min****Ocorrência**Mensagem "Essa reunião não poderá ser excluída, pois já foi realizada". Ao tentar excluir uma **Agenda CIPA** (MDTA665) no modulo Medicina e Segurança do Trabalho.  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as versões  
  
**Causa**Essa mensagem ocorre devido ao usuário tentar excluir uma **Agenda CIPA** em data posterior a data definida na agenda. Nesse caso o sistema entende que a reunião já ocorreu e não permite a exclusão.  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500000099622)  
  
**Solução**Caso a data informada na agenda esteja incorreta sendo necessário excluir, ou a agenda foi cadastrada por engano, é possível fazer a exclusão da agenda seguindo os seguintes passos:  
  
1. Acesse no modulo SIGAMDT o caminho: Atualizações - CIPA - Agenda Reuniões (MDTA665);  
2. Entre como alterar na agenda que será excluída, e apague o o conteúdo do campo **Data Real** (TNR\_DTREAL) e **Hora Real** (TNR\_HRREAL), e depois confirme;  
3. Clique em Outras - Ações - Excluir e Confirme.  
  
Exemplo:  
  
![Excluir_agenda_cipa.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/1500000096541)  
  
**Saiba Mais**  
[Artigos CIPA](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360012070553-MDT-CIPA)  
[Documentação Técnica Laudos (MDTA210)](https://tdn.totvs.com/x/6NybFg)  
[Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6961760300311-EC-Assistente-Carolina-Segmentos-Funcionalidades-da-Carolina)
