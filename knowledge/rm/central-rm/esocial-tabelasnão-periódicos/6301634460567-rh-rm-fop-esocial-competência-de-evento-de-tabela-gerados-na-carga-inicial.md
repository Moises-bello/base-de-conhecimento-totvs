---
article_id: 6301634460567
category: eSocial - Tabelas/Não Periódicos
content_hash: a607c251f695f279e6da9ab7ddcb94646c82f203df2689d1bb71fa4da87d5004
fetched_at: '2026-06-28T22:47:10.305248+00:00'
product: rm
section_id: 1500000834421
source: central-rm
title: RH - RM - FOP - eSocial - Competência de evento de tabela gerados na Carga
  Inicial
type: support-article
updated_at: '2024-06-26T14:35:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6301634460567-RH-RM-FOP-eSocial-Compet%C3%AAncia-de-evento-de-tabela-gerados-na-Carga-Inicial
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24446245068439) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**Quando é gerado o gatilho do tipo **Carga inicial** para os eventos de tabela, o campo **Competência** do gatilho será 01-1900?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial- Todas as Versões  
  
**Solução**Os gatilhos de carga inicial serão gerados com a competência 01-1900, porém o XML não obedecerá a competência gerada no gatilho e sim a data contida no parâmetro **Datas de Obrigatoriedade/Adesão ao eSocial** localizado no menu **Configurações | Parametrizador | eSocial | Configurações Gerais 1/7**.  
Veja o exemplo abaixo:

* Início de obrigatoriedade de **Tabelas** é 01/2018.

![](https://totvssuporte.zendesk.com/attachments/token/Ep5aqqr9VGwM9jb9yrrmIRLhB/?name=inline1824459169.png)

* Competência do evento como **Tipo de Operação Carga Inicial** igual à 01/1900. XML gerado com a *tag* **iniValid** 01/2018.

![](https://totvssuporte.zendesk.com/attachments/token/IYQAC9YqEjOAyOcbUangLztaP/?name=inline-1765536832.png)

Caso seja necessário integrar um evento com início validade após o início da obrigatoriedade, poderá ser criado o gatilho do tipo **Inclusão** e apresentar no campo **Competência** a data de início de validade, sendo informado na *tag* **iniValid**.

No exemplo abaixo, foi criado o gatilho de uma nova rubrica na competência 10/2020, sendo o XML gerado da seguinte forma:

![](https://totvssuporte.zendesk.com/attachments/token/2BKgD8lsZhY9ojVkO3REf5dFL/?name=inline1295965168.png)

**Saiba mais**- [Carga Inicial de eventos de Tabela](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6296513311255-RH-RM-FOP-eSocial-O-funcion%C3%A1rio-chapa-xxxx-est%C3%A1-demitido-e-possui-eventos-de-remunera%C3%A7%C3%A3o-que-n%C3%A3o-se-referem-a-pagamentos-de-diss%C3%ADdio-ou-conven%C3%A7%C3%A3o-coletiva?source=search)
