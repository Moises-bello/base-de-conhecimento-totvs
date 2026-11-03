---
content_hash: d8dc45272de7c7f21ac4a3f57eeebecb4b9c8b000ced8588a838eaeb5f91b056
fetched_at: '2026-06-29T00:09:50.651631+00:00'
page_id: '435105507'
product: rm
source: tdn-rm
title: Relatórios - Ficha Financeira do Locatário
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435105507
version: 14
---

# Procedimentos para utilização

---

Este relatório é um objeto gerencial criado para exibir os lançamentos financeiros de uma determinada competência informada pelo usuário.

Para utilizar este relatório é necessário importar o Objeto Gerencial 'TCGIRELALG0071 - Ficha Financeira do Locatário.TotvsReport' através de Gestão / RM Reports / Processo de Importar Estrutura de Relatório.

O relatório estará disponível na pasta de Objetos Gerenciais da instalação do RM.

Após a importação deste relatório, basta então acessar Aluguel / Relatórios / Ficha Financeira, e  selecionar o relatório TCGIRELALG0071 - Ficha Financeira do Locatário. O sistema dará a opção de três filtros que levam em consideração sempre a coligada corrente. São eles:

* **Contratos**: Permite listar os lançamentos financeiros associados a um contrato;
* **Locador**: Permite listar os lançamentos financeiros associados a um locador;
* **Locatário**: Permite listar os lançamentos financeiros associados a um locatário.

Após selecionar um filtro e avançar, o relatório será gerado e dividido em 6 grupos, sempre agrupados para o contrato em questão, que trarão informações sobre:

* **Grupo 1**: Dados do contrato de locação;
* **Grupo 2**: Dados dos imóveis do contrato;

Importante

Caso o locatário seja Pessoa Jurídica, o relatório apresentará um subgrupo "Contato(s)", que mostrará os dados de contato deste cliente. Este cadastro pode ser acessado no Módulo Financeiro, na edição de cadastros de Clientes / Fornecedores, opção "Contatos do Cli/For".

Para lançamentos que foram baixados via [**processo de Acordo**](https://tdn.totvs.com/display/LRM/FIN+-+Acordo), o relatório não irá sumarizar os valores baixados destes lançamentos. Além disso, estes lançamentos serão exibidos como "**Acordo**", ao invés de "Baixa".

* **Grupo 3**: Dados das áreas dos imóveis;
* **Grupo 4**: Dados dos fiadores/garantias;
* **Grupo 5**: Resumo com totalizadores dos lançamentos e baixas;
* **Grupo 6**: Resumo com totalizadores dos valores de composição;
* **Grupo 7**: Detalhamento dos lançamentos existentes, com informações de seus valores de composição e também das baixas.

Entre os lançamentos estarão sendo exibidas informações de cobrança de locação, Eventos Financeiros avulsos, Despesas avulsas dos imóveis do contrato e Seguros.

Atenção

A partir da versão 12.1.2302, algumas melhorias foram realizadas para o relatório exibir mais informações do contrato de locação, tais como a integração com condomínio (lançamentos, CRD, cobranças fixas de orçamento), reajustes, fundos promocionais e aditivos.
