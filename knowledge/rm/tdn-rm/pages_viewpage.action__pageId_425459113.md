---
content_hash: 4d96784b04afd4e1fed76ea4e70081dc936f71a3a8130b582fc831f2a64a307b
fetched_at: '2026-06-29T00:09:34.016525+00:00'
page_id: '425459113'
product: rm
source: tdn-rm
title: Classificação de Bolsas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459113
version: 5
---

---

A classificação serve para possibilitar que a instituição possa aplicar  para os  de diversas formas. É comum que eles tenham mais de uma bolsa cadastrada, para isso faz-se necessário definir ordens e formas de aplicação.

Existem 4 tipos de bolsas, a saber:

* **Somar bolsas**

Somado o percentual/valor das bolsas e incidido sobre o valor total.  
 *Exemplo*   
Parcela: R$ 1000,00.  
  
 Bolsa 1             5%  
Bolsa 2             15%  
Bolsa 3             R$ 65,00

Valor a ser pago:  
 R$ 1000,00 – (soma das Bolsas R$ 265,00) = **R$ 735,00.**

* **Aplicar bolsas em cascata**

É verificada a ordem das bolsas e aplicado o desconto em cascata.  
 *Exemplo*  
 Parcela: R$ 1000,00.  
 Bolsa 1            18%                    Ordem 1   
Bolsa 2            5%                      Ordem 3   
Bolsa 3            10%                    Ordem 2  
  
 Valor a ser pago:  
  
 R$ 1000,00 – Bolsa 1 = R$ 820,00                                     
R$ 820,00 – Bolsa 3 = R$ 738,00                                                                       
R$ 738,00 – Bolsa 2 = **R$ 701,10.**

Ao marcar o parâmetro de sistema *"Ambiente | Parâmetros | Educacional | Integração | Financeiro | Educacional | Fin - Geral 2/4 | Somar bolsas de mesma ordem e tipo de aplicação em cascata"*o comportamento de aplicação das bolsas em Cascata será modificado para que todas as bolsas que possuírem a mesma ordem de aplicação, definida tanto na classificação de bolsas quanto no , sejam primeiramente somadas e somente depois sejam aplicadas sobre o valor base da parcela.

*Exemplo* Parcela: R$ 1000,00.  
 Bolsa 1            18%                    Ordem 1   
Bolsa 2            5%                      Ordem 2   
Bolsa 3            10%                    Ordem 1  
  
 Valor a ser pago:  
  
 R$ 1000,00 - (Bolsa 1 + Bolsa 3) = R$ 720,00                                                       
R$ 720,00 - Bolsa 2 = **R$ 684,00**.  
  
 *Atenção:*  
 Nos parâmetros do sistema existe o parâmetro *'Aplicação de Bolsa'* que define onde o sistema irá verificar o tipo de bolsa a ser aplicada.   
    
 Se a escolha for ***'Classificação de bolsas'***, dentro do cadastro da própria bolsa é que devemos definir o seu *tipo*, associando à cada bolsa a *classificação* correspondente (Somar, Cascata, Maior bolsa ou Exclusiva) podendo a instituição de ensino, desta forma, conceder tipos diferentes de bolsas para o aluno no mesmo contrato.   
 Esta *classificação* é que irá definir como os cálculos das bolsas deverão ser feitos, pois na *classificação* além de se definir o tipo da bolsa, ou seja, a forma de aplicação da bolsa nos cálculos também se define a *ordem* em que as bolsas deverão ser aplicadas nos cálculos, principalmente porque este tipo de 'Aplicação de Bolsa' possibilita a inclusão de diversos tipos de bolsa no mesmo contrato.  
    
 Se a escolha for ***'Contrato'***, o tipo de bolsa a ser aplicada deve ser definida dentro do cadastro do contrato e assim, todas as bolsas incluídas no contrato assumirão o mesmo tipo e então, a *ordem* de aplicação da bolsa, deverá ser definida dentro do próprio cadastro da bolsa no contrato. Se por ventura, a *ordem* de alguma bolsa no contrato ficar em branco, o sistema interpretará como zero (0).

* **Aplicar somente a maior bolsa**

Ignorada a bolsa com menor percentual/valor e aplicado a bolsa de maior desconto.  
  
 *Exemplo*   
Parcela: R$ 1000,00.  
  
 Bolsa 1            9%   
Bolsa 2            R$ 110,00   
Bolsa 3            5%  
 Valor a ser pago:  
 R$ 1000,00 – Bolsa 2 = **R$ 890,00**.

* **Exclusiva**

Não pode ser cadastrada junto com outra bolsa para a mesma parcela.  
 *Exemplo* Parcela: R$ 1000,00.  
Bolsa 1            15%     
Bolsa 2            40%                   (Cenário que não existe)     
Bolsa 3            16%  
  
 Com a bolsa do tipo Exclusiva é possível que tenha apenas uma única bolsa. Neste caso:  
  
 Bolsa 40%  
  
 Valor a ser pago:  
 R$ 1000,00 – 40% = **R$ 600,00.**  
 Considerações importantes:

* Este cadastro poderá ser feito no contexto superior e básico.
