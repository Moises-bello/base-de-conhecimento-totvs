---
content_hash: 07edc9ea6f0593f5f1687c6c8788684fa37602ce2b91cb8ce5283236ffaedc0a
fetched_at: '2026-06-29T00:06:09.834964+00:00'
page_id: '203757622'
product: rm
source: tdn-rm
title: TTHHMZ_DT_Geracao_Arquivo_Nis
type: documentation
url: https://tdn.totvs.com/display/LRM/TTHHMZ_DT_Geracao_Arquivo_Nis
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
| **Chamados relacionados:** | *TTHHMZ* |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *12.1.8* |
