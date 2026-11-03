---
content_hash: edd5ece5ef2c98feb1439f0583c61e3bb2909457e95bac73248252c434e9fa0e
fetched_at: '2026-06-29T00:10:07.875868+00:00'
page_id: '452719459'
product: rm
source: tdn-rm
title: Código de Cálculo 349 - INSS Férias no Terceiro Mês
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719459
version: 3
---

Desconto do tipo valor. Caso o campo Deduz INSS Integral (inclui mês seguinte) do menu Opções | Parâmetros | RM Labore | pasta Parâmetros Férias, estiver confirmado, o valor do INSS de Férias será proporcionalizado no evento com código de cálculo   
 082 - INSS Férias e no evento com código de cálculo 130 (cento e trinta), no caso de férias partidas.  
    
    
    
    
    
 **Observações:**  
    
 Sistema não possui tratamento para período de férias que atinge 3 meses consecutivos.   
 Esta situação pode ocorrer em 3 casos:  
    
 1) 30 dias de férias iniciados em 31 de janeiro em ano que não é bissexto. Neste caso seria 1 dia em janeiro, 28 dias em fevereiro e 1 dia em março.  
    
 2) 30 dias de férias desconsiderando feriados. Por exemplo, inicio em 30 de novembro, desconsiderando feriados de 24/12, 25/12, 31/12 e 01/01, resultaria em 1 dia em novembro, 28 dias em dezembro e 1 dia em janeiro.  
    
 3) Férias considerando somente dias úteis, ou seja desconsiderando todos os feriados, sábados e domingos, pode resultar em até 40 dias consecutivos.  
    
 Foram implementados recursos para atender a situação de férias que atinge 3 meses consecutivos, conforme abaixo.  
    
 Criação de 3 novos códigos de cálculo:  
 349 - INSS FÉRIAS NO TERCEIRO MÊS  
 350 - FÉRIAS NO TERCEIRO MÊS  
 351 - ADICIONAL DE 1/3 FÉRIAS NO TERCEIRO MÊS  
    
 Estes eventos serão lançados no envelope, sempre que existir o 3o. mês no período de férias.   
    
 O processo de Finalizar Férias deverá ser executado duas vezes:  
    
 1 - No segundo mês, serão apenas lançadas as bases de cálculo, CC's 44, 78 e 131. O funcionário permanecerá na situação F - Férias.  
    
 2 - No terceiro mês, serão lançados novamente os mesmos eventos de base, CC's 44, 78 e 131, mas demonstrando os valores deste mês. A situação do funcionário será alterada para A - Ativo, e dos dados de férias serão atualizados no cadastro do período aquisitivo.  
    
 No lançamento do segundo mês, geralmente serão lançados 28 ou 29 dias de férias, por exemplo. Neste caso será necessário lançar um complemento salarial para completar o pagamento dos 30 dias do mês ao funcionário.  
    
 Para isto, foi criada a opção do usuário informar o evento que achar mais apropriado, no Parametrizador, pasta Férias/Controle. Campo "Evento para pagamento do complemento salarial, quando período de férias atinge 3 meses". Este evento obrigatoriamente deverá ter CC 1 ou 2.  
    
 No cálculo da Diferença de Férias, serão utilizados os mesmos eventos de diferença do segundo mês, para o terceiro mês.
