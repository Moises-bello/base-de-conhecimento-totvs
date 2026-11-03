---
article_id: 360022837272
category: Escrita Fiscal - CIAP
content_hash: e861f62230a847eb8822da646b7d80c16ef2f6a52e5086bcd0bf0604ff40ef75
fetched_at: '2026-06-28T22:39:33.882743+00:00'
product: protheus
section_id: 1500001538561
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Composição do valor
  total de saídas tributadas (FA_TOTTRIB) e de todas as saídas (FA_TOTSAI) no CIAP
type: support-article
updated_at: '2021-07-29T12:56:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022837272-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Composi%C3%A7%C3%A3o-do-valor-total-de-sa%C3%ADdas-tributadas-FA-TOTTRIB-e-de-todas-as-sa%C3%ADdas-FA-TOTSAI-no-CIAP
---

**Dúvida**

Como o sistema compõe o Valor total de saídas tributadas ( FA\_TOTTRIB) e de todas as saídas ( FA\_TOTSAI) no CIAP?

**Ambiente**Protheus – Livros Fiscais– A partir da versão 11.80  
  
**Solução**

**Cálculo interno do Protheus para chegar ao valor das colunas “Total das Saídas Tributadas” e “Total das Saídas” no Livro CIAP**

**Filtro de notas fiscais:**

1) A movimentação utilizada na emissão do Livro CIAP baseia-se em um filtro na tabela SD2 (Itens do documento de Saída) pela **Data de emissão (D2\_EMISSAO)** de todas as notas fiscais que NÃO sejam de Complemento de ICMS **(D2\_TIPO=”I”)**;

2) Por padrão, junto com o filtro anterior, dependendo do parâmetro**MV\_P3CIAP** temos que considerar/desconsiderar os itens que estão em poder de terceiros **(F4\_PODER3=”S”)**. Se este parâmetro (**MV\_P3CIAP**) estiver como **T – True**, estas movimentações deverão ser consideradas, caso contrário (**F – Falso**) deverão ser desconsideradas;

3) Também devemos desconsiderar os itens do documento fiscal cuja TES não gere Livro Fiscal de ICMS ou quando gere Zerado (**F4\_LFICM contém N**ou**Z**);

4) Quando a nota fiscal for de Complemento de IPI **(D2\_TIPO=’P’)**, teremos como valor do item a soma dos campos **D2\_VALIPI**e**D2\_ICMSRET** da tabela SD2 (Itens dos documentos de saída); caso contrário, será assumida a soma dos campos **D2\_TOTAL**,**D2\_VALIPI**e**D2\_ICMSRET**. Este valor é armazenado para uso posterior;

5) Após os itens acima, iniciam-se os critérios para cálculo das referidas colunas.

**Cálculo:**

1) Tratamento para quando o parâmetro **MV\_CIAPCFO** estiver VAZIO ou estiver preenchido e o parâmetro **MV\_CIAPVER** estiver **T - True**;

    a. Se o parâmetro **MV\_CIAPCFO** estiver preenchido e o parâmetro **MV\_CIAPVER** estiver habilitado, somente os CFOP´s relacionados serão considerados na emissão do Livro;

    b. Mesmo que um determinado item do documento fiscal satisfaça a condição do item anterior (a), observe se o parâmetro **MV\_CFOPEXC** não exclui algum CFOP do movimento durante o processamento;

    c. No caso do item do documento fiscal passar pelas validações anteriores (itens a e b), as Exportações (**D2\_CF=”7”**) ou equiparados à Exportação (CFOP´s contidos no parâmetro **MV\_CFOPEXP**) terão as

        colunas **Total das Saídas Tributadas** e **Total das Saídas** calculadas da seguinte forma:

i. No caso do parâmetro **MV\_CIAPTOT** estar habilitado (T - True) ou a base de cálculo do ICMS estiver zerada, o valor apresentado é obtido de acordo com o item 4 (item anterior);

ii.Se as duas situações do item anterior (i) falharem (F – Falso), ou seja, o parâmetro **MV\_CIAPTOT** estiver desabilitado (F - Falso) e a base de cálculo do ICMS estiver com valor (diferente de ZERO), é a base do ICMS que será apresentada;

    d. Caso o item em processamento do documento fiscal não se enquadre no item anterior (c), será verificado se é uma escrituração **Isenta** ou **Outras** **(F4\_LFICM contém I**ou**O)**, para proceder da seguinte forma:

i.Se possuir base de cálculo reduzida **(F4\_BASEICM>0)**, o valor da coluna **Total das Saídas Tributadas** é calculado com o valor da Base de Cálculo do item da nota fiscal em processamento caso seja maior que zero, senão, será assumido o valor calculado no item 4 (item anterior).

 2) Para a coluna **Total das Saídas**, se o parâmetro **MV\_CIAPTOT** estiver habilitado (**T – True**) será assumido o valor calculado no item 4 (item anterior), senão (**MV\_CIAPTOT igual F – Falso**), utilizaremos o valor da Base de Cálculo do próprio item do documento fiscal em processamento;

i.Caso não possua base de cálculo reduzida (**F4\_BASEICM=0**), somente a coluna **Total das Saídas** será calculada com o valor da Base de Cálculo do item da nota fiscal em processamento caso seja maior que zero, senão, será assumido o valor do item 4 (item anterior);

ii. Caso o item do documento fiscal em processamento não se enquadre em nenhum dos dois itens anteriores (c e d), será assumido para as colunas **Total das Saídas Tributadas** e **Total das Saídas** o valor calculado no item 4 (item anterior), caso o parâmetro **MV\_CIAPTOT** esteja habilitado (**T – True**), senão, a base de cálculo do ICMS do item caso esteja como (**F – Falso**);

No caso do parâmetro **MV\_CIAPCFO** estar preenchido e o parâmetro **MV\_CIAPVER** estar como **F – Falso**, teremos para as colunas **Total das Saídas Tributadas** e **Total das Saídas**, o valor calculado no item 4 (item anterior) caso o parâmetro **MV\_CIAPTOT** esteja habilitado (**T – True**), senão, a base de cálculo do ICMS do item em processamento caso esteja como (**F – Falso**).

**Para análise dos Valores informados no MATA906 referentes aos totais de saídas, verificar documentação:**

<http://tdn.totvs.com/pages/releaseview.action?pageId=239022208>
