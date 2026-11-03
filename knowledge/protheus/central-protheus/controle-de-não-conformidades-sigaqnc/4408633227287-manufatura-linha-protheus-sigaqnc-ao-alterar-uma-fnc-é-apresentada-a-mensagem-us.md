---
article_id: 4408633227287
category: Controle de Não Conformidades (SIGAQNC)
content_hash: fff77c52b993f46d707c9268aaadc15b5cf75a6031e82dff7f15f34c80487528
fetched_at: '2026-06-28T22:42:27.894017+00:00'
product: protheus
section_id: 360005876654
source: central-protheus
title: 'Manufatura - Linha Protheus - SIGAQNC - Ao alterar uma FNC é apresentada a
  mensagem: Usuário não autorizado a fazer Manutenção nesta Ficha de Ocorrências/Não-Conformidades'
type: support-article
updated_at: '2026-06-17T12:26:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4408633227287-Manufatura-Linha-Protheus-SIGAQNC-Ao-alterar-uma-FNC-%C3%A9-apresentada-a-mensagem-Usu%C3%A1rio-n%C3%A3o-autorizado-a-fazer-Manuten%C3%A7%C3%A3o-nesta-Ficha-de-Ocorr%C3%AAncias-N%C3%A3o-Conformidades
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17382102284823) Tempo aproximado para leitura: **00:02:15 min**  
  
**Ocorrência**  
Ao alterar uma **FNC - Ficha de Não Conformidade** por meio da rotina **QNCA040 - Cadastro de Ocorrências/Não Conformidades**, é apresentada a mensagem: **Usuário não autorizado a fazer Manutenção nesta Ficha de Ocorrências/Não conformidades.**  
  
**Ambiente**  
TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) – Controle de Não Conformidades (SIGAQNC) – Versão 12  
  
**Causa**  
Esta mensagem é exibida quando o usuário que está alterando a **FNC** não é o usuário responsável pela **FNC** ou quando o parâmetro **MV\_QALTFNC - Define se todos usuários poderão efetuar manutenção no cadastro de FNC** está com conteúdo igual à **2 - Não**.  
  
**Solução**  
Para que seja possível alterar a **FNC**, verifique o conteúdo do parâmetro **MV\_QALTFNC**:  
1. Se o parâmetro estiver como **2 - Não**:

* E a situação da **FNC** for igual à **1 - Registrada**, o usuário logado deve ser igual ao usuário que incluiu a **FNC**. Esta informação consta no campo **QI2\_MAT - Cod Usr Dig**;
* E a situação da **FNC** for diferente de **1 - Registrada**, o usuário logado deve ser igual ao usuário que incluiu a **FNC** no campo **QI2\_MAT** e também ao usuário responsável pela FNC  no campo **QI2\_MATRES - Cod Usr Resp**.

2. Se o parâmetro estiver como **1 - Sim**:

* Qualquer usuário poderá alterar a **FNC**, ou seja, se o usuário logado for diferente dos usuários que estiverem nos campos **QI2\_MAT** e **QI2\_MATRES**, desde que a **FNC** não esteja encerrada, ou seja, que o campo **QI2\_CONREA - Dt. Con. Real** esteja em branco.

**Saiba Mais**  
Caso deseje alterar a regra do Sistema para adicionar outros usuários que poderão alterar a **FNC**, pode ser utilizado o ponto de entrada [QN040AUT - Autoriza usuários a alterar a FNC](http://tdn.totvs.com/pages/viewpage.action?pageId=62390525)
