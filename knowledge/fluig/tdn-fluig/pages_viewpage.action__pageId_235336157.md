---
content_hash: 481a36f7dc9950dcabb3dd987f8302d9d6207803368a5bc46c70c63ad91c70ef
fetched_at: '2026-06-28T21:35:22.257176+00:00'
page_id: '235336157'
product: fluig
source: tdn-fluig
title: BPM 030 - Porque é exibida uma mensagem de erro ao editar um processo ou formulário
  no fluig?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=235336157
version: 6
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:**fluig

**Versão:**Todas as versões

# Ocorrência

Mensagem de erro ao editar um processo ou formulário no fluig.

# Solução

Essa mensagem é padrão do produto. Processos e formulários criados e exportados através do fluig Studio/Eclipse e utilizam BPMN Estendido (BPMN 2.0) por padrão, por isso não podem ser editados no modelador web do fluig.

Isso acontece porque o BPMN 2.0 possui recursos de desenvolvimento de processos, datasets e formulários mais avançados que não estão disponíveis na web e seriam perdidos caso a edição fosse permitida.

**Figura 1 - Mensagem de erro.**
