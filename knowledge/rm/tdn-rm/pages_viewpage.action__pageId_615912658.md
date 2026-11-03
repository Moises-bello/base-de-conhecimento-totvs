---
content_hash: b92af0970241838d744b839e9c20c7024a8cd6b7daec53f54cde6025b69f6df9
fetched_at: '2026-06-29T00:10:59.766988+00:00'
page_id: '615912658'
product: rm
source: tdn-rm
title: MP 1046 - Adicional de Férias
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=615912658
version: 17
---

Conforme a MP 1406, Art. 7º O adicional de um terço relativo às férias concedidas durante o período a que se refere o art. 1º poderá ser pago após a sua concessão, a critério do empregador, até a data em que é devida a gratificação natalina prevista no [art. 1º da Lei nº 4.749, de 12 de agosto de 1965](http://www.planalto.gov.br/ccivil_03/leis/l4749.htm).

Para atender a determinação do Art 7º, o Módulo TOTVS Folha de Pagamento disponibiliza o recurso de fórmulas que pode ser configurado pelo usuário para que não calculo 1/3 de férias caso seja opção do empregador.

Abaixo iremos exemplificar como proceder:

**Cálculo de Férias**

Passo 1 - Criar a fórmula conforme o exemplo abaixo e vincular no evento de código de cálculo 40:

Fórmula - Cálculo 1/3 de Férias

Passo 2: Criar uma fórmula para incluir um evento de base para armazenar o valor de 1/3 de férias que será pago posteriormente.

Fórmula - Base 1/3 de Férias

O evento pode ser incluído no parametrizador como evento adicional para ser lançado automaticamente no recibo de férias

Passo 3 - Calculando as férias, no recibo de férias o evento de CC 40 não será lançado e o evento de Base será lançado com o valor correspondente:

Passo 4: lançar as férias, o evento de Base também será lançado no envelope de pagamento:

**Provisão de Férias**

Após o pagamento das férias, o período aquisitivo é fechado. E mesmos naqueles casos onde não são fechados, o processo de provisão considera somente como devido os avos restantes, não contabilizando o passado. No caso do 1/3 que não foi pago junto com as férias, o sistema não entende que este este debito não contabilizado o valor devido.

Para solucionar este cenário gerando a provisão com o valor devido, poderá usar o recuso disponibilizado no parametrizador, que permite informar uma fórmula para adicionar no valor de férias vencidas ou proporcionais no final da geração da provisão.

Abaixo exemplificarmos uma sugestão de Fórmula para que seja somada na provisão de Férias:

Calculamos e lançamos as férias para o funcionário. Foi lançado somente os dias de férias e não lançamos o adicional de Férias. Para facilitar a identificação do adicional devido, inserimos o evento de base de cálculo no envelope do funcionário com o valor do 1/3 de férias.

No parametrizado, na menu Férias | Fórmulas, inserimos uma fórmula que retorna o valor do 1/3 de férias devido. No nosso exemplo colocamos no campo para somar com férias vencidas:

Na fórmula utilizada, usamos a variável MV que retorna a soma do evento de base de cálculo B099, B198 e B199 pago durante o ano de 2021 e abatemos os eventos de proventos que serão usados para pagar o 1/3 quando for o caso. Assim, quando o pagamento for efetuado o mesmo não será mais somado na provisão. A formula abaixo contem os eventos que foram sugeridos no roteiro de [abono pecuniário](https://tdn.totvs.com/pages/viewpage.action?pageId=615606796) e [rescisão](https://tdn.totvs.com/pages/viewpage.action?pageId=615919977)

Fórmula - Provisão de 1/3 de férias

Ao gerar a provisão, o valor pago de férias foi informado e o valor retornado pelo fórmula somado ao campo de provisão de férias vencidas.

Após o pagamento do 1/3 que será exemplificado no tópico abaixo, a provisão não considerou o valor do 1/3 de férias:

**Pagamento do 1/3 férias**

O pagamento de 1/3 de férias, deverá  ocorrer até dia 20/12, devendo as tributações ocorrer na competência/caixa em que o pagamento for efetuado. 

Outro ponto levantado foi que, caso a realização da remuneração de 1/3 não seja pago antes de vencer o próximo período aquisitivo, irá caracterizar como férias em dobro, devido aquele período não ter sido quitado.

No modulo da Folha de Pagamento, o mesmo pode ser feito usando evento calculado por fórmula e lançado diretamente no envelope do funcionário, através dos processos disponibilizados pelo folha, como Grupo de Eventos, Entrada de dados, Eventos Programados, etc.

Abaixo, exemplificaremos Sugestão de Fórmula:

*lançamento direto no envelope - Grupo de Eventos*

Fórmula para pagamento de 1/3 de Férias. Usando a função MV abaixo irá considerar o evento de Base de Cálculo lançado no envelope acima durante o ano de 2020:

Fórmula - Pagamento de 1/3 de Férias

Criado o evento de provento e inserido a fórmula no campo de valor:

Ao fazer o lançamento dos eventos para a Folha, incluído o evento acima, o mesmo foi calculado:

Para pagamento de Férias em dobro, criamos um exemplo de sugestão de fórmula, que verifica se o valor pendente a se quitado já ultrapassou dois período vencidos de férias, considerando o primeiro dia da competência atual. A Consulta SQL está exemplificada no Pagamento de 1/3 de Férias Vencidas neste [link](https://tdn.totvs.com/pages/viewpage.action?pageId=615919977).

Fórmula - Pagamento de Férias Dobro CHAPA
ENTAO
0
SENAO
SETVAR (QUANTDIAS, SUBTRAIDATAS(MTDATA(01,MES,ANO),FIMPERAQUIS1));
SE QUANTDIAS > 365 E (DATAPGTOFERIAS >= MTDATA(28,04,2021) E DATAPGTOFERIAS <= MTDATA(25,08,2021))
ENTAO
VALOREVENTO \* ARRED(QUANTDIAS/365);
FIMSE;
FIMSE;]]>

Associando a fórmula em um evento:

Lançado o evento de férias em dobro, para um funcionário onde o pagamento foi feito após o vencimento de dois períodos aquisitivos:

*Lançamento usando o processo de Diferença de Férias*

Criamos a fórmula para pagamento de 1/3 de férias:

Fórmula - Pagamento de 1/3 de Férias

Associar a fórmula no evento de diferença e inserir o mesmo em Eventos Adicionais Globais de férias. O evento deve ser do tipo provento e ter prioridade 70.

Executar o processo de diferença de Férias, marcando a opção dissídio não:

Após executar a diferença, foi calculado o evento adicional global com o valor do 1/3 devido:

falseObservação

1. No cadastro do Evento Adicional Global é possível inserir uma fórmula de seleção para que o processo considere somente os funcionários elegíveis ao recebimento da verba adicionada. Orientamos a usar este recurso.
2. Para que seja calculada a tributação exclusiva de IR para férias é necessário marcar a incidência 'IRRF de Férias' no evento acima. O sistema irá lançar o evento de CC 61.
3. Para que seja calculada a Pensão de Férias, é necessário marcar a incidência de pensão Férias. O sistema irá lançar o evento de CC 197 e inserir na movimentação de pensão do dependente o valor correspondente a cada dependente com o tipo de movimentação 5 - Dif. Férias.
4. O valor de diferença (1/3 de férias) é lançado no envelope com o evento de CC 88. Caso queira discriminar o valor do 1/3 de férias em um evento diferente, poderá informar no evento de código 'B101' um evento de diferença de Salário.

**Calculo de Diferença de Férias - Dissídio**

Para o calculo de diferença o produto verifica os eventos lançados no período original para fazer o recalculo. Caso o mesmo não tenha sido lançado, como é o caso do evento de 1/3 (código de cálculo 40), o mesmo não é calculado, mesmo se retirada a fórmula que zera o evento como sugerido neste documento.

Para os casos onde teve evento de base sugerido lançado no recibo de férias para armazenar o valor do 1/3 de férias que será pago até dia 20/12, o mesmo deve ser informado um evento de diferença que irá armazenar o valor. Iremos da uma sugestão que atenda os usuários que lançaram o evento de base no recibo de férias e informaram o evento no parametrizador.

No evento B099, incluir o evento para ser lançado do evento de diferença, também como base:

Ao calcular a diferença para um funcionário que teve o evento B099 lançado no recibo de férias, no calculo da diferença o mesmo é considerado e calculado a diferença, lançando o evento de BD99 com o valor da diferença:

Dica

Caso o entendimento do cliente seja que o evento diferença de 1/3 de férias tenha que ser pago no cálculo da diferença por dissídio e não junto com 1/3 de férias até dia 20/12 conforme determinado na MP 1046, ou no caso do cálculo de uma diferença retroativa ao período de férias após demissão, poderá alterar o tipo do evento para lançar a diferença na folha, 'BD99', para provento.
