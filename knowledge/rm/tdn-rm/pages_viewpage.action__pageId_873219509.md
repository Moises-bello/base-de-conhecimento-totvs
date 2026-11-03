---
content_hash: 8a19d2450ff505a6cc125aa33246c66592519d2da4804a79a6aafab723346d0a
fetched_at: '2026-06-29T00:11:56.986718+00:00'
page_id: '873219509'
product: rm
source: tdn-rm
title: Restauração de Banco - Variáveis de Ambiente
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=873219509
version: 6
---

## **Restauração de Banco**

A lista a seguir apresenta os campos da atividade que podem ser substituídos por variáveis de ambiente:

1. Caminho do arquivo de backup para SQL Server
2. Nome do PDB de origem a ser clonado para Oracle

Exemplo de Uso

## **Exemplo de Uso**

Na imagem abaixo, pode ser observado um exemplo de criação de ambiente para substituir o parâmetro listados acima em qualquer atividade de Restauração de Banco:

Criação de uma atividade utilizando as variáveis de ambiente definidas anteriormente:

Assim, ao executar a atividade, você poderá selecionar o ambiente desejado e o parâmetro de versão será automaticamente substituído pela versão correspondente ao ambiente escolhido.
