---
content_hash: d3053db1390b900d8e221a4dc460b04f829642883245953f98fd699929081c4a
fetched_at: '2026-06-29T00:09:47.596064+00:00'
page_id: '435105022'
product: rm
source: tdn-rm
title: Tipos de Componentes - Seguro
type: documentation
url: https://tdn.totvs.com/display/LRM/Tipos+de+Componentes+-+Seguro
version: 2
---

**Seguro - Componente Modalidade**   
 Para efetuar o Seguro, é necessário efetuar uma Venda ou Aluguel que tenha cadastrada uma modalidade que haja o componente de Seguro. Este componente deve estar parametrizado o seu valor opcional no Fluxus, com o tipo de ação = nada.  
 O seguro pode ser gerado por um percentual do valor da parcela ou cadastrando um valor e periodicidade fixa. Também pode ser criado seguro para mais de um tipo de parcela, deve-se criar grupos separados para cada tipo de parcela (anual, mensal, semestral, etc) e colocar o componente de seguro em cada um destes grupos e parametrizá-los de acordo com a necessidade de cada tipo de parcela. O tipo de parcela que conterá o seguro, deve estar marcado o parâmetro "Tipo Parcela tem seguro".  
    
 O valor do seguro pode fazer parte de parcelas do tipo Principal ou ser criado parcelas para o seguro. Se o parâmetro "Tipo Parcela tem seguro" do componente Principal estiver marcado e a data de início do componente de seguro estiver dentro da data do componente principal, o valor do seguro será somado ao valor da parcela do tipo principal, senão, será criado parcelas de seguro.  
 Para gerar seguro pelo percentual da parcela, devemos informar o percentual e o número de parcelas de seguro. Atente para periodicidade do componente de seguro, este deve acompanhar a periodicidade do componente principal.  
    
 Ao cadastrar ou editar o componente de Seguro da Modalidade da Venda, informe os seguintes campos:  
    
 **Definir valor usando:**  
 Informe se o valor do seguro será gerado a partir de um valor fixo ou um percentual sobre o valor das parcelas.  
    
 **Valor Total:**  
 Informe o valor total do componente de seguro caso este seja fixo, se não for fixo, deixe o campo em branco para ser informado posteriormente na inclusão de uma venda ou aluguel.  
    
 **Observação:**  
 Este campo somente será habilitado se o valor definido a ser usado for "Valor".  
    
 **Valor unitário da parcela:**   
 Informe o valor unitário da parcela de Seguro.  
    
 **Observação:**  
 Este campo poderá ser preenchido automaticamente se os campos Valor Total e Número de Parcelas já estiverem parametrizados.  
    
 **Número de Parcelas:**  
 Informe o número de parcelas que serão criadas para este componente caso este seja fixo, se não for fixo, deixe o campo em branco para ser informado posteriormente na inclusão de uma venda ou aluguel.  
    
 **Percentual s/ Parcela:**  
 Informe o percentual sobre a parcela para o cálculo do seguro caso este seja fixo, se não for fixo, deixe o campo em branco para ser informado posteriormente na inclusão de uma venda ou aluguel. Se for utilizar seguro sobre o percentual da parcela, deve-se informar o Número de parcelas.  
    
 **Observação:**  
 Este campo somente será habilitado se o valor definido a ser usado for "Porcentagem".  
    
 **Periodicidade (meses):**  
 Informe a periodicidade das parcelas de Seguro que serão criadas caso este seja fixo, se não for fixo, deixe o campo em branco para ser informado posteriormente na inclusão de uma venda ou aluguel.   
    
 **Exemplo:**  
 1 mês, 3 meses  
    
 **Vencimento Inicial das Parcelas:**   
 Informe a data de vencimento da primeira parcela que este componente irá agir.
