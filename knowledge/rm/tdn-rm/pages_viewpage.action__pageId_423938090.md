---
content_hash: 6fe2b91d83aa814c4c4c7df3eabd5378c4dceea860987a4e13bb2a06773b96fa
fetched_at: '2026-06-29T00:09:25.267451+00:00'
page_id: '423938090'
product: rm
source: tdn-rm
title: Gerar Acertos e Encerrar o Inventário
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938090
version: 3
---

A partir da visão de inventários, pode-se encerrar o Inventário e realizar a geração dos movimentos de acerto de acordo com o quantidade calculada do campo "Diferença Apurada" de cada [Item do Inventário](http://tdn.totvs.com/pages/viewpage.action?pageId=423937977), após a execução do processo [Apurar Diferença do Inventário](http://tdn.totvs.com/pages/viewpage.action?pageId=423938270).

O Inventário somente é fechado após gerados todos movimentos de acerto necessários para produtos que estejam com a opção "Gerar Acerto" marcada.

O processo de Geração de Acertos e Encerramento de Inventário gera os movimentos  de acertos das quantidades dos itens inventariados, gerando movimentações de ajustes positivos e negativos (conforme tipos de movimentos parametrizados em [Gestão de Estoque | Inventário | Inventário | Definições de Inventário | Tipo de Movimento de Acerto de Entrada/Saída](http://tdn.totvs.com/pages/viewpage.action?pageId=423938132), e encerra o inventário em seguida.

O processo de Geração de Acertos e Encerramento gera as movimentações para os produtos presentes no inventário de acordo com a unidade de controle padrão do produto.

Atenção:

O sistema verifica se a data da última geração de saldos e custo do produto é igual ou menor que a data base do inventário, caso seja menor será exigido que seja regerado saldo e custos do produto.
