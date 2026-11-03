---
content_hash: bca858a327b0c33eaa6af35e88cf957abd2033481f2458ca1bfff2ff36ac68f8
fetched_at: '2026-06-29T00:06:27.263122+00:00'
page_id: '232816836'
product: rm
source: tdn-rm
title: TUCR96_DT_Msg_Aviso_CadEvento_Pensao_Formula
type: documentation
url: https://tdn.totvs.com/display/LRM/TUCR96_DT_Msg_Aviso_CadEvento_Pensao_Formula
version: 2
---

# MENSAGEM DE AVISO NO CADASTRO DE EVENTO DE PENSÃO COM FÓRMULA

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Pensão Alimentícia* |
| **Situação/Requisito:** | *Quando é utilizada fórmula nos eventos de pensão alimentícia (CC's 13, 113, 120, 121 e 319), o valor da pensão não é inserido no cadastro do dependente, aba "Movimentação da Pensão de Dependentes".* |
| **Solução/Implementação:** | *O lugar correto para informar a fórmula para o cálculo da pensão alimentícia é dentro do cadastro do dependente de pensão.*  *Para assim, o sistema poder identificar que o valor calculado é deste pensionista, e inserir o registro na respectiva movimentação.*  *No cadastro do evento, quando for informada uma fórmula valor nos eventos de pensão alimentícia, deverá ser exibida uma mensagem de aviso, informando que não será possível atualizar automaticamente o movimento de pensão.* |
| **Chamados   relacionados:** | *TUCR96, TUJ007* |
| **Versões/Release:** | *11.82.43, 12.1.10* |
