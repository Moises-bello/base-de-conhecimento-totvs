---
content_hash: fa356a5ff3e43e2256df2b7a2150927439a3f64711e226a9822cc055afa74276
fetched_at: '2026-06-29T00:06:09.831165+00:00'
page_id: '203757551'
product: rm
source: tdn-rm
title: TTGUX8_DT_Geracao_Arquivo_Nis
type: documentation
url: https://tdn.totvs.com/display/LRM/TTGUX8_DT_Geracao_Arquivo_Nis
version: 1
---

# GERAÇÃO ARQUIVO NIS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Geração Arquivo NIS* |
| **Situação/Requisito:** | *Erro ao gerar código de município do NIS retirando zeros à esquerda* |
| **Solução/Implementação:** | *Ajuste em valor de código de município no arquivo NIS para não desconsiderar Zeros à esquerda nos campos 091108 (código município endereço) e 039000 (código de município de nascimento)* |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | *TTGUX8* |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *11.82.41* |
