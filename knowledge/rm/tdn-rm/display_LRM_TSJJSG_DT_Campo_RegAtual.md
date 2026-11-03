---
content_hash: 586eb7e779faa95bc721767a38453b739f2ccf97555637160880dd869a396abb
fetched_at: '2026-06-29T00:06:05.737392+00:00'
page_id: '201726872'
product: rm
source: tdn-rm
title: TSJJSG_DT_Campo_RegAtual
type: documentation
url: https://tdn.totvs.com/display/LRM/TSJJSG_DT_Campo_RegAtual
version: 4
---

# ALTERAÇÃO DOS REGISTROS NO CAMPO REGATUAL NA TABELA PFUNC

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *TOTVS Folha de Pagamento* |
| **Função:** | *Alteração dos registros no campo RegAtual na tabela PFunc* |
| **Situação/Requisito:** | O campo REGATUAL da tabela PFUNC deve ser preenchido com o valor 0 quando a situação do funcionário for igual a D, porém se existir mais de uma chapa para a pessoa na mesma coligada, o sistema verifica se existe alguma situação ativa, senão existir verifica qual a maior data de demissão ou se a data de demissão esta vazia para preencher o campo REGATUAL com 1. |
| **Solução/Implementação:** | Foi realizado a alteração do campo RegAtual da tabela PFUNC deve ser preenchido com o valor 0 quando a situação do funcionário for igual a D, porém se existir mais de uma chapa para a pessoa na mesma coligada, o sistema verifica se existe alguma situação ativa, senão existir verifica qual a maior data de demissão ou se a data de demissão esta vazia para preencher o campo REGATUAL com 1 |
| **Versões/Release:** | *11.82.41* |
