---
content_hash: 90a12aa5155795c1df80a516d853a3112e10f7df4eaf44389759b27598506da8
fetched_at: '2026-06-29T00:06:14.995952+00:00'
page_id: '210051003'
product: rm
source: tdn-rm
title: DT_CCTSindados
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_CCTSindados
version: 3
---

# IMPLEMENTAÇÃO PARA ATENDER NOVAS REGRAS DA CCT SINDADOS

## Características do Requisito

  

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | **TOTVS Automação de Ponto** |
| **Rotina:** | | **Rotina** | **Nome Técnico** | | --- | --- | | *Ambiente / Parâmetros* | *CCT Sindados BH* | |
| **Versões/Release:** | *12.1.4* |

## Descrição

Nesta versão, o usuário pode realizar as seguintes configurações nos parâmetros do sindicato:

› Definir o tipo de faixa de extra: Diário/Semanal/Período.

› Definir os limites de extras do banco de horas diário, com a possibilidade de alterar a atitude das ocorrências ou alterar a faixa para qual elas vão ser distribuídas

## Procedimento para Utilização

**Definir o tipo de faixa de extra: Diário/Semanal/Período**

Com essa configuração, é possível definir se a totalização das faixas de extras será por dia, semana, ou período.

Tipo de Faixa: Campo que armazena o tipo de faixa de extra.

A seguir serão demonstrados exemplos com as faixas de extra normal. As regras são as mesmas para as faixas de extra de compensado, descanso e feriado:

**Diário**:

Nesse caso a totalização será reiniciada para cada dia.

Configuração das faixas:

1ª Faixa Extra Normal: 02:00  
2ª Faixa Extra Normal: 02:00

Ocorrências:

01/11: 04:00 Extra Normal  
02/11: 02:00 Extra Normal

Com a totalização diária a distribuição ficará da seguinte forma:

1ª Faixa Extra Normal: 04:00 (2 horas do dia 01/11 + 2 horas do dia 02/11)  
2ª Faixa Extra Normal: 02:00 (2 horas do dia 01/11)

**Semanal:**

Nesse caso a totalização será reiniciada para cada semana.

Configuração das faixas:

1ª Faixa Extra Normal: 10:00  
2ª Faixa Extra Normal: 04:00

Ocorrências:

01/11: 04:00 Extra Normal  
02/11: 04:00 Extra Normal  
03/11: 04:00 Extra Normal

Com a totalização diária a distribuição ficará da seguinte forma:

1ª Faixa Extra Normal: 10:00 (4 horas do dia 01/11 + 4 horas do dia 02/11 + 2 horas do dia 03/11)  
2ª Faixa Extra Normal: 02:00 (2 horas do dia 03/11)

**Período:**

Nesse caso a totalização será para todo o período.

Configuração das faixas:

1ª Faixa Extra Normal: 20:00  
2ª Faixa Extra Normal: 10:00

Ocorrências:

01/11: 04:00 Extra Normal  
02/11: 04:00 Extra Normal  
03/11: 04:00 Extra Normal  
16/11: 04:00 Extra Normal  
17/11: 02:00 Extra Normal  
18/11: 04:00 Extra Normal  
19/11: 04:00 Extra Normal

Com a totalização diária a distribuição ficará da seguinte forma:

1ª Faixa Extra Normal: 10:00 (4 horas dos dia 01/11, 02/11, 03/11, 16/11 + 2 horas do dia 17/11 + 2 horas do dia 18/11)  
2ª Faixa Extra Normal: 06:00 (2 horas do dia 18/11 + 4 horas do dia 19/11)

**Definir limites de extra do banco de horas diário**

Com essa nova configuração, é possível definir o limite de extra diário, semanal e por período, e que operação será realizada ao passar o limite: se a atitude vai ser alterada ou se a faixa será alterada.  
Por padrão, será realizada a operação de alteração de atitude. No caso de ser escolhido a opção de alterar faixa, também pode ser configurado quais os tipos de extra serão considerados para alteração.   
Caso sejam configurados dois limites, onde um altera a atitude e outro a faixa, as horas que forem para o movimento serão lançadas para o evento do banco de horas, e não o evento do labore padrão:

Em relação a prioridade, a aplicação dos limites respeitará a seguinte ordem: **diária / semanal / período**

 

Campos:

