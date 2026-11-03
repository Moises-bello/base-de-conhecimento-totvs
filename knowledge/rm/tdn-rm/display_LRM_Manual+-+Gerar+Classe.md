---
content_hash: b350e0e88d2afdc7b69d8eef945b69b9e5ac03e2b5dc618b8877dbc6f2a29de6
fetched_at: '2026-06-29T00:08:47.200574+00:00'
page_id: '319787263'
product: rm
source: tdn-rm
title: Manual - Gerar Classe
type: documentation
url: https://tdn.totvs.com/display/LRM/Manual+-+Gerar+Classe
version: 3
---

Esta opção irá gerar o código fonte para execução do Layout, ela é utilizada para encontrar possíveis erros em expressões de filtro e campo, e para diagnóstico de problemas na geração.

![](/download/attachments/319787263/gerar_classe.png?version=1&modificationDate=1512921813000&api=v2)

1Lista de Erros

A lista de erros é exibida caso o Layout possua algum erro de compilação. Clique duas vezes no erro para ir para a posição do código correspondente ao erro. Você pode avaliar o código gerado para identificar qual foi a expressão que causou o erro e fazer os ajustes necessários para a compilação correta.

2Código do Layout

Exibe o código gerado para execução do Layout. O código está em linguagem C# e é gerado automaticamente de acordo com a estrutura do Layout, seus registros, contextos e expressões.

3Fechar

Clique para fechar a janela.

Observação

Normalmente os erros são causados por expressões inválidas ou por problemas nas ligações dos registros, como por exemplo um registro que está associado a uma ligação, que não é filha de uma ligação do registro pai.
