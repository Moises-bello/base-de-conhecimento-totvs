---
content_hash: 3fafb06fff8104c324e1f062f8ad3f176bfc8ffa503e36326d62831d4ec2a13c
fetched_at: '2026-06-29T00:09:32.481740+00:00'
page_id: '425458858'
product: rm
source: tdn-rm
title: Bolsa do contrato
type: documentation
url: https://tdn.totvs.com/display/LRM/Bolsa+do+contrato
version: 15
---

---

Tela para realização do cadastro de bolsas para o contrato do aluno. As principais informações presentes no cadastro são:

- Desconto por antecipação:Possibilita que o cálculo do  seja aplicado antes ou depois do cálculo de uma determinada bolsa vinculada ao contrato do aluno. Este campo só ficará visível para o usuário se o parâmetro de aplicação de bolsa nos  parâmetros do sistema Educacional estiver marcado como valor "Contrato".

Veja mais na guia "Ordem de Aplicação do Desconto por Antecipação" na seção [Bolsas de Contratos](https://tdn.totvs.com/x/iZ2yKg).

- Bolsa - bolsa que será aplicada a um serviço específico do contrato.

- Serviço - serviço ao qual a bolsa será aplicada.

- Período - tempo de vigência da bolsa (pode ser por data ou por parcela).

- Tipo de desconto - tipo de desconto concedido pela bolsa (percentual ou valor).

- Ordem da bolsa - define a ordem de aplicação da bolsa quando o modelo definido no contrato for "aplicar bolsas em cascata".

No caso de classificação de bolsa considerando a maior bolsa, para que o sistema considere apenas a bolsa com o maior percentual é necessário informar a mesma ordem em todas as classificações das bolsas.

*Exemplo*

Bolsa 1            60%                    Aplicar em cascata              Ordem null  
Bolsa 2            40%                    Aplicar a maior bolsa          Ordem 1

O sistema considerará as duas bolsas na geração do lançamento.

Bolsa 1            60%                    Aplicar em cascata              Ordem 1  
Bolsa 2            40%                    Aplicar a maior bolsa          Ordem 1

O sistema considerará apenas a bolsa com maior percentual. Neste caso, a bolsa 1.

**Observação:****Ordem de aplicação das bolsas em cascata**

Ao se definir a ordem de aplicação das bolsas em um contrato onde o campo "Tipo da Bolsa = aplicar bolsas em cascata", todas as bolsas do contrato serão aplicadas em cascata de acordo com a ordem definida, um bolsa por vez.

*Exemplo*   
Parcela: R$ 1000,00.  
Bolsa 1            18%                    Ordem 1   
Bolsa 2            5%                      Ordem 3   
Bolsa 3            10%                    Ordem 2

Valor a ser pago:  
R$ 1000,00 – Bolsa 1 = R$ 820,00                                      
                                      R$ 820,00 – Bolsa 3 = R$ 738,00                                                                       
                                                                           R$ 738,00 – Bolsa 2 = **R$ 701,10.**

Se o parâmetro de sistema "Parâmetros | Educacional | Integração | Financeiro | Educacional | Fin - Geral 2/4 | Somar bolsas de mesma ordem e tipo de aplicação em cascata" for marcado, o comportamento de aplicação das bolsas em cascata será modificado para que todas as bolsas que possuem a mesma ordem de aplicação, tanto no contrato do aluno e quanto na , sejam somadas antes de serem aplicadas sobre o valor base da parcela.

*Exemplo*   
Parcela: R$ 1000,00.  
Bolsa 1            18%                    Ordem 1   
Bolsa 2            5%                      Ordem 2   
Bolsa 3            10%                    Ordem 1

Valor a ser pago:  
R$ 1000,00 - (Bolsa 1 + Bolsa 3) = R$ 720,00                                                       
                                                        R$ 720,00 - Bolsa 2 = **R$ 684,00**.

**Atenção:**

No TOTVS Educacional quando são adicionadas bolsas no contrato do aluno cujo a soma do seu percentual ultrapassem 100% de descontos o sistema emite um alerta bloqueando a adição desta bolsa.

*Exemplo*   
Parcela: R$ 1000,00.  
Bolsa 1            50%                       
Bolsa 2            60%

Total               110% de bolsa

Ao tentar inserir a segunda bolsa de 60% o sistema irá emitir um alerta pois o total de bolsas neste caso ultrapassa o valor permitido de 100%, sendo assim esta bolsa não é inserida no contrato. Para que essa regra surta efeito o sistema deve estar parametrizado para que a  esteja por "**contrato**" e o tipo de classificação seja igual a "**somar bolsas**". Veja mais sobre estes parâmetros clicando .

Porém existe uma exceção na regra para que as bolsas que contenham fórmula parametrizada não sejam levadas em consideração no somatório dos percentuais da bolsa, pois este percentual será customizado pela própria fórmula cadastrada na bolsa e nesse caso a regra estará na fórmula. Veja mais sobre bolsa por fórmula clicando [aqui](http://tdn.totvs.com/pages/viewpage.action?pageId=354469739).

Quando o "Modo de aplicação de bolsa" for "Classificação de bolsas", o sistema mostrará um campo explicativo do funcionamento do cálculo das bolsas na frente do campo ordem.

**Contabilização**

Quando estiver parametrizado no sistema para utilizar a contabilização por competência e a contabilização estiver no modelo revitalizado, se a bolsa estiver parametrizada como "Compõe contabilização por competência", o sistema irá disponibilizar uma aba para que seja possível definir um período de competência da contabilização.

Quando existir um período padrão de contabilização para o período letivo da bolsa informada, ao selecionar a bolsa no contrato, o sistema carrega esse período na aba de contabilização.

O período de contabilização deve seguir as seguintes premissas:

* Quando informada uma data inicial ou final a outra deve ser preenchida;
* Data inicial não pode ser maior que a data final;
* O período de contabilização não pode repetir em registros distintos dentro da mesma bolsa no período letivo.

Se o contrato já possui apropriação mensal não será possível modificar:  
- O período da competência no cadastro da bolsa do contrato  
- A quantidade de parcelas ou período (data) na bolsa do contrato  
Caso a alteração seja em função de ajustes que tenham como consequência o aumento na quantidade de parcelas ou período de bolsa, é recomendado que seja adicionado um novo registro para a bolsa com uma nova competência ou que seja executado o estorno da contabilização do contrato.

Para entender o impacto no processo de contabilização [clique aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=425458834#bolsaxcontabiliza%C3%A7%C3%A3o1-periodobolsa)

**Movimento por competência**

Quando estiver parametrizado no sistema para utilizar movimento por competência o período utilizado para a bolsa, pode ser definido no Contrato, Parametrização por Curso ou Período Letivo.

O período do movimento deve seguir as seguintes premissas:

* Quando informada uma data inicial ou final a outra deve ser preenchida;
* Data inicial não pode ser maior que a data final;

Para que a bolsa entre como dedução ou desconto no movimento, essa bolsa deve ser parametrizada dentro de [Bolsa por Filial](https://tdn.totvs.com/display/LRM/Bolsas+-+Educacional) como Bolsa Incondicional.

Quando incluir bolsas no contrato e esse contrato já possui algum movimento gerado, não será permitido alterar a bolsa dentro do cadastro, essa bolsa só fica disponível para alteração caso não exista nenhum movimento gerado.

 Informações Complementares

---

   
  
  
[Detalhamento do cálculo da bolsa do aluno](https://tdn.totvs.com/pages/viewpage.action?pageId=531024083)

 Recursos Adicionais

---

[Passo a Passo - Inclusão e Exclusão de Bolsas Retroativas](http://tdn.totvs.com/pages/viewpage.action?pageId=317301097)
