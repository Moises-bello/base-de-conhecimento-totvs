---
article_id: 1500011922982
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 9fbc298bd9bcc593ce99d6800618d41531878ef72e2dd738a5153e7ce52d4f05
fetched_at: '2026-06-28T22:42:43.569650+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Mensagem A093DEL
type: support-article
updated_at: '2025-08-13T12:45:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500011922982-Manufatura-Linha-Protheus-SIGAPCP-Mensagem-A093DEL
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34148945349271)***Tempo aproximado para leitura: **00:01:25 min**  
**Ocorrência**Ao tentar excluir uma família de produtos ou característica através do **MATA093 - Cadastro de Famílias**, ou tentar excluir um conjunto ou opção do conjunto através do **MATA099 - Configurador de produtos** surge a mensagem **A093DEL**.  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Causa**Essa mensagem surge no **MATA093** ao tentar excluir uma família e há opções já vinculadas às características relacionadas a esta família no **MATA098 - Codificação**, ou quando existem produtos já cadastrados e vinculados à esta família no **MATA010 - Cadastro de produtos**.   
Também surge ao editar uma família e tentar excluir uma característica que já possui opções vinculadas no **MATA098** ou produto cadastro e vinculado à esta família e característica no **MATA010**.  
Já no **MATA099** essa mensagem surge quando o conjunto que se deseja excluir está relacionado a uma característica no **MATA099** ou quando a opção que se deseja excluir já está relacionada a algum produto no **MATA010**.  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
1. Acesse o **MATA010** e verifique se há produtos vinculados à família, característica, conjunto ou opção que se deseja excluir;  
2. Acesse o **MATA098** e verifique se há opções vinculadas a característica ou conjunto que se deseja excluir.
