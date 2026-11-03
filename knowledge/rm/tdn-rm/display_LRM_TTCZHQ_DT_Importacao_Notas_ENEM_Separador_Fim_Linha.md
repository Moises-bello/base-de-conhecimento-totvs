---
content_hash: da90e1e4b525ec364e358e08ef2b3ff769b36ddc416fc0716c871bedb4e3f958
fetched_at: '2026-06-29T00:06:05.790065+00:00'
page_id: '201727375'
product: rm
source: tdn-rm
title: TTCZHQ_DT_Importacao_Notas_ENEM_Separador_Fim_Linha
type: documentation
url: https://tdn.totvs.com/display/LRM/TTCZHQ_DT_Importacao_Notas_ENEM_Separador_Fim_Linha
version: 1
---

# NOME DO REQUISITO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Processo Seletivo* |
| **Função:** | *Importar Notas ENEM* |
| **Situação/Requisito:** | *O arquivo enviado pelo INEP no formato do layout 2014 continha o carácter ';' no final da linha, diferente do arquivo de especificação, fazendo o sistema identificar que existe mais uma coluna, ou seja, 23 colunas, sendo que o sistema espera 22.* |
| **Solução/Implementação:** | *Foi feito um ajuste no processo de importação para que no momento da leitura do arquivo o sistema identifique se há o ';' no final da linha, e remover caso exista, assim o sistema consegue processar corretamente as notas tendo ou não o ';' no final.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |
| **Versões/Release:** | *12.1.7* |
