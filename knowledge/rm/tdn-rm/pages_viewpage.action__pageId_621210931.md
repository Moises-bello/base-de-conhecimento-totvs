---
content_hash: 910f486f5c4505fcfa7df6939bb0e10a64e693fa83550c976aa30f8f2b3d87d1
fetched_at: '2026-06-29T00:11:03.365021+00:00'
page_id: '621210931'
product: rm
source: tdn-rm
title: MP 1045 - Indenização em caso de dispensa sem justa causa
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=621210931
version: 6
---

A dispensa sem justa causa, que ocorrer durante o período de garantia provisória no emprego, sujeitará o empregador ao pagamento, além das parcelas rescisórias previstas na legislação em vigor, de indenização no valor de :

* 50 % do salário a que o empregado teria direito no período de garantia provisória no emprego, na hipótese de redução de jornada de trabalho e de salário igual ou superior a 25% e inferior a 50%

* 75% do salário a que o empregado teria direito no período de garantia provisória no emprego, na hipótese de redução de jornada de trabalho e de salário igual ou superior por 50% e 75%

* 100 % do salário a que o empregado teria direito no período de garantia provisória no emprego, na hipótese de redução de jornada de trabalho em percentual superior a 70% ou de suspensão temporária de contrato de trabalho.

Não se aplica às hipóteses de dispensa a pedido ou por justa causa do funcionário.

O módulo TOTVS folha de pagamento permite calcular a indenização prevista através de fórmula.

Abaixo exemplificaremos sugestão de fórmulas que calcula a indenização conforme regras de MP 1045

Consulta SQL necessária para executar a Fórmula de Indenização:

sqlConsulta SQL - Retornar o Histórico do BEMsqlSQL - Afastamento Licença Maternidade= '28/04/2021' AND PFHSTAFT.CHAPA=:FRM\_CHAPA AND PFHSTAFT.CODCOLIGADA=:FRM\_COLIGADA]]>

Fórmula que retorna a data de Inicio da Licença Maternidade. A mesma será chamada na fórmula para o cálculo de Indenização por dispensa sem justa causa com o Código 'LICMATER':

Retorna data Início de Licença Maternidade

Fórmula para calcular a indenização quando devida para funcionário que teve acordos celebrados durante o ano de 2020 e 2021 e com Licença posterior a este acordos. A Fórmula abate os dias trabalhados entre este acordos:

