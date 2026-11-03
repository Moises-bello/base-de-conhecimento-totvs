---
content_hash: 8c699e01f5ee3648b7f92aab09c6ee5c1305c1c8836c59fead2fd184ef4fab0e
fetched_at: '2026-06-29T00:06:03.561810+00:00'
page_id: '200900655'
product: rm
source: tdn-rm
title: TSTAIM_DT_Edicao_de_Medias_do_Sindicato
type: documentation
url: https://tdn.totvs.com/display/LRM/TSTAIM_DT_Edicao_de_Medias_do_Sindicato
version: 1
---

# CADASTRO DE SINDICATOS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *C&P* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Edição de Médias do Sindicato* |
| **Situação/Requisito:** | *Ao tentar salvar a edição de um sindicato, era apresentada a mensagem de erro: Violação de concorrência: UpdateCommand afetou 0 dos registros 1 esperados.* |
| **Solução/Implementação:** | *Foi removida uma chamada desnecessária ao AcceptChanges do DataSet que estava interferindo em uma função para tratamento de registros faltantes na tabela de médias do sindicato.* |
| **Chamados relacionados:** | *TSTAIM* |
| **Versões/Release:** | *12.1.7* |
