---
content_hash: e7fd8d49318f494e214a51eb0c537d5ad37ac366b335ab3bbc8a19acdd239245
fetched_at: '2026-06-29T00:10:59.760371+00:00'
page_id: '615606796'
product: rm
source: tdn-rm
title: MP 1046 - Abono Pecuniário
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=615606796
version: 25
---

Conforme a MP1046 Art. 8º, A conversão de 1/3 do período de férias  de que trata o caput em abono pecuniário dependerá do empregador, hipótese em que o pagamento poderá ser efetuado até a data de que tratar o art. 7º: O adicional de um terço relativo às férias concedidas durante o período a que se refere o art. 1º poderá ser pago após a sua concessão, a critério do empregador, até a data em que é devida a gratificação natalina prevista no [art. 1º da Lei nº 4.749, de 12 de agosto de 1965](http://www.planalto.gov.br/ccivil_03/leis/l4749.htm).

Para atender a determinação do Art 8º, o Módulo TOTVS Folha de Pagamento disponibiliza o recurso de fórmulas que pode ser configurado pelo usuário para que não calculo 1/3 de abono pecuniário caso seja opção do empregador.

Abaixo iremos exemplificar como proceder:

### **Cálculo de Férias**

Passo 1 - Criar a fórmula conforme o exemplo abaixo e vincular no evento de código de cálculo 39 e 56:

Fórmula - Cálculo Abono PecuniárioFórmula - Cálculo 1/3 de Abono Pecuniário

Cadastro do evento código de cálculo 39 e 56:

 

Passo 2: Criar a Fórmula para incluir em um evento de base para armazenar o valor devido de Abono pecuniário e 1/3 de abono, que será pago posteriormente.

Fórmula - Base Abono PecuniárioFórmula - Base 1/3 de Abono Pecuniário

Incluir um evento do tipo Base de Cálculo com a fórmula acima para ser lançado no recibo de férias. O mesmo pode ser informado como evento adicional:

 

Passo 3 - Cadastrar/Calcular as Férias. Recibo de Férias após o cálculo das Férias lançou os eventos de base e não lançou os eventos de provento referente ao pagamento de abono:

Passo 4: Lançar Férias. Os eventos de base também será lançado no envelope do funcionário:

### **Provisão de Férias**

Após o pagamento das férias, o período aquisitivo é fechado. E mesmos naqueles casos onde não são fechados, o processo de provisão considera somente como devido os avos restantes, não contabilizando o passado. No caso do abono pecuniário e 1/3 de abono pecuniário que não foi pago junto com as férias, o sistema não entende que existe este debito não provisionando o valor devido.

Para solucionar este cenário gerando a provisão com o valor devido, o módulo Folha de Pagamento disponibiliza no parametrizador o recurso de  fórmulas, que permite informar uma fórmula para adicionar no valor de férias vencidas ou proporcionais no final da geração da provisão.

Abaixo exemplificarmos uma sugestão de Fórmula para que seja somada na provisão de Férias:

Calculamos e lançamos as férias para o funcionário conforme o exemplo acima. Foi lançado somente os dias de férias e não lançamos o abono pecuniário, 1/3 de abono pecuniário e 1/3 de férias. Para facilitar a identificação do adicional devido, inserimos o evento de base de cálculo no envelope do funcionário com os respectivos valores.

No parametrizado, na menu Férias | Fórmulas, inserimos uma fórmula que retorna o valor do 1/3 de férias devido, o valor do abono pecuniário e o valor de 1/3 de abono pecuniário. No nosso exemplo colocamos no campo para somar com férias vencidas:

Na fórmula utilizada, usamos a variável MV que retorna a soma do evento de base de cálculo B099, B198 e B199 pago durante o ano de 2021 e abatemos os eventos de proventos que serão usados para pagar o abono pecuniário, 1/3 de abono pecuniário e 1/3 de férias quando for o caso ([Folha](https://tdn.totvs.com/pages/editpage.action?pageId=615912658) ou [Rescisão](https://tdn.totvs.com/pages/viewpage.action?pageId=615919977)). Assim, quando o pagamento for efetuado o mesmo não será mais somado na provisão:

Fórmula - Provisão de 1/3 de férias e 1/3 de abono pecuniário

Ao gerar a provisão, o valor pago de férias no mês foi informado e o valor retornado pelo fórmula somado ao campo de provisão de férias vencidas.

Após o pagamento do Abono pecuniário e 1/3 de abono pecuniário que será exemplificado no tópico abaixo, a provisão não considerou o valor do Abono pecuniário e 1/3 de abono pecuniário:

### **Pagamento do Abono pecuniário e 1/3 de abono pecuniário**

O pagamento do abono pecuniário e 1/3 de abono pecuniário, deverão  ocorrer até dia 20/12, devendo as tributações ocorrer na competência/caixa em que o pagamento for efetuado. 

Caso a realização do pagamento do abono pecuniário e 1/3 de abono pecuniário não sejam pagos antes de vencer o próximo período aquisitivo, irá caracterizar como férias em dobro, devido aquele período não ter sido quitado.

No modulo da Folha de Pagamento, o mesmo pode ser feito usando evento calculado por fórmula e lançado diretamente no envelope do funcionário, através dos processos disponibilizados pelo folha, como Grupo de Eventos, Entrada de dados, Eventos Programados, etc.

Abaixo, exemplificaremos o pagamento com a Sugestão de Fórmula:

*lançamento direto no envelope - Grupo de Eventos*

Fórmula para pagamento de Abono Pecuniário e 1/3 de abono pecuniário. Usando a função MV abaixo irá considerar o evento de Base de Cálculo lançado no envelope acima durante o ano de 2021:

Fórmula - Pagamento de Abono PecuniárioFórmula - Pagamento de 1/3 de Abono Pecuniário

Criado o evento de provento e inserido a fórmula no campo de valor:

Ao fazer o lançamento dos eventos para a Folha, o mesmo foi calculado:

Para pagamento de Férias em dobro, criamos um exemplo de sugestão de fórmula, que verifica se o valor pendente a se quitado já ultrapassou dois período vencidos de férias, considerando o primeiro dia da competência atual. A Consulta SQL está exemplificada no Pagamento de Abono Pecuniário e 1/3 de Abono Pecuniário Vencidas neste [link](https://tdn.totvs.com/pages/viewpage.action?pageId=615919977).

*Fórmula para pagamento de Abono Pecuniário em Dobro:*

sqlPagamento de Abono Pecuniário em Dobro CHAPA
ENTAO
0
SENAO
SETVAR (QUANTDIAS, SUBTRAIDATAS(MTDATA(01,MES,ANO),FIMPERAQUIS1));
SE QUANTDIAS > 365 E (DATAPGTOFERIAS >= MTDATA(28,04,2021) E DATAPGTOFERIAS <= MTDATA(25,08,2021))
ENTAO
VALOREVENTO \* ARRED(QUANTDIAS/365);
FIMSE;
FIMSE;]]>

Associando a Formula acima em um evento de provento:

*Fórmula para pagamento de 1/3 de Abono Pecuniário em Dobro:*

sqlPagamento de 1/3 de Abono Pecuniário em Dobro CHAPA
ENTAO
0
SENAO
SETVAR (QUANTDIAS, SUBTRAIDATAS(MTDATA(01,MES,ANO),FIMPERAQUIS1));
SE QUANTDIAS > 365 E (DATAPGTOFERIAS >= MTDATA(28,04,2021) E DATAPGTOFERIAS <= MTDATA(25,08,2021))
ENTAO
VALOREVENTO \* ARRED(QUANTDIAS/365);
FIMSE;
FIMSE;]]>

