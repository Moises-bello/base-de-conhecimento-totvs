---
content_hash: 8e27cd9d0071210f75452900ddeda485874cce80c241dcb70eed4567609e15b9
fetched_at: '2026-06-29T00:10:09.448043+00:00'
page_id: '452719671'
product: rm
source: tdn-rm
title: Código de Cálculo 379 - Indenização por Tempo de Serviço de Safrista
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719671
version: 2
---

Como o safrista tem o contrato de trabalho por tempo determinado e, para atender o art. 14 da Lei nº 5889/73, que entende que faz jus o pagamento de uma indenização do empregador para o trabalhador rural devido a sua temporalidade, foi criado o código de cálculo 379 que calcula e lança a indenização por tempo de serviço de safrista, conforme a lei citada.  
 O cálculo é feito considerando cada avo trabalhado considerando todo o tempo de serviço (contrato) do safrista.  
    
 **Exemplo**  
 Admitido em 01/05/2017  
 Demissão em 31/07/2018  
 Salário do Funcionário: R$1000,00  
 Cálculo: (1000,00 / 12) \* 15(avos/meses trabalhados) = R$ 1250,00  
 Será lançado no evento de código de cálculo 379 o valor de R$ 1250,00  
    
 **Observação**  
 Para que o evento seja lançado, é necessário que o parâmetro 'Lança indenização por tempo de serviço de safrista (Rural) esteja marcado no parametrização, na pasta Rescisão.  
 A rescisão do funcionário deve ser do tipo T e o funcionário deve ser do tipo Rural.  
    
 **Atenção**  
 É considerado como avo para pagamento de indenização, a fração superior a 14 dias de trabalho no mês. Caso o funcionário tenha algum afastamento ou faltas superior a 15 dias dentro do mês, independente do ano do afastamento ou da falta, será desconsiderado o avo para contagem de pagamento da verba de indenização.   
 Se o parâmetro 'meses de afastamento por acidente de trabalho reduz avo de 13º salário' estiver desmarcado na pasta 13º Salário | Cálculo no parametrizador, os afastamentos do tipo T não serão desconsiderados na contagem de avos para pagamento da verba indenizatória.     
 O sistema considera como data termino de contrato a data de desligamento do safrista, informado no cadastro de rescisão e não a data final do contrato informado no cadastro do funcionário.  

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Códigos de Cálculo
