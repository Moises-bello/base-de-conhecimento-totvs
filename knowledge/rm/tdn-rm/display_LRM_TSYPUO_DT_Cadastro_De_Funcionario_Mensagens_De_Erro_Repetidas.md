---
content_hash: 1633a087fabe862db2c6bb555be01d4b8f47b381c8863a0783c0438188bbe06a
fetched_at: '2026-06-29T00:06:03.497004+00:00'
page_id: '198955690'
product: rm
source: tdn-rm
title: TSYPUO_DT_Cadastro_De_Funcionario_Mensagens_De_Erro_Repetidas
type: documentation
url: https://tdn.totvs.com/display/LRM/TSYPUO_DT_Cadastro_De_Funcionario_Mensagens_De_Erro_Repetidas
version: 1
---

# CADASTRO DE FUNCIONÁRIOS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *C&P* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Cadastro de Funcionários* |
| **Situação/Requisito:** | *No cadastro de funcionários, a função de validação era chamada duas vezes, causando algumas mensagens de erro ou alertas a serem exibidos mais de uma vez.* |
| **Solução/Implementação:** | *Foi removida uma das chamadas redundantes à função de validação* |
| **Chamados relacionados:** | *TSYPUO* |
| **Versões/Release:** | *11.82.40* |
