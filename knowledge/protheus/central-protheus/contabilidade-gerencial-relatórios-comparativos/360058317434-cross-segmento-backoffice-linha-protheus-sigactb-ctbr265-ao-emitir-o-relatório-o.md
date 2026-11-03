---
article_id: 360058317434
category: Contabilidade Gerencial - Relatórios Comparativos
content_hash: c2658c71189b546b4cc05bde77d7dd004a5545fa69dc0ee7b7b4d8d8f24d3d31
fetched_at: '2026-06-28T22:40:37.144569+00:00'
product: protheus
section_id: 1500001548922
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBR265 Ao emitir o
  relatório o saldo é apresentado zerado
type: support-article
updated_at: '2022-05-25T21:05:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058317434-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBR265-Ao-emitir-o-relat%C3%B3rio-o-saldo-%C3%A9-apresentado-zerado
---

**Ocorrência**

Ao emitir o relatório CTBR265 ,após realizar [Apuração Trimestral : Apuração Sem conta PONTE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041554693-MP-SIGACTB-CTBA211-Exemplo-Apura%C3%A7%C3%A3o-Trimestral-Apura%C3%A7%C3%A3o-Sem-conta-PONTE?source=search) sistema não presenta o saldo em todos os meses

Exemplo:

* Foi realizada a apuração de resultado

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360098714374/mceclip0.png)

* Configuração dos parâmetros "[Posição Ant. L/P](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360061200054-MP-SIGACTB-pergunta-Posi%C3%A7%C3%A3o-antes-de-L-P-?source=search)?" está como **SIM**e a "Data Lucros e Perdas?"**31/03/2019**

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360100931573/mceclip3.png)

* Veja que o sistema só apresenta o saldo da conta de 01/01 a 31/03

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360100932513/mceclip4.png)

* Configuração dos parâmetros "[Posição Ant. L/P](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360061200054-MP-SIGACTB-pergunta-Posi%C3%A7%C3%A3o-antes-de-L-P-?source=search)?" está como **SIM**e a "Data Lucros e Perdas?"**30/06/2019**

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360098715654/mceclip5.png)

* Veja que o sistema só apresenta o saldo da conta de 01/04 a 30/06

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360100932813/mceclip6.png)

* Configuração dos parâmetros "[Posição Ant. L/P](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360061200054-MP-SIGACTB-pergunta-Posi%C3%A7%C3%A3o-antes-de-L-P-?source=search)?" está como **SIM**e a "Data Lucros e Perdas?"**30/09/2019**

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360100932993/mceclip7.png)

* Veja que o sistema só apresenta o saldo da conta de 01/07 a 30/09

![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360098715974/mceclip8.png)

* Configuração dos parâmetros "[Posição Ant. L/P?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360061200054-MP-SIGACTB-pergunta-Posi%C3%A7%C3%A3o-antes-de-L-P-?source=search)" está como **SIM**e a "Data Lucros e Perdas?"**31/12/2019**

![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360100933113/mceclip9.png)

* Veja que o sistema só apresenta o saldo da conta de 01/10 a 31/12

![mceclip10.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360100933333/mceclip10.png)

**Ambiente**

Microsiga Protheus – Contabilidade Gerencial  – A partir da versão 11.80  
  
**Causa**

[COMPORTAMENTO DO RELATÓRIO COM APURAÇÃO TRIMESTRAL](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058313714-MP-SIGACTB-CTBR265-EMISS%C3%83O-DO-RELAT%C3%93RIO-COM-APURA%C3%87%C3%83O-TRIMESTRAL?source=search)  
  
**Solução** **1º Sugestão**

* Ao emitir o relatório **CTBR265** configuração dos parâmetros **"[Posição Ant. L/P?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360061200054-MP-SIGACTB-pergunta-Posi%C3%A7%C3%A3o-antes-de-L-P-?source=search)"** está como **NÃO** e a "**Data Lucros e Perdas**?" está em **BRANCO**

**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360098714414/mceclip1.png)**

* Será apresentado todos os saldos conforme indicado no período.  **mesmo após Apuração de resultado**

**![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360100931553/mceclip2.png)**

**2º Sugestão**Como a apuração da empresa é efetuada de forma Trimestral, indicamos que seja efetuada a emissão do relatório de forma também trimestralmente no período 01/01 a 31/03, ou seja se houver mais de uma apuração no período esta não será desconsiderada.

Somente será desconsiderado a Apuração de Resultado informado no parâmetro "Data Lucros e Perdas?".

Com isso os parâmetros  abaixo devem ser informados:

![mceclip12.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360100933633/mceclip12.png)  
  
01/01 a 31/03 - emita o relatório 

* Configuração dos parâmetros "Posição Ant. L/P?" está como **SIM**e a "Data Lucros e Perdas?"**31/03/20xx**

01/04 a 30/06 - emita o relatório 

* Configuração dos parâmetros "Posição Ant. L/P?" está como **SIM**e a "Data Lucros e Perdas?"**30/06/20xx**

01/07 a  30/09 - emita o relatório 

* Configuração dos parâmetros "Posição Ant. L/P?" está como **SIM**e a "Data Lucros e Perdas?"**30/09/20xx**

01/10 a 31/12 - emita o relatório 

* Configuração dos parâmetros "Posição Ant. L/P?" está como **SIM**e a "Data Lucros e Perdas?"**31/12/20xx**
