---
content_hash: 5061725e8f71221b86a4adcf07768058b7f6555ba275e80a1c43e6620a7e8a0a
fetched_at: '2026-06-29T00:10:32.521708+00:00'
page_id: '527003238'
product: rm
source: tdn-rm
title: Permissões por Tipo de Movimento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=527003238
version: 4
---

O anexo de Permissões por Tipo de Movimento tem o objetivo de controlar as ações dos usuários sobre os Tipos cadastrados no configurador de parâmetros do sistema de Gestão de Estoque, Compras e Faturamento do BackOffice RM. Este anexo será exibido somente aos usuários que tenham permissão de acesso ao cadastro de usuários, e que tenham selecionado o contexto do sistema de Gestão de Estoque, Compras e Faturamento.

**Pré-Condições:**

1. Ter permissão de acesso e edição do cadastro de Usuários.
2. Ter cadastrado os tipos de movimento nos parâmetros do sistema de Gestão de Estoque, Compras e Faturamento.
3. Ter selecionado o contexto do sistema de Gestão de Estoque, Compras e Faturamento, através do cadastro de Usuários.

**Incluindo as permissões para um usuário.**

**Passo 1**→ Acesse: TOTVS RM/ Serviços Globais/ Segurança/ Usuários.

**Passo 2 →** Selecione o usuário desejado e clique em: Anexos/ Permissões por Tipo de Movimento.

* Esta opção está presente nos Anexos, quando o módulo dos Sistema selecionado for: "Gestão de Estoque, Compras e Faturamento".

**Passo 3** → Será exibido o formulário de permissões. Selecione o [Tipo de Movimento] qual deseja conceder a permissão e marque as opções desejadas. As opções de permissão são:

* Consultar
* Alterar
* Incluir
* Excluir
* Ativar / Tornar Inativo
* Alterar após E-mail
* Cancelar
* Reabrir
* Alterar após Imprimir
* Alterar Item Integrado:
  + Com este parâmetro selecionado o usuário conseguirá editar todos os campos dos itens de movimentos, mesmo com o bloqueio de acesso a campos no perfil do usuário, portanto o uso deverá ser avaliado.
* Imprimir
* Copiar
* Enviar E-mail
* Lançar
* Faturar
* Cotar
* Contabilizar
* Estornar Contabilidade
* Incluir Por Faturamento
* Incluir Por Contrato:
  + Com este parâmetro selecionado o usuário poderá incluir um movimento por faturamento de contrato mesmo que não tenha permissão de inclusão direta do movimento. No entanto, se o parâmetro "Incluir" já estiver marcado, mesmo que o "Incluir Por Contrato" esteja desmarcado, será possível incluir movimentos via faturamento de contrato.

**Observação:** O sistema exibe dois botões do lado inferior direito do formulário que permitem Marcar e Desmarcar todas as opções, porém só efetuam suas ações no tipo de movimento selecionado na lista [Tipos de Movimento]

**Passo 4 →**Após selecionar as opções desejadas, clique no botão [Salvar] para continuar alterando outros tipos de movimento, ou clique no botão [Ok] para salvar as configurações e fechar o formulário.

---

FAQ's e Documentos Técnicos

* [DT Melhoria Permissões por Tipo de Movimento por Usuário.](https://tdn.totvs.com/pages/viewpage.action?pageId=286723927)
* [DT Melhorias no Processo de Conclusão](https://tdn.totvs.com/pages/viewpage.action?pageId=212894614)
* [Como atribuir permissão ao usuário em Tipo de Movimento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000563827-RM-MOV-Como-atribuir-permiss%C3%A3o-ao-usu%C3%A1rio-em-Tipo-de-Movimento)
