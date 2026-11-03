---
content_hash: f73948f724845a130b5e40ddbb8c352425f53f7b8a6c63c8c253db8e38c54241
fetched_at: '2026-06-29T00:05:55.414128+00:00'
page_id: '142812397'
product: rm
source: tdn-rm
title: Como Fazer - Parametrizacao de Banco de Horas
type: documentation
url: https://tdn.totvs.com/display/LRM/Como+Fazer+-+Parametrizacao+de+Banco+de+Horas
version: 5
---

**Produto:** *TOTVS* *Gestão* *de* *Automação* *de* *Ponto* **Versão:** *Apartir* *da* *10.80*  
 **Processo:** *Banco* *de* *Horas*  
 **Subprocesso:** *Parametrização* *de* *Banco* *de* *Horas* *Diário* *e* *por* *Período*

**Introdução**   
 Neste "*Como* *Fazer*" será apresentado os passos necessários para a parametrização do banco de horas.

**Pasta** **de** **Banco** **de** **Horas** **-** **Sindicato** **RM** **Chronus**   
  
 **Campos:**

**Utiliza** **Banco** **de** **Horas:** Ao selecionar este parâmetro o usuário terá na pasta Movimento do cadastro de funcionários uma guia chamada Banco de Horas onde ele visualizará as ocorrências diárias e também terá as demais opções relativas a Banco de Horas como a Compensação de Banco de Horas.   
  

**Tipo** **de** **Banco** **de** **Horas:**

 **Banco** **de** **Horas** **por** **Período**   
 Este tipo de banco de horas grava as compensações do período agrupados por evento.

 **Atenção:**   
 A compensação manual do banco de horas por período deve ser efetuada todo o período após fechar o ponto do funcionário e antes da liberação mensal mesmo para os funcionários que não iremos lançar eventos de extras, atrasos ou faltas para o movimento.

A compensação deve ser feita para que seja efetuada a atualização do saldo do banco de horas por período.   
 Temos que observar que em períodos anteriores ao atual não podemos ter armazenados no banco de horas eventos de horas extras junto com eventos de faltas ou atrasos.   
  

**Opções**   
 **Utiliza** **limite** **de** **horas** **diário:**   
 Habilitando esse campo, o sistema irá habilitar também os campos Limite Diário e Percentual Extra  
 Normal.   
   
**Observações:**

1. Para utilizar o limite de horas diário o parâmetro "Utiliza compensação manual de horas" na o cadastro do funcionário não pode está marcado.

2. Para utilizar este parâmetro todas as horas extras executadas pelo funcionário tem que ser autorizada, pois se não estiver o parâmetro não irá funcionar, porque neste caso todas as horas extras serão consideradas para o cálculo do sistema para compensação ou para serem pagas na movimentação do funcionário.

**Limite** **Diário:**   
 Informe o limite de horas diárias até onde serão lançadas horas para a pasta   Acima desse limite, todas as horas extras serão pagas no movimento.   
   
   
 **Exemplo:**

Limite Diário = 10:00 horas   
 Horário do funcionário:   
 08:00E 12:00S 14:00E 18:00S

Batidas do dia:  
 08:00E 12:00S 14:00E 21:00S

Neste dia o funcionário trabalhou 11:00 horas, e o limite estipulado era de 10:00 horas diárias. Neste caso o sistema irá lançar 02:00 horas extras para o banco de horas e a 01:00 que ultrapassou o limite de horas diário será paga no movimento do funcionário.

