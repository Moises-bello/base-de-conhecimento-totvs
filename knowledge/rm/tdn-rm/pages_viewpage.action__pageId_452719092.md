---
content_hash: 188215d0fed9e8bf104738733d816660c36acf814bceebb643649289e748bd72
fetched_at: '2026-06-29T00:10:03.293886+00:00'
page_id: '452719092'
product: rm
source: tdn-rm
title: Relatório de Batidas fora da tolerância
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719092
version: 2
---

**Relatório de Batidas fora da tolerância**

O relatório se aplica apenas para  funcionários que tenham horário do tipo rígido.  
É considerado o intervalo planejado com as tolerâncias definidas, para verificar se as batidas estão dentro ou fora. 

Os horários de entrada e saída dos funcionários são cadastrados como horários exatos e como períodos de entrada e saída. Em várias empresas com elevado número de funcionários, para que todos conseguissem bater o ponto no espaço de tempo de apenas um minuto, seria necessário um grande número de relógios de ponto e/ou o escalonamento de horários por departamentos da empresa. Visando sanar este problema, o sistema permite o cadastramento de períodos ou **intervalos de tolerância** dentro dos quais, o horário de batida do ponto será considerado como correspondente ao horário oficial durante os cálculos, sem que calcule atrasos ou extras.  
Utilize o **Relatório de Batida fora da tolerância** para visualizar as batidas que se encontram fora do horário de tolerância cadastrado para o funcionário.  Estas tolerâncias podem ser cadastradas no horário do funcionário ou no sindicato sendo que a prioridade é sempre da tolerância que está cadastrada no horário.  
   
**Exemplo**  
Suponhamos que o funcionário tem o seguinte horário:  
Entrada   Saída   
14:00      20:00  
Intervalo de tolerância de 10 minutos antes e 10 minutos depois das batidas de entrada e saída.  
O funcionário registrou as seguintes batidas:  
Dia 2  13:47 – 19:52  
Dia 3  14:05 – 20:00  
Dia 4  14:10 – 20:05  
Dia 5  14:00 – 20:15  
Dia 6  13:49 – 19:40  
Neste caso o relatório de Batidas fora da tolerância trará as seguintes batidas:  
Dia 2   13:47E  
Dia 5   20:15S  
Dia 6   13:49E   19:40S  
   
Para flexibilizar a utilização, o layout do relatório poderá ser configurado de acordo com a necessidade da empresa através do novo gerador de relatório (RM Reports).   
**Observação**  
A utilização desse relatório dependerá de um modelo criado pela TOTVS, no qual ficará disponível no momento da instalação do aplicativo RM Chronus. Basta acessar o RM Reports e realizar a importação do arquivo com a estrutura do arquivo (PTOREL01.0009 - Relatório Batidas Fora da Tolerância .TotvsReport).
