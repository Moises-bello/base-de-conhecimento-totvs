---
article_id: 33540576067351
category: Administração de Pessoal
content_hash: aa74d1e925ce22274667a6878c2bd05a5e1a86c4399f20c715a1e70cd0ca31f5
fetched_at: '2026-06-28T22:47:01.112847+00:00'
product: rm
section_id: 1500000861042
source: central-rm
title: RH - RM - FOP - ERRO "The INSERT statement conflicted with the FOREIGN KEY
  constraint "FKPEVENTO_PCODGRPAAS". Copia de eventos entre coligadas
type: support-article
updated_at: '2025-08-08T11:37:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/33540576067351-RH-RM-FOP-ERRO-The-INSERT-statement-conflicted-with-the-FOREIGN-KEY-constraint-FKPEVENTO-PCODGRPAAS-Copia-de-eventos-entre-coligadas
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33540576038807) Tempo aproximado para leitura: **00:01:10 min**  
  
**Dúvida**  
Na copia de eventos entre Coligadas ocorre o erro The INSERT statement conflicted with the FOREIGN KEY constraint **"FKPEVENTO\_PCODGRPAAS".** The conflict occurred in database "VALINHOBD", table "dbo.PCODGRPAAS". The statement has been terminated.

**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**  
Para Solução do erro apresentado na tabela FKPEVENTO\_PCODGRAAS deve se realizar a copia da Tabela Dinâmica código  INT 35 Nome do grupo de AAS da Coligada Origem para a Coligada Destino .

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33540576041623)

Algumas Tabelas podem apresentar error por não serem permitidas ser visível a todas Coligadas uma opção é   selecionar todas as tabelas com o valor 'Não' desmarcando a flag  **'Visível a todas coligadas'.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33540576043799)

Quando a Coligada Origem utilizar o Parâmetro marcado Utiliza Grupo AAS Discriminado é necessário que a Coligada Destino seja marcado em **Configurações / Parametrizador /Folha Normal/ Encargos Sociais / Utiliza Grupo AAS Discriminado.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33540563274135)

O parâmetro de Grupo AAS e marcado dentro do cadastro de eventos na aba incidências de Proventos .

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33540563276311)

**Saiba mais**

[RH - RM - FOP - Cópia de registros entre coligadas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021778232-RH-RM-FOP-C%C3%B3pia-de-registros-entre-coligadas)