**Percentual** **Extra** **Normal:**   
 Informe o percentual, dentro do limite de horas, que será pago (portanto, não irá para o     
   
**Exemplo:**   
 Limite Diário = 10:00 horas   
 Percentual Extra Normal = 50

Horário do funcionário:   
 08:00E 12:00S 14:00E 18:00S

Batidas do dia:

08:00E 12:00S 14:00E 21:00S

Neste caso o sistema irá pagar 02:00 horas extras no movimento do funcionário, e 01:00 hora extra irá lançar no banco de horas.

Cálculos efetuados:

Horas extras lançadas para o movimento do funcionário

11:00 (horas trabalhadas) – 10:00 (limite diário) = 01:00 hora extra acima do limite   
 02:00 (horas extras para compensação ) x 50% ( percentual extra normal ) = 01:00

Horas extras lançadas para o banco de horas do funcionário   
 02:00 (horas extras para compensação ) – 01:00 ( percentual da extra normal ) = 01:00

**Utiliza** **limite** **máximo** **de** **horas** **semanais:**   
 Ao selecionar este parâmetro o Sistema irá considerar um limite máximo de horas trabalhadas a partir da qual todas as horas extras realizadas deverão ser pagas no movimento (observando o limite diário).   
   
   
 **Observação:**   
 As horas que ultrapassarem o "Limite Diário" não entram na contagem do limite de horas semanais, pois estas já foram pagas no movimento do funcionário.

**Limite** **Máximo:**   
 Informe o limite a ser considerado como máximo de horas trabalhadas na semana para verificar se as horas extras irão para o movimento ou para o banco de horas.   
   
**Exemplo** **1:**

Limite diário 10 horas   
 Limite máximo de horas semanais 48 horas   
 Jornada semanal 40 horas

Horário:   
 08:00 12:00 14:00 18:00

SEG 08:00 12:00 14:00 21:00   
 TER 08:00 12:00 14:00 20:00   
 QUA 08:00 12:00 14:00 22:00   
 QUI 08:00 12:00 14:00 21:00   
 SEX 08:00 12:00 14:00 20:00   
 SAB DOM

Segue demonstração para o cálculo do limite máximo de horas semanais:

Dia Horas para o cálculo  
 SEG 10:00   
 TER 10:00   
 QUA 10:00   
 QUI 10:00   
 SEX 10:00   
 SAB 00:00   
 DOM 00:00

Total 50:00

Limite máximo 48:00

Horas ultrapassaram o limite 02:00

Se não tivesse o limite de horas semanais, as horas que iriam para o movimento e para o banco de horas seriam respectivamente:

Movimento Banco de Horas   
 004:00        010:00

Com o limite de horas semanais o funcionário ultrapassou 02:00 de acordo com cálculo a cima das 48:00 horas estipuladas, então iremos diminuir duas horas do Banco de Horas e lançá-las para o movimento ficando com o seguinte cálculo:

Movimento Banco de Horas   
 006:00        008:00   
   
   
 **Exemplo** **2:**   
 Limite diário 10 horas   
 Limite máximo de horas semanais 48 horas   
 Jornada semanal 40 horas   
 Horário:   
 08:00 12:00 14:00 18:00   
 SEG 08:00 12:00 14:00 18:00   
 TER 08:00 12:00 14:00 19:00   
 QUA 08:00 12:00 14:00 22:00   
 QUI 08:00 12:00 14:00 22:00   
 SEX 08:00 12:00 14:00 21:00   
 SAB DOM  
 Segue demonstração para o cálculo do limite máximo de horas semanais: Dia Horas para o cálculo  
 SEG 00:00   
 TER 09:00   
 QUA 10:00   
 QUI 10:00   
 SEX 10:00   
 SAB 00:00   
 DOM 00:00

Total 39:00

Limite máximo 48:00   
 Horas ultrapassaram o limite 00:00

Como não ultrapassou o limite de horas semanais o sistema só irá considerar o cálculo do limite de horas diário de 10:00 horas.

Movimento Banco de Horas   
 005:00        007:00   
   
   
 **Exemplo** **3:**

Um funcionário trabalha 8:00 horas diária e utiliza Banco de Horas por Período com Limite Diário de 10:00.

O funcionário teve as seguintes batidas que lhe renderam hora extra no período:

Dia:       Batidas:                                       Horas Extras   
 05/05   08:00 – 12:00 14:00 – 20:00    02:00   
 06/05   08:00 – 12:00 14:00 – 21:00    03:00   
 10/05   08:00 – 12:00 13:00 – 21:00    04:00

Observe que nos dias 06/05 e 10/05, o funcionário trabalhou mais de 10:00 hs diárias. Sendo assim, o sistema fará a seguinte distribuição dessas horas extras:

Dia       Banco de Horas por Período     Movimento   
 05/05   02:00                                              00:00   
 06/05   02:00                                              01:00   
 10/05   02:00                                              02:00

Totalizando 6 horas extras no banco de horas e 3 horas extras no movimento.   
   
   
 **Observação:**   
 Se por acaso o campo "Percentual Extra Normal" estivesse marcado com um percentual de 50, o sistema lançará para o movimento 50% das horas que iriam para o Banco de Horas fazendo a seguinte distribuição:

Dia         Banco de Horas por Período        Movimento

05/05     01:00                                                  01:00   
 06/05     01:00                                                  02:00   
 10/05     01:00                                                  03:00

Totalizando 3 horas extras no banco de horas e 6 horas extras no movimento.   
   
   
 **Observações:**   
 1. Para a contagem do limite máximo de horas semanais apenas as horas que não ultrapassarem o limite diário serão consideradas para o cálculo.  
 2. As horas extras de descanso e feriado não entram para o cálculo do limite máximo de horas semanais.  
 3. Quando selecionado o limite de horas semanais, os parâmetros "Compensa extras de descanso" e "Compensa extras de feriado deverão ser desabilitados.  
 4. O parâmetro "Compensa extras de compensado" será habilitado e poderá ser utilizado também para o cálculo do limite máximo de horas semanais o "Percentual extra compensado".

**Compensa** **extras** **de** **descanso:**   
 Habilitando este parâmetro, o sistema irá lançar extras realizadas em dia de descanso no  Horas por Período,observando o limite diário. Caso contrário, as mesmas serão pagas no movimento.   
   
   
 **Observação:**   
 Compensa extras de descanso será desabilitado quando o parâmetro "Utiliza limite máximo  
 de horas semanais" estiver marcado.

**Percentual** **extra** **descanso:**   
 Informe o percentual, dentro do limite de horas, que será pagas (não irá para o

**Compensa** **extras** **de** **feriado:**   
 Habilitando este parâmetro, o sistema irá lançar extras realizadas em dia de feriado no   
  observando o limite diário. Caso contrário, as extras serão pagas no movimento.   
   
   
 **Observação:**   
 Compensa extras de descanso será desabilitado quando o parâmetro "Utiliza limite máximo de horas semanais" estiver marcado.

**Percentual** **extra** **feriado:**   
 Informe o percentual, dentro do limite de horas, que será pago (não irá para o

**Compensa** **extras** **de** **dia** **compensado:**   
 Habilitando este parâmetro, o Sistema irá lançar extras realizadas em dia de dia Compensado no Banco de Horas por Período, observando o Limite Diário. Caso contrário, as mesmas serão pagas no movimento.

**Percentual** **extra** **compensado:**   
 Informe o percentual, dentro do limite de horas, que serão pagas (não irão para o [ por Período).|mk:@MSITStore:C:/totvs/CorporeRM1140/RMChronus/Help/RMChronus.CHM::/RMChronus\_rtf/IDH\_crDFuncPMovSPFichaCompensacao.htm ]   
   
   
 **Exemplo:**   
 Se selecionarmos o parâmetro "Compensa extra de dia de compensado" e informarmos 50 no campo "Percentual extra compensado" o sistema irá fazer o seguinte cálculo para o funcionário que trabalha de segunda à sexta de 08:00 12:00 14:00 18:00, compensa no sábado e descansa no domingo:   
 Dia: Batidas: Horas Extras   
 Segunda 08:00 – 12:00 14:00 – 18:00 00:00   
 Terça 08:00 – 12:00 14:00 – 18:00 00:00   
 Quarta 08:00 – 12:00 14:00 – 18:00 00:00   
 Quinta 08:00 – 12:00 14:00 – 18:00 00:00   
 Sexta 08:00 – 12:00 14:00 – 18:00 00:00   
 Sábado 10:00 – 22:00 12:00   
 O sistema fará a seguinte distribuição dessas horas extras: Dia Banco de Horas por Período Movimento  
 Sábado 06:00 06:00

**Utiliza** **limite** **mínimo** **de** **horas** **semanais:**   
 Ao selecionar este parâmetro o Sistema irá considerar um limite mínimo de horas trabalhadas a partir da qual considerará se as horas de atrasos e/ou faltas deverão ou não ser lançadas no movimento para serem descontadas.

**Limite** **Mínimo:**   
 Informe o limite a ser considerado como mínimo de horas trabalhadas na semana para verificar se as horas de atrasos/ faltas irão para o movimento ou para o banco de horas.   
   
**Exemplo:**   
 Limite mínimo: 26 horas   
 Horas a serem trabalhadas na semana: 40 horas Horas realmente trabalhadas na semana: 24 horas Movimento Banco de Horas  
 002:00 atrasos 014:00 atrasos   
   
**Observação:**   
 Todos estes parâmetros referem-se apenas aos funcionários que possuem horário rígido.

 **Banco** **de** **Horas** **Diário:**   
 Este tipo de banco de horas mostra as ocorrências separadas por dia, informando o número de horas de cada ocorrência do funcionário naquele dia, como faltas, atrasos e os diversos tipos de horas extras.   
   
**Observações:**   
 1. Os funcionários com horário do tipo flexível podem utilizar o banco de horas diário, mas o tipo de compensação determinada no everá ser diária.  
 2. Não podemos utilizar o banco de horas diário com a Tabela de Extra e o parâmetro  
 Considera distr. extras de acordo com a jornada.   
   
**Observação:**   
 Os funcionários com horário do tipo flexível podem utilizar o banco de horas diário, mas o tipo de compensação determinada no everá ser diária.   
   
**Início** **da** **Compensação:**

**Primeira** **Faixa:**  
 Indica se a compensação começará a partir da primeira faixa de extra cadastrada em OPÇÕES |  
 PARAMETROS | SINDICATO RM CHRONUS | FAIXA DE EXTRAS .   
   
   
 **Exemplo:**   
 Caso as extras realizadas pelos funcionários sejam pagas da seguinte maneira: As duas primeiras horas extras serão pagas 50% a hora e se referem a 1a. Faixa. As horas subseqüentes serão pagas 100% a hora e se referem a 2a. Faixa.  
 Se marcar este parâmetro o sistema irá fazer a compensação pelas horas extras 50% e depois irá compensar as horas extras 100%.

**Última** **Faixa:**   
 Indica se a compensação começará a partir da última faixa de extra.   
   
**Exemplo:**   
 Caso as extras realizadas pelos funcionários sejam pagas da seguinte maneira: As duas primeiras horas extras serão pagas 50% a hora e se referem a 1a Faixa. As horas subseqüentes serão pagas 100% a hora e se referem a 2a. faixa  
 Se marcar este parâmetro o sistema irá fazer a compensação pelas horas extras 100% e depois irá compensar as horas extras 50%.   
 **Utiliza** **banco** **por** **ocorrências:**   
 Ao marcar este parâmetro o sistema disponibilizará um campo onde será selecionado as atitudes para as ocorrências dos funcionários, seja se as horas extras serão pagas ou compensadas e se os atrasos ou faltas serão descontados ou compensados.   
 As atitudes das ocorrências podem ser alteradas individualmente pelo módulo MOVIMENTO | OCORRÊNCIAS | COLETADAS ou global no módulo MOVIMENTO LANÇAMENTOS GLOBAIS | AUTORIZAÇÃO.   
   
**Exemplo:**   
 Todas as horas extras, atrasos e faltas serão compensadas (irão para o banco de horas), mas no dia 12/02 o funcionário fez duas horas extras e estas horas serão pagas no movimento  
 do funcionário e não compensadas.   
 Para pagar estas horas extras basta que no módulo MOVIMENTO | OCORRÊNCIAS |  
 COLETADAS altere a atitude desta ocorrência para pagar.   
   
   
 **Observação:**   
 1. Funcionários com tipo de horário flexível com compensação por período ou semanal e horário núcleo não podem utilizar "banco por ocorrências".   
  

**Limite** **de** **Extras:**

**Limita** **Extras** **por** **período**   
 Limita extras por período e o campo Limite de Horas.   
 Ao habilitar este parâmetro o sistema irá limitar o número de horas extras por período que serão enviadas para o banco de horas. As horas extras restantes (superiores ao limite informado) serão pagas na movimentação do funcionário.   
   
**Observações:**   
 1) Esta opção está disponível apenas para banco de horas diário. Banco de Horas diário por ocorrência não pode utilizar este recurso.   
 2) Utilizando o Limite de Horas por período, o parâmetro de limite de horas por semana será desabilitado.   
   
**Exemplo:**   
 [ X ] Limita Extra por período   
 Limite de Horas: 20:00 horas extras.   
 Extras efetuadas pelo funcionário no período: 23:00   
 Banco de horas do funcionário: 20:00 horas extras   
 Movimento do funcionário: 03:00 horas extras ( horas pagas na movimentação do funcionário )

**Limita** **Extras** **por** **semana**   
 Marcando esta opção o sistema irá habilitar o campo "Limite de horas" para informar o número de horas extras que serão encaminhadas para o banco de horas. As horas extras que ultrapassarem o limite semanal informado serão pagas no movimento do funcionário.   
   
**Observações:**   
 1) Esta opção está disponível apenas para banco de horas diário. Banco de Horas diário por  
 ocorrência não pode utilizar este recurso.   
 2) Utilizando o Limite de Horas por semana, o parâmetro de limite de horas por período será desabilitado.   
   
