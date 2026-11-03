---
content_hash: 1004bc94709f967f9c59b8fd91270bbf51d226d364be4b86eb036c8b76407dfd
fetched_at: '2026-06-29T00:10:38.922156+00:00'
page_id: '545622002'
product: rm
source: tdn-rm
title: MP 936 - Indenização em caso de dispensa sem justa causa no período de adesão
  a MP 936
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=545622002
version: 24
---

A dispensa sem justa causa, que ocorrer durante o período de garantia provisória no emprego, sujeitará o empregador ao pagamento, além das parcelas rescisórias previstas na legislação em vigor, de indenização no valor de :

* 50 % do salário a que o empregado teria direito no período de garantia provisória no emprego, na hipótese de redução de jornada de trabalho e de salário igual ou superior a 25% e inferior a 50%

* 75% do salário a que o empregado teria direito no período de garantia provisória no emprego, na hipótese de redução de jornada de trabalho e de salário igual ou superior por 50% e 75%

* 100 % do salário a que o empregado teria direito no período de garantia provisória no emprego, na hipótese de redução de jornada de trabalho em percentual superior a 70% ou de suspensão temporária de contrato de trabalho.

Não se aplica às hipóteses de dispensa a pedido ou por justa causa do funcionário.

O módulo TOTVS folha de pagamento permite calcular a indenização prevista através de fórmula.

Abaixo exemplificaremos sugestão de fórmulas que calcula a indenização conforme regras de MP 936.

Consulta SQL necessária para executar a Fórmula de Indenização por redução de jornada:

sqlConsulta SQL - Retornar o Histórico do BEM

Fórmula para calcular a indenização quando devida para funcionário que teve redução de salário:

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
SE DataInicioAcordoAnt = DataInicioAcordo
ENTAO SETVAR (DiasDuracao, 0);
FIMSE;
SE DiasProrrogAnt = DiasProrrog
ENTAO SETVAR (DiasProrrog, 0);
FIMSE;
SE DataFimAcordoAnt <> DATANULA
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
SE PercAcodr < 50
ENTAO SETVAR (ValorInd, (SalMensal \* (DiasDuracao/30) \* 0.50));
SENAO
SE PercAcodr < 70
ENTAO SETVAR (ValorInd, (SalMensal \* (DiasDuracao/30) \* 0.75));
SENAO
SE PercAcodr >= 70
ENTAO SETVAR (ValorInd, (SalMensal \* (DiasDuracao/30)));
FIMSE;
FIMSE;
FIMSE;
SETVAR (ValorTotal, ValorTotal+ValorInd);
SETVAR (DuracaoTotal, DuracaoTotal+DiasDuracao);
SETVAR (DataInicioAcordoAnt, DataInicioAcordo);
SETVAR (DiasProrrogAnt, DiasProrrog);
SETVAR (DataFimAcordoAnt, DataFimAcordo);
ATE ProxRegSQL('BEM' ) = Falso
FIMSE;
/\* Abate os dias de Estabilidade que não entra no cálculo da indenização\*/
SE SUBTRAIDATAS (DTD, DataFimAcordo) = DiasDuracao
ENTAO SETVAR (DiasAbatidos, 0);
SENAO
SETVAR (DiasAbatidos, SUBTRAIDATAS (DTD, DataFimAcordo));
FIMSE;
SE DiasAbatidos > 0 E (DuracaoTotal - DiasAbatidos ) > 0;
ENTAO SETVAR (DiasDireito, DuracaoTotal - DiasAbatidos);
SETVAR (ValorTotal, (ValorTotal/DuracaoTotal)\*DiasDireito);
SENAO
ValorTotal;
FIMSE;
FIMSE;
]]>

Fórmula para calcular para calcular a indenização quando devida para funcionário que teve Suspensão temporário de trabalho. Para esta fórmula usaremos a consulta SQL sugerida abaixo:

sqlConsulta SQL - AFASTAMENTOFórmula - Indenização por demissão sem justa causa - Contrato Suspenso '01/01/0001' E TPDEMISSAO = 2
ENTAO
SETVAR (QUANTDIAS, SUBTRAIDATAS(DATAFIM, DATAINICIO));
SE (DATAFIM+QUANTDIAS) > DTD
ENTAO
RC
SENAO
0]]>

Após criadas as fórmulas, associar as mesmas em eventos para serem lançados na rescisão, quando for o caso. Como exemplo, colocamos o o mesmo no parametrizador:

Ao executar o processo de rescisão, o evento é lançado. No envelope abaixo o funcionário tinha estabilidade por Redução de Jornada:

**eSocial**

****Observação:****Disponível a partir das versões 12.1.25.268, 12.1.26.212, 12.1.27.166 e 12.1.28.102

Para o eSocial foi adicionada a natureza de rubrica 6119 - Indenização rescisória – MP 936:   Indenização pela dispensa sem justa causa que ocorrer durante o período de garantia provisória no emprego de que trata o art. 10 da MP 936/2020. Início de validade: 01/04/2020.

Atenção

As verbas rescisórias deve ser calculadas considerando o valor integral, não podendo as verbas de rescisão serem calculadas considerando o salário reduzido mesmo que esteja dentro do período de acordo de redução de jornada/salário.
