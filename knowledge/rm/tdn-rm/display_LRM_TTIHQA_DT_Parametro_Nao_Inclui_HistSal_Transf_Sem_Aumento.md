---
content_hash: dadc0349f8a0b69326e48ef795831a40621ad0de35a5d6fe4865dd663f2ca5f6
fetched_at: '2026-06-29T00:06:10.549978+00:00'
page_id: '203764391'
product: rm
source: tdn-rm
title: TTIHQA_DT_Parametro_Nao_Inclui_HistSal_Transf_Sem_Aumento
type: documentation
url: https://tdn.totvs.com/display/LRM/TTIHQA_DT_Parametro_Nao_Inclui_HistSal_Transf_Sem_Aumento
version: 1
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
| **Chamados relacionados:** | *TTIHQA* |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *11.82.41* |
