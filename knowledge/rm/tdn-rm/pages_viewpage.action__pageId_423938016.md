---
content_hash: 4c7b675301db48dfdf3cde5c55ee813bd2eb3b721d957f0d7c3426031e2a4e38
fetched_at: '2026-06-29T00:09:24.788959+00:00'
page_id: '423938016'
product: rm
source: tdn-rm
title: Importação de Cotação WEB
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938016
version: 7
---

O processo de Importação de Cotação tem como objetivo atualizar as tabelas do TOTVS Gestão de Estoque, Compras e Faturamento com as informações dos orçamentos dos fornecedores que foram inseridas no portal web, agilizando e facilitando o processo de cotação de produtos de uma Solicitação de Compra.  
   
**Data de Entrega**

No portal,tela Principal está disponível o campo Data da Cotação que não poderá ser alterado.   
Os campos Data de Entrega e Prazo de Entrega estão disponíveis  tanto na tela de Principal como no Item de Orçamento.  
Ao informar um valor para o campo Prazo de Entrega, a Data de Entrega será calculada de acordo com a Data da Cotação, exemplo:

Data da Cotação: 10/06/2016  
Prazo de Entrega: 5 dias  
Data de Entrega: 15/06/2016

Caso o usuário opte por informar a Data de Entrega, o campo Prazo de Entrega será preenchido com "-1".

**Produto Indisponível**

Na tela de Item de Orçamento, existe um campo do tipo checkbox para marcar o Produto Indisponível. Este campo será importado com status Indisponível.  
**Marca**: Quando o parâmetro Usar Marca de Produto na Cotação estiver habilitado, será exibido o campo Marca no Portal Web.  
Este campo exibirá a marca informada no item de solicitação de compras e não poderá ser editado.  
Para efetuar a importação de cotação web acesse: **BackOffice | Gestão de Estoque, Compras e Faturamento | Compras | Cotação | Processos | Importação de Cotação Web.**  
No assistente de Importação de Cotação Web selecione uma das opções de importação:

1. Importação pela Data Limite de Resposta: Consiste em importar todas aquelas cotações que já ultrapassaram a data limite de resposta.
2. Importação por Cotações orçadas e Data Limite de Resposta: Consiste em importar todas as cotações que já foram sinalizadas pelo fornecedor como "orçadas" e as que se encontram na situação do item 1.
3. Cotações Selecionadas (Que atendem as regras para importação): as cotações marcadas na visão serão importadas, nessa modalidade de importação não é verificado "Data Limite Resposta" ou "Cotação Orçada", as ordens escolhidas serão importadas se houver dados a importar. Quando utilizada a opção "Cotações Selecionadas" é exibida uma etapa mostrando uma lista com as cotações que serão importadas, nessa tela é exibida a caixa de checagem "Aceita importar cotações selecionadas?" é necessário marcar essa caixa para que o botão "Avançar" seja habilitado e se possa prosseguir com a importação das cotações selecionadas.

Este processo irá importar todas as informações inseridas pelos fornecedores que utilizaram o Portal Web para efetuar as cotações. As tabelas do módulo de Compras serão atualizadas com as informações e as tabelas Web serão limpas, para que não acumule informações desnecessárias.  
As informações importadas poderão ser visualizadas no Orçamento: Duplo clique na cotação, aba Orçamentos, duplo clique no Fornecedor desejado, aba Produtos.

**Observação**:

A Importação de Cotação WEB deixa de ser utilizada para as novas cotações exportadas para WEB na versão 12.1.34, atualizações e melhorias no portal registram os dados diretamente na cotação dispensando essa etapa, tornando o processo mais simples e ágil.

[Importação de Cotacao WEB](http://tdn.totvs.com/display/LRM/CMP_BT_Importacao_de_Cotacao+Web_BRA_PCREQ-2231?preview=/185734032/185664610/CMP_BT_Importacao_de_Cotacao%20Web_BRA_PCREQ-2231.pdf)
