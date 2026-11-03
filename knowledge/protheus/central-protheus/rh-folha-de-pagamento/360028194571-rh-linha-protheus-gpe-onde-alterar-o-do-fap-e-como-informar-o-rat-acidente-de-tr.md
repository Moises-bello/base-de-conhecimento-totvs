---
article_id: 360028194571
category: RH - Folha de Pagamento
content_hash: 0c05be14e39180661a0d1adcf560b757a934444e0fc002849170f43878f0cf38
fetched_at: '2026-06-28T22:44:16.448551+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE-  Onde alterar o % do FAP e como informar o RAT (acidente
  de trabalho) no sistema
type: support-article
updated_at: '2026-01-26T20:27:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028194571-RH-Linha-Protheus-GPE-Onde-alterar-o-do-FAP-e-como-informar-o-RAT-acidente-de-trabalho-no-sistema
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26328684675735)** Tempo aproximado para leitura: **00:03:00 min**

**Dúvida**  
Onde alterar o % do FAP, informar o RAT (acidente de trabalho) no sistema e como enviar ao e-social?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12  
  
**Solução**  
Para ajuste do valor do **RAT,** deve ser feita a **multiplicação** entre o **FAP** e o **percentual do Acidente de Trabalho.**

O valor encontrado deverá ser informado no campo Acidente de Trabalho **%ACID. TRAB.** na Tabela S037 da rotina Manutenção Tabelas, pelo caminho **>Atualizações >Definições de Cálculo >Manutenção Tabelas**.

Exemplo:

Acidente de Trabalho = **3.00**  
FAP = **1.5687**

Calculo:  
Percentual Acidente de Trabalho = **3.000 \* 1.5687 = 4.7061**   
  
-A coluna **%Acid. Trab.** passará a ter o percentual de **4.7061%**   
-O percentual do **FAP** deverá ser digitado na coluna **%RAT**   
  
Abaixo exemplo:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4405940459671)

Calculo da Folha.  
Conferência: Soma dos Ids **0013 e 0014** \* Alíquota Acid Trabalho **(4.7061%) = Acidente trabalho (ID 0150)**  
**R$ 4.384,00 \* 4.7061% = 206,32**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29129168547991)

**OBS:** Mesmo existindo o campo **FAP** no programa da **Sefip,** não existe leiaute para este campo, portanto ele **deve** ser informado manualmente, e este campo **% do FAP não** aceita as **4 casas decimais**, o sistema da **Sefip** aceita somente as **duas primeiras** casas decimais.

A **Sefip** valida este campo onde o valor deve estar **entre 0,50 e 2,00.** Já o campo do **RAT** aceita de **0,0 até 3,0%**

A Sefip faz o seguinte calculo:  
Alíquota RAT \* FAP=  o percentual encontrado o sistema aplica na base do INSS para entrar o RAT  
Neste exemplo ficaria da seguinte forma:  
3,00\* 1,56= 4,68

**Saiba Mais**  
[RH - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)  
[RH - Linha Protheus - GPE - eSocial - S-1005 - Como realizar alteração do FAP](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041285873)  
[ChatBot Carol Assistant](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022200991)
