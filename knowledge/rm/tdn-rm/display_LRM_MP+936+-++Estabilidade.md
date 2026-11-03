---
content_hash: b42ffd7796d3eb2e26709a5386cb45ab23a07118a619bbcf0358c8824dd31d51
fetched_at: '2026-06-29T00:10:38.917977+00:00'
page_id: '545621924'
product: rm
source: tdn-rm
title: MP 936 -  Estabilidade
type: documentation
url: https://tdn.totvs.com/display/LRM/MP+936+-++Estabilidade
version: 23
---

Fica reconhecida a garantia provisória no emprego ao funcionário que receber o benefício emergencial de preservação do emprego e da renda. Em decorrência da redução da jornada de trabalho e de salário ou da suspensão temporária do contrato de trabalho, nos seguintes termos :

* Durante o período de acordado de redução da jornada de trabalho e de salário ou de suspensão temporária do contrato de trabalho
* Após o restabelecimento da jornada de trabalho e de salário ou encerramento da suspensão temporária do contrato de trabalho, por período equivalente ao acordado para a redução ou a suspensão.

A dispensa sem justa causa, que ocorrer durante o período de garantia provisória no emprego, sujeitará o empregador ao pagamento, além das parcelas rescisórias previstas na legislação em vigor, de indenização que serão documentadas [aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=545622002)

O módulo TOTVS Folha de Pagamento permite configurar mensagens de aviso para informar se o funcionário possui estabilidade nos termos estabelecidos na MP. Também é possível fazer o controle através de Fórmulas Visuais.

Abaixo, exemplificaremos com a sugestão de fórmulas de aviso configurada no parametrizador.

**Passo 1:**Utilizar a mesma consulta SQL abaixo para retornar o histórico do BEM:

sqlSQL - Retorna registros do Histórico do BEM de tipo de adesão Redução de Jornada de Trabalho

**Passo 2**: Criar uma fórmula que valias as condições de estabilidade para redução de Jornada/Salario. Abaixo um exemplo de fórmula que retorna mensagens conforme as regras da MP 936:

Fórmula - Estabilidade de Redução de Jornada/Salário DATANULA
ENTAO SETVAR (DiasDuracao, (SUBTRAIDATAS (DataAntecipacao, DataInicioAcordo)));
FIMSE;
SE DataCancelamento <> DATANULA
ENTAO SETVAR (DiasDuracao, (SUBTRAIDATAS (DataCancelamento, DataInicioAcordo)));
FIMSE;
SE DataInicioAcordo = DataInicioAcordoAnt;
SETVAR (DiasDuracao, DiasProrrog);
FIMSE;
SETVAR (DataFimAcordo, DataInicioAcordo+DiasDuracao+DiasProrrog);
SETVAR (DuracaoTotal, DuracaoTotal+DiasDuracao);
SETVAR (DataInicioAcordoAnt, DataInicioAcordo);
ATE ProxRegSQL('BEM') = Falso
FIMSE;
SE DataFimAcordo = (DataInicioAcordo + DuracaoTotal);
SETVAR (DataFimAcordo, DataInicioAcordo + DuracaoTotal);
FIMSE;
SE (DataFimAcordo + DuracaoTotal) > MTDATA(01,MES,ANO)
ENTAO
CONCAT ('FUNCIONÁRIO POSSUÍ ESTABILIDADE POR REDUÇÃO DE JORNADA/SALÁRIO OU SUSPENSÃO DE CONTRATO ATÉ ', DataFimAcordo+DuracaoTotal)
SENAO
'FUNCIONÁRIO SEM ESTABILIDADE POR REDUÇÃO DE JORNADA/SALÁRIO OU SUSPENSÃO DE CONTRATO CONFORME MP 936.'
FIMSE;
]]>

**Passo 3**: No parametrizador, menu Rescisão | Cálculo, inserir a fórmula no campo 'Fórmula para Mensagem ao calcular a rescisão':

Ao clicar Clicar no ícone Rescisão, a mensagem será exibida conforme a estabilidade do funcionário. No exemplo abaixo, o funcionário não teve redução de Jornada/Salário, mas teve a suspensão do contrato de trabalho do dia 14/04/2020 a 23/05/2020, totalizando 164 dias. A mensagem retornou a data fim da estabilidade devida para este funcionário, somando 40 dias em que estava com o contrato suspenso, a data de retorno da suspensão.

Observação

A mensagem configurada acima não impede a rescisão, sendo somente informativa.