Fórmula - Indenização por dispensa sem justa causa - redução de Jornada 2;
ENTAO 0;
SENAO
SE (EXECSQL ('BEM') = FALSO)
ENTAO 0;
SENAO
/\* Retorna o valor de indenização devido considerando todos acordos\*/
SE (EXECSQL ('BEM') = Verdade)
ENTAO
REPITA
SETVAR (DataInicioAcordo,resultsql('BEM','DTACORDOBEM'));
SETVAR (DiasDuracao,resultsql('BEM','DURACAOBEM'));
SETVAR (DiasProrrog,resultsql('BEM','DIASPRORROGACAOBEM'));
SETVAR (DataCancelamento,resultsql('BEM','DTCANCELAMENTOBEM'));
SETVAR (DataAntecipacao,resultsql('BEM','DTANTECIPACAOBEM'));
SETVAR (PercAcodr,resultsql('BEM','PERCENTUALREDUCAOBEM'));
SETVAR (TpAcordo, resultsql('BEM', 'TIPOADESAOBEM'));
SE DataInicioAcordoAnt = DataInicioAcordo
ENTAO SETVAR (DiasDuracao, 0);
FIMSE;
SE DiasProrrogAnt = DiasProrrog
ENTAO SETVAR (DiasProrrog, 0);
FIMSE;
SE (DataFimAcordoAnt <> DATANULA) E (DataInicioAcordo = DataInicioAcordoAnt);
ENTAO SETVAR (DataFimAcordo, (DataFimAcordoAnt + DiasDuracao+ DiasProrrog));
SENAO
SETVAR (DataFimAcordo, DataInicioAcordo + DiasDuracao + DiasProrrog)
FIMSE;
SE DataAntecipacao <> DATANULA
ENTAO SETVAR (DiasDuracao, (SUBTRAIDATAS ((DataAntecipacao+1),DataFimAcordo)));
FIMSE;
SE DataCancelamento <> DATANULA
ENTAO SETVAR (DiasDuracao, (SUBTRAIDATAS ((DataCancelamento+1), DataFimAcordo)));
FIMSE;
SETVAR (DiasDuracao, (DiasDuracao+DiasProrrog));
SE DataFimAcordoAnt = DATANULA OU DataInicioAcordo = DataInicioAcordoAnt;
ENTAO 0
SENAO
SETVAR (DiasAbatidos2, (SUBTRAIDATAS(((DataFimAcordo-DiasDuracao)-1),DataFimAcordoAnt)));
FIMSE;
FIMSE;
SE PercAcodr < 50 E TpAcordo = 1
ENTAO SETVAR (ValorInd, (SalMensal \* (DiasDuracao/30) \* 0.50));
SENAO
SE PercAcodr < 70 E TpAcordo = 1
ENTAO SETVAR (ValorInd, (SalMensal \* (DiasDuracao/30) \* 0.75));
SENAO
SE PercAcodr >= 70 OU TpAcordo = 0
ENTAO SETVAR (ValorInd, (SalMensal \* (DiasDuracao/30)));
FIMSE;
FIMSE;
FIMSE;
SETVAR (ValorTotal, ValorTotal+ValorInd);
SETVAR (DuracaoTotal, DuracaoTotal+DiasDuracao);
SETVAR (DataInicioAcordoAnt, DataInicioAcordo);
SETVAR (DiasProrrogAnt, DiasProrrog);
SETVAR (DataFimAcordoAnt, DataFimAcordo);
SETVAR (DiasAbatidosTotal, DiasAbatidosTotal+DiasAbatidos2);
ATE ProxRegSQL('BEM' ) = Falso
FIMSE;
SETVAR (DataInicAfastLicMater, (FOR ('LICMATER')));
SE (DataInicAfastLicMater <> DATANULA) E (DataInicAfastLicMater >= DataFimAcordo);
ENTAO
SETVAR (DataFimAcordo, (DataFimAcordo+150));
FIMSE;
/\* Abate os dias de Estabilidade que não entra no cálculo da indenização\*/
SE SUBTRAIDATAS (DTD, DataFimAcordo) = DiasDuracao
ENTAO SETVAR (DiasAbatidos, 0);
SENAO
SETVAR (DiasAbatidos, SUBTRAIDATAS (DTD, DataFimAcordo));
FIMSE;
SE (DataInicAfastLicMater <> DATANULA) E ((DataInicAfastLicMater +150) >= DataFimAcordo) E (DuracaoTotal - DiasAbatidos - DiasAbatidosTotal) > 0
ENTAO SETVAR (DiasDireito, DuracaoTotal - DiasAbatidos - DiasAbatidosTotal);
SETVAR (ValorTotal, (ValorTotal/DuracaoTotal)\* DiasDireito);
SENAO
SE DiasAbatidos > 0 E (DuracaoTotal - DiasAbatidos - DiasAbatidosTotal) > 0;
ENTAO SETVAR (DiasDireito, DuracaoTotal - DiasAbatidos - DiasAbatidosTotal);
SETVAR (ValorTotal, (ValorTotal/DuracaoTotal)\* DiasDireito);
SENAO
ValorTotal;
FIMSE;
FIMSE;
]]>

Após criadas as fórmulas, associar as mesmas em eventos para serem lançados na rescisão, quando for o caso. Como exemplo, colocamos o mesmo no parametrizador:

Ao executar o processo de rescisão, o evento é lançado:

**eSocial**

Para o eSocial foi adicionada a natureza de rubrica 6119 - Indenização rescisória - Lei 14.020/2020:   Indenização pela dispensa sem justa causa que ocorrer durante o período de garantia provisória no emprego. Início de validade: 01/04/2020.

Atenção

As verbas rescisórias deve ser calculadas considerando o valor integral, não podendo as verbas de rescisão serem calculadas considerando o salário reduzido mesmo que esteja dentro do período de acordo de redução de jornada/salário.
