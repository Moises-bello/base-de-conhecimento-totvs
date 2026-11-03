---
article_id: 4411690878103
category: Rescisão
content_hash: 6283d04a118e7ac418eb6aa6babd8f56d6e0468a28b340ccf319fc0cc8dfb5f9
fetched_at: '2026-06-28T22:46:54.512823+00:00'
product: rm
section_id: 1500000834561
source: central-rm
title: RH - RM - FOP - Parametrização Folha de Pagamento - Emissão TRCT
type: support-article
updated_at: '2024-06-17T15:10:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411690878103-RH-RM-FOP-Parametriza%C3%A7%C3%A3o-Folha-de-Pagamento-Emiss%C3%A3o-TRCT
---

****![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24231564918167)****Tempo aproximado para leitura:**00:17:00 min  
  
Dúvida**Como realizar parametrização da emissão do TRCT - Portaria 1621/2010? **Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
**Solução**O novo Termo de Rescisão do Contrato de Trabalho (TRCT) foi instituído pela portaria 1.621/2010 do Ministério do Trabalho e Emprego (MTE) e atualmente, está alterada pela portaria  [1057 de 06 de julho de 2012.](http://portal.mte.gov.br/data/files/8A7C816A36A27C1401389A26D1F73CB8/Portaria%201.057%20unificado.pdf)

No TOTVS Folha de Pagamento, através deste módulo será gerado para os funcionários demitidos o termo de rescisão no padrão definido pela portaria.  
  
**Parametrizações para emissão do termo**

**1.1  – Emissão do termo**Ao termino da importação do relatório, acesse:  
  
Aba *Rescisão*|Opção*TRCT Portaria 1621/2010*

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10385278359447)

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10385280775703)

Ao iniciar a parametrização do processo de geração do TRCT, será necessário gravar um *Perfil de Parâmetros* para que todos os parâmetros definidos fiquem “salvos” para futuras gerações do relatório TRCT.

Para gravar o perfil, na primeira tela do wizard insira uma descrição no campo *Perfil de Parâmetros* e clique no Box *Salvar perfil ao concluir*.

Se desejar, poderá informar uma Descrição do Processo, para que no histórico de processo executados seja identificado com a descrição preenchida.  Após informar estes parâmetros clique em **Avançar.**

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10385332789783)

Nesta parte do wizard deverá ser preenchido os campos abaixo para a correta emissão do termo através das formulas e seleções informadas.  
  
***Quebra de Seção e Seleção de Funcionários***Esta parametrização servirá como filtro, ou seja, serão gerados TRCT cujas seções dos funcionários correspondam à quebra informada e os funcionários tenham dados compatíveis com a grade de seleção definida.  
No campo *Chapa* da **Seleção de Funcionários**, serão listados os funcionários que estão na situação demitidos ou com rescisão calculada para próximo mês.  
  
***Competência do movimento***Os campos que indicam a grade **Competência do Movimento:** *Mês*, *Ano* e *Período* respectivamente, deverão ser informados obrigatoriamente para referenciar o movimento de rescisão que será considerado no TRCT.  
  
***Período de Demissão***As datas dos campos *Início* e *Término* da grade **Período de Demissão** são obrigatórias, e determinarão um intervalo para que somente funcionários demitidos dentre o intervalo, tenham o TRCT gerado.  
  
**Exemplo de Rescisão:**O funcionário Chapa 0001 – Itamar teve cálculo de rescisão em 20/10/2021, na Competência do Movimento: Mês: 10,  Ano: 2021, Período: 3.  
  
Para a correta emissão do TRCT a seguinte parametrização deverá ser informada:

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10385336546583)

**Exemplo de Rescisão Complementar:**O funcionário Chapa: 0002 – João teve cálculo de rescisão em 10/09/2020.

Houve cálculo de rescisão complementar para o João em 15/09/2021 na Competência do Movimento:

Mês: 09, Ano: 2021, Período: 3  
  
 Para a correta emissão do TRCT a seguinte parametrização deverá ser informada:

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10385313971351)

***Fórmula para Saldo de Salário (Campo 50)***Este campo deverá referenciar uma fórmula que tenha como retorno o valor do *Saldo de Salário Líquido* pago na rescisão. É necessário informar a fórmula para cálculo do Campo 50, pois não existem rubricas padrão pré-definidas pelo MTE para representar Faltas, DSR Perdido, Reflexo de DSR Perdido.  
  
Exemplificamos abaixo uma estrutura de fórmula a ser utilizada:

(MV(PARMQRY('MESCOMP'), PARMQRY('ANOCOMP'), '0001') + MV(PARMQRY('MESCOMP'), PARMQRY('ANOCOMP'), '0002'))

