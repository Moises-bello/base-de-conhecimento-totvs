---
content_hash: 08563b3c4e9a610d9284c2cd8b2efe408a86fca83405d38a7cc365d15af73dd0
fetched_at: '2026-06-29T00:11:32.381623+00:00'
page_id: '747314339'
product: rm
source: tdn-rm
title: Objeto de Negócio - EFD-REINF (Bloco 40)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=747314339
version: 34
---

# Conteúdo

Conteúdo

# 1. Visão Geral

O objeto de negócio da EFD-REINF permite que os dados dos lançamentos que compõem os registros da REINF sejam disponibilizados para visualização na ferramenta "Smart View", independentemente dos eventos já terem sido gerados ou não.

* R-4010
* R-4020
* R-4080

# 2. Exemplos do ON EFD-REINF

## 2.1 Visão de Dados

A visão de dados permite uma visualização mais detalhada e extensa de cada informação.  
No exemplo abaixo, ao vincular o objeto de negócio da EFD-REINF a uma visão de dados, foram filtradas as informações referentes a coliga, filial e data mensal.

Exemplo de visão de dados

## 2.2 Tabela Dinâmica

É possível ter várias perspectivas diferentes sobre suas informações ao vincular o objeto de negócio da EFD-REINF à uma tabela dinâmica.  
Neste exemplo, foram realizados agrupamentos por Filial e Valor Dedução para obter a sumarização de seus totais.

Exemplo de tabela dinâmica

# 3. Campos do objeto de negócio

Atualmente, são disponibilizados os seguintes campos referentes aos lançamentos no objeto de negócio:

Tabela de campos

| Nome | Tipo |
| --- | --- |
| Código da coligada | Literal |
| Código da filial | Literal |
| Data Inicial | Data |
| Data Final | Data |
| Id Lançamento Financeiro | Literal |
| Id Lançamento Fiscal | Literal |
| Id Baixa | Literal |
| Período Apuração | Literal |
| Natureza Rendimento | Literal |
| Data Fator Gerador | Data |
| Valor Original (Financeiro) | Decimal |
| Valor Total (Fiscal) | Decimal |
| Valor Base IR | Decimal |
| Valor IR | Decimal |
| Série | Literal |
| Número Documento | Literal |
| Código Cli/For | Literal |
| Data Emissão | Data |
| Tipo Evento | Literal |
| Id Processo Judicial | Literal |
| Tipo Dedução | Literal |
| Valor INSS Empregado | Decimal |
| Valor Dedução | Decimal |
| Tipo Isenção | Literal |
| Valor Isenção | Decimal |
| Valor da base de cálculo do IRRFPJ | Decimal |
| Valor do IRRFPJ | Decimal |
| Valor da base de retenção de tributos de forma agregada | Decimal |
| Valor da retenção em valor agregado | Decimal |
| Valor da base de cálculo CSLL | Decimal |
| Valor CSLL | Decimal |
| Valor da base de cálculo Cofins | Decimal |
| Valor da retenção relativa a Cofins | Decimal |
| Valor da base do PIS/PASEP | Decimal |
| Valor da retenção do PIS/PASEP | Decimal |
| Rendimento Isento/Não Tributável | Lógico |

# 4. Permissões

Para conseguir visualizar o objeto de negócio da EFD-REINF no Smart View, ou para importar os objetos disponibilizados no TOTVS Compartilhamento, é necessário que o usuário tenha permissão de acesso na EFD-REINF

Imagem

# 5. Outras Informações

O objeto de negócio da EFD-REINF requer quatro parâmetros para selecionar os lançamentos, sendo eles:

* Código da Coligada
* Código da Filial
* Data Inicial do período desejado
* Data Final do período desejado

As datas inicial e final não precisam ser exatamente as mesmas informadas no cadastro do parâmetro de processo. Caso seja informado um intervalo que abrange dois ou mais parâmetros de processos, o relatório irá considerar todos os parâmetros cadastrados naquele intervalo e, consequentemente, todos os lançamentos que se aplicarem para o(s) devido(s) evento(s) da REINF.

Parâmetros de visualização

Após gerar o relatório, é possível exportar o resultado para PDF. Basta clicar no botão de imprimir.

Imprimir relatório em PDF

Para exportar a tabela dinâmica ou visão de dados em ".xlsx", basta clicar no ícone.

Exportar em xlsx

Ainda que o relatório possa ser gerado antes de se enviar os eventos do bloco 40, é importante relembrar da necessidade de que os **parâmetros de processo da EFD-REINF** sejam criados conforme o período desejado, assim como já é parametrizado para a geração da EFD-REINF. Caso essa parametrização já tenha sido feita, não há necessidade de realizá-la novamente.  
Para mais informações, acesse "[Parâmetros de Processo - EFD-REINF](https://tdn.totvs.com/pages/viewpage.action?pageId=490650588#Par%C3%A2metrosdeProcessos-EFDReinf)". É a partir dessa parametrização que o objeto de negócio conseguirá filtrar os lançamentos considerados na geração da rotina, assim como já é feito com a própria geração dos eventos.

Smart View

Para informações de instalação, configuração e uso dessa ferramenta, acesse a documentação clicando [aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=626926739).

Filtro do objeto de negócio

Não há filtros disponíveis diretamente no objeto de negócio. Os dados devem ser filtrados no tipo de visão escolhida para exibição dos dados.

Atualmente, não há um relatório padrão da EFD-REINF do produto TOTVS Gestão Fiscal; porém tabelas dinâmicas e uma visão de dados são disponibilizadas à partir do TOTVS Compartilhamento.  
A criação dos relatórios é flexível e poderá ser realizada de acordo com as necessidades especificas utilizando o ON da EFD-REINF.

---
