---
content_hash: 5dac06ded3d45d5646c8d0861ed41ad6f7db08aaa6582746bb2e3b8a7c7ac794
fetched_at: '2026-06-29T00:06:04.603328+00:00'
page_id: '200909430'
product: rm
source: tdn-rm
title: TRAAKS_DT_Faltas_No_Periodo_Aquisitivo
type: documentation
url: https://tdn.totvs.com/display/LRM/TRAAKS_DT_Faltas_No_Periodo_Aquisitivo
version: 1
---

# CADASTRO DE FÉRIAS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *C&P* |
| **Módulo:** | *TOTVS Folha de Pagamento* |
| **Função:** | *Cadastro de Férias* |
| **Situação/Requisito:** | *Foi criado um campo "FALTAS" na tabela de férias, que é preenchido ao finalizar as férias. Ao abrir um registro de férias de um período aquisitivo antigo de antes de o campo ser criado, esse campo vem zerado mesmo em casos que houveram faltas, fazendo com que o saldo daquele período seja exibido de forma incorreta.* |
| **Solução/Implementação:** | *Foi criada uma rotina a ser executada pelo menu "Executar", chamada "Manutenção de Faltas em Períodos Antigos". Ao executar essa rotina, os campos de faltas são recalculados para todos os períodos em que estiverem zerados.* |
| **Chamados relacionados:** | *TRAAKS* |
| **Versões/Release:** | *12.1.7* |
