---
content_hash: 3b806314d0331aefcca7b3ff63b7d56e59eb19315fa287a7dc28101beb6ae5b1
fetched_at: '2026-06-29T00:10:10.466881+00:00'
page_id: '452719844'
product: rm
source: tdn-rm
title: Lançamento de horários
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719844
version: 34
---

**Lançamento de horários**   
O lançamento de horários permite que sejam inseridas automaticamente e de forma global batidas no espelho de ponto do funcionário conforme seu horário e parâmetros disponíveis para seleção. As batidas são inseridas com o status digitadas e necessitam de justificativa conforme determinação da portaria 1510/2009.

***Seleção de datas***  
**Início/Fim:** Informe as datas de início e fim do período para lançamento dos horários. Somente são permitidas inserção de batidas em período ativo.

**Grupo de funcionários**  
Deverá ser realizada a seleção de funcionários em Seleção de funcionários e informada a quebra preferencial em Quebra de seção.

**Tipos de batidas** Neste quadrante tem-se opção de realizar o lançamento de batidas conforme a necessidade. Os tipos de batidas disponíveis são:   
Batidas normais de jornada: Entrada da jornada, saídas intermediárias, entradas intermediárias e saída da jornada.  
Ausência planejada: Entrada, saída e por tempo.  
Intervalo de ausência do limite de refeição: Entrada, saída, não lançar em dias com batidas ímpares e  por tempo.

O sistema irá comparar o limite de refeição para realizar o lançamento do intervalo de ausência. Se a batida realizada estiver em interseção com o limite de refeição a batida não será lançada, caso não exista o par de entrada e saída correspondente.

**Exemplo 1:**  Batida de refeição não será lançada

Horário do funcionário: 07:00-12:00-14:00-18:00

Intervalo de Refeição: 12:00-14:00

Limite de refeição : 08:00-16:00

Batida Realizada: 08:00-16:00

Batida Lançada: Nenhuma batida será lançada

**Exemplo 2:**  Batida de refeição será lançada

Horário do funcionário: 07:00-12:00-14:00-18:00

Intervalo de Refeição: 12:00-14:00

Limite de refeição : 08:00-16:00

Batida Realizada: 08:00-16:01

Batida lançada: 12:00-13:00

Para habilitar o campo **Por tempo** é necessário marcar o campo Entrada ou o campo Saída. O valor que for informado neste campo será o valor considerado no lançamento das batidas de ausência planejada ou do intervalo de ausência do limite de refeição. Exemplo:

Horário planejado   
08:00      12:00      13:00    17:00

Preenchendo o campo Por tempo com o valor 00:30, será lançado as seguintes batidas:

08:00      12:00      12:30    17:00

Quando este campo for preenchido com um valor maior que a ausência ou limite cadastrado no horário, as batidas lançadas devem respeitar o horário planejado:

Horário planejado  
08:00      12:00      13:00    17:00

Preenchendo o campo Por tempo com o valor 02:00, será lançado as seguintes batidas:

08:00      12:00      13:00    17:00

Para habilitar o parâmetro **Não lançar em dias com batidas Ímpares**é necessário marcar os campos Entrada e Saída .

Quando o parâmetro for marcado , o sistema irá validar os dias que tem batidas ímpares e não será realizado o lançamento de nenhuma marcação de refeição, caso tenha batida PAR seguirá as regras padrões de lançamento.

Quando o parâmetro estiver desmarcado, permanece o comportamento atual, complementando os pares.

Exemplo:

Horário Planejado:

| 08:00 | 12:00 | 14:00 | 18:00 |
| --- | --- | --- | --- |

Batidas Coletadas