**Exemplo:**   
 [ X ] Limita Extra por semana   
 Limite de Horas: 05:00 horas extras.   
 Extras efetuadas pelo funcionário na primeira semana: 02:15   
 Extras efetuadas pelo funcionário na segunda semana: 07:32   
 Extras efetuadas pelo funcionário na terceira semana: 04:00   
 Extras efetuadas pelo funcionário na quarta semana: 05:52   
 Banco de horas do funcionário: 16:15 horas extras   
 Movimento do funcionário: 03:24 horas extras ( horas pagas na movimentação do funcionário )   
  

**Atitudes:**   
 Para banco de horas diário ou diário por ocorrência serão habilitadas as atitudes ( Atrasos, Faltas, Horas Extras Normais, Horas Extras Feriado, Horas Extras Descanso, Horas Extras Compensado ) abaixo discriminadas para escolher quais serão compensadas ( irão para o banco de horas ), pagas, ou descontadas.

**Atitude** **Atrasos**   
 Compensar - Ao marcar a atitude como Compensar, todas as ocorrências de atrasos serão utilizadas para a compensação.   
 Descontar - Ao marcar a atitude como Descontar, todas as ocorrências de atrasos serão descontadas no movimento do funcionário.

**Atitude** **Faltas**   
 Compensar - Ao marcar a atitude como Compensar, todas as ocorrências de faltas serão utilizadas para a compensação.   
 Descontar - Ao marcar a atitude como Descontar, todas as ocorrências de faltas serão descontadas no movimento do funcionário.

