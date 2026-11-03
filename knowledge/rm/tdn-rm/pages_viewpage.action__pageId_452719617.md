---
content_hash: 596136faf8e621a828b580da19394c7db92992728c98a03f7e25fe66e2a2f3c6
fetched_at: '2026-06-29T00:10:08.974994+00:00'
page_id: '452719617'
product: rm
source: tdn-rm
title: Cálculo - Rescisão
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719617
version: 8
---

Nesta etapa será definido como será feito o cálculo da rescisão.  
   
**Campos e Parâmetros**  
Utiliza período fixo para rescisão no próximo mês  
Marque este parâmetro caso deseje um período fixo para o lançamento da Rescisão quando Calculada para o próximo mês. Ao marca-lo, será habilitado o campo "Período a ser utilizado para rescisão no próximo mês", que deverá ser preenchido.  
Deixando este parâmetro desmarcado, a rescisão para o próximo mês será calculada no período de livre escolha do usuário.   
   
Inibe lançamento da Indenização Artigo 479 (CC 124) para Menor Aprendiz  
   
   
Lança indenização por tempo de serviço de safrista (Rural)  
Com este parâmetro marcado será lançado no movimento da rescisão do funcionário o evento de Código de Cálculo 379 - INDENIZAÇÃO POR TEMPO DE SERVIÇO DE SAFRISTA e o evento de Código de Cálculo 380 - DIFERENÇA INDENIZAÇÃO TEMPO DE SERVIÇO DE SAFRISTA, conforme o art. 14 da Lei nº 5889/73. Os eventos só serão lançados quando o funcionário é do tipo R - Rural e a rescisão for processada com o tipo T - Término de Contrato de trabalho.  
**Observação**  
Mesmo que o parâmetro não esteja marcado, o sistema valida se o evento de CC 379 está lançado no movimento de rescisão para recalcular e lançar o evento de CC 380.  
   
**Atenção**  
Os eventos de CC 379 e 380 devem está cadastrados na base para o correto funcionamento do parâmetro.   
   
Fórmula para mensagem ao calcular rescisão  
   
   
Lança evento de saldo de salário  
Marque este parâmetro se pretender que o mesmo seja lançado na rescisão automaticamente, ou seja, o correspondente ao número de dias trabalhados entre o fim do período anterior até o dia da demissão do empregado. Quando este parâmetro é marcado é habilitado os campos abaixo, onde será possível selecionar somente um deles:

* *Evento de saldo salário*: Este campo destina-se à seleção de um evento onde será lançado o saldo de salário na rescisão.
* *Fórmula p/ o evento de saldo de salário*: Este campo destina-se à seleção de uma fórmula, que pode conter mais de uma evento a ser considerado para o saldo de salário na rescisão.

**Exemplo**  
SE CREC = 'M'  
ENTAO '0085'  
SENAO '0086'  
FIM SE  
   
Com esta fórmula, se a forma de recebimento for 'M' (mensalista), será considerado o evento "0085", caso contrário assumirá o evento "0086".  
   
**Observação**  
Não marcando esse parâmetro, o próprio usuário deverá lançar o evento na rescisão.  
Recebem verbas rescisórias  
Marque os tipo de funcionário que desejar calcular a rescisão. Os tipos são:

* Autônomos
* Estagiários
* Diretores
* Conselheiros

**Observação**  
Estes parâmetros virão marcados automaticamente e o usuário deverá desmarcar se não desejar calcular a rescisão

Data de Pagamento da Rescisão

Calcular a data de pagamento e último movimento considerando a quantidade de dias informado

Quando o parâmetro estiver marcado, nos processo de Rescisão Individual. Coletiva e Global haverá o preenchimento do campo Data de Pagamento e Data do último movimento considerando a data de desligamento + quantidade de dias informado no campo ‘Quantidade de dias’. 

IMPORTANTE

* A contagem dos dias será feita a partir do dia posterior a data cadastrada na rescisão, ou seja, se a quantidade de dias informado for 1 retornará a data do dia seguinte a demissão, se a quantidade de dias informado for 2 retornará a data de dois dias seguintes à demissão.
* Esse parâmetro estará disponível a partir das versões:
  + 12.1.2402.195
  + 12.1.2406.122
  + 12.1.2410 e superiores

Quando o parâmetro estiver desmarcado, seguirá o fluxo preenchendo os campos com a mesma data de desligamento.

Atenção:

01 - Para rescisão individual não será considerado o parâmetro quando o funcionário tem aviso prévio trabalhado (campo DTAVISOPREVIOTRAB preenchido) ou para o tipo de demissão do tipo 5 e 6 (transferência), conforme entendimento do art. 477, § 6º.

02 - Para os processos de coletivas e global, será validado somente o tipo 5 e 6 que são transferências, visto que teremos N funcionário e alguns podem ter ou não aviso prévio trabalhado.

Quantidade de dias - Ficará habilitado se o parâmetro ‘Calcular a data de pagamento e último movimento considerando a quantidade de dias informado’ estiver marcado. A quantidade de dias informada terá o limite de até 10 dias, conforme a legislação.

Atenção:

01 - O campo ‘Quantidade de dias’ será iniciado com zero quando o parâmetro ‘Calcular a data de pagamento e último movimento considerando a quantidade de dias informado’ estiver marcado. A quantidade de dias a ser preenchida é de responsabilidade do usuário.

02 - Para a data de pagamento calculada quando o parâmetro ‘Calcular a data de pagamento e último movimento considerando a quantidade de dias informado’  estiver marcado será verificado se o dia de pagamento será sábado, domingo ou feriado e preencherá os campos de data de pagamento e ultimo movimento com o dia útil anterior.

Observação:

A data de pagamento e/ou data de último movimento poderá ser alterada pelo usuário, somente será apresentada a mensagem abaixo quando o parâmetro  ‘Calcular a data de pagamento e último movimento considerando a quantidade de dias informado’ estiver marcado:

Para rescisão Individual:

* Caso o usuário queira alterar esta data será permitido apresentando mensagem:

+ “A data de pagamento e/ou último movimento foi alterada pelo usuário e não será considerada a data calculada pelo sistema conforme parametrização.”

Para rescisão Global e Coletiva:

* Caso o usuário queira alterar esta data será permitido e no final do processo apresenta aviso:

+ “A data de pagamento e/ou último movimento foi alterada pelo usuário e não será considerada a data calculada pelo sistema conforme parametrização.”

Em ambos casos de alteração manual pelo usuário, não faremos nenhuma validação se é sábado ou domingo ou se é maior que 10 dias.

---

<<Retornar para **Rescisão**
