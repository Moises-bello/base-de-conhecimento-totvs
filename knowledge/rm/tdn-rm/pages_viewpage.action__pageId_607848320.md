---
content_hash: 63b8901c370afab5c64dce84e05d1b914376533e4fa53eb6d456fd39ebd26da4
fetched_at: '2026-06-29T00:10:58.930094+00:00'
page_id: '607848320'
product: rm
source: tdn-rm
title: Registro de Atendimento Externo (Particular) com Lançamento de Procedimento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=607848320
version: 12
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Configurações**
4. **Tela Registro de Atendimento e Lançamento na Conta**
5. **Tabelas utilizadas**

sumarioVisão Geral

## **01. VISÃO GERAL**

No Registro de Atendimento Externo será habilitado o item "Lançamento em Conta", quando o grupo de convênio do atendimento for Particular, então será possível lançar procedimentos na conta do paciente pelo próprio registro do atendimento.

## **02. EXEMPLO DE UTILIZAÇÃO**

No Registro de Atendimento Externo de Particular, acesse o item "Lançamento em Conta".

Insira ou Edite a tela "Lançamento em Conta" e preencha todos os campos: data da guia e procedimento.

Caso esteja parametrizado conforme citado anteriormente, este procedimento será lançado na conta do paciente.

Configurações

## **03. CONFIGURAÇÕES**

**Principais Campos e Parâmetros**

| Campo | Descrição |
| --- | --- |
| Grupo de convênios | No Cadastro do convênio, preencher com a opção PARTICULAR |
| Lança procedimentos das guias de autorização na conta do paciente, se dentro da faixa de codificação | No Cadastro das Condições Contratuais, marcar o parâmetro para que o procedimento seja lançado na conta. |

Para que seja possível realizar o lançamento, deve-se:

A) Na tela de cadastro de convênios, o **Grupo de Convênios** deve estar selecionado **PARTICULAR**.

B) Na tela de condições contratuais com convênios, na aba **Parâmetros 1**, marcando o campo **Lança procedimentos das guias de autorização na conta do paciente, se dentro da faixa de codificação**.

Tela de registro de atendimento

## **04. TELA REGISTRO DE ATENDIMENTO**

## **05. TABELAS UTILIZADAS**

* SZATENDAUTORIZ
