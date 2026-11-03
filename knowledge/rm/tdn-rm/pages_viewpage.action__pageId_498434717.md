---
content_hash: 0215ea9eb9cea7a51911437a462249c0163290211b9621d2a6d0502139eb1997
fetched_at: '2026-06-29T00:10:22.637291+00:00'
page_id: '498434717'
product: rm
source: tdn-rm
title: Importar Insumos de Suprimentos/Faturamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=498434717
version: 2
---

---

Na elaboração de um Orçamento em consequência do início de um Projeto, podemos elaborar a base de insumos de diferentes fontes de informações, ORCECERTO, Importação de Planilhas ou a partir da Importação de Insumos de Suprimentos/Faturamento.

A melhor fonte de informação será definida conforme as características do Projeto (Construção Civil ou Construção Pesada e Outros) onde também poderá ser utilizada uma mescla de diferentes fontes de informação, sendo sugerido a criação de um Projeto Modelo para receber as informações. Uma boa base de dados de insumos modelo é a garantia de que seus orçamentos serão cada vez mais assertivos.

O processo de Importação de Insumos (Produtos) consiste em realizar a criação de Insumos através de Produtos cadastrados no Suprimentos/Faturamento.

As seguintes opções de filtro estão disponíveis:

* **Por Faixa de Produto -** Será filtrado de um Produto Inicial até o Produto Final
* **Por Classificação -** O filtro será aplicado de acordo com as Tabelas de Classificação, que são configuradas no TOTVS Gestão de Estoque, Compras e Faturamento, por exemplo:
  + **Tabela 1 = Tipo**: por exemplo, Acessórios, Serviços, Veículos;
  + **Tabela 2 = Classe**: por exemplo, Produto de Classe A, Produto de Classe B;
  + **Tabela 3 = Status do Produto**: por exemplo, Produto Normal, Produto em Promoção ou Produto para Oferta;
  + **Tabela 4**;
  + **Tabela 5**.
* **Por faixa do código no fabricante:** Possibilita filtrar por uma determinada faixa de produto de determinado fabricante, informando um Número do produto no fabricante (Inicial) até o Número do produto no fabricante (Final).

As seguintes opções de parametrizações estão disponíveis:

**Tipos a serem importados**

* Todos;
* Produto;
* Serviço.

**Preço a ser Ativado**

* Preço à Vista;
* Preço à Prazo;
* Preço Promoção;
* Preço em Dólar;
* Preço em Oferta;
* Custo Médio;
* Custo Unitário.

**Observação:** Para a utilização destes campos, eles devem estar habilitados nos parâmetros do Gestão de Estoque, Compras e Faturamento.

**Criar descrição a partir**

* Do nome fantasia;
* Da descrição;
* Da descrição auxiliar.

**Criar o código a partir**

* Do código do produto;
* Do número do produto fabricante.

**Criar descrição completa a partir**

* Do nome fantasia;
* Da descrição;
* Da descrição auxiliar.

Opções:

* Importar produtos inativos;
* Relacionar insumos a produtos
* Importar somente preço a ser ativado;
* Ignorar Custos (Médio e Unitário);
* Importar Custos por Filial.

**Para realizar a importação, siga as instruções abaixo:**

1. Acesse o processo em "Menu Projeto | Importações | Importar Insumos de Suprimentos/Faturamento";
2. Selecionar o Filtro e parametrizações dos produtos a serem importados, podendo ser Por Faixa de Produto, Por Classificação ou Por faixa do código no fabricante;
3. Marcar uma opção em “Tipos a serem importados”;
4. Marcar uma opção em “Criar descrição a partir”;
5. Marcar uma opção em “Criar o código a partir”;
6. Marcar a opção “Criar descrição completa a partir”;
7. Marcar uma opção em “Preço a ser ativado”;
8. Informar o Grupo de Custo;
9. Selecionar as opções de Parametrização;
10. "Executar" o processo. Após estes passos será gerada a mensagem de log.

**Importante:**

* Caso o código não esteja de acordo com a Máscara Parametrizada, será aberto uma tela para realizar o ajuste;

* Para casos onde ocorrer erros durante a importação será registrado um Log, informando quais Insumos não foram importados.
