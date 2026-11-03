---
content_hash: 240499e80be93a6fd5d8caff7f7f9c1ab073108014b038da26fd4b1e346583f9
fetched_at: '2026-06-29T00:09:25.281528+00:00'
page_id: '423938100'
product: rm
source: tdn-rm
title: Exportação de Dados (Parceiro)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938100
version: 10
---

A Exportação de Dados consiste na geração de dados previamente configurados através do [esquema de exportação](http://tdn.totvs.com/pages/viewpage.action?pageId=423938099). As informações geradas variam de acordo com o layout do parceiro, seja Elbrus ou SpressCom, e podem incluir dados sobre produtos, estoque, clientes, fornecedores, entre outros.

Importante

1. Para acessar este processo, é necessário conceder a permissão por meio do perfil do usuário.
2. A Exportação de Esquemas é agrupada em lotes e sempre será executada em função destes. Ou seja, quando um lote for executado, todos os esquemas do lote serão processados e gerados de acordo com o Nome do Arquivo, Layout e Filtro. O Log é gerado no mesmo diretório do RM com o nome "ExportacaoParceiro.txt".
3. O recurso de Exportação de Dados também pode ser executado por meio do TOTVS Integração, acessando o menu Gerador de Saídas | Layouts | [Geração de Saídas](http://tdn.totvs.com/pages/viewpage.action?pageId=237383341). Para isso, os layouts dos parceiros Elbrus e SpressCom devem ser previamente importados pelo caminho Gerador de Saídas | Layouts | Importar layouts.

***Atenção!*** No caso da importação, o processo é realizado pelo módulo Integração | Conceito. E para a exportação pelo módulo Integração | Gerador de Saídas para as exportações.

Tabelas Utilizadas: **TLOTEESQUEMA** e **TESQUEMA**

Observações

O processo acima não funciona em ambiente multi-tenant.
