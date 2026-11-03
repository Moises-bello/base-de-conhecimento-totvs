---
content_hash: 5416d3b9c7656d16093aed0422b0fb094708860e210ba2befc3953ee31a885c5
fetched_at: '2026-06-29T00:09:24.736210+00:00'
page_id: '423938012'
product: rm
source: tdn-rm
title: Importação de dados via XML - Ponto de Venda
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938012
version: 4
---

O processo de Importação de Dados via XML para o Ponto de Venda, importa os dados respeitando os layouts das Tabelas do Movimento (TMOV) e suas Tabelas Filhas, como: Item de Movimento, Item de Lote, Número de Série, Financeiro e Cupom Fiscal, que por sua vez, possui também, tabelas Filhas, como: Item de Cupom Fiscal e Pagamento do Cupom Fiscal, Escrituração (TREDUCAOZ) e a Tabela Filha de Item de Escrituração e a Tabela de Cliente/Fornecedor (FCFO).  
Para efetuar a importação de dados via XML, devem ser seguidos os passos abaixo:

1. Importar o arquivo de Conceito que é responsável pela importação disponível no módulo de Integração;
2. Executar no menu a Importação de dados via XML;
3. Selecionar o Conceito importado no item anterior;
4. Na aba de seleção de Ponto de Venda é necessário para:
   1. Ao selecionar o Ponto de Venda, o sistema recupera o Diretório de Saída e importa os arquivos "TFRETORNO\*.xml";
   2. Caso não seja selecionado o Ponto de Venda o processo irá recuperar todos os Ponto de Venda que estão com a opção de Importação Automática marcada no seu respectivo cadastro.
5. A ultima etapa é de Execução ou Agendamento de Jobs, caso queira, colocar o processo para retornar em determinado momento.

O Conceito disponibilizado pela TOTVS está configurado para recuperar os arquivos através de Diretórios, conforme supracitado. Caso o usuário queira informar um arquivo especifico na execução do Processo será necessário Exportar o Conceito original e importar e em seguida alterar a Conexão de Origem do conceito para buscar arquivos através de Parâmetros.

Atenção

No caso da importação, o processo é realizado pelo módulo Integração | Conceito. E para a exportação pelo módulo Integração | Gerador de Saídas para as exportações.

Este processo não ainda não está disponível para uso em ambiente Multi Tenant.

Informações Adicionais

* [Ponto de Venda](http://tdn.totvs.com/display/LRM/Ponto+de+Venda)
* [Cupom Fiscal](http://tdn.totvs.com/display/LRM/Cupom+Fiscal)
* [Tributação Cupom Fiscal](http://tdn.totvs.com/pages/viewpage.action?pageId=423938773)
* [Redução Z](http://tdn.totvs.com/pages/viewpage.action?pageId=423938855)
