---
content_hash: 914202d4e1208319ba08b9742b702941db93c82e752fe2d828350cd8250bd993
fetched_at: '2026-06-29T00:10:05.409505+00:00'
page_id: '452719288'
product: rm
source: tdn-rm
title: Adicional Noturno
type: documentation
url: https://tdn.totvs.com/display/LRM/Adicional+Noturno
version: 90
---

**Adicional Noturno**

**Início, Fim e Tolerância diária** Defina em qual período o sistema irá calcular Adicional Noturno, e se haverá uma tolerância.  
Exemplo:  
Início: 22:00 - Fim: 05:00 - Tolerância: 01:00  
Horário Executado

|  |  |  |  |
| --- | --- | --- | --- |
| Data | Entrada 1 | Saída1 | Adicional Noturno |
| 25/02/2011 | 14:00 | 22:50 | 00:00 |
| 26/02/2011 | 14:00 | 23:00 | 00:00 |
| 27/02/2011 | 14:00 | 23:01 | 01:01 |
| 28/02/2011 | 04:00 | 05:00 | 00:00 |
| 29/02/2011 | 04:30 | 05:00 | 01:30 |

**Abate tolerância de adicional noturno** Habilitando esse parâmetro as horas de tolerância de adicional noturno serão abatidas no adiciona noturno realizado pelo funcionário.  
Início: 22:00 - Fim: 05:00 - Tolerância: 01:00  
Abate Tolerância  
Horário Executado

|  |  |  |  |
| --- | --- | --- | --- |
| Data | Entrada 1 | Saída1 | Adicional Noturno |
| 25/02/2011 | 14:00 | 22:50 | 00:00 |
| 26/02/2011 | 14:00 | 23:00 | 00:00 |
| 27/02/2011 | 14:00 | 23:01 | 00:01 |
| 28/02/2011 | 04:00 | 05:00 | 00:00 |
| 29/02/2011 | 04:30 | 05:00 | 00:30 |

**Calcula adicional noturno para o intervalo de refeição** Habilitando esse parâmetro caso o funcionário tenha uma Ausência Planejada (Intervalo de Refeição) cadastrado em seu horário o sistema irá inserir as horas do intervalo no cálculo de adicional noturno.  
**Exemplo:**  
Início: 22:00 - Fim: 05:00  
   
Horário Planejado

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Data | Entrada1 | Saída1 | Entrada2 | Saída2 | Entrada3 |
| 25/02/2011 | 22:00 | 22:59 | 23:59 |  |  |
| 26/02/2011 |  | 05:00 | 22:00 | 22:59 | 23:59 |
| 27/02/2011 |  | 05:00 |  |  |  |

Horário Executado

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Data | Entrada1 | Saída1 | Entrada2 |  |  |
| 25/02/2011 | 22:00 | 22:59 | 23:59 |  |  |
| 26/02/2011 |  | 05:00 | 22:00 |  |  |
| 27/02/2011 |  | 05:00 |  |  |  |

Na jornada do dia 25/02/2011 o funcionário teve um total de Adicional Noturno de 06:00 horas, ao habilitar o parâmetro o sistema também calcula o intervalo de refeição de 22:59 ás 23:59 totalizando 07:00 horas de Adicional Noturno na jornada.   
Já na jornada do dia 26/02/2011 o funcionário teve um total de Adicional Noturno de 07:00 horas, pois ele não efetuou intervalo de refeição, assim mesmo com o parâmetro habilitado será calculado 07:00 horas de Adicional Noturno para a jornada.  
**Observação:** Para funcionários que utilizam Horário por Jornada, o intervalo de refeição será calculado caso:

* O campo 'Tempo de Refeição' no cadastro do índice da jornada seja maior que 00:00;
* Deverá ter interseção com o adicional noturno conforme configuração do Parâmetro do sindicato;
* Como o horário por jornada não possui intervalo de refeição, será considerado o primeiro intervalo do horário executado, independente se existir mais de um intervalo no horário.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Data | Entrada 1 | Saída1 | Atraso | Extra |
| 01/02/2011 | 14:00 | 23:00 | 01:00 | 01:00 |
| 02/02/2011 | 14:00 | 22:00 | 00:00 | 00:00 |
| 03/02/2011 | 14:00 | 22:00 | 00:00 | 00:00 |

 Com o parâmetro marcado:  
No dia 01/02/2011 houve compensação, assim irá gerar 00:00 de extra, e não irá calcular Extra de Adicional Noturno, pois as extras foram compensadas.  
Atrasos: 00:00  
Extras: 00:00  
Extra de Adicional Noturno: 00:00  
   
Com o parâmetro desmarcado:  
Para o exemplo acima do dia 01/02/2011 o cálculo irá gerar Extras de Adicional Noturno sobre as extras compensadas.  
Atrasos: 00:00  
Extras: 00:00  
Extras de Adicional Noturno: 01:00  
   
