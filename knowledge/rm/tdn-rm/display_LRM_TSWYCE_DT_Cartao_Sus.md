---
content_hash: bc0bbc39a41830e5f4eb4b2d7a0508bd63788bed8c211a0ac6411ebe3b0b642a
fetched_at: '2026-06-29T00:06:04.068371+00:00'
page_id: '200905231'
product: rm
source: tdn-rm
title: TSWYCE_DT_Cartao_Sus
type: documentation
url: https://tdn.totvs.com/display/LRM/TSWYCE_DT_Cartao_Sus
version: 2
---

# Número cartão SUS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM.* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de pagamento* |
| **Função:** | *Cadastro de funcionário* |
| **Situação/Requisito:** | No cadastro do funcionário (aba Documentação) e do dependente (aba identificação) existe o campo Número do Cartão SUS, que permite informar um número com no máximo 20 caracteres. Porém a empresa possui funcionários com número de cartão do SUS com mais caracteres que o permitido no sistema. |
| **Solução/Implementação:** | Otimizado número do cartão do SUS, alterada a quantidade máxima  de 20 para 100 caracteres.  Solicitação de script, alterando a quantidade máxima de caracteres do campo Número do Cartão SUS, de forma que seja possível inserir um número maior que 20 caracteres. Chamado TSZSVK |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | TSWYCE, TSZSVK |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *11.82.41* |
