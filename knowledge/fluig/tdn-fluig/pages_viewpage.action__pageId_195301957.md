---
content_hash: afaa4b9a259363d75669b9caeff2c9dccd24f47c19bcebaef2e16f619275ddbd
fetched_at: '2026-06-28T21:35:19.150312+00:00'
page_id: '195301957'
product: fluig
source: tdn-fluig
title: BPM 004 - Por que os campos de formulário não aparecem na criação de filtro
  na Central de Tarefas?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=195301957
version: 9
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:** fluig

**Versão:**Todas as versões

# Ocorrência

Na Central de tarefas, ao tentar adicionar o filtro 'Campos de Formulário' de um processo com formulário, não é apresentado nenhum campo para seleção.

# Solução

Na exportação do diagrama do processo para o fluig é preciso selecionar os campos descritores na aba Formulário das Propriedades do Diagrama no TDS. Estes campos serão considerados no momento da criação de um filtro.

Caso tenha desenvolvido o seu processo pela interface gráfica web do fluig, nas Propriedades do Processo, aba Formulário, selecione os campos a serem utilizados como filtro conforme exemplo abaixo. Salve as alterações e libere uma nova versão.
