---
content_hash: e24e703a39e6de97f5fbdd1389bf5a06d9825b1bf8c5e1b9f16b073029adb09c
fetched_at: '2026-06-29T00:12:16.262492+00:00'
page_id: '983797619'
product: rm
source: tdn-rm
title: Permitir alta à pacientes com requisições pendentes
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=983797619
version: 8
---

## **ÍNDICE**

1. **Visão Geral**
2. **Processo de alta**
3. **Processo**
   1. **Parâmetro desativado**
   2. **Parâmetro ativado**
4. **Parâmetro**

sumarioVisão Geral

O objetivo desta funcionalidade é fornecer um controle sobre a permissão de alta de pacientes que ainda possuem requisições pendentes na farmácia.

A ativação ou desativação desta funcionalidade é controlada por um parâmetro de configuração.

Processo de alta

Essa funcionalidade está associada ao processo de alta descrito conforme documentação:

Processo OperaçõesParâmetro desativado

* Com o parâmetro desativado o RM irá aplicar a validação, caso encontre alguma requisição pendente de processamento associada ao atendimento um aviso de erro será exibido ao usuário. A mensagem exibirá informações que auxiliem o usuário a identificar a requisição e seguir com o ajuste necessário.

Parâmetro ativado

Com o parâmetro ativado o RM irá seguir o fluxo de alta normalmente sem aplicar essa regra, caso nenhuma outra validação seja impeditiva o processo de alta será finalizado e uma mensagem de confirmação será exibida ao usuário

Informação

Requisições não processadas podem ser executadas após a alta do paciente, contanto que as datas e as demais regras de validação do processo sejam atendidas.

Parâmetro

O parâmetro deve ser acessado através da tela padrão de gerenciamento de parâmetro do TOTVS RM Gestão Hospitalar.

Gestão Hospitalar > Cuidados com o paciente > Configuração > Permitir dar alta ao paciente com requisições de estoque pendentes de processamento
