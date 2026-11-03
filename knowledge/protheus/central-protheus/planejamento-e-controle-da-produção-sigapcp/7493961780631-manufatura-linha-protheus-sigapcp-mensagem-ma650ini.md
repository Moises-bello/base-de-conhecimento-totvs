---
article_id: 7493961780631
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 004be7bc97c7d70643fc1b78074dbde5845f8145b5c23fc23fafb46187ad05a1
fetched_at: '2026-06-28T22:42:44.505799+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Mensagem MA650INI
type: support-article
updated_at: '2025-04-28T19:30:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7493961780631-Manufatura-Linha-Protheus-SIGAPCP-Mensagem-MA650INI
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23086330692503) Tempo aproximado para leitura: **00:00:51 min****Ocorrência**Ao tentar excluir uma ordem de produção é apresentada a mensagem **MA650INI**.  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12   
  
**Causa**Esta situação ocorre pois a **OP - Ordem de Produção** possui apontamentos de produção ou movimentos de requisição.  
  
**Solução**Para que seja possível excluir a **OP** será necessário realizar o estorno dos apontamento de produção, caso tenham sido realizados ou verificar se existe alguma requisição e excluí-la/estorná-la.  
  
Consulte as rotinas **MATA250 - Produção simples , MATA681 - Modelo 2  e MATA685 - Apontamento de perda** analisando se existe algum registro para a ordem.  
  
**Saiba mais**  
Para mais informações de como estornar uma **OP** acesse a documentação: [Manufatura - Linha Protheus - SIGAPCP - Reabrir uma OP que já foi encerrada](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500002187821-Manufatura-Linha-Protheus-SIGAPCP-Reabrir-uma-OP-que-j%C3%A1-foi-encerrada)
