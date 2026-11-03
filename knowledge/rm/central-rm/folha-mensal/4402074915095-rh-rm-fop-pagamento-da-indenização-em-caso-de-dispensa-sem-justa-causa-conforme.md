---
article_id: 4402074915095
category: Folha Mensal
content_hash: 8838380e28e005e76f15b47f7d64d982798e10754551c20211c182129e346049
fetched_at: '2026-06-28T22:46:59.381793+00:00'
product: rm
section_id: 1500000861062
source: central-rm
title: RH - RM - FOP - Pagamento da Indenização em caso de dispensa sem justa causa
  conforme MP 1.045/2021
type: support-article
updated_at: '2025-03-12T20:07:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4402074915095-RH-RM-FOP-Pagamento-da-Indeniza%C3%A7%C3%A3o-em-caso-de-dispensa-sem-justa-causa-conforme-MP-1-045-2021
---

**Dúvida**Como realizar o pagamento da indenização em caso de dispensa sem justa causa durante o período de garantia provisória no emprego?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - A partir das versões:

* 12.1.28.293
* 12.1.29.257
* 12.1.31.162
* 12.1.32.104

**Solução**A dispensa sem justa causa, que ocorrer durante o período de garantia provisória no emprego, sujeitará o empregador ao pagamento, além das parcelas rescisórias previstas na legislação em vigor, de indenização no valor de:

* 50 % do salário a que o empregado teria direito no período de garantia provisória no emprego, na hipótese de redução de jornada de trabalho e de salário igual ou superior a 25% e inferior a 50%

* 75% do salário a que o empregado teria direito no período de garantia provisória no emprego, na hipótese de redução de jornada de trabalho e de salário igual ou superior por 50% e 75%

* 100 % do salário a que o empregado teria direito no período de garantia provisória no emprego, na hipótese de redução de jornada de trabalho em percentual superior a 70% ou de suspensão temporária de contrato de trabalho.

**Importante: Não se aplica às hipóteses de dispensa a pedido ou por justa causa do funcionário.**Atualmente o sistema permite o cálculo da indenização prevista através de fórmula. Segue exemplos de sugestão de fórmulas conforme regras de MP 1.045.  
  
**1)** Criar a consulta SQL necessária para executar a Fórmula de Indenização:  
  
**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4402074842135/mceclip0.png)****2)** Cadastrar a fórmula a seguir para calcular a indenização quando devida para funcionário que teve acordos celebrados durante o ano de 2020 e 2021 e com licença posterior a este acordos. A fórmula abate os dias trabalhados entre este acordos:

