---
content_hash: e80fae85865cce03ea8ef5909c37b52c49b630f10732a7ff4e1a3aa101056874
fetched_at: '2026-06-29T00:06:04.085900+00:00'
page_id: '200905329'
product: rm
source: tdn-rm
title: TT8611_DT_Cartao_Sus
type: documentation
url: https://tdn.totvs.com/display/LRM/TT8611_DT_Cartao_Sus
version: 1
---

# Número cartão SUS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM.* |
| **Segmento:** | *C&P* |
| **Módulo:** | *Folha de pagamento* |
| **Função:** | *Cadastro de funcionário* |
| **Situação/Requisito:** | No cadastro do funcionário (aba Documentação) e do dependente (aba identificação) existe o campo Número do Cartão SUS, que permite informar um número com no máximo 20 caracteres. Porém a empresa possui funcionários com número de cartão do SUS com mais caracteres que o permitido no sistema. |
| **Solução/Implementação:** | Otimizado número do cartão do SUS, código defensivo que seta a quantidade máxima de caracteres de acordo com a base do cliente.  Solicitação de script, alterando a quantidade máxima de caracteres do campo Número do Cartão SUS, de forma que seja possível inserir um número maior que 20 caracteres. Chamado TSZSVK |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | TT8611, TSZSVK |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *12.1.7* |
