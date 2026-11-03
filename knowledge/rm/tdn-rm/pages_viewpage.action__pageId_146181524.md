---
content_hash: edfce35274c6603bd86be9136abf693ae7fa4541031ea06c2fcb06f27173e380
fetched_at: '2026-06-29T00:05:55.766132+00:00'
page_id: '146181524'
product: rm
source: tdn-rm
title: Cópia de Permissões de Usuário
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=146181524
version: 11
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**

## **01. VISÃO GERAL**

  O RM possui uma funcionalidade de criar um novo perfil baseado em outro perfil já existente, ou mesmo copiar as permissões de um perfil para um ou mais perfis existentes.

        As operações possíveis da Cópia de Permissões de Usuário são:

* Copiar apenas as permissões do usuário corrente.
* Remover todas as permissões existentes antes de copiar.

## **02. EXEMPLO DE UTILIZAÇÃO**

**PRIMEIRO PASSO:**

Após realizado login na nova MDI, selecione o módulo: Serviços Globais

**SEGUNDO PASSO:**

Em seguida acesse o menu "Segurança | Usuários". Após ser carregada a visão:

* Selecione o sistema "Serviços Globais"
* Selecione o usuário que receberá o novo perfil
* Acesse "Processos | Cópia de Permissões de Usuários"

**TERCEIRO PASSO:**

Processo da Cópia de Permissões:

* Preencher o campo "Usuário de Origem" com o usuário do qual será copiado as permissões do perfil:

* Se a opção "Copiar apenas as permissões do sistema corrente" for marcada, as permissões serão copiadas apenas para o sistema selecionado (neste exemplo, sistema globais). Caso queira copiar de todos os outros, deixá-la desmarcada:

* Se a opção "Remover todas as permissões existentes antes de copiar" não for marcada, os perfis do usuário de origem e destino serão somados. Por exemplo, Se o usuário possui um perfil na aplicação e recebe outro na cópia, ao final do processo ele ficará com dois perfis associados

**Importante:**

Ao copiar as permissões de um usuário para o outro, as configurações de 'Supervisor' e 'Pode Incluir Relatórios' serão sobrepostas prevalecendo as configurações do usuário de origem. Ou seja, o usuário que recebe a cópia das permissões pode ter os campos Supervisor e Incluir Relatórios alterados de acordo com o usuário onde as permissões serão copiadas.

false

**Versão:** 11.82.XX e 12.01.XX
