---
content_hash: e3adbc968bc8a9e966d1d361ba75bea60b097c782857363ac148697ba5f8cbe7
fetched_at: '2026-06-29T00:10:08.730145+00:00'
page_id: '452719568'
product: rm
source: tdn-rm
title: Acerta Período Aquisitivo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719568
version: 5
---

Este módulo tem o objetivo em ajustar o período aquisitivo do funcionário afastado e/ou com faltas.  
   
É verificado se o funcionário perde o direito às férias, observando se durante o período aquisitivo ocorreu uma das seguintes situações:  
   
a)    houve faltas superiores á 32 dias;  
**Atenção:**  
É necessário verificar parametrizações de faltas.

Para a situação acima, o funcionário perde todo o período aquisitivo e é aberto um novo período acrescido de 1 ano.  
   
b)    houve afastamento do tipo R-Licença Remunerada por mais de 30 dias;

**Atenção:**  
Para a situação acima, o novo período aquisitivo será iniciado quando o funcionário retornar ao serviço.  
   
c)     houve afastamento dos tipos: P-Previdência, T-Acidente do Trabalho ou O-Doença Ocupacional por mais de seis meses (180 dias), embora descontínuos e desconsiderando os 15 dias pagos pela empresa;  
Neste caso, o novo período aquisitivo será iniciado quando o funcionário retornar ao serviço do último afastamento cuja soma de dias for maior que 195 dias, somando os 15 dias  pagos pela empresa.  
   
**Exemplo 1:**  
Período aquisitivo: 21/02/2019 a 20/02/2020  
Afastamento P-Previdência: 01/03/2019 a 15/10/2019  
Competência: 10/2019  
Após processar o Acerta Período Aquisitivo o período aquisitivo é alterado para 16/10/2019 a 15/10/2020, ou seja, o início do período aquisitivo passar a ser o primeiro dia de trabalho após o afastamento.

**Exemplo 2:**  
Período aquisitivo: 17/10/2018 a 17/10/2019  
Afastamentos P-Previdência:

21/12/2018 30/03/2019 100 dias afastamento tipo P pelo motivo 10  
01/04/2019 10/05/2019 40 dias afastamento tipo P pelo motivo 10  
01/06/2019 25/07/2019 55 dias afastamento tipo P pelo motivo 10  
04/09/2019 08/09/2019 5 dias afastamento tipo P pelo motivo 10  
16/09/2019 19/09/2019 4 dias afastamento tipo P pelo motivo 10

TOTAL = 204 dias de afastamento pelo mesmo tipo e motivo, contando com os 15 dias pagos pela empresa.

Competência: 09/2019  
Após processar o Acerta Período Aquisitivo o período aquisitivo é alterado para 09/09/2019 a 08/09/2020, ou seja, o início do período aquisitivo passar a ser o primeiro dia de trabalho após o afastamento em que o limite de 180  dias mais os 15 dias pagos pela empresa foram atingidos. O outro afastamento de 16/09/2019 19/09/2019 passa a ser contado no período aquisitivo aberto.

d)    houve afastamento dos tipos: L-Licença s/ Vencimento, M-Serviço Militar, I-Aposentadoria por invalidez, S - Mandato Sindical, C- Contrato suspenso ou Q - Prisão/Cárcere:  
Neste caso, o término do período aquisitivo é ajustado somando o total de dias de afastamento à data final do período;

É imprescindível que este módulo seja executado todo mês antes da geração do histórico de provisão de férias.  
Para evitar esquecimento existe o parâmetro 'Acerta de período aquisitivo obrigatório' em Configurações | Parametrizador | Férias | Controle.  
    
O período aquisitivo é acertado a partir do período aquisitivo com status 'Aberto'.  
    
Quando o saldo do período aquisitivo vencido é negativo, este período é fechado sendo aberto um novo.  
   
**Atenção:**   
O período somente é acertado quando às férias estão finalizadas.
