---
content_hash: 81e6523cf5e342313cbdbcafcee1ead34a692ed735d3fde6a8367de86b38000f
fetched_at: '2026-06-29T00:09:23.716721+00:00'
page_id: '422546107'
product: rm
source: tdn-rm
title: Registro Y560 - Detalhamento das Exportações da Comercial Exportadora
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422546107
version: 11
---

Na geração deste registro para compor o valor da Exportações serão selecionados os Lançamentos Fiscais de Saída com Natureza de Operação 7.501 do período de geração da rotina considerando para isto a data de averbação gravada na pasta exterior do mesmo.  
Os itens a serem considerados na geração devem possuir referência da Nota de Compra.  
Comporão o valor das compras os Lançamentos Fiscais de Entrada que possuam os CFOP 1.501 e 2.501 e a data do Lançamento (DLAF.DATALF) estiver contida no período da geração da ECF.  
Para o campo CNPJ será carregado o valor gravado no cadastro do Cli/For constante na Nota Fiscal de compra da mercadoria associada no item da Nota de Exportação.  
Não serão carregados neste processo Lançamentos Fiscais Cancelados, Estornados ou de Devolução.  
   
**O cálculo do Valor das Exportações será feito de acordo com a fórmula abaixo e  agrupado por NCM:**  
[(ItemSaida.VALORMERC/ItemSaida.QTDEPRD) \* ItemRefEntrada.QTDEPRD] +  
[(ItemSaída.VLRFRETE/ItemSaida.QTDEPRD) \* ItemRefEntrada.QTDEPRD] +   
[(ItemSaida.VALORSEGURO/ItemSaida.QTDEPRD) \* ItemRefEntrada.QTDEPRD] +   
[(ItemSaida.VALORDESPESA/ItemSaida.QTDEPRD) \* ItemRefEntrada.QTDEPRD] -  
[(ItemSaida.DESCONTOITEM/ItemSaida.QTDEPRD) \* ItemRefEntrada.QTDEPRD]  
   
**O cálculo do Valor das Compras será feito de acordo com a fórmula abaixo e agrupado por NCM:**   
ItemEntrada.VALORMERC  +   
ItemEntrada.VLRFRETE +   
ItemEntrada.VALORSEGURO +  
ItemEntrada.VALORDESPESA -  
ItemEntrada.DESCONTOITEM

Descontinuado na versão 0007

Seguindo as orientações da SEFAZ, este registro não será mais gerado a partir da versão 0007.
