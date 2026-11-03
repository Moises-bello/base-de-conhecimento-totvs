---
content_hash: 0ce8d2b7c5cf94b1edef6c029f67933bc1cd604928be61929c696650fd5374f4
fetched_at: '2026-06-29T00:11:49.804910+00:00'
page_id: '838692998'
product: rm
source: tdn-rm
title: Férias Individuais - Validação de dias de gozo de férias e regras de inicio
  de férias
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=838692998
version: 20
---

**CONTEÚDO**

1. **Versões**
2. **Visão Geral**
3. **O que é necessário**
4. **Exemplo de utilização**

## **01. VERSÕES**

false

**A partir dos patches:**

* 12.1.2310.194
* 12.1.2402.132
* 12.1.2406 e Superiores

## **02. VISÃO GERAL**

Com as alterações provenientes da Reforma Trabalhista de acordo com a Lei nº 13.467 de 13 Julho de 2017, o colaborador poderá flexibilizar as férias em até **3** (**três)** períodos de gozo, sendo que nenhum deles pode ser menor que **5 (cinco)** dias e pelo menos deve existir um período com **14 (quatorze)** dias ou mais de gozo.  Antes da reforma, as férias podiam ser divididas em no máximo **2 (dois)** períodos, com a exigência de que um deles fosse de no mínimo **10 (dez)** dias. Além disso, a Reforma também orienta que nenhum período de gozo deve iniciar em dia de descanso ou feriado ou até dois dias antes destes.

Este tratamento já existe no Portal Meu RH, porém no RM.exe retornava somente mensagens indicando quando o usuário cadastrava algum período de gozo fora das regras acima, mas não era feito nenhum tipo de trava, permitindo seguir com o cadastro das férias.

Diante deste cenário, foi feito tratamento no Cadastro de Férias Individuais, mediante a parametrização, para não permitir cadastrar férias para o colaborador, caso não esteja de acordo com as regras acima.

## **03. O QUE É NECESSÁRIO**

Necessário que o parâmetro **"Ativar alterações da Reformar Trabalhista de acordo com a Lei Nº 13.467 de 13 de Julho de 2017" (Parametrizador | Folha de Pagamento | Folha Normal | Geral 1/2)** esteja ativo

Além disso, ativar no novos parâmetros criados em Parametrizador | Folha de Pagamento | Férias | Controle 2/2:

## **04. EXEMPLO DE UTILIZAÇÃO**

Para a utilização é necessário o entendimento de algumas regras e cada parâmetro faz uso de uma destas regras:

Validar a quantidade de dias de Gozo de Férias conforme as regras da Reforma Trabalhista

Podemos exemplificar o uso desta regra com o parâmetro **Validar a quantidade de dias de Gozo de Férias conforme as regras da Reforma Trabalhista** marcado.  
  
Caso tentemos cadastrar três períodos de 10 dias de férias, será exibida a mensagem de alerta ao usuário no cadastro do segundo período, informando que só será permitido cadastrar 3 períodos de férias caso o funcionário tenha ao menos 1 período com um descanso de 14 dias ou mais, como no exemplo abaixo:  
  
O funcionário já havia marcado um período com 10 dias de férias e tentou cadastrar mais um período com 10 dias de férias, nenhum período comportou a regra de no mínimo 14 dias de descanso.

Caso o funcionário quisesse usufruir de apenas 10 dias de descanso e utilizar o abono para a contagem desses dias de descanso, será permitido, caso o mesmo não esteja utilizando o parâmetro **Desconsiderar dias de Abono na contagem.**  
  
No exemplo abaixo, o funcionário já tem uma marcação de férias com 10 dias de férias para o primeiro período. Quando no segundo período tentar cadastrar mais 10 dias de férias e 10 dias de abono, será permitido a inclusão.

Desconsiderar os dias de abono na contagem

As regras quando o parâmetro Desconsiderar Dias de Abono na contagem está ativo permanecem iguais, o que muda é o comportamento do sistema passa a entender que **Dias de Abono não podem ser considerados como dias de descanso.**No exemplo abaixo, o funcionário já tem 10 dias de férias marcados para o primeiro período de gozo. Ao tentar marcar 10 dias de férias mais 10 dias de abono, será considerado que em nenhum período o funcionário terá um descanso de 14 dias no mínimo. Sendo assim, não será permitido a inclusão. 

falseAtenção

Só será permitido a inclusão de férias que tenham no mínimo 5 dias de descanso, mas vale lembrar que caso o parâmetro Desconsiderar dias de Abono na contagem' esteja desmarcado e o usuário cadastre 3 dias de férias + 2 dias de abono, será considerado o total de 5 dias de férias.

No exemplo abaixo, o funcionário tenta marcar apenas 3 dias de férias  e 2 de abono. Com o parâmetro marcado, o sistema irá barrar essa marcação de Férias:

Mas caso o parâmetro esteja desmarcado, será permitido a marcação de Férias, conforme abaixo:

Impedir início de férias em feriados, dias de descanso ou até 2 dias antes destes

Caso esse parâmetro esteja ativo, e tentemos cadastrar as férias do funcionário no seu **dia de descanso, feriado ou até 2 dias antes destes dias**, não será permitido e exibirá a mensagem de erro abaixo.

Observação

É verificado a jornada de trabalhado do funcionário, verificando se é até dois dias antes do dias de descanso/compensação, conforme o cadastro de horário e os feriados cadastrados no calendário vinculado a seção do funcionário.

Não Impedir a marcação de férias para a jornada 12x36

Quando o parâmetro **Não Impedir a marcação de férias para a jornada 12x36** estiver **inativo** e tentarmos cadastrar uma, férias para o funcionário que utilize desta jornada, será exibida a mensagem de erro.  
No exemplo abaixo, o funcionário está com sua jornada apontando para a segunda-feira do dia 01/01/2024 como dia de **trabalho** e a terça-feira, dia 02/01/2024, está como seu dia de **descanso**, configurando assim sua jornada 12x36. 

 Mas se marcamos o parâmetro e tentarmos cadastrar as férias do funcionário em dia de **descanso,** será exibida a seguinte mensagem: 

Caso a marcação seja no dia de trabalho, será permitido:

false

Para ser considerado uma Jornada 12x36 é verificado a informação do campo Tipo  de Jornada e-Social = **2 - Jornada 12 x 36 (12 horas de trabalho seguidas de 36 horas ininterruptas de descanso)** no cadastro de horário vinculado ao funcionário.

Desconsiderar Dia Compensado

Com o parâmetro **Desconsiderar dia compensado** ativo, serão desconsiderados os dias compensados como dias de descanso, permitindo assim o cadastro nestes dias, como no exemplo abaixo:

Caso tente marcar as férias do funcionário para o sábado, com o parâmetro Impedir início de férias em feriados, dias de descanso ou até 2 dias antes destes, ativo, e o parâmetro Desconsiderar Dia Compensado, também ativo, será permitido, não barrando a inclusão da marcação.
