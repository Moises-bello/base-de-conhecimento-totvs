---
content_hash: dd31c2ce4b1b6a66d30ad0f4083850ecadf27bd96994a1e081d220a02c90c8cc
fetched_at: '2026-06-29T00:09:11.684610+00:00'
page_id: '415700176'
product: rm
source: tdn-rm
title: 3844527 EDUCACIONAL01-6421 DT Geração de usuário com validação da complexidade
  da senha
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=415700176
version: 2
---

# GERAÇÃO DE USUÁRIO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Gestão Educacional |
| **Função:** | Geração de usuário |
| **Situação/Requisito:** | Ao gerar usuário utilizando tipo de senha "Data de nascimento", o sistema emite mensagem de erro "A senha deve conter caracteres em maiúsculo". Obs.: nos parâmetros Globais de Segurança está configurando para que a senha tenha caracteres maiúsculos. |
| **Solução/Implementação:** | Alterado o comportamento na geração de usuário para observar o parâmetro “Validar complexidade da senha no cadastro” do menu “Parâmetros Globais | Segurança”.  Somente será validado a complexidade da senha na inclusão de usuário, se marcado no menu "Ambiente -> Parâmetros -> Parâmetros Globais -> Segurança" o campo “Validar complexidade de senha no cadastro”. A validação somente será feita em senha fixa, ou seja, no parâmetro “Educacional | Geração de usuários” estiver marcado o campo Senha igual a Fixa. Caso a validação da complexidade de senha estiver marcado, não será permitido utilizar tipo de senha igual a data de nascimento.  **Importante:** quando for parametrizado para utilizar tipo de senha “Data de Nascimento”, deverá ser desmarcado nos parâmetros globais a opção de validar a complexidade da senha no cadastro, pois não se aplica a este caso. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A |
| **Documento de Referência:** | N/A |
| **Pacote:** | Informe o [linkdopacote] |
