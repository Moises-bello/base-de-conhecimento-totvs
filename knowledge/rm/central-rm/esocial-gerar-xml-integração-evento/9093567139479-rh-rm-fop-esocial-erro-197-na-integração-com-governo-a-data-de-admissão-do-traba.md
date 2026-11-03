---
article_id: 9093567139479
category: eSocial - Gerar XML/ Integração Evento
content_hash: 6cb5bccf233fdeb9169ff54376b0d7393be594be5623f50e9ffe918be962e4e6
fetched_at: '2026-06-28T22:47:12.108884+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: 'RH - RM - FOP - eSocial - Erro 197 na integração com governo: A data de admissão
  do trabalhador não poderá ser anterior a data de abertura da empresa '
type: support-article
updated_at: '2024-12-30T11:45:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9093567139479-RH-RM-FOP-eSocial-Erro-197-na-integra%C3%A7%C3%A3o-com-governo-A-data-de-admiss%C3%A3o-do-trabalhador-n%C3%A3o-poder%C3%A1-ser-anterior-a-data-de-abertura-da-empresa
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:00 min****Ocorrência**Ao transmitir o evento S-2200 ou S-2399 para o governo é retornado a inconsistência **O evento ID 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX foi rejeitado pelo RET. Erro código 197: A data de admissao (xx/xx/xx) do trabalhador nao podera ser anterior a data de abertura (xx/xx/xxxx) da empresa ou posterior a sua data de encerramento.**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9144578273559/mceclip0.png)

**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - eSocial - Todas as versões  
  
**Causa**Essa mensagem de erro ocorre no retorno do Evento **S-2200** ou **S-2300** quando a **Data de Admissão** do funcionário está **Anterior a Data de Início da Empresa** ou após seu encerramento.  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
1. Acesse **eSocial | Informações do Empregador** e consulte a data de início da atividade da empresa.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9144070907031/mceclip0.png)

2. Após, no cadastro do funcionário na aba **Registro** realize o ajuste da data de admissão para uma data igual ou posterior a data de abertura da empresa.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9144187507479/mceclip1.png)

3. Na fila de eventos regere o XML  e envie ao eSocial.