› Limite extras pro dia: Campo que armazena a configuração do limite diário.  
› Limite extras por semana: Campo que armazena a configuração do limite semanal.  
› Limite extras por período: Campo que armazena a configuração do limite do período.

No caso do limite semanal, pode acontecer da semana iniciar em um período e terminar em outro período.  
Para essa situação, o comportamento será o seguinte:

Semana: 29/11 a 05/12  
Período corrente: 29/11 a 30/11  
Próximo período: 01/12 a 05/12

Para o período corrente será feito a projeção da semana apenas para aplicar o limite semanal.  
Portanto, considerando um limite semanal de 4 horas, caso ultrapasse as 4 horas no dia 29/11 ou 30/11, essas extras serão lançadas para o movimento do período corrente, apenas dos dias 29/11 e 30/11.

Para o próximo período será considerado o início da semana no período corrente para aplicar o limite semanal.   
Portanto, considerando um limite semanal de 4 horas, caso ultrapasse as 4 horas no dia 29/11 ou 30/11, todas as extras da primeira semana no próximo período, do dia 01/12 ao 05/12, serão lançadas para o movimento do próximo período.

****Exemplo de utilização****

Configuração dos limites

Limite diário: 02:00 Alterar Atitude  
Limite Semanal: 12:00 Alterar Atitude  
Limite Período: 30:00 Alterar Faixa – EA (Extra normal autorizado), ECA (Extra compensado autorizado)

Semanas para cálculo:

Semana 1: 01/11 a 07/11  
Semana 2: 08/11 a 14/11  
Semana 3: 15/11 a 21/11  
Semana 4: 22/11 a 28/11  
Semana 5: 29/11 a 05/12

Ocorrências:

01/11: 04:00 Extra Normal - Compensar  
02/11: 04:00 Extra Normal - Compensar  
03/11: 04:00 Extra Normal - Compensar  
04/11: 04:00 Extra Normal - Compensar  
05/11: 04:00 Extra Normal - Compensar  
06/11: 04:00 Extra Compensado - Compensar  
07/11: 04:00 Extra Descanso - Compensar  
08/11: 04:00 Extra Normal - Compensar  
09/11: 04:00 Extra Normal - Compensar  
10/11: 04:00 Extra Normal - Compensar  
11/11: 04:00 Extra Normal - Compensar  
12/11: 04:00 Extra Normal - Compensar  
13/11: 04:00 Extra Compensado - Compensar  
14/11: 04:00 Extra Descanso - Compensar  
15/11: 04:00 Extra Normal - Compensar  
16/11: 04:00 Extra Normal - Compensar  
17/11: 02:00 Extra Normal - Compensar  
18/11: 04:00 Extra Normal - Compensar  
19/11: 04:00 Extra Normal - Compensar  
20/11: 04:00 Extra Compensado - Compensar  
21/11: 04:00 Extra Descanso – Compensar

Total banco: 84:00  
Total movimento: 00:00

**Aplicando o limite diário****:**

Ocorrências:

01/11: 02:00 Extra Normal – Compensar / 02:00 Extra Normal - Pagar  
02/11: 02:00 Extra Normal – Compensar / 02:00 Extra Normal - Pagar  
03/11: 02:00 Extra Normal – Compensar / 02:00 Extra Normal - Pagar  
04/11: 02:00 Extra Normal – Compensar / 02:00 Extra Normal - Pagar  
05/11: 02:00 Extra Normal – Compensar / 02:00 Extra Normal - Pagar  
06/11: 02:00 Extra Compensado – Compensar / 02:00 Extra Compensado – Pagar  
07/11: 02:00 Extra Descanso – Compensar / 02:00 Extra Descanso – Pagar  
08/11: 02:00 Extra Normal – Compensar / 02:00 Extra Normal - Pagar  
09/11: 02:00 Extra Normal – Compensar / 02:00 Extra Normal - Pagar  
10/11: 02:00 Extra Normal – Compensar / 02:00 Extra Normal - Pagar  
11/11: 02:00 Extra Normal – Compensar / 02:00 Extra Normal - Pagar  
12/11: 02:00 Extra Normal – Compensar / 02:00 Extra Normal - Pagar  
13/11: 02:00 Extra Compensado – Compensar / 02:00 Extra Compensado – Pagar  
14/11: 02:00 Extra Descanso – Compensar / 02:00 Extra Descanso – Pagar  
15/11: 02:00 Extra Normal – Compensar / 02:00 Extra Normal - Pagar  
16/11: 02:00 Extra Normal – Compensar / 02:00 Extra Normal - Pagar  
17/11: 02:00 Extra Normal – Compensar / 02:00 Extra Normal - Pagar  
18/11: 02:00 Extra Normal – Compensar / 02:00 Extra Normal - Pagar  
19/11: 02:00 Extra Normal – Compensar / 02:00 Extra Normal - Pagar  
20/11: 02:00 Extra Compensado – Compensar / 02:00 Extra Compensado – Pagar  
21/11: 02:00 Extra Descanso – Compensar / 02:00 Extra Descanso – Pagar

