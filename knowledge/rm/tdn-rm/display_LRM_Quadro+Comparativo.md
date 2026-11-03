---
content_hash: 22ceaed5775f6d5be66513c84a084b1fe5ee05ce272cf53ef8d0566759176e0a
fetched_at: '2026-06-29T00:10:57.868134+00:00'
page_id: '600295739'
product: rm
source: tdn-rm
title: Quadro Comparativo
type: documentation
url: https://tdn.totvs.com/display/LRM/Quadro+Comparativo
version: 28
---

Para geração do Quadro Comparativo, para acessá-lo, basta clicar no ícone destacado abaixo:

Vale ressaltar que é necessário clicar na botão Calcular, para que o sistema realize os cálculos e defina quem foi o vencedor da cotação.

**Ações possíveis a serem realizadas no Quadro:**

  Imprimir o Quadro Comparativo de Preços a partir de relatórios criados no RM Reports.

Enviar o Quadro Comparativo via E-mail utilizando relatórios criados no RM Reports.

Gerar dados do Quadro Comparativo para uma planilha baseado em um modelo predefino.

Gerar Ordem de Compra diretamente pela tela.

Exportar os dados para o MS Excel.

Realizar Interferência por fornecedor.

Registrar Justificativa para Fornecedor Não Qualificado.

**Informações visualizadas no Quadro**

Totalizadores

* **Valor Total:** Valor de todos produtos disponíveis para aquele fornecedor.
* **Frete:** Valor de Frete total dos produtos para aquele fornecedor.

Produto

* **Quantidade Solicitada**: Quantidade solicitada do produto na ordem de compras.
* **Preço Orçado**: Valor orçado do produto, (*passou a ser exibido após Out/2025*).
* **Preço****Negociado**:  Valor final do produto.
* **Preço Total Bruto:** Valor total multiplicando quantidade x preço de cada item.
* **Data de****Entrega**:  Data de entrega do produto no orçamento.

Paginação

* Os botões de paginação permitem a visualização de mais fornecedores.

**Visualizando Ganhadores da Cotação**

Ao gerar o quadro comparativo de cotação é calculado qual a Melhor Oferta, para a exibição é considerado o Parâmetro "Usar Tipo de julgamento da Melhor Oferta", com ele marcado é possível definir o Tipo de Julgamento, sendo eles:

Melhor Oferta Global - Na melhor oferta Global é possível identificar o Fornecedor vencedor da cotação ou os Fornecedores Empatados.

Fornecedor Vencedor:

Fornecedores Empatados com vencedor:

Fornecedores Empatados sem Vencedor:

Melhor Oferta Por Produto - Na Melhor oferta por Produto é possível visualizar os produtos que estão empatados e quais venceram

Produtos Vencedores:

Produtos Empatados:

\* Caso o Parâmetro "Usar Tipo de julgamento da Melhor Oferta" não esteja marcado será exibido a tela de melhor oferta por produto.

**Coluna Melhor Oferta**

O objetivo principal do comprador é otimizar as solicitações de compras internas e reduzir custos, conciliando Melhor Preço e Melhor Prazo de Entrega. Com este objetivo, foi adicionada uma nova coluna no quadro, a qual oferece para o comprador informações prontas e rápidas para facilitar a análise e negociação com os Fornecedores.

Esta coluna contém os dados referentes a melhor oferta. Nela serão exibidos por produto e de forma imparcial, o menor preço e a menor data de entrega informados pelos fornecedores.

**Importante:**1) Esta coluna estará sempre fixa na primeira posição da grid, facilitando a análise durante a navegação entre as páginas do quadro comparativo.

2) O valor total desta coluna é calculado da seguinte forma: Quantidade Negociada \* Preço Negociado, ou seja, não serão considerados rateios de desconto, despesa ou qualquer valor de tributação.

**Legenda de cores nos itens no Quadro Comparativo**

Quando um item do Quadro Comparativo já teve um pedido gerado, o mesmo será sinalizado com cores para determinar o atual status do mesmo. 

Verde - Item com pedido gerado total;

Amarelo- Item com pedido gerado parcial;

Vermelho- Item sem pedido gerado total;

 

Caso não exista nenhum pedido gerado para a cotação ou o itme não esteja cotado, nenhuma cor será informada. 

**Detalhes do produto**

Ao clicar no ícone  será aberta a tela de detalhes do produto para os fornecedores apresentados no quadro.

Assim como no quadro comparativo, caso exista um fornecedor vencedor da cotação, o mesmo estará fixo na primeira coluna, independente da página acessada.

**Log do Cálculo**

Após o cálculo do Quadro, seu log pode ser visualizado ao clicar no botão à esquerda do "OK", localizado no canto inferior direito.

Uma vez aberta, a tela terá essa configuração.

\*Nessa tela é possível ver um detalhamento dos cálculos realizados.

1) Filtros:

* Visualizar: filtro pré-estabelecido destinado à exibir Todos os Registros, Apenas os **Vencedores** ou Apenas os **Empatados**;
* Pesquisar: pode-se escolher um campo que será utilizado em conjunto com a barra de pesquisa (Código do Fornecedor, Nome do Produto, etc.).

2) Árvore de Entidades:

* Nesta árvore serão dispostos todos os Fornecedores participantes da cotação e seus respectivos itens. Ao clicar sobre o Fornecedor, o painel ao lado (Memória de Cálculo) exibirá seus detalhes e de todos seus itens. Clicar sobre um item específico trará apenas suas próprias informações.

3) Memória de Cálculo:

* Neste painel serão exibidos os cálculos de todos os campos envolvidos no processo da cotação, de acordo com a parametrização e o cenário de cada uma.

800600
