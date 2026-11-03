---
content_hash: bed751d29414e69c9dabb9b3631da75cadfee3cb96e0bc1e736fe229d83cc3a0
fetched_at: '2026-06-29T00:11:32.772515+00:00'
page_id: '748072981'
product: rm
source: tdn-rm
title: Relatórios - Disponibilidade e Velocidade de Venda de Imóveis - Smart View
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=748072981
version: 9
---

## **Introdução**

---

O relatório de **Disponibilidade e Velocidade de Venda de Imóveis**, inclui a quantidade de imóveis disponíveis, valor dos imóveis disponíveis e a velocidade de vendas do empreendimento.   
  
As informações podem ser filtradas por coligada e empreendimento, e são baseadas em pré-requisitos como a existência de uma data de lançamento do empreendimento preenchida e a associação das subunidades a uma tabela de preço principal e situação efetivada.

Importante!

Para ter acesso a este relatório, é preciso que o Perfil do usuário tenha acesso à opção: *[01.01.01] - Contratos de Venda*, sem necessidade de ter acesso às demais tarefas abaixo desta.

## **Procedimentos para utilização**

---

Ao utilizar este relatório no Smart View, é possível aplicar os seguintes Parâmetros de Visualização:

**Coligada:** Neste agrupador o sistema apresenta o Código da [Coligada](https://tdn.totvs.com/display/LRM/Coligada) e a sua Descrição no sub cabeçalho deste relatório.

Esta informação pode ser filtrada através do Parâmetro de Visualização *Cód Coligada*, onde o valor *-1*, que é o valor padrão/default, processa todas as coligadas e caso o usuário queira filtrar uma ou mais coligadas específicas, pode-se realizar esta ação alterando este valor e/ou acrescentando as demais coligadas, através do botão "+" localizado em frente à descrição do mesmo;

* **Empreendimento:** Nesta coluna é apresentado o Código do [Empreendimento](https://tdn.totvs.com/pages/viewpage.action?pageId=435105154) e o seu Nome de Fantasia.

Nos Parâmetros de Visualização, o sistema trás por padrão o valor *-1*, que processa todos os empreendimentos e como ocorre com o parâmetro da entidade acima, caso o usuário tenha necessidade, pode-se filtrar um ou mais empreendimentos específicos através dos botões destinados a este fim;

* Quantidade de **Imóveis Disponíveis**: Nesta coluna são apresentadas a quantidade de [subunidades](https://tdn.totvs.com/display/LRM/Unidade+-+Anexos+-+Subunidade) disponíveis para venda em cada empreendimento. ou seja, as subunidades com [situação](https://tdn.totvs.com/pages/viewpage.action?pageId=435105411) igual a *100 - Disponível para Venda*;
* **Valor dos Imóveis Disponíveis:** Nesta  coluna é apresentado a soma dos valores de todas as subunidades disponíveis para venda, com base na Tabela de Preço Principal aplicada a elas;
* **Velocidade de Vendas:** Nesta coluna o sistema apresenta o número de subunidades vendidas em 1 mês, ou seja subunidades vendidas por mês.

Esta informação é obtida através do Número de Subunidades Vendidas, que são as subunidades com situação *900 - Vendido*, dividido pela quantidade de meses compreendida desde a Data de Lançamento do Empreendimento, até a data de geração deste relatório. ou seja:

*Velocidade de Vendas do Empreendimento = Número de Subunidades Vendidas / Tempo Total das Vendas em Meses*, onde

*Número de Subunidades Vendidas:* É a soma das subunidades com situação igual a 900 - Vendido;

*Tempo Total das Vendas em Meses:* É a data de emissão do relatório - Data Lançamento Empreendimento

Desta forma, são pré-requisitos para este relatório:

* O campo *Data de Lançamento* do [Empreendimento](https://tdn.totvs.com/pages/viewpage.action?pageId=435105154) esteja preenchido;
* As subunidades devem estar associadas a uma [Tabela de Preço](https://tdn.totvs.com/pages/viewpage.action?pageId=435105236) do tipo Principal e em situação Efetivada.