Total banco: 42:00  
Total movimento: 42:00

**Aplicando o limite semanal:**

 Ocorrências:

01/11: 02:00 Extra Normal – Compensar / 02:00 Extra Normal - Pagar  
02/11: 02:00 Extra Normal – Compensar / 02:00 Extra Normal - Pagar  
03/11: 02:00 Extra Normal – Compensar / 02:00 Extra Normal - Pagar  
04/11: 02:00 Extra Normal – Compensar / 02:00 Extra Normal - Pagar  
05/11: 02:00 Extra Normal – Compensar / 02:00 Extra Normal - Pagar  
06/11: 02:00 Extra Compensado – Compensar / 02:00 Extra Compensado – Pagar  
07/11: **04:00 Extra Descanso – Pagar (Passou das 12 horas)**08/11: 02:00 Extra Normal – Compensar / 02:00 Extra Normal - Pagar  
09/11: 02:00 Extra Normal – Compensar / 02:00 Extra Normal - Pagar  
10/11: 02:00 Extra Normal – Compensar / 02:00 Extra Normal - Pagar  
11/11: 02:00 Extra Normal – Compensar / 02:00 Extra Normal - Pagar  
12/11: 02:00 Extra Normal – Compensar / 02:00 Extra Normal - Pagar  
13/11: 02:00 Extra Compensado – Compensar / 02:00 Extra Compensado – Pagar  
14/11: **04:00 Extra Descanso – Pagar (Passou das 12 horas)**15/11: 02:00 Extra Normal – Compensar / 02:00 Extra Normal - Pagar  
16/11: 02:00 Extra Normal – Compensar / 02:00 Extra Normal - Pagar  
17/11: 02:00 Extra Normal – Compensar / 02:00 Extra Normal - Pagar  
18/11: 02:00 Extra Normal – Compensar / 02:00 Extra Normal - Pagar  
19/11: 02:00 Extra Normal – Compensar / 02:00 Extra Normal - Pagar  
20/11: 02:00 Extra Compensado – Compensar / 02:00 Extra Compensado – Pagar  
21/11: **04:00 Extra Descanso – Pagar (Passou das 12 horas)**

Total banco: 36:00  
Total movimento: 48:00

 **Aplicando o limite do período:**

Ocorrências:

01/11: 02:00 Extra Normal – Compensar – 1ª Faixa  
02/11: 02:00 Extra Normal – Compensar – 1ª Faixa  
03/11: 02:00 Extra Normal – Compensar – 1ª Faixa  
04/11: 02:00 Extra Normal – Compensar – 1ª Faixa  
05/11: 02:00 Extra Normal – Compensar – 1ª Faixa  
06/11: 02:00 Extra Compensado – Compensar – 1ª Faixa  
07/11:  
08/11: 02:00 Extra Normal – Compensar – 1ª Faixa  
09/11: 02:00 Extra Normal – Compensar – 1ª Faixa  
10/11: 02:00 Extra Normal – Compensar – 1ª Faixa  
11/11: 02:00 Extra Normal – Compensar – 1ª Faixa  
12/11: 02:00 Extra Normal – Compensar – 1ª Faixa  
13/11: 02:00 Extra Compensado – Compensar – 1ª Faixa  
14/11:  
15/11: 02:00 Extra Normal – Compensar – 1ª Faixa  
16/11: 02:00 Extra Normal – Compensar – 1ª Faixa  
17/11: 02:00 Extra Normal – Compensar – 1ª Faixa  
18/11: **02:00 Extra Normal – Compensar** **– 2ª Faixa**19/11: **02:00 Extra Normal – Compensar – 2ª Faixa**20/11: **02:00 Extra Compensado – Compensar** **– 2ª Faixa**21/11:   
Total banco 1ª faixa: 30:00  
Total banco 2ª faixa: 06:00  
Total movimento: 48:00
