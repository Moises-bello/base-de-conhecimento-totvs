---
content_hash: d47c8c70d3c98efc408099c905730951ec2bc504abc72faff1c934489a98f804
fetched_at: '2026-06-29T00:06:06.979257+00:00'
page_id: '201734055'
product: rm
source: tdn-rm
title: TTDYEX_DT_Campo_RegAtual
type: documentation
url: https://tdn.totvs.com/display/LRM/TTDYEX_DT_Campo_RegAtual
version: 3
---

# Funcionário

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção & Projetos* |
| **Módulo:** | *TOTVS Folha de Pagamento* |
| **Função:** | *Alteração dos registros no campo RegAtual na tabela PFunc* |
| **Situação/Requisito:** | O campo REGATUAL da tabela PFUNC deve ser preenchido com o valor 0 quando a situação do funcionário for igual a D, porém se existir mais de uma chapa para a pessoa na mesma coligada, o sistema verifica se existe alguma situação ativa, senão existir verifica qual a maior data de demissão ou se a data de demissão esta vazia para preencher o campo REGATUAL com 1. |
| **Solução/Implementação:** | Foi realizado a alteração do campo RegAtual da tabela PFUNC deve ser preenchido com o valor 0 quando a situação do funcionário for igual a D, porém se existir mais de uma chapa para a pessoa na mesma coligada, o sistema verifica se existe alguma situação ativa, senão existir verifica qual a maior data de demissão ou se a data de demissão esta vazia para preencher o campo REGATUAL com 1 |
| **Versões/Release:** | *12.1.8* |
