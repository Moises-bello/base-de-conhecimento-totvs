---
article_id: 360021138172
category: Controle de Não Conformidades (SIGAQNC)
content_hash: 4931aadb8b9fb42c9861459f41fa4fc652e139db8bb98d2a7a8b969af6e4a544
fetched_at: '2026-06-28T22:42:27.907028+00:00'
product: protheus
section_id: 360005876654
source: central-protheus
title: 'Manufatura - Linha Protheus - SIGAQNC - Ao excluir uma FNC é apresentada a
  mensagem: Usuário não autorizado'
type: support-article
updated_at: '2023-06-02T13:58:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021138172-Manufatura-Linha-Protheus-SIGAQNC-Ao-excluir-uma-FNC-%C3%A9-apresentada-a-mensagem-Usu%C3%A1rio-n%C3%A3o-autorizado
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:01:23 min  
  
Ocorrência**Ao tentar excluir uma **FNC - Ficha de Não Conformidade** por meio da rotina **QNCA040 - Cadastro de Ocorrências/Não Conformidades**, é apresentada a mensagem: **Usuário não autorizado a fazer Manutenção nesta Ficha de Ocorrências/Não-conformidades. A Ficha de Ocorrências/Não-Conformidades será apenas visualizada.**  
  
**Ambiente**  
TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) – Controle de Não Conformidades (SIGAQNC) – Todas as versões  
  
**Causa**Esta situação ocorre devido a permissões do usuário ou situação não permitida para exclusão.  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
1. Verifique se o usuário que está tentando excluir a **FNC** é o usuário responsável pela **FNC**, no campo **QI2\_MATRES - Cod Usr Resp**;  
2. Verifique se a situação, no campo **QI2\_STATUS - Situação** da **FNC** está como **Registrada**. Este é o único status que permite a exclusão.  
  
**Saiba Mais**  
Caso deseje alterar a regra do Sistema para adicionar outros usuários que poderão excluir a **FNC**, pode ser utilizado o ponto de entrada **[QNCDELFNC - Ficha de Não-Conformidades](https://tdn.totvs.com/pages/releaseview.action?pageId=6801013)**.
