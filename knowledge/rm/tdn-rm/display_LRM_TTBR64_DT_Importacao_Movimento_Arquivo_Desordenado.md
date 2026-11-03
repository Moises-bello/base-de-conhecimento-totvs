---
content_hash: e3483be2b63f8f10d37165aaa36748f3a025d0d757eaa5c499efd309bbab4b88
fetched_at: '2026-06-29T00:06:10.904507+00:00'
page_id: '203766036'
product: rm
source: tdn-rm
title: TTBR64_DT_Importacao_Movimento_Arquivo_Desordenado
type: documentation
url: https://tdn.totvs.com/display/LRM/TTBR64_DT_Importacao_Movimento_Arquivo_Desordenado
version: 3
---

# IMPORTAÇÃO DE MOVIMENTO COM ARQUIVO DESORDENADO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção & Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Importação de Movimento* |
| **Situação/Requisito:** | *Ao realizar importação de movimento com um arquivo que contenha funcionários ativos e demitidos misturados e linhas fora da ordenação por chapa, algumas linhas do arquivo são desconsideradas caso não seja marcado o parâmetro "Importa demitido".* |
| **Solução/Implementação:** | *Ajuste na importação de movimento para não desconsiderar nenhuma linha, mesmo que o arquivo esteja sem ordenação, e contenha funcionários demitidos, apesar de não importar demitidos.* |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | *TTBR64* |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *12.1.8* |
