---
content_hash: e8244528b47de01d7d767096103388ccb221a5541bf8cd0adf08783f3070e653
fetched_at: '2026-06-28T21:35:24.000414+00:00'
page_id: '268571267'
product: fluig
source: tdn-fluig
title: BPM 078 - Como configurar frequência de solicitação?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=268571267
version: 4
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:**fluig

**Versão:** 1.5.11 Ep3

**Ambiente:**

**Banco de Dados:**

**Tipo de API:** Webservice

# Ocorrência

Como configurar uma frequência de cobrança para realização de uma atividade no workflow.   
em que o usuário responsável receba a notificação de tempo em tempo.

# Solução

Na atividade em que deseja notificar o responsável, configure o prazo de conclusão na aba Geral.

Na aba Atraso, Configure a notificação de responsável adicionando os valores para os prazos de Tolerância, Frequência e  Aviso de expiração.

Após o processo configurado, é necessário configurar o agendador de tarefas, para o tipo Expiração de Tarefas.

Feito essa configuração o responsável será notificado até o momento em que a atividade não estiver atrasada.

# Observações

para atividades atrasadas é necessário criar o agendador do tipo Tarefas atrasadas.
