---
article_id: 4402064259351
category: Administração de Pessoal
content_hash: 4d804d03badfa5009b4b8e20dd497813a65a8e221340feea5632c1827b1c7997
fetched_at: '2026-06-28T22:47:02.143998+00:00'
product: rm
section_id: 1500000861042
source: central-rm
title: RH - RM - FOP - Parametrização dos avisos de estabilidade conforme MP 1.045/2021
type: support-article
updated_at: '2025-03-13T11:22:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4402064259351-RH-RM-FOP-Parametriza%C3%A7%C3%A3o-dos-avisos-de-estabilidade-conforme-MP-1-045-2021
---

**Dúvida**Como parametrizar o sistema para que o mesmo me informe que determinado funcionário possui estabilidade conforme MP?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - A partir das versões:

* 12.1.28.293
* 12.1.29.257
* 12.1.31.162
* 12.1.32.104

Fica reconhecida a garantia provisória no emprego ao funcionário que receber o benefício emergencial de preservação do emprego e da renda. Em decorrência da redução da jornada de trabalho e de salário ou da suspensão temporária do contrato de trabalho, nos seguintes termos:

* Durante o período de acordado de redução da jornada de trabalho e de salário ou de suspensão temporária do contrato de trabalho;
* Após o restabelecimento da jornada de trabalho e de salário ou encerramento da suspensão temporária do contrato de trabalho, por período equivalente ao acordado para a redução ou a suspensão;
* No caso de empregada gestante, por período equivalente ao acordado com a redução da Jornada de trabalho e do salário ou para a suspensão temporário do contrato de trabalho, contado da data do termino do período de garantia estabelecida na [alínea "b" do inciso II do **caput** do art. 10 do Ato das Disposições Constitucionais Transitórias](http://www.planalto.gov.br/ccivil_03/constituicao/constituicaocompilado.htm#adct).

A dispensa sem justa causa, que ocorrer durante o período de garantia provisória no emprego, sujeitará o empregador ao pagamento, além das parcelas rescisórias previstas na legislação em vigor, de indenização que serão documentadas neste tópico: **[RH - RM - FOP - Pagamento da Indenização em caso de dispensa sem justa causa conforme MP 1.045/2021](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4402074915095)**

Os prazos da garantia provisória no emprego decorrente dos acordos de redução proporcional de jornada e de salário ou de suspensão de contrato de trabalho de que trata o[art. 10 da Lei nº 14.020, de 6 de julho de 2020](http://www.planalto.gov.br/ccivil_03/_ato2019-2022/2020/lei/L14020.htm#view), ficarão suspensos durante o recebimento do Benefício Emergencial de Manutenção do Emprego e da Renda e somente retomarão a sua contagem após o encerramento do período da garantia de emprego de que trata este artigo. Pode-se configurar mensagens de aviso para informar se o funcionário possui estabilidade nos termos estabelecidos na MP via fórmula e também é possível fazer o controle através de Fórmulas Visuais.

Abaixo, exemplificaremos com a sugestão de fórmulas de aviso configurada no parametrizador.

**1)** Utilizar a mesma consulta SQL abaixo para retornar o histórico do BEM. Também será necessário cadastrar uma consulta SQL para retornar os afastamentos de Licença Maternidade iniciados após a publicação da MP 1045:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4402063716247/mceclip1.png)  
  
**2)** Criar uma fórmula que valias as condições de estabilidade para redução de Jornada/Salario. Abaixo um exemplo de fórmula que retorna mensagens conforme as regras da MP 936:

|  |
| --- |
| DECL DataInicioAcordo; DECL DiasDuracao; DECL DiasProrrog; DECL DataCancelamento; DECL DataAntecipacao; DECL DataFimAcordo; DECL DuracaoTotal; DECL DataInicioAcordoAnt; DECL DiasAbatidos; DECL DiasAbatidosTotal; DECL DataInicAfastLicMater;      SETVAR (DataInicioAcordoAnt, DATANULA); SETVAR (DataFimAcordo, DATANULA);      SE (EXECSQL ('BEM') = FALSO) ENTAO 'FUNCIONÁRIO SEM ESTABILIDADE POR REDUÇÃO DE JORNADA/SALÁRIO OU SUSPENSÃO DE CONTRATO CONFORME MP 936.'; SENAO    /\* Retorna a quantidade total de dias de acordo por redução de Jornada\*/ SE (EXECSQL ('BEM') = Verdade); REPITA SETVAR (DataInicioAcordo,resultsql('BEM','DTACORDOBEM')); SETVAR (DiasDuracao,resultsql('BEM','DURACAOBEM')); SETVAR (DiasProrrog,resultsql('BEM','DIASPRORROGACAOBEM')); SETVAR (DataCancelamento,resultsql('BEM','DTCANCELAMENTOBEM')); SETVAR (DataAntecipacao,resultsql('BEM','DTANTECIPACAOBEM'));     SE DataAntecipacao <> DATANULA ENTAO SETVAR (DiasDuracao, (SUBTRAIDATAS (DataAntecipacao, DataInicioAcordo))); FIMSE; SE DataCancelamento <> DATANULA ENTAO SETVAR (DiasDuracao, (SUBTRAIDATAS (DataCancelamento, DataInicioAcordo))); FIMSE;      SE DataInicioAcordo = DataInicioAcordoAnt; SETVAR (DiasDuracao, DiasProrrog); FIMSE;   SE DataFimAcordo = DATANULA OU DataInicioAcordo = DataInicioAcordoAnt; ENTAO 0 SENAO SETVAR (DiasAbatidos, (SUBTRAIDATAS(DataInicioAcordo,DataFimAcordo+1))); FIMSE;      SETVAR (DataFimAcordo, DataInicioAcordo+DiasDuracao+DiasProrrog); SETVAR (DuracaoTotal, DuracaoTotal+DiasDuracao); SETVAR (DataInicioAcordoAnt, DataInicioAcordo); SETVAR (DiasAbatidosTotal, DiasAbatidosTotal+DiasAbatidos);       ATE ProxRegSQL('BEM') = Falso FIMSE;   SETVAR (DataInicAfastLicMater, (FOR ('LICMATER')));    SE DataFimAcordo = (DataInicioAcordo + DuracaoTotal-DiasAbatidosTotal); SETVAR (DataFimAcordo, DataInicioAcordo + DuracaoTotal-DiasAbatidosTotal); FIMSE;      SE (DataInicAfastLicMater <> DATANULA) E (DataInicAfastLicMater >= DataFimAcordo) E (DataFimAcordo+DuracaoTotal+150-DiasAbatidosTotal) > MTDATA(01,MES,ANO) ENTAO CONCAT ('FUNCIONÁRIO POSSUÍ ESTABILIDADE POR REDUÇÃO DE JORNADA/SALÁRIO OU SUSPENSÃO DE CONTRATO COM PRORROGAÇÃO DEVIDO A LICENÇA MATERNIDADE ATÉ ', DataFimAcordo+DuracaoTotal-DiasAbatidosTotal+150); SENAO SE (DataFimAcordo + DuracaoTotal-DiasAbatidosTotal) > MTDATA(01,MES,ANO) ENTAO CONCAT ('FUNCIONÁRIO POSSUÍ ESTABILIDADE POR REDUÇÃO DE JORNADA/SALÁRIO OU SUSPENSÃO DE CONTRATO ATÉ ', DataFimAcordo+DuracaoTotal-DiasAbatidosTotal); SENAO 'FUNCIONÁRIO SEM ESTABILIDADE POR REDUÇÃO DE JORNADA/SALÁRIO OU SUSPENSÃO DE CONTRATO CONFORME MP 936.' FIMSE; FIMSE; |

**3)** No parametrizador, menu Rescisão | Cálculo, inserir a fórmula no campo 'Fórmula para Mensagem ao calcular a rescisão:  
  
![](https://tdn.totvs.com/download/attachments/621208202/image2021-5-30_22-45-48.png?version=1&modificationDate=1622425548253&api=v2)  
  
Ao clicar no ícone Rescisão, a mensagem será exibida conforme a estabilidade do funcionário. No exemplo abaixo, o funcionário teve redução de Jornada/Salário e suspensão do contrato de trabalho durante o ano de 2020 e 2021, totalizando 270 dias. Porém foi desconsiderado os períodos onde o mesmo não tinha acordos conforme a MP 936 e/ou 1045. A soma destes dias é feita no final do ultimo acordo celebrado entre o empregado e empregador. A mensagem retornou a data fim da estabilidade devida para este funcionário, conforme a regra acima.   
  
![](https://tdn.totvs.com/download/attachments/621208202/image2021-5-30_22-48-39.png?version=1&modificationDate=1622425719040&api=v2)  
  
Quando o funcionário tem licença maternidade iniciando após a publicação da MP 1045 e possui acordos de redução de jornada/salário ou suspensão de contrato anteriores à licença maternidade, é feita a validação destes dias para considerar o período de estabilidade por afastamento de licença maternidade, prorrogando o período de estabilidade garantida:  
  
![](https://tdn.totvs.com/download/attachments/621208202/image2021-5-30_22-51-35.png?version=1&modificationDate=1622425895800&api=v2)

![](https://tdn.totvs.com/download/attachments/621208202/image2021-5-30_22-54-12.png?version=1&modificationDate=1622426052433&api=v2)

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4402063795479/mceclip3.png)