| Dia | Entrada | Saída | Entrada | Saída |
| --- | --- | --- | --- | --- |
| 01/10/2021 | 08:00 |  |  |  |
| 02/10/2021 | 08:00 | 12:00 |  |  |
| 03/10/2021 | 08:00 | 1200 |  | 18:00 |
| 04/10/2021 | 08:00 |  | 14:00 | 18:00 |
| 05/10/2021 |  | 12:00 |  |  |
| 06/10/2021 |  |  | 14:00 | 18:00 |
| 07/10/2021 |  |  | 14:00 |  |
| 08/10/2021 |  |  |  | 18:00 |
| 09/10/2021 | 08:00 |  |  | 18:00 |

Com o parâmetro marcado o espelho ficará da seguinte forma:

| Dia | Entrada | Saída | Entrada | Saída |
| --- | --- | --- | --- | --- |
| 01/10/2021 | 08:00 |  |  |  |
| 02/10/2021 | 08:00 | 12:00 |  |  |
| 03/10/2021 | 08:00 | 1200 |  | 18:00 |
| 04/10/2021 | 08:00 |  | 14:00 | 18:00 |
| 05/10/2021 |  | 12:00 |  |  |
| 06/10/2021 |  |  | 14:00 | 18:00 |
| 07/10/2021 |  |  | 14:00 |  |
| 08/10/2021 |  |  |  | 18:00 |
| 09/10/2021 | 08:00 | 1200 | 1400 | 18:00 |

\*\*Em amarelo são as batidas lançadas.

Com o parâmetro desmarcado  o espelho ficará da seguinte forma:

| Dia | Entrada | Saída | Entrada | Saída |
| --- | --- | --- | --- | --- |
| 01/10/2021 | 08:00 | 12:00 |  |  |
| 02/10/2021 | 08:00 | 12:00 |  |  |
| 03/10/2021 | 08:00 | 1200 | 14:00 | 18:00 |
| 04/10/2021 | 08:00 | 12:00 | 14:00 | 18:00 |
| 05/10/2021 |  | 12:00 |  | 18:00 |
| 06/10/2021 |  |  | 14:00 | 18:00 |
| 07/10/2021 |  | 12:00 | 14:00 |  |
| 08/10/2021 |  |  | 14:00 | 18:00 |
| 09/10/2021 | 08:00 | 12:00 | 14:00 | 18:00 |

\*\*Em amarelo são as batidas lançadas.

**Extra** Neste quadrante é possível parametrizar para realizar o lançamento de batidas com horas extras. Pode-se definir o lançamento no inicio ou fim da jornada e a quantidade de horas conforme parâmetros ativados. Importante: Caso realize um lançamento de extras, não deverá ser marcado a opção para lançamento de batidas normais. Se lançar extras no inicio da jornada não deverá lançar a batida normal de entrada (Entrada da jornada) e o mesmo comportamento deverá ser realizado caso opte pelo lançamento de extra no final da jornada.

**Horas extras da jornada:** Habilitando o parâmetro é possível fazer o lançamento de extras ativando demais parâmetros de definição de lançamento **No início da jornada:** Define lançamento de extras no início da jornada **No fim da jornada:** Define lançamento de extras no fim da jornada **Quantidade:** informar a quantidade de horas extras a serem lançadas

**Justificativa**  
Conforme portaria 1.510/2009 do MTE, o campo justificativa é de preenchimento obrigatório para realizar o Lançamento Global de Horários.  
***Formas de Lançamentos***

**Lançar batidas fixas**  
Selecionando este parâmetro, o Sistema irá lançar as batidas do horário exatamente como cadastrado para o funcionário.

**Batidas aleatórias dentro da tolerância**  
Possibilita gerar batidas do horário-padrão, considerando as tolerâncias cadastradas para o parâmetro Sindicato do funcionário. Exemplo:   
Suponhamos que, para o horário padrão, estejam cadastrados as seguintes batidas: 07:00 11:00 13:30 17:30. Ao lançar o horário padrão juntamente com a opção de lançar batidas aleatórias, serão geradas as seguintes batidas:   
Entr 1  Saída 1  Entr 2  Saída 2  
07:04  10:57  13:26  17:36   
06:59  11:08  13:35  17:29   
As tolerâncias cadastradas no parâmetro Sindicato deste funcionário são:  
 Antes Depois  
