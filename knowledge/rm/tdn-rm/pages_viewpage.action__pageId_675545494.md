---
content_hash: 766f786ccea9fe574a4d8670c74be3b64b4a11871f4004c49c60de3442b8cb29
fetched_at: '2026-06-29T00:11:16.991706+00:00'
page_id: '675545494'
product: rm
source: tdn-rm
title: Relatório Inspeção de Qualidade
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=675545494
version: 4
---

O relatório **CRMREL0016 - Inspeção de Qualidade** retorna os dados informados na Inspeção de Qualidade pelo app Minhas Inspeções e poderá ser importado no TOTVS Aprovações e Atendimento.

O relatório contém na parte superior em Dados Gerais o nome da inspeção, o usuário que respondeu o formulário, o nome da tarefa/projeto ao qual o formulário está vinculado e o score de pontuação das respostas da inspeção. Na parte inferior o relatório contém em Itens da Inspeção todas as perguntas e respostas inseridas no app.

O relatório só será gerado corretamente quando ele estiver vinculado a um atendimento gerado pelo WorkFlow dos **Minhas Inspeções**. Para que seja gerado, o relatório deve estar informado na etapa do fluxo de atendimento e o workflow utilizado no formulário da inspeção deve possuir a ação Criar Atendimento no TOTVS Aprovações.

* **Ação no workflow para que a Inspeção gere Atendimento**
  1. No workflow do TOTVS Minhas Inspeções inserir uma ação
  2. Parametrizar a ação com o tipo de ação: Criar atendimento no TOTVS Aprovações
* **Relatório informado nas etapas do fluxo do atendimento**
  1. No tipo de atendimento do TOTVS Aprovações e Atendimento, abrir o anexo das etapas
  2. Editar a etapa desejada e na aba **Configurações do aplicativo 'Minhas Inspeções'** informar o relatório CRMREL0016 - Inspeção de Qualidade
  3. O relatório será gerado quando o atendimento chegar na etapa onde ele está configurado. O relatório será anexado em pdf no anexo **Arquivos anexos do atendimento**
