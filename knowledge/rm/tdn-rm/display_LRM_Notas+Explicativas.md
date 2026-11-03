---
content_hash: d33b1a80c208d044d50ae3fd26b3ae4ea38311bdb7c9ac72c689ad95ee7bbbfe
fetched_at: '2026-06-29T00:09:27.875467+00:00'
page_id: '423938552'
product: rm
source: tdn-rm
title: Notas Explicativas
type: documentation
url: https://tdn.totvs.com/display/LRM/Notas+Explicativas
version: 3
---

O novo layout da ECD (6.0) trouxe como principal mudança a inclusão do campo NOTA\_EXP\_REF (Notas explicativas relativas às demonstrações contábeis.), o novo campo vai afetar três registros já existentes, sendo eles: J100 – Balanço Patrimonial, J150 – Demonstração dos Resultados e J210 - DLPA – Demonstração de Lucros ou Prejuízos Acumulados/DMPL – Demonstração de Mutações do Patrimônio Líquido.

O preenchimento do novo campo é facultativo, o usuário pode informar em um(a), todos(as) ou nenhum(a) conta/fato contábeis presente no seu respectivo registro.

Exemplos de preenchimento dos registros no arquivo:

**J100**

|J100|1|1|1|ATIVO|936844,99|D|100000,00|D|A Empresa fez um Ajuste a Valor Presente

* Campo 01 – Tipo de Registro: J100
* Campo 02 – Código de Aglutinação das Contas Atribuído pelo Empresário ou Sociedade Empresário: 1
* Campo 03 – Nível do Código de Aglutinação: 1
* Campo 04 – Indicador de Grupo do Balanço: 1 (Ativo)
* Campo 05 – Descrição do Código de Aglutinação: ATIVO
* Campo 06 – Valor Total do Código de Aglutinação: 936844,99 (936.844,99)
* Campo 07 – Indicador da Situação do Saldo Informado no Campo Anterior: D (Devedor)
* Campo 08 – Valor Inicial do Código de Aglutinação: 100000,00 (100.000,00)
* Campo 09 – Indicador da Situação do Saldo Inicial Informado no Campo Anterior: D (Devedor)
* Campo 10 – Notas explicativas (A Empresa fez um Ajuste a Valor Presente)

**J150**

|J150|DESP.003|2|MULTAS|15,00|D|20,0|D|A receita compreende o valor justo da contraprestação recebida ou a receber pela comercialização de produtos no curso normal das atividades da Companhia

* Campo 01 – Tipo de Registro: J150
* Campo 02 – Código de Aglutinação das Contas Atribuído pelo Empresário ou Sociedade Empresário: DESP.003
* Campo 03 – Nível do Código de Aglutinação: 2
* Campo 04 – Descrição do Código de Aglutinação: MULTAS
* Campo 05 – Valor Total do Código de Aglutinação: 15,00
* Campo 06 – Indicador da Situação do Saldo Informado no Campo Anterior: D (Despesa ou valor que represente parcela redutora do lucro)
* Campo 07 – Valor do Saldo Final do Código de Aglutinação Antes do Encerramento: 20,00
* Campo 08 – Indicador da Situação do Saldo Informado no Campo Anterior: D (Despesa ou valor que represente parcela redutora do lucro)
* Campo 09 – Notas explicativas (A receita compreende o valor justo da contraprestação recebida ou a receber pela comercialização de produtos no curso normal das atividades da Companhia)

**J150**

|J210|0|1.1|LUCROS ACUMULADOS|0,00|C|0,00|C|Demonstração das mutações do PL|

* Campo 01 – Tipo de Registro: J210
* Campo 02 – Indicador do Tipo de Demonstração: 0 (DLPA)
* Campo 03 – Código de Aglutinação das Contas do Patrimônio Líquido: 1.1
* Campo 04 – Descrição do Código de Aglutinação: Lucros Acumulados
* Campo 05 – Saldo Final do Código de Aglutinação: 0,00
* Campo 06 – Indicador da Situação do Saldo Final: C
* Campo 07 – Saldo Inicial do Código de Aglutinação: 0,00
* Campo 08 – Indicador da Situação do Saldo Inicial: C
* Campo 09 – Notas Explicativas (Demonstração das mutações do PL)

As notas explicativas serão informadas dentro da demonstração contábil, cada fato poderá ter uma ou mais notas desde que em períodos distintos. Poderão ser cadastradas notas para atender quem realiza encerramentos trimestrais e anual. O sistema irá verificar no momento da geração do SPED Contábil a quantidade de encerramentos realizados pelo usuário e para cada fato contábil, buscará uma nota explicativa respectiva ao período de encerramento.

O registro J210 tem um comportamento exclusivo para enviar a nota explicativa para o SPED, o registro se refere a demonstração como um todo e não a cada fato como nos registros J100 e J150, sendo assim, deve ser enviada apenas uma nota que represente a demonstração no período. Pensando nisso, caso o usuário necessite de incluir uma ou mais notas para atender o J210, está nota deve ser cadastrada no primeiro fato da demonstração, caso seja cadastrada notas em fato que não seja o primeiro, estas não serão recuperadas para a emissão do SPED Contábil.

**IMPORTANTE**:

Caso o usuário gere a rotina da ECD com apenas um encerramento, isto é, anual, as suas notas explicativas também devem ser cadastradas para o período que compreende um ano, caso contrário as notas não serão enviadas para o arquivo.txt. O mesmo serve para quando gerar a rotina do SPED com encerramento trimestral, neste caso as notas explicativas devem ser cadastradas de forma trimestral, caso contrário as notas não serão enviadas para o arquivo.txt da ECD.
