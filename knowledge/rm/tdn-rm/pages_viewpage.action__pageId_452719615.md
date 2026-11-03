---
content_hash: e18e0ad96be9ac0674db9bc35331a4e4781b108eab6b7504f6d94c23aff0016b
fetched_at: '2026-06-29T00:10:08.965303+00:00'
page_id: '452719615'
product: rm
source: tdn-rm
title: Código de Cálculo 387 - Base Tributada de INSS Folha Múltiplos Vínculos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719615
version: 2
---

Evento tipo base, valor.  
 Este evento é calculado caso o sistema esta com o parâmetro 'Calcula INSS conforme eSocial' estiver marcado em Configuração | Parâmetros | Parametrizador | 06.01 - Folha de Pagamento | 06.01.03 - Folha Normal | Geral.  
    
 Quando o funcionário está usando o cálculo de INSS conforme o eSocial, é calculada a base de INSS e lança o evento de CC 387 com o valor da base que foi usada para fazer o calculo de INSS. Quando é feito o cálculo na próxima chapa, este evento é considerado para base de INSS.  
    
 **Exemplo**

Chapa 1 -  base de INSS 1000,00

Chapa 2 - base de INSS 1500,00

Chapa 3 - Base de INSS 3000,00  
    
 Tabela de INSS:  
 Até 2000,00 - 8%  
 Até 3500,00 - 9%  
 Até 5000,00 - 11%  
    
 O cálculo ocorrerá da seguinte forma:

* Quando lança o movimento para a chapa 1, não é lançado o evento de CC 387, mas é calculado o CC 3 considerando a base de INSS como é feito por padrão, aplicando a alíquota de 8%, encontrando o valor de 80,00.
* Quando lança o movimento para a chapa 2, é considerando a base de INSS da Chapa 1 (que neste caso será 2500,00, somando as bases de INSS da Chapa 1 e Chapa 2) e a alíquota de cálculo para desconto de INSS é feito considerando a base total e a tabela de cálculo de INSS, porém o cálculo é feito somente na base de INSS de chapa 2, que neste caso é 1500,00. É lançado o evento de CC 387 com a base de calculo de INSS para a chapa 2 e o desconto no CC 3 aplicando a alíquota de 9%, que será no valor 135,00.
* Quando é feito lançamento para a chapa 3, é feito considerado as bases de INSS da chapa 1 e  2 e caso atinja o limite da tabela de cálculo de INSS, no evento de CC 387 é lançado somente o valor desse limite. Considerando o exemplo onde o limite da tabela é 5000,00, na chapa 3 será lançado 2500,00 para o evento de CC 387 e não 3000,00. Para o cálculo de desconto de INSS, será considerado a base de 5000,00 e, de acordo com a tabela de cálculo, aplicado a alíquota de 11%. E evento de CC3 receberá somente o valor de desconto da base de cálculo de INSS da chapa 3, que será 2500,00 x 11% = 275,00

Após os lançamentos, deverá ser feito o recalculo na chapa 1 e chapa 2, para que em ambas chapas seja aplicado a alíquota de 11%, que é a alíquota de cálculo de toda a base de cálculo de INSS dos vínculos acima.  
    
 **Observação**  
 Este evento foi criado para que o cálculo do INSS calcule considerando as bases corretas, sem descontar um valor indevido e para que seja lavado o valor de desconto de acordo com a base de INSS de cada Chapa.  
 Este evento também é lançado na rescisão, para que seja considerada a base de INSS do vínculo demitido.  
    
 *Outro ponto*  
 Caso o recalculo seja feito na chapa 1, será considerado os eventos do CC 387 das outras chapas e, caso ache um valor ou alíquota de cálculo diferente, será alterado valor do desconto e lançado o valor da base no CC 387. Quando atinge o limite da Tabela de INSS e por exemplo, ainda tenha uma 4ª chapa com base de INSS, no evento de CC 387 será lançado o valor 0 (zero), pois já atingiu o limite.  
 Quando não é encontrado o evento de CC 387, como no caso da chapa 1, é considerado os eventos que incidem em INSS.   
    
 **Atenção**  
 Para o correto lançamento do desconto de INSS em todas as chapas do mesmo vínculo, é necessário executar o recalculo em todas as chapas que ainda não foi lançado o evento de CC 387.  
 Atualmente, o cálculo de férias não verifica a base de INSS de outro vínculo.  
  

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Códigos de Cálculo
