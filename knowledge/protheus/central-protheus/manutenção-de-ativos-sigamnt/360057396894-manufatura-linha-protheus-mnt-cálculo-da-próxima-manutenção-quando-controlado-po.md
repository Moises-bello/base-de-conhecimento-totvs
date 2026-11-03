---
article_id: 360057396894
category: Manutenção de Ativos (SIGAMNT)
content_hash: 92449373a165bf22f4e968a9787256424b388ea22133d32a73b7f4e112309a68
fetched_at: '2026-06-28T22:42:32.838604+00:00'
product: protheus
section_id: 360012117993
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Cálculo da próxima manutenção quando controlado
  por 1 ou 2 contadores
type: support-article
updated_at: '2022-02-21T12:20:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057396894-Manufatura-Linha-Protheus-MNT-C%C3%A1lculo-da-pr%C3%B3xima-manuten%C3%A7%C3%A3o-quando-controlado-por-1-ou-2-contadores
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*Tempo aproximado para leitura: **00:01:15 min**  
**Dúvida**Como é calculada a **Data da próxima manutenção** quando o **Bem** é controlado por 1 ou 2 contadores?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Manutenção de Ativos (SIGAMNT) - Versão 12  
  
**Solução**O cálculo segue os seguintes passos:

1. Inicialmente é verificada a condição atual do **bem**, buscando saber qual a **Data do último acompanhamento do contador - T9\_DTULTAC / TPE\_DTULTA**, seu **Contador acumulado - T9\_CONTACU / TPE\_CONTAC** e sua **Variação dia - T9\_VARDIA / TPE\_VARDIA**.
2. Posteriormente busca as informações da **Manutenção - STF**, a fim de projetar o **Contador da próxima manutenção - TF\_CONMANU+TF\_INENMAN**.
3. Com base nos dados acima, pode-se calcular a **Data da próxima manutenção** realizando o cálculo abaixo.

Variáveis:  
**A - T9\_DTULTAC ou TPE\_DTULTA  
B - T9\_CONTACU ou TPE\_CONTAC  
C - T9\_VARDIA ou TPE\_VARDIA  
D - TF\_CONMANU  
E - TF\_INENMAN****Data da Próxima Manutenção = (((D + E) - B ) / C ) + A**Exemplo: **A - T9\_DTULTAC = 10/04/2020  
B - T9\_CONTACU = 6.000  
C - T9\_VARDIA = 100  
D - TF\_CONMANU = 5.500  
E - TF\_INENMAN = 1.000  
  
Data da Próxima Manutenção =((( 5.500 + 1.000) - 6.000 ) / 100) + 10/04/2020 =15/04/2020**.  
  
**Importante**Caso a **Data da próxima manutenção** calculada seja menor que **31/12/1899**, será fixada a data como **31/12/1899**.
