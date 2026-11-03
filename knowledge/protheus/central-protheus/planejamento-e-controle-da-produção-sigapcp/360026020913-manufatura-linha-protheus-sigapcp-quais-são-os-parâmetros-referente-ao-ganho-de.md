---
article_id: 360026020913
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: fd50ccf89fd178251b43c454a3f6c10c0163369e896244e59c97b11a88f6ba01
fetched_at: '2026-06-28T22:42:45.775540+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Quais são os parâmetros referente ao
  ganho de produção e produção a maior
type: support-article
updated_at: '2021-05-11T12:07:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026020913-Manufatura-Linha-Protheus-SIGAPCP-Quais-s%C3%A3o-os-par%C3%A2metros-referente-ao-ganho-de-produ%C3%A7%C3%A3o-e-produ%C3%A7%C3%A3o-a-maior
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura**: 00:01:00 min**  
 **Dúvida**Através de quais rotinas de apontamento podemos fazer uso da parametrização referente ao **ganho de produção** e **produção a maior**?  
  
 **Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**Ao apontar uma produção maior do que a prevista na abertura da **OP - Ordem de Produção** é possível identificá-la como **ganho de produção** ou **produção a maior**. Esse recurso está disponível nos apontamentos através dos programas **MATA250 - Produção Simples**, **MATA680 - Produção PCP Mod1** e **MATA681 - Produção PCP Mod2**.Os parâmetros envolvidos no processo são o **MV\_GANHOPR - Utilizado para verificar se permite o conceito de Ganho de Produção na inclusão do apontamento de produção** e o **MV\_PERCPRM - Percentual da quantidade das ordens de produção qual será permitido apontado a maior**, uma vez configurados conforme a necessidade do cliente será possível utilizar o recurso através das três rotinas indicadas.
