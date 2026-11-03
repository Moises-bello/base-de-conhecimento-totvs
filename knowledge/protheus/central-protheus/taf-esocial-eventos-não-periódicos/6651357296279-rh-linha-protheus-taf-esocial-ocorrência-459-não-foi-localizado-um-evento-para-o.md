---
article_id: 6651357296279
category: TAF - eSocial - Eventos Não Periódicos
content_hash: 13611d28633fdccfd82f26dcd88d880983f23e7dcd436794bc50da8662a8c911
fetched_at: '2026-06-28T22:45:18.133888+00:00'
product: protheus
section_id: 1500001548002
source: central-protheus
title: RH - Linha Protheus - TAF - eSocial - Ocorrência 459 - Não foi localizado um
  evento para o recibo de entrega informado ou o mesmo foi excluído/retificado
type: support-article
updated_at: '2024-12-27T17:48:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6651357296279-RH-Linha-Protheus-TAF-eSocial-Ocorr%C3%AAncia-459-N%C3%A3o-foi-localizado-um-evento-para-o-recibo-de-entrega-informado-ou-o-mesmo-foi-exclu%C3%ADdo-retificado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23700501164823) Tempo aproximado para leitura: **05:00:00 min** **Dúvida**Inconsistência do RET - 459 - Nao foi localizado um evento para o recibo de entrega informado ou o mesmo foi excluido/retificado. Acao Sugerida: Devera existir um Evento ja recebido, quot;Ativoquot; (nao excluido ou retificado), com numero de recibo de entrega igual ao informado no campo.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - eSocial - Todas as versões  
  
**Solução**1. Verifique se no eSocial existe um evento para o mesmo período e CPF que está sendo retificado;  
  
2. Caso não exista, provavelmente o evento foi excluído diretamente no site do governo.  
OBS: É de responsabilidade do cliente verificar se o evento foi excluído diretamente no site do eSocial pois o suporte não tem acesso ao ambiente do governo para realizar essa verificação.  
  
3. Caso o evento não esteja no eSocial, para correção pelo sistema deve ser excluído o evento no Protheus, para isso, gere um evento S-3000 (para o registro com número de recibo), pela rotina do evento, após gerar, realize ajuste de protocolo no evento S-3000 pela rotina >Atualizações >Eventos Esocial >Não periódicos >Exclusão de eventos (insira um número aleatório, somente para indicar ao sistema que o evento foi excluído).

Após, faça o ajuste de status da exclusão.

Verifique se o evento original foi excluído (ele estará com legenda vermelha) dentro da rotina do TAF.

Integre novamente o evento que deseja transmitir ao eSocial para que o mesmo entre como uma Inclusão e não como uma retificação.

Para maiores informações acesse:

[TAF - FUNCIONALIDADES - Como realizar ajuste de recibo do e-Social no TAF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019678672-TAF-FUNCIONALIDADES-Como-realizar-ajuste-de-recibo-do-e-Social-no-TAF)

[Automação Fiscal - NÃO PERIÓDICOS - Como ajustar status de exclusão no TAF - S-3000](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360055468253-Automa%C3%A7%C3%A3o-Fiscal-N%C3%83O-PERI%C3%93DICOS-Como-ajustar-status-de-exclus%C3%A3o-no-TAF-S-3000?source=search)  
  
4. Caso o evento que esta sendo enviado retificando esteja no Portal do eSocial, deve ser verificado se o numero de protocolo do evento que esta no governo é o mesmo que esta no TAF.
