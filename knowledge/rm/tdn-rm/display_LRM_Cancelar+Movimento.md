---
content_hash: 75460bd7d049ba961e791fe5e3cabb106d83f824fc1aafb30039cdcc852ff00f
fetched_at: '2026-06-29T00:10:08.771883+00:00'
page_id: '452719576'
product: rm
source: tdn-rm
title: Cancelar Movimento
type: documentation
url: https://tdn.totvs.com/display/LRM/Cancelar+Movimento
version: 3
---

**Cancelar Movimento**   
Através do recurso Cancelar Movimento, você poderá desconsiderar as batidas para o cálculo, eventos lançados ou toda a movimentação do período de um ou mais funcionários/visitantes, para correção/complementação de informações já lançadas. Conforme Portaria 1510/2009 do MTE, o SREP (Sistema de Registro Eletrônico de Ponto) deve registrar fielmente as marcações efetuadas, não sendo permitida qualquer ação que desvirtue os fins legais a que se destina, ou seja, as batidas provenientes do terminal de coleta deverão ser mantidas registradas e não poderão sofrer cancelamento definitivo, no qual dá origem ao módulo AFDT.  
Veja mais informações nas Adequações do RM Chronus à Portaria 1510/2009.  
O intervalo de datas do período de seleção de datas será utilizado para delimitar o cancelamento do movimento.  
**Observação:**  
O sistema não permite gerenciar batidas de períodos anteriores ao período atual informado no módulo de períodos do sistema.  
   
Considerando a data de importação, o sistema fará com que as batidas sejam desconsideradas para o cálculo de acordo com a data da importação no período informado. Caso contrário, serão desconsideradas de acordo com a data da batida no período informado.  
   
**Exemplo:**  
Importação de batidas no dia 02/09/XXXX.  
   
Chapa Data               Batida  Status   Natureza DataInsercao  
00002  01/09/XXXX    08:00    C         0            02/09/XXXX  
00002  01/09/XXXX    14:00    C         1            02/09/XXXX  
00002  02/09/XXXX    08:00    C         0            02/09/XXXX  
00002  02/09/XXXX    14:05    C         1            02/09/XXXX  
00002  03/09/XXXX    08:00    C         1            03/09/XXXX  
   
Desconsiderar batidas de acordo com a data de importação = 02/09/XXXX  
Período: Início: 02/09/2007 Término: 02/09/XXXX  
Marcar o parâmetro Considera data de importação  
Neste caso todas as batidas com DataInsercao = 02/09/XXXX serão desconsideradas para o cálculo.  
   
**Observação:**  
Apenas batidas com o Status de coletadas poderão ser desconsideradas quando utilizar o parâmetro Considerar data de importação.  
   
Na seleção de tipos de pessoas, há a possibilidade de desconsiderar batidas de funcionários, visitantes ou dos dois tipos de pessoas ao mesmo tempo.  
   
O Status da batida deve ser informado no cancelamento, sendo:   
**Coletadas** - Coletadas pelo relógio.  
**Digitadas** - Incluídas ou alteradas pelo usuário.  
**Trânsito** - Coletadas pelos terminais de coleta e que não são consideradas pelo cálculo.  
   
No movimento do cancelamento é possível desconsiderar:  
**Batidas conforme jornada** – onde serão desconsideradas as batidas considerando a jornada cadastrada no horário do funcionário, facilitando o controle de jornadas de um dia para o outro.  
**Exemplo:**  
Considerando as seguintes batidas cadastradas para o horário:  
01/09/XXXX - 22:00E  
02/09/XXXX - 02:00S 03:00E 05:00S 22:00E  
03/09/XXXX - 02:00S 03:00E 05:00S 22:00E  
Jornada: 22:00h as 05:00h  
   
Ao desconsiderar as batidas da data 02/09 marcando o parâmetro, o sistema irá desconsiderar para o cálculo as seguintes batidas:  
02/09/XXXX - 22:00E  
03/09/XXXX - 02:00S 03:00E 05:00S  
**Abonos** - onde serão cancelados os abonos do período informado, além do movimento.  
**Cancela batidas de refeição -** onde serão desconsideradas as batidas que foram coletadas pelo relógio de refeitório que estão cadastradas no cadastro do funcionário, na pasta Refeições, subpasta Batidas de Refeições.  
   
Os Tipos de batidas serão selecionados de acordo com a necessidade:  
**Batidas normais** – onde serão desconsideradas as batidas;   
**Batidas da ausência planejada -** onde serão desconsideradas as batidas que foram lançadas para a pasta de Espelho do período do funcionário que coincidirem com o intervalo de refeição cadastrado no horário do funcionário. O sistema também verificará a tolerância cadastrada no parâmetro Sindicato RM Chronus do funcionário para efetuar o processo.  
**Exemplo:**  
Horário do funcionário: 08:00E 12:00S 14:00E 18:00S  
Intervalo de refeição definido no horário: 12:00 às 14:00  
Intervalo de tolerância cadastrado no parâmetro Sindicato RM Chronus: Saída 1 = 00:10 antes e depois, Entrada 2 = 00:10 antes e depois.  
Batidas efetuadas pelo funcionário:  
Seg 08:00E 12:05S 13:52E 18:00S  
Ter 08:00E 13:00S 14:00E 18:00S  
Qua 08:00E 11:40S 14:05E 18:00S  
Qui 08:00E 12:15S 14:15E 18:00S  
Sex 08:00E 11:00S 12:00E 18:00S  
Batidas do funcionário após o cancelamento do intervalo de refeição:  
Seg 08:00E 18:00S  
Ter 08:00E 18:00S  
Qua 08:00E 11:40S18:00S  
Qui 08:00E 14:15E 18:00S  
Sex 08:00E 11:00S 18:00S  
O sistema não irá desconsiderar as batidas de 11:40 da Qua, 14:15 da Qui e 11:00 da Sex porque estas batidas não estão no intervalo e também não se encontram na tolerância do intervalo de refeição.  
   
Conforme portaria 1.510/2009 do MTE, o campo "Justificativa" é de preenchimento obrigatório para Cancelar o Movimento.  
   
**Observação:** Caso o recálculo para o usuário logado esteja travado  ou recálculo do funcionário contido no filtro de seleção esteja bloqueado, o processo de cancelamento de batidas não será executado.

**Gerar log analítico do processo:** Este parâmetro determina se será gerado um log detalhado do processo de cancelamento do movimento. Ele será válido apenas se o cancelamento for executado para apenas 1 funcionário.
