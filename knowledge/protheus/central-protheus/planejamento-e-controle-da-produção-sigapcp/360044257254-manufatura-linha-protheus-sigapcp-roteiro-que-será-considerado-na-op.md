---
article_id: 360044257254
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 1170449d37fd232e1ab72067661602fed9b6a8cd13af7cfb861ca7b2eb47096a
fetched_at: '2026-06-28T22:42:45.907003+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Roteiro que será considerado na OP
type: support-article
updated_at: '2021-07-15T14:27:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044257254-Manufatura-Linha-Protheus-SIGAPCP-Roteiro-que-ser%C3%A1-considerado-na-OP
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:00:57 min**  
**Dúvida**Qual **roteiro** o Sistema irá considerar para realizar o apontamento quando ele não for informado na **OP - Ordem de Produção**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**Ao realizar apontamento através do **MATA681 - Produção PCP Mod2** o Sistema irá verificar:

1. Se existe roteiro informado na **OP**, no campo **C2\_ROTEIRO - Roteiro**;
2. Se estiver **em branco**, será considerado o roteiro que estiver informado no campo **B1\_OPERPAD - Rt.OP Padrão** do **MATA010 - Cadastro de Produto**;
3. Se no produto também não tiver roteiro informado, o Sistema irá considerar por padrão o **roteiro 01**;
4. Se não existir o **roteiro 01**, é necessário informar na **OP** ou no **Produto** qual roteiro será utilizado.
