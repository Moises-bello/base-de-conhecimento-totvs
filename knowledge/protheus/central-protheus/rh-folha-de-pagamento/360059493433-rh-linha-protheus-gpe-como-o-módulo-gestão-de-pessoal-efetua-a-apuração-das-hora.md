---
article_id: 360059493433
category: RH - Folha de Pagamento
content_hash: 1bea20eb271cc9b63eb3a7f7e143efd35a9882e8beaed09a44e5978fe634162e
fetched_at: '2026-06-28T22:44:13.575215+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Como o módulo Gestão de Pessoal efetua a apuração
  das Horas Normais e DSR
type: support-article
updated_at: '2025-08-12T13:21:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059493433-RH-Linha-Protheus-GPE-Como-o-m%C3%B3dulo-Gest%C3%A3o-de-Pessoal-efetua-a-apura%C3%A7%C3%A3o-das-Horas-Normais-e-DSR
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26350205723927) Tempo aproximado para leitura: 00:03:00 min**

**Ocorrência**Como o módulo Gestão de Pessoal efetua a apuração das Horas Normais e DSR.   
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – A partir da versão 12.1.17  
  
**Causa**O sistema efetua a apuração de acordo com o conteúdo do Mnemônico **P\_NDSRHORI**. O cálculo do **salário do horista** é feito da seguinte forma: campo **Horas Dia (RA\_HRSDIA)** multiplicado pelo campo **Dias Uteis (RCF\_DUTEIS)**, o cálculo do **DSR** segue o mesmo raciocínio, sendo o campo **Horas Dia (RA\_HRSDIA)** multiplicado pelo campo **Nº Dias DSR (RCF\_DIADSR)**.

Ocorre que com este cálculo, caso o funcionário não tenha trabalhado todos os dias do mês, não é possível obter o número exato de horas normais e de DSR,

**Solução**Devido a isto foi criado o Mnemônico **P\_NDSRHORI** que irá alterar a forma de apuração dos dias trabalhados para os horistas.

Rotina **Mnemônicos - GPEA300:** SIGAGPE > **Atualizações >Definições de Cálculo >Mnemônicos**  
  
![mnemonico.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/360100064433)

Para essa apuração quatro opções: 

* **0**, a apuração será feita da maneira que é hoje, ou seja, campo Horas Dia (RA\_HRSDIA) X campo Dias Uteis (RCF\_DUTEIS) no caso do **salário do horista** e campo Horas Dia (RA\_HRSDIA) X Nº Dias DSR (RCF\_DIADSR) para o **DSR.**
* **1**, a apuração será feita através do calendário de períodos da folha (**SIGAGPE**), ou seja, dentro do período trabalhado serão apurados quantos dias de DSR e quantos dias trabalhados existiram, multiplicando estes dias pelo conteúdo do campo **Horas Dia** (**RA\_HRSDIA**), ou seja, dentro do período que o funcionário trabalhou quantos dias são de DSR e quantos dias são trabalhados (não inclui dias compensados).
* **2**, a apuração será feita através do calendário do ponto (**SIGAPON**), ou seja, dentro do período trabalhado serão apurados quantos dias de DSR e quantos dias de trabalhados s existiram, multiplicando estes dias pelo conteúdo do campo **Horas Dia (RA\_HRSDIA)**, ou seja, dentro do período que o funcionário trabalhou quantos dias são de DSR e quantos dias são trabalhados.
* **3**, a apuração será feita considerando somente o calendário do ponto (**SIGAPON**), ou seja, dentro do período trabalhado serão apurados as respectivas horas trabalhadas e de DSR.

**Saiba Mais**  
[TVKTW6\_DT\_Mnemonico\_PNDSRHORI\_Apuracao\_DSR\_e\_Horas\_Normais\_Horistas](https://tdn.totvs.com/display/public/PROT/TVKTW6_DT_Mnemonico_PnDSRHori_Apuracao_DSR_e_Horas_Normais_Horistas#exemplo-3)

[RH - Protheus - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)

[RH - Linha Protheus - GPE - Como fazer o download (baixar) do pacote de expedição contínua (acumulado) do RH Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)
