---
content_hash: e016df53123f914d2c2b120acad0479614d1d3d0d38d726cabaee8882e5c1d8f
fetched_at: '2026-06-29T00:09:47.646728+00:00'
page_id: '435105035'
product: rm
source: tdn-rm
title: Anexo- Preço do Apartamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435105035
version: 38
---

**Introdução**

---

O anexo Preço da Subunidade (Apartamento) é responsável por atribuir o preço de venda de uma subunidade de uma unidade de um empreendimento.

Através do anexo é possível inserir o preço de uma subunidade por vez.

Caso deseje gerar de diversas subunidades simultaneamente execute o processo Gerar Preço.

**Pré-Condições:**

1. Ter incluído uma Tabela de preços com a situação "em Preparação".
2. Ter incluído um Bloco e seus apartamentos no Empreendimento da Tabela de Preços.

**Incluindo Preço de Subunidade**

---

1. Selecione a Tabela de preços que atenda a pré-condição acima.
2. Acesse: Anexos / Preço Apartamento.
3. O sistema exibira a tela de filtros. Se não deseja incluir um filtro ou se a tabela de preços não tiver preço gerado para suas subunidades, clique em **Fechar**.
4. Se Houver Preço gerado para alguma subunidade da tabela de preços, eles serão exibidos. Clique em **Incluir**
5. Será exibido o formulário de cadastro de preço para as subunidades. Preencha os campos e clique em **Salvar**.

Os campos exibidos no formulário são:

* + **Nº Tabela de Preço**: Número da tabela de preços. Preenchido automaticamente com dados da Tabela de Preços.
  + **Empreendimento**: Código do empreendimento da Tabela de Preços. Preenchido automaticamente com dados da Tabela de Preços.
  + **Unidade (Bloco)**: Código da unidade do Empreendimento.
  + **Subunidade (Apartamento)**: Código da subunidade das unidades do Empreendimento.
  + **Preço da Subunidade (Apartamento)**: Preço de venda de uma subunidade.
  + **Histórico**: Aba que registra todas as ações feitas na subunidade.

Após o procedimento acima, o sistema insere o preço para a subunidade, com a coluna **Situação da Subunidade** "Ativa". Para visualizar realize a filtragem das colunas da tela.

**Valores de comissão sobre o preço da sub unidade.**

---

Para atender uma demanda do mercado sobre as comissões recebidas pelas vendas das sub unidades, foram criados novos campos para realizar este cálculo e obter essas informações. Inicialmente o TCGI tratará apenas de forma informativa o valor da comissão, sendo ela a comissão interna (paga pela empresa).

A integração com o Portal de Imóveis tratará de forma mais abrangente a distribuição da comissão paga pelos clientes (Compradores).

Aba Identificação:

* **Código da Fórmula**: Para o cálculo da comissão será possível inserir fórmulas, dessa forma será possível criar inclusive faixas de preço, utilizar metadados para realizar o cálculo e  condições para ter a comissão de acordo com a necessidade do negócio.
* **% da Comissão**: De uma forma mais simples é possível digitar apenas um percentual para o cálculo da comissão. Esse valor será multiplicado pelo valor do imóvel na tabela de preço, dessa forma será gerado o valor venal desta subunidade.
* **Valor de Comissão**: Assim como o percentual, é possível digitar diretamente o valor da comissão para a subunidade, esse valor também será calculado para encontrar o valor venal da sub unidade.
* **Valor Venal**: Este é o valor total da subunidade somada a comissão. É um campo que pode ser informado diretamente, ou calculado pelo valor da sub unidade mais o valor do percentual informado, ou o valor de comissão digitado, ou pelo valor gerado pela fórmula.

Observações

Todas as alterações dos campos acima criarão um registro no histórico do preço da subunidade. Outro ponto importante é que esses valores podem ser alterados mesmo com a tabela de preço efetivada. Os processos de gerar preço, reajustar tabela de preço e reajuste Multi-coligada também oferecerão a possibilidade de alterar esses campos.