-

 (MV(PARMQRY('MESCOMP'), PARMQRY('ANOCOMP'), '0008') + MV(PARMQRY('MESCOMP'), PARMQRY('ANOCOMP'), '0182') + MV(PARMQRY('MESCOMP'), PARMQRY('ANOCOMP'), '0070'))

Detalhando a fórmula, temos:

**MV**= função de fórmula que retornará o valor de um evento. Os parâmetros desta função são:

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

![62.png](https://tdn.totvs.com/download/attachments/42042615/62.png?version=1&modificationDate=1350592398000&api=v2)

***Formula para dias de salário (Campo 50)***Este campo permite que a referencia do campo 50 quanto à quantidade de dias trabalhados seja calculado por formula.   
  
Exemplo de fórmula:  
  
N(‘0001’)  
  
Será demonstrado como referencia de dias trabalhados no termo a referencia apresentada para o evento 0001 lançado na rescisão do funcionário  
  
***Formula para falta/DSR (Campo 50)***Assim como o campo **Formula para dias de salário (Campo 50)** a referencia para faltas/DSR do campo 50 também poderá ser calculo por formula.  
  
Exemplo de fórmula:  
  
N(‘0008’)  
  
Será apresentado no termo a referencia do evento 0008, relacionado às faltas do funcionário.  
  
***Fórmula para Remuneração Mês Anterior Afastamento (Campo 23)***Neste campo associe a fórmula criada para o calculo da remuneração do mês anterior. Ficando a critério do cliente definir junto ao sindicato qual o valor a ser demonstrado.  
  
Exemplo de formula para o calculo do campo 23:

MV(MESDT(DTD)-1,ANO,'INFORME O EVENTO DE REMUNERAÇÃO') +   
  
MV(MESDT(DTD)-1,ANO,'INFORME O EVENTO DE REMUNERAÇÃO') +   
  
MV(MESDT(DTD)-1,ANO,'INFORME O EVENTO DE REMUNERAÇÃO') +   
  
MV(MESDT(DTD)-1,ANO,'INFORME O EVENTO DE REMUNERAÇÃO') 

Nesta fórmula o sistema irá buscar o valor da competência anterior nos eventos informados em 'INFORME O EVENTO DE REMUNERAÇÃO'  
  
***Fórmula Pensão Alimentícia (%) FGTS (Campo 29)***Neste campo devemos informar o percentual devido a título de pensão alimentícia, definida em decisão judicial, mesmo que seja 0,00%.  
  
Exemplo de preenchimento do campo 29:

1- Cadastre a formula abaixo:

Código: CHAPA

Titulo: CHAPA

Texto: CHAPA

2-Cadastre a consulta SQL abaixo:

Código: Campo29

Titulo: Campo29

Texto:

SELECT SUM(PERCENTUAL) FROM PFDEPEND   
WHERE CHAPA =:FRM\_CHAPA

3-Cadastre a formula abaixo:

Código: CAMPO29  
Titulo: CAMPO29  
Texto:

EXECSQL('CAMPO29');  
RESULTSQL('CAMPO29','Column1')

Informe a formula CAMPO29 no campo ***Fórmula Pensão Alimentícia (%) FGTS (Campo 29)*****Código do relatório**Informe o código do relatório importado.  
  
***Opção Alterar Rubricas***No TOTVS Folha de Pagamento, o TRCT será gerado a partir das referencias das Rubricas em cada campo correspondente, com exceção do campo 50 que como citado acima, é calculado por fórmula.

[RM - FOP - Parametrização de Rubricas do TRCT](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360003040531-RM-FOP-Parametriza%C3%A7%C3%A3o-de-Rubricas-do-TRCT?source=search)  
  
***Imprimir verbas rescisórias pré-definidas quando valor igual a zero***

Na tela de Parametrização de Geração do TRCT existe o parâmetro “Imprimir verbas rescisórias pré-definidas quando valor igual a zero”. Este parâmetro quando marcado, irá imprimir todos os campos de verbas rescisórias que estão definidos no Anexo I, da Portaria Nº1.621 de 14/07/2010, mesmo que algum tenha valor igual zero.

Com o parâmetro desmarcado, serão impressos os campos definidos no Anexo I, que o valor for maior que zero.

![](https://tdn.totvs.com/download/attachments/42042615/65.png?version=1&modificationDate=1350592398000&api=v2)

A tabela abaixo detalha os campos de Verbas Rescisórias do TRCT com a relação das rubricas pré-definidas e a indicação dos campos que terão rubricas criadas pelo usuário a partir do número 100.

![](https://tdn.totvs.com/download/attachments/42042615/66.png?version=1&modificationDate=1350592398000&api=v2)

![](https://tdn.totvs.com/download/attachments/42042615/67.png?version=1&modificationDate=1350592398000&api=v2)

![](https://tdn.totvs.com/download/attachments/42042615/68.png?version=1&modificationDate=1350592398000&api=v2)
