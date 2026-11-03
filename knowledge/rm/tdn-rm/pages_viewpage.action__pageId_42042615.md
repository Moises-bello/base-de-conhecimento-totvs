---
content_hash: f6e20799f1bed5b590e2d47122c3de408ca912bf4b59d92a6d0662912cecf11f
fetched_at: '2026-06-29T00:09:13.427920+00:00'
page_id: '42042615'
product: rm
source: tdn-rm
title: COMO FAZER - Parametrização TOTVS Folha de Pagamento - Emissão TRCT
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=42042615
version: 1
---

**Produto:** TOTVS Folha de Pagamento                                                        Versões:11.40, 11.50 e 11.80.

**Processo de Negocio:** Emissão do TRCT em conformidade com a portaria 1057 do MTE.

**Processo do Sistema:** Termo Rescisão Contrato de Trabalho (Portarias MTE)

**Introdução**

Este roteiro visa demonstrar a parametrização que deve ser realizada no aplicativo TOTVS Folha de pagamento, para a correta emissão do Termo de rescisão referente à portaria 1057 do MTE.

1. **Conceito**

O novo Termo de Rescisão do Contrato de Trabalho (TRCT) foi instituído pela portaria 1.621/2010 do Ministério do Trabalho e Emprego (MTE) e atualmente, está alterada pela portaria  [1057 de 06 de julho de 2012.](http://portal.mte.gov.br/data/files/8A7C816A36A27C1401389A26D1F73CB8/Portaria%201.057%20unificado.pdf)

No TOTVS Folha de Pagamento, através deste módulo será gerado para os funcionários demitidos o termo de rescisão no padrão definido pela portaria.

 Ao iniciar a parametrização do processo de geração do TRCT, será necessário gravar um *Perfil de Parâmetros* para que todos os parâmetros definidos fiquem “salvos” para futuras gerações do relatório TRCT.

Para gravar o perfil, na primeira tela do wizard deverá inserir uma descrição no campo *Perfil de Parâmetros* e clicar no Box *Salvar perfil ao concluir*.

 Se desejar, poderá informar uma Descrição do Processo, para que no histórico de processo executados seja identificado com a descrição.

1. **Parametrizações para emissão do termo**

**1.1  – Importação do relatório**

Para realizar a importação do relatório acesse:

Visualização em Delphi: *Relatórios* | *Gerador.NET (Preview)*

Nova MDI: Aba *Gestão* |Opção *RM Reports*

Na tela exibida acesse:

Visualização em Delphi: *Processos*| *Importar estrutura de relatório*

Nova MDI: *Processos*| *Importar estrutura de relatório*

Selecione o relatório a ser importado através da janela aberta e clique em *Abrir.*

A seguinte tela será exibida, mostrando as informações: Código do relatório e Sistema para importação.

Após informar estes dados, clique em *Executar.*

Ao termino da importação uma tela como está deverá ser apresentada.

**1.1  – Emissão do termo**

Ao termino da importação do relatório, acesse:

Visualização em Delphi: *Relatórios* | *TRCT Portaria 1621/2010*

Nova MDI: Aba *Rescisão* |Opção *TRCT Portaria 1621/2010*

Ao iniciar a parametrização do processo de geração do TRCT, será necessário gravar um *Perfil de Parâmetros* para que todos os parâmetros definidos fiquem “salvos” para futuras gerações do relatório TRCT.

Para gravar o perfil, na primeira tela do wizard insira uma descrição no campo *Perfil de Parâmetros* e clique no Box *Salvar perfil ao concluir*.

Se desejar, poderá informar uma Descrição do Processo, para que no histórico de processo executados seja identificado com a descrição preenchida.  Após informar estes parâmetros clique em **Avançar.**

Nesta parte do wizard deverá ser preenchido os campos abaixo para a correta emissão do termo através das formulas e seleções informadas.

***Quebra de Seção e Seleção de Funcionários***

Esta parametrização servirá como filtro, ou seja, serão gerados TRCT cujas seções dos funcionários correspondam à quebra informada e os funcionários tenham dados compatíveis com a grade de seleção definida.

No campo *Chapa* da **Seleção de Funcionários**, serão listados os funcionários que estão na situação demitidos ou com rescisão calculada para próximo mês.

***Competência do movimento***

Os campos que indicam a grade **Competência do Movimento:**  *Mês*, *Ano* e *Período* respectivamente, deverão ser informados obrigatoriamente para referenciar o movimento de rescisão que será considerado no TRCT.

***Período de Demissão***

As datas dos campos *Início* e *Término* da grade **Período de Demissão** são obrigatórias, e determinarão um intervalo para que somente funcionários demitidos dentre o intervalo, tenham o TRCT gerado.

**Exemplo de Rescisão:**

O funcionário Chapa 0001 – Itamar teve cálculo de rescisão em 20/08/2011, na Competência do Movimento: Mês: 08,  Ano: 2011, Período: 3.

Para a correta emissão do TRCT a seguinte parametrização deverá ser informada:

**Exemplo de Rescisão Complementar:**

O funcionário Chapa: 0002 – João teve cálculo de rescisão em 10/12/2010.

Houve cálculo de rescisão complementar para o João em 15/07/2011 na Competência do Movimento:

Mês: 07, Ano: 2011, Período: 5

 Para a correta emissão do TRCT a seguinte parametrização deverá ser informada:

***Fórmula para Saldo de Salário (Campo 50)***

Este campo deverá referenciar uma fórmula que tenha como retorno o valor do *Saldo de Salário Líquido* pago na rescisão. É necessário informar a fórmula para cálculo do Campo 50, pois não existem rubricas padrão pré-definidas pelo MTE para representar Faltas, DSR Perdido, Reflexo de DSR Perdido.

Exemplificamos abaixo uma estrutura de fórmula a ser utilizada:

(MV(PARMQRY('MESCOMP'), PARMQRY('ANOCOMP'), '0001') + MV(PARMQRY('MESCOMP'), PARMQRY('ANOCOMP'), '0002'))

-

 (MV(PARMQRY('MESCOMP'), PARMQRY('ANOCOMP'), '0008') + MV(PARMQRY('MESCOMP'), PARMQRY('ANOCOMP'), '0182') + MV(PARMQRY('MESCOMP'), PARMQRY('ANOCOMP'), '0070'))

Detalhando a fórmula, temos:

**MV** = função de fórmula que retornará o valor de um evento. Os parâmetros desta função são:

Mês Competência, Ano Competência, Código do Evento.

**PARMQRY('MESCOMP')**, retornará o mês competência informado na geração do TRCT.

**PARMQRY('ANOCOMP')**, retornará o ano competência informado na geração do TRCT.

Para obtenção do “Saldo de Salário Líquido” a fórmula utilizada na base exemplo considerou:

Para a soma, os valores dos eventos:

0001 – Horas Normais

0002 – Dias Trabalhados

Para subtração, os valores dos eventos:

0008 – Faltas

0182 – Horas de Faltas (atraso)

0070 – DSR Perdido

A fórmula acima contempla o cálculo de Saldo de Salário da base Exemplo. Desta forma o usuário deverá verificar os códigos de eventos a considerar no cálculo do Líquido Salarial pago na Rescisão e adequar à fórmula.

***Formula para dias de salário (Campo 50)***

Este campo permite que a referencia do campo 50 quanto à quantidade de dias trabalhados seja calculado por formula.

Exemplo de fórmula:

N(‘0001’)

Será demonstrado como referencia de dias trabalhados no termo a referencia apresentada para o evento 0001 lançado na rescisão do funcionário

***Formula para falta/DSR (Campo 50)***

Assim como o campo **Formula para dias de salário (Campo 50)** a referencia para faltas/DSR do campo 50 também poderá ser calculo por formula.

Exemplo de fórmula:

N(‘0008’)

Será apresentado no termo a referencia do evento 0008, relacionado às faltas do funcionário.

***Fórmula para Remuneração Mês Anterior Afastamento (Campo 23)***

Neste campo associe a fórmula criada para o calculo da remuneração do mês anterior. Ficando a critério do cliente definir junto ao sindicato qual o valor a ser demonstrado.

Exemplo de formula para o calculo do campo 23:

MV(MESDT(DTD)-1,ANO,'INFORME O EVENTO DE REMUNERAÇÃO') +   
   
 MV(MESDT(DTD)-1,ANO,'INFORME O EVENTO DE REMUNERAÇÃO') +   
   
 MV(MESDT(DTD)-1,ANO,'INFORME O EVENTO DE REMUNERAÇÃO') +   
   
 MV(MESDT(DTD)-1,ANO,'INFORME O EVENTO DE REMUNERAÇÃO')

Nesta fórmula o sistema irá buscar o valor da competência anterior nos eventos informados em 'INFORME O EVENTO DE REMUNERAÇÃO'

***Fórmula Pensão Alimentícia (%) FGTS (Campo 29)***

Neste campo devemos informar o percentual devido a título de pensão alimentícia, definida em decisão judicial, mesmo que seja 0,00%.

Exemplo de preenchimento do campo 29:

1-      Cadastre a formula abaixo:

Código: CHAPA

Titulo: CHAPA

Texto: CHAPA

2-      Cadastre a consulta SQL abaixo:

Código: Campo29

Titulo: Campo29

Texto:

SELECT SUM(PERCENTUAL) FROM PFDEPEND   
 WHERE CHAPA =:FRM\_CHAPA

3-      Cadastre a formula abaixo:

Código: CAMPO29  
 Titulo: CAMPO29  
 Texto:

EXECSQL('CAMPO29');  
 RESULTSQL('CAMPO29','Column1')

Informe a formula CAMPO29 no campo ***Fórmula Pensão Alimentícia (%) FGTS (Campo 29)***

**Código do relatório**

Informe o código do relatório importado no passo 2.1 deste roteiro

***Opção Alterar Rubricas***

No TOTVS Folha de Pagamento, o TRCT será gerado a partir das referencias das Rubricas em cada campo correspondente, com exceção do campo 50 que como citado acima, é calculado por fórmula.

Nos cadastros dos eventos deverão existir as rubricas correspondentes a cada evento, sendo as rubricas pré-definidas pelo MTE que tem faixa de código 001 a 036, e as rubricas criadas pelo usuário a partir do número 100, de acordo com a necessidade.

Exemplo de associação de rubrica ao evento:

As rubricas pré-definidas pelo MTE estão especificadas no [manual 2.10 do Sistema HomologNet](http://portal.mte.gov.br/data/files/8A7C816A2E7311D1012EFC5F01A5639F/LAYOUT%20ARQUIVO%20IMPORTA%C3%87%C3%83O%20Vers%C3%A3o%202%2010%2011_02_2011%20site.pdf) instituído pela Portaria Nº 1.620, de 14/07/2010, disponível no site do MTE.

 O Cadastro de Rubricas no TOTVS Folha de Pagamento está localizado em:

Visualização em Delphi: *Cadastros* | *Tabelas Dinâmicas* | Tabela *HOMOLOGRUB*

Nova MDI: Aba *Administração de pessoal* |*Cadastros Globais* | Opção *Tabelas Dinâmicas* |Tabela *HOMOLOGRUB*

Nesta tabela poderá verificar as rubricas pré-definidas pelo MTE e cadastrar as rubricas que forem necessárias a partir do número 100.

Na geração do TRCT, para relacionar as rubricas aos campos correspondentes do relatório, marque o Box *Alterar Rubricas* e clique em **Avançar**.

Será exibida a Tela “Edição das Rubricas”, divididas em duas páginas **Proventos** e **Descontos**, com todos os campos do relatório que deverão ter relacionada sua respectiva rubrica.

Por existir rubricas pré-definidas pelo MTE, os campos de Rubricas para a geração do relatório TRCT que são correspondentes a estas rubricas, estarão desabilitados.

Os campos desabilitados são: 51, 52, 53, 54, 55, 56, 57, 60, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93 e 98.

Os campos que não são correspondentes as rubricas pré-definidas pelo MTE, estarão habilitados e neles deverão ser informadas as rubricas correspondentes que foram cadastradas pelo usuário a partir do número 100.

***Imprimir verbas rescisórias pré-definidas quando valor igual a zero***

Na tela de Parametrização de Geração do TRCT existe o parâmetro “Imprimir verbas rescisórias pré-definidas quando valor igual a zero”. Este parâmetro quando marcado, irá imprimir todos os campos de verbas rescisórias que estão definidos no Anexo I, da Portaria Nº1.621 de 14/07/2010, mesmo que algum tenha valor igual zero.

Com o parâmetro desmarcado, serão impressos os campos definidos no Anexo I, que o valor for maior que zero.

A tabela abaixo detalha os campos de Verbas Rescisórias do TRCT com a relação das rubricas pré-definidas e a indicação dos campos que terão rubricas criadas pelo usuário a partir do número 100.

Ao termino da parametrização realizada clique em **Avançar** e sem seguida **Executar**.

Sendo apresentado o relatório para impressão:
