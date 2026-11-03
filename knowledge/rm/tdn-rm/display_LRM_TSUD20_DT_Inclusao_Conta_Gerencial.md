---
content_hash: 7d75b8dd7454c4116e47d7d0ed94d0a9f552edef40d2dfd1caf680c97e6ed6f6
fetched_at: '2026-06-29T00:06:01.003298+00:00'
page_id: '196814032'
product: rm
source: tdn-rm
title: TSUD20_DT_Inclusao_Conta_Gerencial
type: documentation
url: https://tdn.totvs.com/display/LRM/TSUD20_DT_Inclusao_Conta_Gerencial
version: 1
---

# NOME DO REQUISITO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Informe o segmento.* |
| **Módulo:** | *Gestão de Estoque* |
| **Função:** | *Inclusão de conta gerencial* |
| **Situação/Requisito:** | *Ao incluir conta gerencial de classificações diferentes no cadastro de uma natureza orçamentária*  *ocorre erro de chave duplicada. a falha ocorre porque o campo IDTBORCAMENTOCONT da tabela GAUTOINC para os produtos T e F estão diferentes.* |
| **Solução/Implementação:** | *A solução é via script e atualiza o valor do campo *IDTBORCAMENTOCONT da tabela GAUTOINC para os produtos T e F para o maior valor existente entre os dois.** |
| **Conversores e Parâmetros:** | *Não se aplica.* |
| **Chamados relacionados:** | *Não se aplica.* |
| **Requisito (ISSUE):** | *Não se aplica.* |
| **Versões/Release:** | *11.82.40* |
