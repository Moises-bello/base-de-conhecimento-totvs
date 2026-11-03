---
content_hash: 15ec5a8adcd327dd3c8eecf76745a0fc57afdc78ed9884227234ea38b10817c9
fetched_at: '2026-06-29T00:11:17.129983+00:00'
page_id: '677021880'
product: rm
source: tdn-rm
title: Relatório WorkFlow - Detalhes da Inspeção
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=677021880
version: 1
---

O relatório **TOPREL0067 - WorkFlow - Detalhes da Inspeção** retorna os dados informados na Inspeção de Qualidade pelo app Minhas Inspeções e poderá ser importado no TOTVS Aprovações e Atendimento.

O relatório contém na parte superior em Dados Gerais o nome da inspeção, o usuário que respondeu o formulário, o nome da tarefa/projeto ao qual o formulário está vinculado e o score de pontuação das respostas da inspeção. Na parte inferior o relatório contém em Itens da Inspeção todas as perguntas e respostas inseridas no app.

O relatório poderá ser enviado em anexo pdf via email para os usuários selecionados no workflow.

* **Ação no workflow:**
  1. Importar o relatório TOPREL0067 - WorkFlow - Detalhes da Inspeção para a base de dados
  2. No workflow do TOTVS Minhas Inspeções inserir uma ação
  3. **Tipo de ação:** Enviar Notificação
  4. **Filtrar por tipo de formulário:** Informar o tipo de formulário onde o workflow poderá ser informado.
  5. **Tipo de notificação:** Notificação via e-mail.
  6. Assunto e corpo do e-mail (Opcional)
  7. **Relatório a ser anexo ao email:** informar o relatório TOPREL0067 - WorkFlow - Detalhes da Inspeção.
  8. **Destino da Inspeção:** informar se o workflow será disparado para o usuário ou para o grupo de usuários
  9. **Tipo de usuário:**informar o tipo de usuário que receberá a notificação.