|  |
| --- |
| mceclip4.png  DECL DataInicioAcordo; DECL DataInicioAcordoAnt; DECL DiasDuracao; DECL DiasProrrog; DECL DiasProrrogAnt; DECL DataCancelamento; DECL DataAntecipacao; DECL DataFimAcordo; DECL DataFimAcordoAnt; DECL PercAcodr; DECL SalMensal; DECL ValorInd; DECL ValorTotal; DECL DuracaoTotal; DECL DiasAbatidos; DECL DiasDireito; DECL TpDemissao; DECL DiasAbatidos2; DECL DiasAbatidosTotal; DECL DataInicAfastLicMater; DECL TpAcordo;     SETVAR (TpDemissao, TABFUNC ('TIPODEMISSAO', ''));  SETVAR (SalMensal, TABFUNC('SALARIO', 'I')); SETVAR (DiasDireito, 1); SETVAR (DataInicioAcordoAnt, DATANULA); SETVAR (DiasProrrogAnt, 0); SETVAR (DataFimAcordoAnt, DATANULA);    SE TpDemissao <> 2; ENTAO 0; SENAO    SE (EXECSQL ('BEM') = FALSO) ENTAO 0; SENAO    /\* Retorna o valor de indenização devido considerando todos acordos\*/ SE (EXECSQL ('BEM') = Verdade) ENTAO REPITA SETVAR (DataInicioAcordo,resultsql('BEM','DTACORDOBEM')); SETVAR (DiasDuracao,resultsql('BEM','DURACAOBEM')); SETVAR (DiasProrrog,resultsql('BEM','DIASPRORROGACAOBEM')); SETVAR (DataCancelamento,resultsql('BEM','DTCANCELAMENTOBEM')); SETVAR (DataAntecipacao,resultsql('BEM','DTANTECIPACAOBEM')); SETVAR (PercAcodr,resultsql('BEM','PERCENTUALREDUCAOBEM')); SETVAR (TpAcordo, resultsql('BEM', 'TIPOADESAOBEM'));    SE DataInicioAcordoAnt = DataInicioAcordo ENTAO SETVAR (DiasDuracao, 0); FIMSE; SE DiasProrrogAnt = DiasProrrog ENTAO SETVAR (DiasProrrog, 0); FIMSE; SE (DataFimAcordoAnt <> DATANULA) E (DataInicioAcordo = DataInicioAcordoAnt); ENTAO SETVAR (DataFimAcordo, (DataFimAcordoAnt + DiasDuracao+ DiasProrrog)); SENAO SETVAR (DataFimAcordo, DataInicioAcordo + DiasDuracao + DiasProrrog) FIMSE;    SE DataAntecipacao <> DATANULA ENTAO SETVAR (DiasDuracao, (SUBTRAIDATAS ((DataAntecipacao+1),DataFimAcordo))); FIMSE; SE DataCancelamento <> DATANULA ENTAO SETVAR (DiasDuracao, (SUBTRAIDATAS ((DataCancelamento+1), DataFimAcordo))); FIMSE;    SETVAR (DiasDuracao, (DiasDuracao+DiasProrrog));   SE DataFimAcordoAnt = DATANULA OU DataInicioAcordo = DataInicioAcordoAnt; ENTAO 0 SENAO SETVAR (DiasAbatidos2, (SUBTRAIDATAS(((DataFimAcordo-DiasDuracao)-1),DataFimAcordoAnt))); FIMSE; FIMSE;    SE PercAcodr < 50 E TpAcordo = 1 ENTAO SETVAR (ValorInd, (SalMensal \* (DiasDuracao/30) \* 0.50)); SENAO SE PercAcodr < 70 E TpAcordo = 1 ENTAO SETVAR (ValorInd, (SalMensal \* (DiasDuracao/30) \* 0.75)); SENAO SE PercAcodr >= 70 OU TpAcordo = 0 ENTAO SETVAR (ValorInd, (SalMensal \* (DiasDuracao/30))); FIMSE; FIMSE; FIMSE;     SETVAR (ValorTotal, ValorTotal+ValorInd); SETVAR (DuracaoTotal, DuracaoTotal+DiasDuracao); SETVAR (DataInicioAcordoAnt, DataInicioAcordo); SETVAR (DiasProrrogAnt, DiasProrrog); SETVAR (DataFimAcordoAnt, DataFimAcordo); SETVAR (DiasAbatidosTotal, DiasAbatidosTotal+DiasAbatidos2);     ATE ProxRegSQL('BEM' ) = Falso FIMSE;   SETVAR (DataInicAfastLicMater, (FOR ('LICMATER'))); SE (DataInicAfastLicMater <> DATANULA) E (DataInicAfastLicMater >= DataFimAcordo); ENTAO SETVAR (DataFimAcordo, (DataFimAcordo+150)); FIMSE;   /\* Abate os dias de Estabilidade que não entra no cálculo da indenização\*/ SE  SUBTRAIDATAS (DTD, DataFimAcordo) = DiasDuracao ENTAO SETVAR (DiasAbatidos, 0); SENAO SETVAR (DiasAbatidos, SUBTRAIDATAS (DTD, DataFimAcordo)); FIMSE;   SE (DataInicAfastLicMater <> DATANULA) E ((DataInicAfastLicMater +150) >= DataFimAcordo) E (DuracaoTotal - DiasAbatidos - DiasAbatidosTotal) > 0 ENTAO SETVAR (DiasDireito, DuracaoTotal - DiasAbatidos - DiasAbatidosTotal); SETVAR (ValorTotal, (ValorTotal/DuracaoTotal)\* DiasDireito); SENAO SE DiasAbatidos > 0 E (DuracaoTotal - DiasAbatidos - DiasAbatidosTotal) > 0; ENTAO SETVAR (DiasDireito, DuracaoTotal - DiasAbatidos - DiasAbatidosTotal); SETVAR (ValorTotal, (ValorTotal/DuracaoTotal)\* DiasDireito); SENAO ValorTotal; FIMSE; FIMSE; |

**3)** Após criadas as fórmulas, deverão associar as mesmas a eventos para serem lançados na rescisão, quando for o caso. Como exemplo, colocamos o mesmo no parametrizador:  
  
![](https://tdn.totvs.com/download/attachments/621210931/image2021-5-31_13-48-6.png?version=1&modificationDate=1622479686800&api=v2)  
  
**4)** Ao executar o processo de rescisão, o evento é lançado:  
  
![](https://tdn.totvs.com/download/attachments/621210931/image2021-5-31_13-49-55.png?version=1&modificationDate=1622479795063&api=v2)  
  
**eSocial**Para o eSocial foi adicionada a natureza de rubrica 6119 - Indenização rescisória - Lei 14.020/2020:   Indenização pela dispensa sem justa causa que ocorrer durante o período de garantia provisória no emprego. Início de validade: 01/04/2020.  
  
![](https://tdn.totvs.com/download/attachments/621210931/image2021-5-31_13-51-0.png?version=1&modificationDate=1622479860890&api=v2)  
  
![](https://tdn.totvs.com/download/attachments/621210931/image2021-5-31_13-56-31.png?version=1&modificationDate=1622480191947&api=v2)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4402064063639/mceclip1.png)  
  
**Saiba mais:** [Indenização em caso de dispensa sem justa causa](https://tdn.totvs.com/pages/releaseview.action?pageId=621210931)
