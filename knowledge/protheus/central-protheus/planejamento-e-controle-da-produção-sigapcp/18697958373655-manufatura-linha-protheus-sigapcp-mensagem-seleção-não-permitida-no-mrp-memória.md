---
article_id: 18697958373655
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 03ce9ee902d1e8194c13cddc6748ec8ebc8fcdd0b312c39920f96bdd5423d3d2
fetched_at: '2026-06-28T22:42:44.546232+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Mensagem Seleção Não Permitida no MRP
  Memória
type: support-article
updated_at: '2023-10-31T17:54:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18697958373655-Manufatura-Linha-Protheus-SIGAPCP-Mensagem-Sele%C3%A7%C3%A3o-N%C3%A3o-Permitida-no-MRP-Mem%C3%B3ria
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18697912789527) Tempo aproximado para leitura: **00:01:12 min****Ocorrência**Ao tentar fazer uma seleção de **produto**, **grupo de material**, **tipo de material**, **documento**, **armazém** ou **demanda** na rotina **PCPA712 - MRP Memória**,  é apresenta a mensagem **Seleção Não Permitida**.  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Causa**Essa mensagem é apresentada quando foram selecionados todos os registros de **produto**, **grupo de material**, **tipo de material**, **documento**, **armazém** ou **demanda**.  
  
**Solução**A seleção deve ser usada quando um ou mais registros não é selecionado, se quiser que o MRP processe todos os dados, não faça a seleção daquele conjunto de informações, deixando o campo em branco.

**Exemplo**Se quiser que o **MRP** processe todos os os produtos, não há a necessidade de selecionar todos os produtos, para isso deixe o campo **Produto** em branco. O mesmo processo deve ser adotado a grupo de material, tipo de material, documento, armazém ou demanda
