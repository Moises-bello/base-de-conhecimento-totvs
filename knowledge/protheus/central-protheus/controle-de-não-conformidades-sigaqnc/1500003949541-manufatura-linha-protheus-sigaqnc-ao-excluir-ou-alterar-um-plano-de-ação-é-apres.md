---
article_id: 1500003949541
category: Controle de Não Conformidades (SIGAQNC)
content_hash: 4ae256445729535b5f569e22f11c8866e129e194cb2a7179d46b89688c6b915d
fetched_at: '2026-06-28T22:42:27.901097+00:00'
product: protheus
section_id: 360005876654
source: central-protheus
title: 'Manufatura - Linha Protheus - SIGAQNC - Ao excluir ou alterar um plano de
  ação é apresentada a mensagem: Usuário não autorizado'
type: support-article
updated_at: '2021-08-18T21:01:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003949541-Manufatura-Linha-Protheus-SIGAQNC-Ao-excluir-ou-alterar-um-plano-de-a%C3%A7%C3%A3o-%C3%A9-apresentada-a-mensagem-Usu%C3%A1rio-n%C3%A3o-autorizado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:30 min**  
**Ocorrência**Ao tentar excluir ou alterar um plano de ação através da rotina **QNCA030 - Cadastro de Plano de Ação**, é apresentada a mensagem: **Usuário não autorizado a fazer Manutenção neste Plano de Ação, será apenas visualizada.**  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) – Controle de Não Conformidades (SIGAQNC) – Todas as versões  
  
**Causa**Essa mensagem ocorre nas seguintes situações:

* Quando o usuário que está tentando excluir ou alterar o plano de ação não é o usuário responsável pelo plano;
* Quando o plano de ação já está com data de encerramento realizado.

**Solução**Para solucionar essa ocorrência, realize os seguintes passos:

1. Verifique qual é o conteúdo do parâmetro **MV\_QNCAPLA - Define se somente o responsável pode alterar Plano de Ação poderá alterar o cadastro**. Se o parâmetro estiver com conteúdo igual à **1 - Sim**, será verificado se o usuário logado, que está tentando excluir o plano é o usuário responsável pelo plano no campo **QI3\_MAT - Mat Usr Resp** na rotina **QNCA030**. Porém, se o parâmetro estiver com conteúdo igual à **2 - Não**, será verificado o usuário responsável que retornar do **PE - Ponto de Entrada QNC030USU**;
2. Se o plano de ação não está com data de encerramento realizado no campo **QI3\_ENCREA - Dt. Encer. Rea** na rotina **QNCA030**.

**Saiba mais**  
Para mais informações referente a utilização do **PE QNC030USU**, consulte a documentação [QNC030USU](https://tdn.totvs.com/pages/releaseview.action?pageId=315883747).
