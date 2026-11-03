---
content_hash: a4badc0ff612517b774eced1356d6fbae912b7231551960059b6cd9494ce6aab
fetched_at: '2026-06-29T00:10:05.033020+00:00'
page_id: '452719271'
product: rm
source: tdn-rm
title: Definição da(s) chapa(s) e coligada centralizadora(s) de IRRF/INSS
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719271
version: 2
---

O objetivo da definição da(s) chapa(s) e coligada centralizadora(s) de IRRF/INSS é tratar o cálculo de IRRF para as pessoas que tiverem mais de um vínculo na mesma coligada e o cálculo de INSS para as pessoas que tiverem mais de um vínculo considerando todas as coligadas.  
    
 Sempre que se tratar de funcionário com múltiplos vínculos, é possível informar a chapa centralizadora para desconto do IRRF/INSS, e a coligada centralizadora para desconto do INSS, onde somente os funcionários centralizadores sofreram os devidos descontos.  
    
 É permitido que apenas uma única coligada seja definida como centralizadora de INSS, e apenas um único vínculo por coligada pode ser definido como centralizador para IRRF/INSS. Uma vez que um dos vínculos for "marcado" para uma pessoa, a alteração é realizada em todas as coligadas. Caso nenhum vínculo for "marcado", não haverá vínculo centralizador e o cálculo será realizado normalmente.  
    
 **Observação:**  
  Serão apresentadas apenas as chapas do funcionário com situação <>D.  
    
 **Exemplo:**  
    
   
    
 No exemplo acima, o desconto de INSS da pessoa ELIANE CORREA DA SILVA será realizado apenas na coligada 1, chapa 0104350. Já o desconto de IRRF, por ser separado por coligada, será realizado nas chapas 0104350, 0000003 e 0000015.   
    
 **Veja também:**  
 Para utilizar o cálculo de INSS e IRRF múltiplos vínculos, é necessário fazer o cadastro de eventos com os seguintes códigos de cálculo:  
    
 **305** - IRRF FOLHA BASE PENSÃO  
 **306** - IRRF FÉRIAS RECIBO BASE PENSÃO  
 **307** - IRRF 13º SALÁRIO BASE PENSÃO  
 **308** - IRRF PARTICIPAÇÃO NOS LUCROS BASE PENSÃO  
 **316** - IRRF FÉRIAS ENVELOPE BASE PENSÃO  
    
 **Atenção:**  
 Estes novos códigos de cálculos serão utilizados no cálculo da pensão alimentícia. Deverão ser cadastrados com o tipo "Base de cálculo" e com as mesmas incidências dos eventos de desconto correspondes (4 - I.R.R.F, 30 - I.R.R.F. Férias, 49 - I.R.R.F. 13º Salário, 127 - I.R.R.F. Partic. nos Lucros, 61 - IRRF FÉRIAS ENVELOPE).  
    
    
 **302** - BASE DE IRRF FOLHA OUTROS VÍNCULOS  
 **303** - BASE DE IRRF 13º SALÁRIO OUTROS VÍNCULOS  
 **304** - BASE DE IRRF PARTICIPAÇÃO LUCROS OUTROS VÍNCULOS  
 **317** - BASE DE IRRF FÉRIAS RECIBO OUTROS VÍNCULOS  
 **318** - BASE DE IRRF FÉRIAS ENVELOPE OUTROS VÍNCULOS  
    
 **Observação:**  
 No vínculo centralizador de IRRF, serão lançados os eventos com os códigos de cálculo acima com a base de IRRF dos outros vínculos para auxiliar na conferência do cálculo do IR descontado.  
    
    
 **Pensão Alimentícia**  
    
 Apesar de existir uma chapa única escolhida para o desconto do IRRF/INSS, entende-se que para efeito do cálculo de pensão alimentícia esta regra não é válida, pois podem ocorrer situações onde seja determinado judicialmente que o recolhimento de pensão seja realizado somente em um vínculo da pessoa. Sendo assim, os valores dos rendimentos sujeitos ao recolhimento de pensão, valores de IRRF a serem utilizados como deduções e o desconto final da pensão devem ser específicos para cada chapa.   
    
 Para tratar esta situação, mesmo que uma determinada chapa não seja centralizadora de desconto de IRRF, serão lançados eventos do tipo base de cálculo com o valor do IRRF que deveria ser descontado na chapa.   
    
 **Observação:**  
 Estes eventos somente serão lançados caso o evento de pensão alimentícia seja lançado e seu valor for diferente de zero.  
    
 Na chapa centralizadora, serão lançados os eventos do tipo base e os eventos de desconto de IRRF.  
    
 Os dependentes de pensão, da mesma forma que já funciona hoje, poderão ser cadastrados tanto na chapa centralizadora, quanto nas demais chapas para o calculo do "IRRF Dedução Pensão".                                                                                                                                                                                                                                                                                               
    
    
 **INSS**  
    
 Para atender a legislação previdenciária (IN 03/2005), onde ordena que quando o empregado tem mais de um vínculo, os pagamentos das suas contribuições devem obedecer ao teto do salário de contribuição.   
 Quando a mesma "Pessoa" for funcionário em mais de uma coligada, o sistema irá calcular o INSS considerando automaticamente todos os vínculos da pessoa em todas as coligadas, e o desconto será realizado apenas na coligada e chapa definidas como centralizadoras.  
    
    
 **IRRF**  
    
 Quando o funcionário tiver mais de um vínculo na mesma coligada, o IRRF será calculado considerando todas as bases de IRRF na coligada corrente, devido se tratar da mesma fonte pagadora, e o desconto será realizado apenas na chapa definida como centralizadora.  
    
 **Atenção:**  
 Os eventos de desconto de IRRF irão considerar apenas os dependentes cadastrados na chapa centralizadora.  
    
    
 **Cálculo de Rescisão e Diferenças**  
    
 Ao calcular rescisão ou diferenças para funcionários com múltiplos vínculos, o sistema deverá fazer o lançamento de INSS e IRRF apenas nas chapas centralizadoras.  
    
    
 **Cálculo de Férias**  
    
 Para cálculo das férias, é regra que todas as chapas (vinculadas e centralizadora) devem ter férias cadastradas no mesmo período de gozo.  
 Quando houver vínculos em outras coligadas, o cálculo das férias deverá ser realizado por último na coligada centralizadora.

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Funcionários
