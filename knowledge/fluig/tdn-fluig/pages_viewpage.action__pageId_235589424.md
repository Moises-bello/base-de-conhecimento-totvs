---
content_hash: 28c1dcf79c089caf0eaddb428f0dad746502af888f1bb6922eec06e049d52729
fetched_at: '2026-06-28T21:35:22.336793+00:00'
page_id: '235589424'
product: fluig
source: tdn-fluig
title: BPM 033 - É possível editar o subprocesso do Listar Tarefas (Ad Hoc)?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=235589424
version: 10
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:**fluig

**Versão:**Todas as versões

# Ocorrência

Não é possível alterar o subprocesso do Listar Tarefas (Ad Hoc), nem importá-lo através do Studio.

Isso ocorre apenas com o subprocesso, o formulário e o processo "pai" podem ser editados normalmente.

# Causa

O subprocesso do Listar Tarefas (Ad Hoc) foi bloqueado para edições.

# Solução

Em situações onde o subprocesso Listar Tarefas não atende as necessidades, por ser um processo simples, com apenas a atividade inicial, atividade comum e atividade final, pode ser desenvolvido um novo subprocesso.

Este subprocesso pode ser iniciado a partir da chamada de um *Web Service* ou API, e sempre que finalizada uma solicitação do subprocesso, este irá alterar o seu 'Status' na solicitação pai, informando a conclusão. O processo pai precisará ter uma validação onde somente após a conclusão de todos os subprocessos, permita continuar o fluxo da solicitação pai.
