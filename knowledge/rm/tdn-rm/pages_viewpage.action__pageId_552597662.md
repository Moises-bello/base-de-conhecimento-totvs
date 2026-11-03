---
content_hash: 282bba403b458c52b00b1c5509fb651ac333a50865b74ce469f4518a9abbe59c
fetched_at: '2026-06-29T00:10:44.509649+00:00'
page_id: '552597662'
product: rm
source: tdn-rm
title: Vínculo do Cartão de Visitante  ao Registro de Atendimento Externo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=552597662
version: 5
---

## 

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Rotinas Envolvidas**
   1. **Outras Ações / Ações relacionadas**
4. **Parâmetros Gerais | Registro e Controle III**
   1. **Principais Campos e Parâmetros**
5. **Tabelas utilizadas**

SumárioVisão Geral

## **01. VISÃO GERAL**

Associar o cartão de acesso de um visitante à um atendimento externo.

Atenção

O Documento Técnico sobre a configuração e utilização do menu “**Controle de Visitantes**” , encontra-se no link <https://tdn.totvs.com/x/P9RhE>

Exemplo de Utilização

## **02. EXEMPLO DE UTILIZAÇÃO**

1 - Para utilizar a funcionalidade é necessário que marcar o parâmetro “**Associa Atendimento ao Nº Cartão Visitante**”, para isso, vá até **Ambiente> Parâmetros > Gestão Hospitalar.**  
  
Após isso, vá em **Registro e Controle > Registro e Controle 2.**E marque o parâmetro necessário para essa rotina.

2 - Para vincular um cartão e visitante a um Atendimento acesse o menu **Atendimento> Registro de Atendimento.**

3 - Pesquise e/ou crie um atendimento Externo (campo Tipo Paciente igual à Externo).

Mesmo com o parâmetro marcado, o usuário não é obrigado a associar um cartão a um registro de atendimento.

**3** **Vinculando um Cartão de Visitante ao Registro de Atendimento Externo**

1 -No campo Cartão Visitante, clique  sem preencher o número do cartão, a tela apresentada irá verificar se já existe um visitante e cartão cadastrado para este paciente e retornará o número do cartão.

2 -Caso não exista cartão de visitante, será apresentado mensagem perguntando se deseja cadastrar.

3 -Em seguida será aberto o menu de Controle de Visitas.

4- Preencha os campos obrigatórios.

Clicar no botão “Gerar” para que seja atribuído um número e impresso a etiqueta do cartão.

5 - O número do cartão (etiqueta) será associado ao retornar para o Registro de Atendimento

Rotinas Envolvidas

## **03. Rotinas Envolvidas**

**Outras Ações / Ações relacionadas**

| Ação | Descrição |
| --- | --- |
| Entrada de Visitantes - Outros Setores  (menu Atendimento/Controle de Visitantes) | Controle de entrada/saida de visitantes. |
| Associar Cartão a Atendimento Paciente Externo  (menu Atendimento/Registro de Atendimento - paciente externo) | Campo "Cartão de Visitante" para realizar a associação do atendimento ao cartão de visitante. |

Paramêtros

## **04. Parâmetros Gerais | Registro e Controle III**

**Principais Campos e Parâmetros**

| Campos e Parâmetros |
| --- |
| Associa Atendimento ao Nº Cartão Visitante |
| Não associar Leito ao Número de Cartão Visitante |
| Dar preferência p/ Cartão Pré Definido |
| Tipo Visitante Default |

## **05. TABELAS UTILIZADAS**

* SZCARTAOVISITANTE

  SZVISITANTE

  SZLOGVISITANTE
