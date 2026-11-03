---
content_hash: b211639ad6f60b667f1851828b7afc982d44cf178742ff8f1445cfea5ef00a26
fetched_at: '2026-06-29T00:06:03.504278+00:00'
page_id: '198955796'
product: rm
source: tdn-rm
title: TSXMNO_DT_Erro_Ao_Importar_Imagens_Violacao_Chave_Estrangeira
type: documentation
url: https://tdn.totvs.com/display/LRM/TSXMNO_DT_Erro_Ao_Importar_Imagens_Violacao_Chave_Estrangeira
version: 2
---

# NOME DO REQUISITO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *C&P* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Importação de Imagens* |
| **Situação/Requisito:** | *Ao realizar importação de imagens ocorre o seguinte erro:*  *Violação de chave estrangeira*  *Possíveis causas:*  *- exclusão de registro que possui outros registros associados*  *- inclusão de registro detalhe sem um registro mestre associado.* |
| **Solução/Implementação:** | *Foi ajustado a forma que o sistema busca o no id na tabela GIMAGEM ao realizar a importação de imagens.* |
| **Chamados relacionados:** | *TSXMNO* |
| **Versões/Release:** | *12.1.7* |