Associando a Fórmula acima em um evento de provento:

Lançado o evento de férias em dobro, para um funcionário onde o pagamento foi feito após o vencimento de dois períodos aquisitivos, através do Grupo de eventos:

*Lançamento usando o processo de Diferença de Férias*

Para o processo de diferença de férias, o sistema calcula os eventos de Código de Cálculo 39 e 56. Neste caso não é necessário criar uma fórmula para que o mesmo seja calculado. Usando o processo de diferença e marcando a opção 'Não' para dissídio o sistema irá calcular e lançar os valores de devidos nos eventos de Código de Cálculo 59 e 176:

Após executar, os eventos com os valores de Abono de Férias e 1/3 de abono de férias foram lançados:

**Calculo de Diferença de Férias - Dissídio**

Para o calculo de diferença a fórmula sugerida não calcula os eventos de Código de Cálculo 39 e 56 quando é um cálculo por dissídio, pois caso a fórmula não tratasse o tipo de cálculo, será lançado todo o valor integral do que não foi pago no recibo de férias. Desta forma, na fórmula do eventos de base, é feito o cálculo somente da diferença devida.

Para os casos onde teve evento de base sugerido lançados no recibo de férias para armazenar o valor do Abono pecuniário e 1/3  abono pecuniário de férias que será pago até dia 20/12, deverá ser informado um evento de diferença que irá armazenar o valor. Iremos da uma sugestão que atenda os usuários que lançaram o evento de base no recibo de férias e informaram o evento no parametrizador.

No evento B198, incluir o evento para ser lançado do evento de diferença, também como base:

No evento B199, incluir o evento para ser lançado do evento de diferença, também como base:

Ao calcular a diferença para um funcionário que teve o evento B198 e B1988 lançado no recibo de férias, no calculo da diferença o mesmo é considerado e calculado a diferença, lançando os evento de BD97 e BD98 com os valores da diferença:

Dica

Caso o entendimento do cliente seja que o evento diferença Abono pecuniário e 1/3 de abono pecuniário de férias tenham que ser pagos no cálculo da diferença por dissídio e não junto com Abono pecuniário e 1/3 de abono pecuniário de férias até dia 20/12 conforme determinado na MP 1046, ou no caso do cálculo de uma diferença retroativa ao período de férias após demissão, poderá alterar o tipo dos eventos de diferença para lançar na folha, 'BD97' e 'BD98' para provento.
