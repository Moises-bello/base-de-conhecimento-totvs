---
content_hash: 109c1b50a280f706eb8dd0a873e1d2e0946da00db63826ffb89723aa3c500151
fetched_at: '2026-06-29T00:10:08.758725+00:00'
page_id: '452719573'
product: rm
source: tdn-rm
title: Horários por jornada
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719573
version: 9
---

Neste cadastro devem ser informados os parâmetros necessários para o cálculo da movimentação do funcionário por jornada. Quando se começa a trabalhar com o cálculo por jornada, a data de mudança deve ser a data do primeiro dia do período, pois o cálculo por jornada deve compreender um período inteiro.

**O que é cálculo por jornada?**  
É o cálculo da movimentação dos funcionários bem como horas trabalhadas, horas extras, atrasos, faltas, entre outros de acordo com um número de horas diárias estipulado para o funcionário. Para isso o funcionário deve ter horário flexível com compensação diária. Com o cálculo por jornada, o funcionário pode trabalhar qualquer hora do dia, mesmo que as horas ultrapassem o dia de início da jornada. O sistema calculará as horas extras, atrasos e faltas comparando o número de horas trabalhadas com o número de horas da jornada

**Identificação**  
**Código**  
Informe um código para o horário por jornada  
**Descrição**  
Informe uma descrição para o horário por jornada  
**Paga adicional noturno**  
Habilitando essa opção, o horário estará apto ao cálculo de adicional noturno. Deverão ser parametrizados as informações em Sindicatos e funcionários para que o cálculo seja realizado.  
**Considera redução de jornada**  
Habilitando essa opção, o horário estará apto ao cálculo de redução de jornada. Será necessário parametrizar o intervalo que deverá ser considerado para iniciar a redução da jornada.  
Os índices deverão ser configurados conforme o horário padrão, não reduzindo o número de horas, pois no horário por jornada será reduzido automaticamente conforme o intervalo de interseção com o intervalo noturno. No horário por jornada existe a flexibilidade de horário, um funcionário poderá iniciar a jornada diurna em um determinado dia e noturna em outro dia.

O cálculo da redução da jornada noturna é realizado conforme a legislação de horas noturnas, considerando um percentual de 12,5% para cada hora noturna dentro do intervalo de adicional noturno (22:00 às 05:00).

Exemplo 1:

01 hora planejada dentro do intervalo (22:00 às 23:00)  
60 minutos \* 0.125 = 7.5 minutos de redução  
A redução será ao final da jornada, portanto o novo planejado seria de 22:00 às 22:53

Como o horário do funcionário não considera os segundos, apenas os 7 minutos serão reduzidos. Para casos onde o valor será inteiro, a redução será um pouco maior.

Exemplo 2:

02 horas planejadas dentro do intervalo (22:00 às 00:00)  
120 minutos \* 0,125 = 15 minutos de redução  
A redução também será ao final da jornada, portanto o novo planejado seria de 22:00 às 23:45

**Observação:** Para que o cálculo da redução atenda a todos os casos, orientamos que o intervalo para considerar a redução seja informado de 00:00 até 23:59.

**Modificação de horário planejado**  
É possível realizar o processo de modificação de horário planejado em um horário por jornada. Para isso, deverá ser realizado o cadastro de modificação na aba Modificação de horário planejado.  
**Anexos | Índices de jornada**  
Nesta aba são cadastrados os índices de horário que correspondem as jornadas diárias.  
**Índice**  
Numeral corresponde ao índice da jornada  
**Tipo**  
Referencia o tipo da jornada. Os tipos disponíveis são: trabalho, descanso, compensado, extra normal.  
**Horas da jornada**  
O número de horas da jornada é o número de horas que o funcionário deve trabalhar em um dia. O sistema considera este número dentro do mesmo dia ou até mesmo quando o funcionário começa a trabalhar em um dia e sai no outro dia.  
**Horas do intervalo de refeição**  
Caso o funcionário trabalhe mais de seis horas consecutivas, de acordo com a CLT, deve ter pelo menos uma hora de descanso. Este intervalo de descanso deve ser informado neste campo como intervalo de refeição. Este campo deve ser informado para o sistema saber quando será o término da jornada, pois se o funcionário tiver intervalo de refeição deverá ter mais de duas batidas dentro da jornada.  
**Número de batidas**  
Informe neste campo o número de batidas pertencentes à jornada do funcionário. Preencha este campo com as seguintes regras:  
1ª - O número de batidas será sempre par, pois toda entrada deve ter a sua saída correspondente.  
2ª - Se tiver cadastrado um número de horas para o intervalo de refeição, o número de batidas terá que ser 4, onde uma batida para entrada do funcionário, duas para a entrada e saída do intervalo de refeição e uma para a saída do término da jornada.

 **Observação:** Para as datas que não existem batidas e o tipo é trabalho, o início da jornada será considerado sempre as 08:00 e o fim com base nas horas da jornada.

|  |  |
| --- | --- |
|  | Informações Complementares |

|  |  |
| --- | --- |
|  | ***Restrições para uso do cálculo por jornada***   * Intervalos de tolerância: As tolerâncias de atrasos e extras são cadastradas dentro do índice da jornada do horário. A tolerância do sindicato não é considerada para o cálculo. * Considera feriado de acordo com a 1ª batida do horário: Sempre desmarcado, o cálculo por jornada já considera a jornada para os cálculos do feriado. * Considera feriado até a saída da jornada: Sempre desmarcado, o cálculo por jornada já considera a jornada para os cálculos do feriado. * Distribui extras em faixas considerando a jornada: Não deve estar marcado, o cálculo por jornada já considera as extras de acordo com a jornada. * Distribui extras descanso, feriado, compensado considerando jornada de trabalho: Não deve estar marcado, o cálculo por jornada já considera as extras de acordo com a jornada. * Distribui extras adicional Noturno considerando a jornada de trabalho: Não deve estar marcado, o cálculo por jornada já considera as extras de adicional de acordo com a jornada. * Considera início da jornada para definir tipo de extra: Não pode estar marcado, o cálculo por jornada já considera a jornada para distribuição de extras. * Considera extras até o fim da jornada na distribuição de extras: Não pode estar marcado, o cálculo por jornada já considera a jornada para distribuição de extras. |

Índice da Jornada