Entr 1 00:05 00:05   
Saída 2 00:05 00:10   
Entr 2 00:05 00:05   
Saída 2 00:05 00:10

**Lançar batidas considerando intervalos abonados**  
Com a opção "Lança batidas considerando intervalos abonados" marcada, o sistema não irá lançar batidas para os intervalos abonados.  
Exemplo:  
Horário: 08:00 12:00 14:00 18:00  
Intervalo de Abono:  
22/08/2006 – 08:00 às 10:00  
23/08/2006 – 10:00 às 11:00  
24/08/2006 – 16:00 às 18:00  
25/08/2006 – 14:00 às 18:00  
Nesse dia serão lançados, para o funcionário, as seguintes batidas:  
Batidas:   
22/08/2006 – 10:00E 12:00S 14:00E 18:00S  
23/08/2006 – 08:00E 12:00S 14:00E 18:00S  
24/08/2006 – 08:00E 12:00S 14:00E 16:00S  
25/08/2006 – 08:00E 12:00S

**Considera feriado para lançamento de batidas**  
Marcando essa opção, em dias de feriado conforme calendário da sessão do funcionário, não ocorrerá o lançamento de batidas.

Para abonos **por número de horas** da **nova gestão de abonos**, o cálculo será baseado sempre na jornada de trabalho prevista para o funcionário no dia, somado ao número de horas informado no abono, independentemente da existência de batidas no dia.  
Exemplos:

Jornada planejada: 0800 1200 1400 1800

Abono 1: 8 horas - não lança batidas  
Abono 2: 2 horas - 1000 1200 1400 1800

**Realizar recálculo após lançamento**  
Marcando este parâmetro o sistema fará o recálculo da movimentação do(s) funcionário(s) logo após o lançamento. Observação: Será efetuado o recálculo apenas para o(s) funcionário(s) que tiveram lançamento de horários.  
Após preencher os campos acima, clique no botão "Executar" para efetuar as alterações realizando o lançamento.

**Importante: Saída efetuada após o horário planejado e em jornada sem trabalho:**

Quando o cálculo da natureza das batidas é realizado considerando a jornada, o sistema poderá priorizar uma jornada de trabalho com relação a jornada sem trabalho.  
Esse cálculo é validado no processo de lançamento de batidas, para que seja considerado  corretamente no limite uma batida de saída da jornada efetuada após o horário planejado daquela batida.  
**Exemplo:** Quando a batida está mais próxima da jornada sem trabalho devido uma extra realizada pelo funcionário.  
Planejado  
Sex [08:00 - 18:00] TRABALHO  
Sab [00:00 +00:00] SEM TRABALHO (COMP)  
    
Executado  
Sex [16:00 - 22:00] ,nesse caso a batida das 22:00 será importada como "ENTRADA".  
Com o tempo de acréscimo, pode ser acrescido um limite para a jornada de trabalho  
ir até as 22:00, por exemplo, e assim a batida ser importada como "SAÍDA"

Nesse caso deve ser definido o tempo de "Acrésc. p/ limite da jornada de trabalho anterior/posterior à jornada sem trabalho, para cálculo da natureza" na parametrização do funcionário em importação de batidas: <https://tdn.totvs.com/display/LRM/Importar+batidas>

**Cálculo do lançamento de batidas**

**Acerto de natureza das batidas:** Será executado quando selecionado as opções: *Desmarcar todos | Avançar | Avançar.* O acerto de natureza será aplicado, para as batidas que fazem parte da jornada planejada calculada para a data e não será executado se existe uma única batida nessa jornada, observando também a configuração definida nos [parâmetros de importação](https://tdn.totvs.com/pages/releaseview.action?pageId=452719611).