**Considera executado efetivo no adicional noturno** Habilitando esse parâmetro o sistema irá considerar o executado efetivo após a aplicação da tolerância de batidas caso tenha cadastrado tolerância no horário do funcionário.

Exemplo:

Horário do Funcionário: 14:00 as 22:30  
Adicional Noturno: 22:00 as 05:00  
Tolerância de Batidas: 00:05 (Abate Tolerância)  
   
Com o parâmetro habilitado  
Horário Executado

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Data | Entrada 1 | Saída1 | Extra | Adicional Noturno |
| 01/02/2011 | 14:00 | 22:35 | 00:00 | 00:30 |
| 02/02/2011 | 14:00 | 22:40 | 00:05 | 00:35 |

Com o parâmetro Desabilitado  
Horário Executado

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Data | Entrada 1 | Saída1 | Extra | Adicional Noturno |
| 01/02/2011 | 14:00 | 22:35 | 00:00 | 00:35 |
| 02/02/2011 | 14:00 | 22:40 | 00:05 | 00:40 |

A partir da versão **12.1.2506.122** o parâmetro "**Para Jornadas iniciadas até [xx : xx]**" foi alterado para "**Para jornadas iniciadas entre xx:xx até xx:xx**"

**Para jornadas iniciadas entre xx:xx até xx:xx**: Neste parâmetro, é definido o intervalo de horário em que as jornadas iniciadas dentro desse período terão direito ao adicional noturno estendido.  
A edição deste campo só será possível caso o parâmetro "Considera adicional noturno até o fim da jornada" esteja marcado.

**Exemplo 1:**

* **Adicional Noturno parametrizado:** Início: 22:00 | Fim: 05:00
* **Horário Planejado:** [22:00E – 05:00S]
* **Horário Executado:** [23:00E – 07:00S]
* **Para jornadas iniciadas entre** [22:00] **até** [02:00]

Como a jornada iniciou às 23:00, que está dentro do período definido no parâmetro, será considerado o adicional noturno estendido até o fim da jornada.  
Total de adicional noturno considerado: 08:00 horas.

**Exemplo 2:**

* **Adicional Noturno parametrizado:** Início: 22:00 | Fim: 05:00
* **Horário Planejado:** [22:00E – 05:00S]
* **Horário Executado:** [02:10E – 07:00S]
* **Para jornadas iniciadas entre** [22:00] **até** [02:00]

Como a jornada iniciou às 02:10, que está fora do período definido no parâmetro, não será considerado o adicional noturno estendido até o fim da jornada.  
Será considerado apenas o adicional noturno padrão configurado, das 02:10 às 05:00, totalizando 2 horas e 50 minutos de adicional noturno.

Importante

O horário final do intervalo do adicional noturno estendido deve estar dentro do período do adicional noturno cadastrado. Caso esteja fora desse limite, o sistema não prosseguirá e exibirá um alerta.

Para mais detalhes sobre o funcionamento do parâmetro "**Para jornadas iniciadas entre XX:XX até XX:XX**" acesse [Configuração e Aplicação do Novo Cálculo do Adicional Noturno Estendido](https://tdn.totvs.com/pages/viewpage.action?pageId=962611128#1-1).

**Considera arredondamento diário no movimento período:** Ao habilitar, o sistema arredonda cada evento de adicional noturno antes de realizar a soma.

**Exemplo parâmetro desmarcado:**

Funcionário: 00001

Período: 20/04/2026 a 19/05/2026

Dias trabalhados no adicional noturno (22:00 às 05:00):

Dia 25/04:

* 00:05:42 (5 minutos e 42 segundos)

Dia 13/05:

* 00:05:42 (5 minutos e 42 segundos)

Total bruto (sem arredondamento): 00:11:24 (11 minutos e 24 segundos)

O produto arredonda os valores no final. Como não ultrapassa 30 segundos**, o valor é arredondado para BAIXO, resultando em 11 minutos.**

**Exemplo parâmetro Marcado:**

Dia 25/04:

* Adicional bruto: 00:05:42 (5 minutos e 42 segundos)
* Arredondamento:  00:06:00 (6 minutos)

Dia 13/05:

* Adicional bruto: 00:05:42 (5 minutos e 42 segundos)
* Arredondamento:  00:06:00 (6 minutos)

Soma dos valores já arredondados:

00:06:00 + 00:06:00 = 00:12:00 (12 minutos)

Arredonda cada evento individualmente e depois soma os valores já arredondados. **Como ultrapassa 30 segundos, o valor é arredondado para CIMA, resultando em 12 minutos.**

Importante

O parâmetro não altera o valor que esta na aba movimento, esses valores de adicional noturno deve refletir o mais próximo que o funcionário executou.

Na aba movimento são somados os valores do movimento do período, em que o tipo de evento do Folha de Pagamento é o mesmo, retornando o evento e seu total no período.

O movimento não é afetado por "**considera arredondamento diário no movimento período"**, apenas por "**considera percentual de adicional noturno"** no cálculo da ocorrência.
