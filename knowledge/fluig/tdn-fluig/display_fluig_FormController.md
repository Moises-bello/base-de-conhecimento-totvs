---
content_hash: 453507f9a3f737ba12759015d9a508fee029c71659fcc14cd8e09ec82ff88f8f
fetched_at: '2026-06-28T21:35:29.270005+00:00'
page_id: '745139208'
product: fluig
source: tdn-fluig
title: FormController
type: documentation
url: https://tdn.totvs.com/display/fluig/FormController
version: 6
---

# Índice

true.\*ndicenone

#f2f2f2#f2f2f2

O FormController é um objeto enviado como parâmetro para todas as funções de personalização do formulário e possui os dados do formulário atual e informações que ajudaram a personalizar ainda mais o formulário

# Descrição

---

O objeto mais importante nos eventos de formulário é o . Com ele o desenvolvedor pode identificar melhor os dados gerais do registro de formulário como o código e a versão, se está no modo de visualização ou alteração, se está sendo visualizado no app mobile ou pelo navegador, além de manipular os valores e o status de cada um dos campos da tela.

Também consegue desabilitar os botões de imprimir e desabilitar o botão de exclusão de registro das tabelas pai x filho.

Esta documentação está em construção e por isso ainda está incompleta. Para ter visualizar todos os métodos, .

# Métodos da instância

---

Retorna o código da empresa do registro de formulário atual

Retorna o código de documento do registro de formulário atual

Retorna a versão do registro de formulário atual

Retorna o código do formulário do qual o registro de formulário pertence

Retorna o valor do campo *fieldname* no registro de formulário atual.
