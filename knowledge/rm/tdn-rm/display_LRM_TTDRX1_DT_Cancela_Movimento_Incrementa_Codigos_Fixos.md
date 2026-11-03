---
content_hash: 4148f8aed7e6d3220003fbf16e2f82c6783a18ae8ee3ae77d8b57ac56cb664ed
fetched_at: '2026-06-29T00:06:06.903178+00:00'
page_id: '201733213'
product: rm
source: tdn-rm
title: TTDRX1_DT_Cancela_Movimento_Incrementa_Codigos_Fixos
type: documentation
url: https://tdn.totvs.com/display/LRM/TTDRX1_DT_Cancela_Movimento_Incrementa_Codigos_Fixos
version: 1
---

# CANCELAMENTO DE MOVIMENTO COM INCREMENTO DE CÓDIGOS FIXOS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *C&P* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Cancelamento de Movimento* |
| **Situação/Requisito:** | *Ao processar o Cancelamento de Movimento selecionando a opção Todos os períodos, com o parâmetro Incrementa códigos Fixos marcado, caso seja a última vez do lançamento do código fixo, o incremento não é realizado.* |
| **Solução/Implementação:** | *Ajuste no tratamento do parâmetro "Incrementa códigos Fixos" do módulo de Cancelamento de Movimento, para o caso de ser a última vez do lançamento do código fixo, ou seja, o número de vezes do cadastro está zerado.*  *O problema só ocorria quando na seleção do periodo era informado "Todos".* |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | *TTDRX1* |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *12.1.7* |
