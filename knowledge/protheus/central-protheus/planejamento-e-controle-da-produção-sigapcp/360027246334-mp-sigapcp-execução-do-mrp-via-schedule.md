---
article_id: 360027246334
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 45f66fc81376ac35107e23ef8a6e747fe1236702e5cb17c9b275e0487cbd0527
fetched_at: '2026-06-28T22:42:47.206920+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: MP - SIGAPCP - Execução do MRP via Schedule
type: support-article
updated_at: '2020-08-28T18:16:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027246334-MP-SIGAPCP-Execu%C3%A7%C3%A3o-do-MRP-via-Schedule
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:01:45 min**  
 **Dúvida**Como executar o **MRP - Material Requirement Planning**através do **Schedule**?  
   
 **Ambiente**Microsiga Protheus – Planejamento e Controle da Produção – Versão 12  
  
**Solução**Para executar o **MRP** através do **Schedule** será necessário desenvolver uma função customizada que executa o **MRP**, passando todos os parâmetros e configurar a execução dessa função customizada no **Schedule.**A função customizada deve realizar chamada do **MATA712 - MRP** conforme exemplo abaixo:

```
MATA712( .T., {npar01, npar02, lpar03, apar04, apar05, lpar06, lpar07, npar08})
```

Onde:  
**npar01** - conteúdo numérico, indicando a periodicidade do **MRP**, sendo **1** para diário, **2** para semanal e assim sucessivamente;  
**npar02** - conteúdo numérico, indicando a quantidade de períodos;  
**lpar03** - conteúdo lógico, indicando se deve considerar pedidos em carteira, sendo **.T.** para considerar e **.F.** para não considerar;  
**apar04** - *array* contendo todos os tipos de produtos existentes e indicando para quais tipos as necessidades são calculadas. Exemplo: { {.T.,'Al'},{.F.,'BN'},...}, neste exemplo é calculada a necessidade para os itens do tipo **Al** e não é calculada para os itens do tipo **BN**;  
**apar05** - *array* contendo todos os grupos de produtos existentes e indicando para quais grupos as necessidades são calculadas. Exemplo: { {{.T.,' '}, {.T.,'0001'},{.F.,'0002'},...}, neste exemplo é calculada a necessidade para os produtos com o grupo em **branco** ou **0001** e não é calculada para o grupo de produto **0002**;  
**lpar06** - conteúdo **lógico**, indicando se considera o número passado no oitavo parâmetro como numero inicial para a geração das **OPs - Ordens de Produção**; **lpar07** - conteúdo lógico indicando se deve ativar o **log** do **MRP**; **cpar08** - conteúdo do tipo *string* indicando o número da primeira **OP** a ser gerada pelo **MRP**.
