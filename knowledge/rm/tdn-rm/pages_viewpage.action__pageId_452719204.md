---
content_hash: f07e363634dcc60898a1357b17006fef0f288d63e3917746e51c17f7378ccd85
fetched_at: '2026-06-29T00:10:04.147775+00:00'
page_id: '452719204'
product: rm
source: tdn-rm
title: Feriado nas Férias
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719204
version: 2
---

Este documento visa detalhar a regra de negócio e os processos técnicos implementados no sistema para permitir que os dias de feriados sejam desconsiderados na contagem dos dias de férias do funcionário.  
    
    
 **Cadastros | Sindicatos**  
 Marcar o parâmetro 'Ignora feriados na contagem das férias'.  
    
 **Observação:**   
 O motivo da existência deste parâmetro no sindicato é para atender a Convenção Coletiva, onde são determinados alguns feriados.  
    
    
 **Cadastros | Calendário**  
 Marcar o parâmetro 'Ignorar o dia na contagem das férias', no calendário utilizado nas seções dos funcionários.  
 Este parâmetro deve ser marcado, quando desejar que o feriado seja desconsiderado na contagem dos dias de férias.  
    
 **Observação:**   
 O motivo da existência deste parâmetro no calendário é porque podem existir seções em cidades diferentes com feriados municipais.   
    
 **Cadastros | Funcionários | Férias**  
 São disponibilizados os campos:  
 Dias de Feriados  
 É apresentado o número total de feriados a serem desconsiderados no período do gozo das férias.  
    
 Feriados  
 São apresentadas as datas dos feriados a serem desconsiderados no período do gozo das férias.   
    
 **Observação I:**   
 Estes campos somente são gravados/atualizados após salvar os dados da tela.  
    
 **Observação II:**   
 Estes campos não são habilitados para edição, e o cálculo do número de dias de férias sempre observa estes campos.  
    
 Ao preencher os campos 'Data Início' e 'Data Fim' é verificado quantos dias têm entre as datas informadas e subtraído o total de dias de feriados para calcular o campo 'Dias de Férias'.  
    
 **Exemplo:**   
 No calendário informado na seção do funcionário, a data 07/09/2012 esta com o parâmetro marcado.  
 No cadastro de férias do funcionário foram preenchidos os seguintes campos:  
 Data Início:       01/09/2012  
 Data Fim:          30/09/2012  
 Ao salvar a tela o campo 'Dias de Férias' é preenchido com o valor de 29 dias  
    
 Ao preencher os campos 'Data Início' e 'Dias de Férias', o campo 'Data Fim' é preenchido de maneira que o número de dias de férias ignorando os dias feriados seja igual ao número informado.   
    
 **Exemplo:**   
 No calendário informado na seção do funcionário, a data 07/09/2012 esta com o parâmetro marcado.  
 No cadastro de férias do funcionário foram preenchidos os seguintes campos:  
 Data Início:       01/09/2012  
 Dias de Férias:  30  
 Ao salvar a tela, o campo 'Data Fim' é preenchido com a data 01/10/2012.  
     
 Os campos 'Dias de Feriados' e 'Feriados', somente ficam visíveis, quando no sindicato do funcionário o parâmetro 'Ignora feriados na contagem das férias' estiver marcado.  
    
    
 **Movimento | Férias | Férias Coletivas/Globais**  
 Não são apresentados os dois campos 'Dias de Feriados' e 'Feriados', estes campos somente são visualizados no cadastro individual de férias.  
    
 Ao preencher os campos 'Data Inicial' e 'Data Final' é verificado quantos dias têm entre as datas informadas e subtraído o total de dias de feriados para calcular o campo 'Dias de Férias' de cada funcionário.   
    
 **Exemplo:**   
 No calendário da seção 01.01 a data 07/09/2012 esta com o parâmetro marcado.  
 No processo de cadastramento de férias foram preenchidos os seguintes campos:  
 Data Inicial       = 01/09/2012  
 Data Final         = 30/09/2012  
 Após a execução do processo, para os funcionários que estão na seção 01.01, serão considerados 29 dias de férias, e para os funcionários das demais seções serão considerados 30 dias de férias.  
    
 **Atenção:**  
 Sendo assim sempre que o campo 'Data Final' é preenchido, o campo 'Dias de Férias' fica em branco.  
    
 Ao preencher os campos 'Data Inicial' e 'Dias de Férias', o campo 'Data Final' é calculado de tal forma que o número de dias de férias ignorando os dias de feriados (conforme calendário da seção do funcionário) seja igual à quantidade de 'Dias de Férias' informado.  
    
 **Exemplo:**   
 No calendário da seção 01.01 a data 07/09/2009 esta com o parâmetro marcado.  
 No processo de cadastramento de férias foram preenchidos os seguintes campos:  
 Data Inicial       = 01/09/2012  
 Dias de Férias   = 30  
 Após a execução do processo, para os funcionários que estão na seção 01.01, a Data Final é preenchida com 01/10/2012, e para os funcionários das demais seções a Data Final é preenchida com 30/09/2012.  
    
 **Atenção:**  
 Sendo assim sempre que o campo 'Dias de Férias' é preenchido, o campo 'Data Final' fica em branco.  
    
    
    
 **Cálculo da Folha**  
 Os dias de feriados a desconsiderar são somados nos códigos de cálculos: 1-Horas Normais e 2-Dias Trabalhados.   
    
 Todos os processos que verificam o total de dias de férias gozadas no período tratam os feriados a desconsiderar. Tais como provisão, variáveis de fórmulas, diferença de férias, finalização de férias, etc.  
     
 **Atenção:**   
 Mesmo quando o feriado cair em dia de compensação ou descanso do funcionário (conforme horário informado no cadastro do funcionário) o feriado nas férias é desconsiderado, caso o parâmetro no sindicato esteja marcado.
