---
content_hash: 9ea58f4e6e764bb0743393f4a0a329bb28ee047ed33add0890c985c1c2e4bbba
fetched_at: '2026-06-29T00:06:10.545351+00:00'
page_id: '203764288'
product: rm
source: tdn-rm
title: TTFNV6_DT_Parametro_Nao_Inclui_HistSal_Transf_Sem_Aumento
type: documentation
url: https://tdn.totvs.com/display/LRM/TTFNV6_DT_Parametro_Nao_Inclui_HistSal_Transf_Sem_Aumento
version: 2
---

# PARÂMETRO PARA NÃO INCLUIR HISTÓRICO SALARIAL EM TRANSFERÊNCIAS SEM AUMENTO DE SALÁRIO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *C&P* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Rescisão com Transferência* |
| **Situação/Requisito:** | *Rescisão com transferência de funcionários não deve inserir linha no histórico salarial se a informação original não for alterada**.* |
| **Solução/Implementação:** | *Criação de um parâmetro no Parametrizador para o usuário optar por não incluir nova linha no histórico salarial em transferências sem alteração de salário.*  *O novo parâmetro será na pasta Rescisão/Transferência, com a descrição "Não inclui nova linha no histórico salarial em transferências sem alteração de salário".* |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | *TTFNV6* |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *12.1.8* |
