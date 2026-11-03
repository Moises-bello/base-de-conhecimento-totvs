---
content_hash: 34b043813ab55df439bab7428b08339fb7b6e4bb3a1554f8ed4e2c96701b3b4b
fetched_at: '2026-06-29T00:09:52.457792+00:00'
page_id: '439367959'
product: rm
source: tdn-rm
title: 4247792 FOPCALCULO01-5318 Importação de Funcionário
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=439367959
version: 1
---

# Importação de Funcionário

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Folha de Pagamento |
| **Função:** | Importação de Funcionário |
| **Situação/Requisito:** | Ao realizar a importação de um funcionário sem marcar o parâmetro "Sobrescrever Dados Cadastrais" e passar um "CodPessoa" já existente na base de dados, o sistema importou o funcionário na coligada Corrente (PFUNC) como funcionário(correto) mas substituindo os dados da tabela PPESSOA já existente na base de dados que era outra pessoa/funcionário. É importante lembrar que o CodPessoa passado na importação pertence à uma pessoa diferente, com "CPF" e "Data de Nascimento" diferentes da que existia previamente no RM. |
| **Solução/Implementação:** | Os dados da pessoa só são sobrescritos quando o parâmetro "Sobrescrever Dados Cadastrais" é marcado e o CPF e Data de Nascimento dos registros de pessoas envolvidas forem iguais. |
