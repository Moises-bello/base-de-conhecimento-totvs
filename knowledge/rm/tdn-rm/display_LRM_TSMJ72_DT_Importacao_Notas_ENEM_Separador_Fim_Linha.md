---
content_hash: 2cf8cb08c24d82c3a6269447091fde302580e0058ec27ef0a7b568bd05681d6b
fetched_at: '2026-06-29T00:06:06.906961+00:00'
page_id: '201733310'
product: rm
source: tdn-rm
title: TSMJ72_DT_Importacao_Notas_ENEM_Separador_Fim_Linha
type: documentation
url: https://tdn.totvs.com/display/LRM/TSMJ72_DT_Importacao_Notas_ENEM_Separador_Fim_Linha
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
| **Versões/Release:** | *11.83.55* |
