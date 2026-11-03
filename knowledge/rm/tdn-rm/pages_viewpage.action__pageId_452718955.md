---
content_hash: e7427870b2133dbefbf660dd8f316d5c63d052359b6e17b9e341750b439a5e21
fetched_at: '2026-06-29T00:10:02.553682+00:00'
page_id: '452718955'
product: rm
source: tdn-rm
title: Código de Cálculo 388 - Base Tributada de INSS 13º Múltiplos Vínculos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452718955
version: 2
---

Evento tipo base, valor.  
 Este evento é calculado caso o sistema esta com o parâmetro 'Calcula INSS conforme eSocial' estiver marcado em Configuração | Parâmetros | Parametrizador | 06.01 - Folha de Pagamento | 06.01.03 - Folha Normal | Geral.  
    
 Quando o funcionário está usando o cálculo de INSS conforme o eSocial, é calculada a base de INSS de 13º salário e lança o evento de CC 388 com o valor da base que foi usada para fazer o cálculo de INSS de 13º salário. Quando é feito o cálculo na próxima chapa, este evento é considerado para base de INSS.  
    
 **Exemplo**

Chapa 1 -  base de INSS 1000,00

Chapa 2 - base de INSS 1500,00

Chapa 3 - Base de INSS 3000,00  
    
 Tabela de INSS:  
 Até 2000,00 - 8%  
 Até 3500,00 - 9%  
 Até 5000,00 - 11%  
    
 O cálculo ocorrerá da seguinte forma:

* Quando lança o movimento para a chapa 1, não é lançado o evento de CC 388, mas é calculado o CC 103 considerando a base de INSS de 13º Salário como é feito por padrão, aplicando a alíquota de 8%, encontrando o valor de 80,00.
* Quando lança o movimento para a chapa 2, é considerando a base de INSS de 13º Salário da Chapa 1 (que neste caso será 2500,00, somando as bases de INSS de 13º Salário da Chapa 1 e Chapa 2) e a alíquota de cálculo para desconto de INSS de 13º Salário é feito considerando a base total e a tabela de cálculo de INSS, porém o cálculo é feito somente na base de INSS de 13º Salário da chapa 2, que neste caso é 1500,00. É lançado o evento de CC 388 com a base de calculo de INSS de 13º Salário para a chapa 2 e o desconto no CC 103 aplicando a alíquota de 9%, que será no valor 135,00.
* Quando é feito lançamento para a chapa 3, é feito considerado as bases de INSS de 13º Salário  da chapa 1 e  2 e caso atinja o limite da tabela de cálculo de INSS, no evento de CC 388 é lançado somente o valor desse limite. Considerando o exemplo onde o limite da tabela é 5000,00, na chapa 3 será lançado 2500,00 para o evento de CC 388 e não 3000,00. Para o cálculo de desconto de INSS de 13º Salário, será considerado a base de 5000,00 e, de acordo com a tabela de cálculo, aplicado a alíquota de 11%. E evento de CC 103 receberá somente o valor de desconto da base de cálculo de INSS de 13º Salário da chapa 3, que será 2500,00 x 11% = 275,00

Após os lançamentos, deverá ser feito o recalculo na chapa 1 e chapa 2, para que em ambas chapas seja aplicado a alíquota de 11%, que é a alíquota de cálculo de toda a base de cálculo de INSS dos vínculos acima.  
    
 **Observação**  
 Este evento foi criado para que o cálculo do INSS de 13º Salário calcule considerando as bases corretas, sem descontar um valor indevido e para que seja lavado o valor de desconto de acordo com a base de INSS de 13º Salário de cada Chapa.  
 Este evento também é lançado na rescisão, para que seja considerada a base de INSS de 13º Salário do vínculo demitido.  
    
 *Outro ponto*  
 Caso o recalculo seja feito na chapa 1, será considerado os eventos do CC 388 das outras chapas e, caso ache um valor de base de INSS de 13º Salário ou alíquota de cálculo diferente, será alterado valor do desconto e lançado o valor da base no CC 388. Quando atinge o limite da Tabela de INSS e por exemplo, ainda tenha uma 4ª chapa com base de INSS de 13º Salário, no evento de CC 388 será lançado o valor 0 (zero), pois já atingiu o limite.  
 Quando não é encontrado o evento de CC 388, como no caso da chapa 1, é considerado os eventos que incidem em INSS 13º Salário.   
    
 **Atenção**  
 Para o correto lançamento do desconto de INSS de 13º Salário em todas as chapas do mesmo vínculo, é necessário executar o recalculo em todas as chapas que ainda não foi lançado o evento de CC 387 ou quando há alguma alteração de valor de base de INSS de 13º Salário em alguma chapa, pois a alíquota pode alterar, somando todas as bases.   
  

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Códigos de Cálculo
