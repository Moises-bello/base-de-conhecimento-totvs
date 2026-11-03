---
content_hash: c5b5fdbafb665aefeb899293ed6b22a4251f51c86f41c438541d9e8e997daecb
fetched_at: '2026-06-29T00:10:35.519553+00:00'
page_id: '531010306'
product: rm
source: tdn-rm
title: Movimento - Rescisão
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=531010306
version: 29
---

Ocorrendo extinção do Contrato de Trabalho Verde e Amarelo, serão devidos:

* do saldo de salário e demais parcelas salariais, com base no valor do salário mensal no mês da rescisão;
* das parcelas de férias proporcionais com acréscimo de um terço e do décimo-terceiro que não tenham sido antecipadas;
* do aviso prévio indenizado, quando for o caso; e
* da indenização sobre o saldo do FGTS, caso não tenha sido acordada a sua antecipação, em conta vinculada do trabalhador, em caso de rescisão antes do término da vigência do contrato, por iniciativa do empregador;

Não se aplica a indenização prevista no art. 479 CLT que trata da indenização por metade, da remuneração a que teria direito até o termo do contrato.

A ocorrência de rescisão com férias pendentes de gozo ou com período aquisitivo incompleto não muda a natureza remuneratória dos valores pagos mensalmente.

### **ALTERAÇÃO NO PRODUTO TOTVS FOLHA DE PAGAMENTO**

Para o cálculo de rescisão, algumas verbas são devidas conforme especificado acima. Outras no entanto são antecipadas juntamente com a remuneração mensal como 13º Salário e Férias.  Desta forma fizemos a adequação do processo de rescisão para não calcular as verbas de 13ª Salário e Férias na demissão do Funcionário de Contrato Verde e Amarelo.

Ao calcular a rescisão, não é lançado nenhum provento/desconto no envelope, sendo lançado somente o eventos de base de Saldo de FGTS e a multa rescisória sobre o saldo, quando é caso:

Orientamos os clientes que ao calcularem a Rescisão a lançarem os eventos orientados no  na rescisão se os mesmos forem devidos, usando uma das opções: Entrada de movimento, Grupo de eventos, Código Fixos, Eventos Programados, Incluir no Envelope de Pagamento, Importação de Movimento ou inserir nos Eventos Adicionais no parametrizador.

Abaixo exemplificaremos como proceder, usando a opção do parametrizador:

* Funcionário admitido em 02/01 e demissão em 30/04, por termino de contrato. O mesmo não tem antecipação de multa rescisória pago junto com a remuneração mensal:

 

 Ao fazer o cálculo da rescisão os eventos adicionais são lançados:

Os eventos de FGTS Quitação, FGTS Artigo 22 e FGTS 13º Salário são calculados considerando os eventos lançados:

* Funcionário com admissão dia 02/01 e demissão dia 30/04 por termino de Contrato. O funcionário teve antecipação de multa rescisória paga junto com a remuneração mensal.

Neste caso orientamos não informar o saldo de FGTS no cadastro do Funcionário, para que não seja calculado o evento de CC 33 - Saldo FGTS no Banco e o mesmo não seja considerado no cálculo da multa rescisória - evento de CC 28 - FGTS Artigo 22:

A multa rescisória foi calculada considerando os eventos lançados. o Evento de Saldo FGTS Banco não foi lançado:

* Funcionário admitido dia 02/01 e demitido dia 01/04 por antecipação por termino de contrato com aviso prévio indenizado.

 

Neste caso, como é devido o pagamento de Aviso prévio indenizado, o processo irá calcular o aviso prévio indenizado automaticamente.

No envelope é lançado o evento de CC 62 - Aviso prévio indenizado. Mas os eventos de 13º Salário indenizado (CC 71) e Férias proporcionais (CC 25) não são calculados automaticamente. Neste caso orientamos a incluir os mesmos para serem lançados pelo usuário calculados por fórmula:

***Exemplo de Fórmula para o cálculo de férias e  13º Salário sobre o aviso prévio:***

DECL DIASAVISO;  
SETVAR (DIASAVISO, TABFUNC('NRODIASAVISO', ''));  
SE TABFUNC ('TEMAVISOPREVIO','1')  
ENTAO  
((RC/12)/30)\*DIASAVISO  
SENAO  
0

***Exemplo de Fórmula para o cálculo de 1/3 de férias sobre aviso prévio:***

C('7030')/3

Conforme a exemplificação usando eventos adicionais no parametrizador, foi incluído os eventos de 13º Salário indenizado sobre aviso prévio e os eventos de Férias e 1/3 de Férias sobre o aviso prévio:

Ao calcular a rescisão, os eventos são lançados conforme abaixo:

E os eventos de FGTS foram calculados conforme os eventos lançados acima:

Indenização prevista no art. 479

Para que o sistema não calcule a indenização por antecipação de contrato de trabalho conforme previsto no art. 479 da CLT e calcule o aviso prévio quando devido, é necessário marcar a flag ' Contém cláusula assecuratória' conforme orientado no [Cadastro do Funcionários](https://tdn.totvs.com/pages/viewpage.action?pageId=528465156).
