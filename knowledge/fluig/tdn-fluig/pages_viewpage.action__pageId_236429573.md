---
content_hash: c6314e23ac2c9136fc1adcc5073e2687496f99a63e511b2abe468f137de31aa3
fetched_at: '2026-06-28T21:35:22.468594+00:00'
page_id: '236429573'
product: fluig
source: tdn-fluig
title: BPM 034 - O usuário que não é responsável pela tarefa consegue movimentá-la?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=236429573
version: 7
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:** fluig

**Versão:**Todas as versões

# Ocorrência

Usuário que não é responsável pela tarefa está conseguindo acessar a solicitação e movimentá-la.

# Causa

Quando definido um usuário Gestor do processo, este usuário terá permissão de movimentar todas as solicitações do processo, em qualquer atividade, inclusive terá permissão de cancelamento da solicitação. Isto não é uma falha de segurança e sim uma regra de negócio do fluig.

O usuário Gestor, poderá visualizar todas as solicitações do processo do qual é gestor pela aba 'Minhas tarefas sob gerência' da Central de tarefas. O cadastro de um usuário Gestor é útil para as situações onde algum usuário é impossibilitado de movimentar uma atividade, e para processos onde algum usuário sempre será responsável e precisará estar ciente de todas as movimentações.

# Solução

Para que não seja possível que outro usuário, além do usuário responsável pela atividade, possa movimentar uma solicitação, remova o usuário Gestor do processo.

Faça isto através do menu 'Configurar Processos': edite o processo em questão e na opção 'Propriedades', aba 'Geral', campo 'Gestor', remova o mecanismo deixando 'Selecione um Mecanismo' e salve.
