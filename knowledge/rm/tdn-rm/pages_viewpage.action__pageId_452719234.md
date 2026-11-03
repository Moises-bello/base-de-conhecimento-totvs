---
content_hash: 0e90aa6d2970d015b5b224aa3e944f406efb97493f9ef6c8d064f9476c09d2c5
fetched_at: '2026-06-29T00:10:04.691380+00:00'
page_id: '452719234'
product: rm
source: tdn-rm
title: Geração da Guia de Recolhimento de Contribuição Sindical Urbana (GRCSU)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719234
version: 2
---

As guias de recolhimento geralmente são fornecidas pelo sindicato, acompanhadas de listas para relacionar os nomes dos empregados, respectivos salários e valores da contribuição.   
 Corresponde a remuneração de um dia de trabalho qualquer que seja a forma de pagamento, podendo o desconto ser efetuado das seguintes formas:

* Março -> desconto anual, para funcionários que tem mais de um ano de casa.
* Admissão janeiro e fevereiro -> efetua-se o desconto em março.
* Admissão março -> deve-se verificar se houve desconto na empresa anterior.
* Admissão após o mês de março -> a empresa deve verificar se houve desconto no emprego anterior. Em caso negativo, efetua-se o desconto no mês subseqüente ao da admissão para o recolhimento do mês seguinte.

O processo de gerar a guia GRCSU é para emissão da guia com o total descontado de contribuição sindical do empregado, conforme layout disponibilizado pela Caixa Econômica Federal.  
    
 **Atenção:** Para este processo ser executado é obrigatório a importação do relatório via RM Report, RM Gerador .Net. E no caso de gerar a guia informando o relatório na tela Parâmetros da GRCSU este relatório deve ser visível para todas as coligadas.   
    
 Para a emissão da guia o campo código de quebra, datas de processamento e vencimento é obrigatório.  
    
 O Mês e ano da competência será em que o sistema irá processar os eventos de código cálculo 12 – Contribuição Sindical e 198 – Dif. De Contribuição Sindical para os seguintes campos da guia: Nº Empregados Contribuintes, Total Remuneração – Contribuintes e o Valor do Documento.  
    
 Se marcado o parâmetro "Usa nome coligada" o campos Nome / Razão dos Dados do contribuinte na guia e/ou no campo contribuinte na pasta Sindicato, será o nome da coligada e não o nome da seção de quebra.  
    
 As informações de Datas de Processamento e de Vencimento da guia de GRCSU serão preenchidas de acordo com as informações no processamento do relatório.  
    
 A GRCSU poderá ser emitida para apenas um sindicato selecionado no campo Sindicato. Deixando em branco a seleção, gera para todos os sindicatos em que houve recolhimento de código cálculo 12 de acordo com a seção de quebra.   
 **Atenção:**  
 Este campo deve ser preenchido de acordo com a numeração do sindicato, se tiver zeros a esquerda estes devem ser informados.  
    
 As instruções que forem necessárias de serem impressas na GRCSU poderão ser digitadas no campo "Instruções", deve ser escrita a   
 norma de pagamento para GRCSU.  
    
 A GRCSU poderá emitida para todas as coligadas com a parametrização feita, caso seja necessária uma parametrização especifica para cada coligada será possível pelo botão "Adicionar parâmetros a coligada".  
    
 **Observação:**  
 A seleção de um funcionário por chapa, seleção por filtro ou por fórmula será possível apenas pela parametrização especifica da coligada.  
 **Atenção:** No caso de gerar a guia utilizando uma parametrização específica, na configuração do relatório  não poderá selecionar a opção 'Visível a todas as Coligadas'.  Nesta situação  o código do relatório deve ser informado  na parametrização especifica da coligada através do botão 'Adicionar parâmetros a coligada'.  
 Após parametrizar de forma global ou especifica serão exibidas as guias que serão impressas, onde devem ser informados obrigatoriamente os campos Agência e DV da Caixa Econômica Federal em que o sindicato tem conta e o restante dos campos poderão ser alterados antes de emitir o relatório de GRCSU.  
    
 A Agência e DV serão preenchidos automaticamente de acordo com as informações do cadastro de sindicatos.  
    
 O Cap. Social Empresa e Cap. Social Estab. informam o capital cadastrado na seção de quebra.  
    
 Os campos Nº Emp.Contribuinte é previamente calculado de acordo com o filtro selecionado e o sindicato na sua seção de quebra com o número de empregado que tiveram evento de código cálculo 12 – Contribuição Sindical e 198 – Dif. De Contribuição Sindical no mês / ano competência.   
    
 Total Rem. Contribuinte é previamente calculado de acordo com o filtro selecionado e o sindicato na sua seção de quebra com o somatório dos salários dos empregados que tiveram evento de código cálculo 12 – Contribuição Sindical e 198 – Dif. De Contribuição Sindical no mês / ano competência.   
    
 Total Emp. Estab. É previamente calculado de acordo com o filtro selecionado e a seção de quebra com o número de empregado independente de ter ou não evento de código cálculo 12 – Contribuição Sindical e 198 – Dif. De Contribuição Sindical no mês / ano competência.   
    
  Valor do Documento é previamente calculado de acordo com o filtro selecionado e o sindicato na sua seção de quebra com o somatório do valor dos eventos de código cálculo 12 – Contribuição Sindical e 198 – Dif. De Contribuição Sindical dos empregados no mês / ano competência.   
    
 **Observação:** Se for necessário os campos acima poderão ser alterados.  
    
 Os campos:  **Desconto / Abatimento**,  **Outras Deduções**,  **Mora / Multa**,  **Outros Acréscimos** quando informados serão considerados como parcelas no cálculo do campo **(=) Valor Cobrado**. Se qualquer um desses campos for informado o campo valor cobrado será impresso na guia, caso não sejam informados o campo valor cobrado não será impresso e passa a ser calculado pela CEF de acordo com a instrução informada na tela anterior.  
  

|  |  |
| --- | --- |
|  | Veja Também |

---

[www.cef.gov.br](http://www.cef.gov.br/)  
 [www.mte.gov.br](http://www.mte.gov.br/)
