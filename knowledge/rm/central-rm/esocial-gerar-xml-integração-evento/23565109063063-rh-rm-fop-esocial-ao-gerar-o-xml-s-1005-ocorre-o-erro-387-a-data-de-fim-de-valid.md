---
article_id: 23565109063063
category: eSocial - Gerar XML/ Integração Evento
content_hash: ab16b544ca28ff3b5d6b529cf1ad78b9a81a31de6554870d776e157450dcfe79
fetched_at: '2026-06-28T22:47:11.926773+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: 'RH - RM - FOP - eSocial - Ao gerar o XML S-1005 ocorre o erro 387: A data
  de fim de validade deverá ser maior ou igual a data de início validade'
type: support-article
updated_at: '2026-06-01T15:12:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23565109063063-RH-RM-FOP-eSocial-Ao-gerar-o-XML-S-1005-ocorre-o-erro-387-A-data-de-fim-de-validade-dever%C3%A1-ser-maior-ou-igual-a-data-de-in%C3%ADcio-validade
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23565109035927) Tempo aproximado para leitura: **00:02:00 min**  
  
**Ocorrência**  
Ao gerar o XML S-1005 ocorre o erro 387: A data de fim de validade deverá ser maior ou igual a data de início validade.

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/23565124679063)**

**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Causa**  
Este erro ocorre quando a data fim, referente ao encerramento da empresa, é anterior a data início da empresa no portal do governo.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23565109042583)

**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
1. Acesse a seção que foi encerrada e identifique a **Data de Encerramento das Atividades;**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23565124685591)

2. Valide no governo em **Empregador - Tabelas - Estabelecimento**a data de início do S-1005;  
3. Ajuste o campo da **Data de Encerramento das Atividades**para uma data igual ou superior ao S-1005.  
  
**Saiba mais**  
Para mais informações acesse:  
[RH - RM - FOP - eSocial - Encerramento das atividades da empresa no eSocial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360030130614-RH-RM-FOP-eSocial-Encerramento-das-atividades-da-empresa-no-eSocial)
