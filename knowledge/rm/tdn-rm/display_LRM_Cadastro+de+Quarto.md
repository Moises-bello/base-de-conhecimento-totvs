---
content_hash: 10bb4e616426dae4bb3c2fc7aac948df67976533c852e13e1a1a3a801f8f1996
fetched_at: '2026-06-29T00:11:36.047785+00:00'
page_id: '770955711'
product: rm
source: tdn-rm
title: Cadastro de Quarto
type: documentation
url: https://tdn.totvs.com/display/LRM/Cadastro+de+Quarto
version: 6
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Cadastro de quarto**
3. **Cadastro de Leitos do Quarto**
4. **Regras/Validações:**

sumarioVisão Geral

## **1. VISÃO GERAL**

A funcionalidade de quartos de leito serve como intuito do hospital cadastrar as enfermarias que possuem múltiplos leitos associadas a mesma.

Este cadastro serve para controle não só dos leitos presentes na enfermaria, mas como o controle de isolamento e higienização dos mesmos.

Cadastro de quarto

## **02. Cadastro de Quarto**

Para realizar o Cadastro de quartos, será necessário realizar o acesso ao módulo **RM Saúde > Aba Cadastros > Registro e Controle > Outros Cadastros > Quartos.**

**Obs:** Ao abrir o Cadastro de Quartos, o anexo de Leitos associados ao Quarto será aberto automaticamente.

Para cadastrar um quarto será necessário informar a “Descrição” (Nome do quarto ou algum código que desejar) e o “Número de Leitos”

(Número limite de leitos que o quarto irá aceitar a associação).

**Obs:** O campo “Isolado?” é apenas para controle do processo de “Isolamento de Quarto” do Painel de Leitos.

Cadastro de Leitos do Quarto

## **03. Cadastro de Leitos do Quarto**

Para que seja feita a associação do leito no Quarto, é necessário que o usuário acesse o anexo do cadastro de “Quartos”

(Anexo Leitos do Quarto, exibido na imagem acima).

O cadastro dos leitos no Quarto requer que o usuário informe os campos da imagem abaixo:

Regras/Validações

## **04. Regras/Validações:**

1. Caso o Quarto esteja com o status “Isolado” (Checkbox “Isolado?” marcado), não será permitido alterar o registro.
2. Ao tentar adicionar um novo Leito ao Quarto, se o Quarto já possuir Leitos do mesmo número do limite de leitos do cadastro de Quarto,

          será exibido a seguinte mensagem:

     3. O campo “Quarto” no cadastro de “Leitos do Quarto” é preenchido automaticamente de acordo com o registro selecionado no cadastro de quarto associado ao anexo.

     4. Ao tentar selecionar o “Leito” no cadastro de “Leitos do Quarto”, será exibido na visão do Lookup apenas os leitos que não estejam vinculados a nenhum quarto.
