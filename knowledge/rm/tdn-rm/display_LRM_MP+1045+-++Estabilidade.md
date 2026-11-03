---
content_hash: ff2ae0085165b31be44eaa2720bfafdf24e7cc9873d79e0b857f306678eb5fde
fetched_at: '2026-06-29T00:11:03.357508+00:00'
page_id: '621208202'
product: rm
source: tdn-rm
title: MP 1045 -  Estabilidade
type: documentation
url: https://tdn.totvs.com/display/LRM/MP+1045+-++Estabilidade
version: 8
---

Fica reconhecida a garantia provisória no emprego ao funcionário que receber o benefício emergencial de preservação do emprego e da renda. Em decorrência da redução da jornada de trabalho e de salário ou da suspensão temporária do contrato de trabalho, nos seguintes termos :

* Durante o período de acordado de redução da jornada de trabalho e de salário ou de suspensão temporária do contrato de trabalho
* Após o restabelecimento da jornada de trabalho e de salário ou encerramento da suspensão temporária do contrato de trabalho, por período equivalente ao acordado para a redução ou a suspensão.
* No caso de empregada gestante, por período equivalente ao acordado com a redução da Jornada de trabalho e do salário ou para a suspensão temporário do contrato de trabalho, contado da data do termino do período de garantia estabelecida na [alínea "b" do inciso II do **caput** do art. 10 do Ato das Disposições Constitucionais Transitórias](http://www.planalto.gov.br/ccivil_03/constituicao/constituicaocompilado.htm#adct).

A dispensa sem justa causa, que ocorrer durante o período de garantia provisória no emprego, sujeitará o empregador ao pagamento, além das parcelas rescisórias previstas na legislação em vigor, de indenização que serão documentadas [aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=621210931)

Os prazos da garantia provisória no emprego decorrente dos acordos de redução proporcional de jornada e de salário ou de suspensão de contrato de trabalho de que trata o[art. 10 da Lei nº 14.020, de 6 de julho de 2020](http://www.planalto.gov.br/ccivil_03/_ato2019-2022/2020/lei/L14020.htm#view), ficarão suspensos durante o recebimento do Benefício Emergencial de Manutenção do Emprego e da Renda e somente retomarão a sua contagem após o encerramento do período da garantia de emprego de que trata este artigo.

O módulo TOTVS Folha de Pagamento permite configurar mensagens de aviso para informar se o funcionário possui estabilidade nos termos estabelecidos na MP. Também é possível fazer o controle através de Fórmulas Visuais.

Abaixo, exemplificaremos com a sugestão de fórmulas de aviso configurada no parametrizador.

**Passo 1:**Utilizar a mesma consulta SQL abaixo para retornar o histórico do BEM. Também será necessário cadastrar uma consulta SQL para retornar os afastamentos de Licença Maternidade iniciados após a publicação da MP 1045:

sqlSQL - Retorna registros do Histórico do BEM de tipo de adesão Redução de Jornada de TrabalhosqlSQL - Afastamento Licença Maternidade= '28/04/2021' AND PFHSTAFT.CHAPA=:FRM\_CHAPA AND PFHSTAFT.CODCOLIGADA=:FRM\_COLIGADA]]>

**Passo 2**:

Fórmula que retorna a data de Inicio da Licença Maternidade. A mesma será chamada na fórmula para o da Estabilidade com o Código 'LICMATER':

Retorna data Início de Licença Maternidade

Criar uma fórmula que valida as condições de estabilidade. Abaixo um exemplo de fórmula que retorna mensagens conforme as regras da MP 1045:

Fórmula - Estabilidade de Redução de Jornada/Salário DATANULA
ENTAO SETVAR (DiasDuracao, (SUBTRAIDATAS (DataAntecipacao, DataInicioAcordo)));
FIMSE;
SE DataCancelamento <> DATANULA
ENTAO SETVAR (DiasDuracao, (SUBTRAIDATAS (DataCancelamento, DataInicioAcordo)));
FIMSE;
SE DataInicioAcordo = DataInicioAcordoAnt;
SETVAR (DiasDuracao, DiasProrrog);
FIMSE;
SE DataFimAcordo = DATANULA OU DataInicioAcordo = DataInicioAcordoAnt;
ENTAO 0
SENAO
SETVAR (DiasAbatidos, (SUBTRAIDATAS(DataInicioAcordo,DataFimAcordo+1)));
FIMSE;
SETVAR (DataFimAcordo, DataInicioAcordo+DiasDuracao+DiasProrrog);
SETVAR (DuracaoTotal, DuracaoTotal+DiasDuracao);
SETVAR (DataInicioAcordoAnt, DataInicioAcordo);
SETVAR (DiasAbatidosTotal, DiasAbatidosTotal+DiasAbatidos);
ATE ProxRegSQL('BEM') = Falso
FIMSE;
SETVAR (DataInicAfastLicMater, (FOR ('LICMATER')));
SE DataFimAcordo = (DataInicioAcordo + DuracaoTotal-DiasAbatidosTotal);
SETVAR (DataFimAcordo, DataInicioAcordo + DuracaoTotal-DiasAbatidosTotal);
FIMSE;
SE (DataInicAfastLicMater <> DATANULA) E (DataInicAfastLicMater >= DataFimAcordo) E (DataFimAcordo+DuracaoTotal+150-DiasAbatidosTotal) > MTDATA(01,MES,ANO)
ENTAO
CONCAT ('FUNCIONÁRIO POSSUÍ ESTABILIDADE POR REDUÇÃO DE JORNADA/SALÁRIO OU SUSPENSÃO DE CONTRATO COM PRORROGAÇÃO DEVIDO A LICENÇA MATERNIDADE ATÉ ', DataFimAcordo+DuracaoTotal-DiasAbatidosTotal+150);
SENAO
SE (DataFimAcordo + DuracaoTotal-DiasAbatidosTotal) > MTDATA(01,MES,ANO)
ENTAO
CONCAT ('FUNCIONÁRIO POSSUÍ ESTABILIDADE POR REDUÇÃO DE JORNADA/SALÁRIO OU SUSPENSÃO DE CONTRATO ATÉ ', DataFimAcordo+DuracaoTotal-DiasAbatidosTotal);
SENAO
'FUNCIONÁRIO SEM ESTABILIDADE POR REDUÇÃO DE JORNADA/SALÁRIO OU SUSPENSÃO DE CONTRATO CONFORME MP 936.'
FIMSE;
FIMSE;
]]>

**Passo 3**: No parametrizador, menu Rescisão | Cálculo, inserir a fórmula no campo 'Fórmula para Mensagem ao calcular a rescisão':

Ao clicar Clicar no ícone Rescisão, a mensagem será exibida conforme a estabilidade do funcionário. No exemplo abaixo, o funcionário  teve redução de Jornada/Salário, e suspensão do contrato de trabalho durante o ano de 2020 e 2021, totalizando 270 dias. Porém foi desconsiderado os períodos onde o mesmo não tinha acordos conforme a MP 936 e/ou 1045. A soma destes dias é feita no final do ultimo acordo celebrado entre o empregado e empregador. A mensagem retornou a data fim da estabilidade devida para este funcionário, conforme a regra acima.

Quando o funcionário tem licença Maternidade iniciando após a publicação da MP 1045 e possui acordos de redução de jornada/salário ou suspensão de contrato anteriores a licença Maternidade, é feito a validação destes dias, para considerar o período de estabilidade por afastamento de licença maternidade, prorrogando o período de estabilidade garantida:

Observação

A mensagem configurada acima não impede a rescisão, sendo somente informativa.