**Atitude** **Extras** **Normais**  
 Compensar - Ao marcar a atitude como Compensar, todas as ocorrências de extras normais serão utilizadas para a compensação.   
 Pagar - Ao marcar a atitude como Pagar, todas as ocorrências de extras normais serão pagas no movimento do funcionário.

**Atitude** **Extras** **Feriado**   
 Compensar - Ao marcar a atitude como Compensar, todas as ocorrências de extras feriado serão utilizadas para a compensação.   
 Pagar - Ao marcar a atitude como Pagar, todas as ocorrências de extras feriado serão pagas no movimento do funcionário

**Atitude** **Extras** **Descanso**   
 Compensar - Ao marcar a atitude como Compensar, todas as ocorrências de extras descanso serão utilizadas para a compensação.   
 Pagar - Ao marcar a atitude como Pagar, todas as ocorrências de extras descanso serão pagas no movimento do funcionário

**Atitude** **Extras** **Compensado**   
 Compensar - Ao marcar a atitude como Compensar, todas as ocorrências de extras compensado serão utilizadas para a compensação.   
 Pagar - Ao marcar a atitude como Pagar, todas as ocorrências de extras compensado serão pagas no movimento do funcionário   
   
**Observação:**   
 Apenas para o banco de horas diário por ocorrências podem ser feitas alterações nas atitudes das ocorrências em apenas um dia em específico ou mais dias, para um ou mais funcionários sem alterar esta atitude no parâmetro Sindicato RM Chronus. Para o banco de horas diário o sistema sempre irá respeitar as atitudes para todo o período determinadas neste parâmetro.
