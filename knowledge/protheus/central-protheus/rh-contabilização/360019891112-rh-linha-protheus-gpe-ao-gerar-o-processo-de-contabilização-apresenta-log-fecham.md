---
article_id: 360019891112
category: RH - Contabilização
content_hash: e70cdb464da13c2934410294b755ae9d15cf7652063c8ce6ea16efbc3457c055
fetched_at: '2026-06-28T22:43:45.765871+00:00'
product: protheus
section_id: 360003109092
source: central-protheus
title: 'RH - Linha Protheus - GPE - Ao gerar o processo de contabilização apresenta
  LOG: Fechamento do Período não foi efetuado'
type: support-article
updated_at: '2025-07-30T20:48:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019891112-RH-Linha-Protheus-GPE-Ao-gerar-o-processo-de-contabiliza%C3%A7%C3%A3o-apresenta-LOG-Fechamento-do-Per%C3%ADodo-n%C3%A3o-foi-efetuado
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33832494090135)** Tempo aproximado para leitura: **00:02:00 min**

**Ocorrência**Ao realizar o processo de contabilização da folha de pagamento é apresentado o LOG: **"Foram encontradas Inconsistências na Contabilização. Fechamento do Período não foi efetuado"**  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.  
  
**Causa**Esse incidente ocorre, caso o parâmetro MV\_GPCTAFM esteja como .T. , pois a contabilização da Folha de Pagamento será efetuada somente após o fechamento Mensal. Neste caso, algum processo cadastrado possui período da competência aberto.   
  
**Solução**Log de Ocorrência apresentado após tentativa de geração da contabilização:  
**Acesse: -> Miscelânea -> Fechamentos -> Contabilização**

**![kcs221118.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360015868051)**

Nesta situação verifique no cadastro de períodos se todos os processos criados para a competência estão fechados, para que a contabilização seja realizada normalmente **(Acesse:->Atualizações -> Definições de Cálculo ->Períodos)**. Caso possua períodos abertos, conclua o fechamento e refaça o processo de contabilização.  **![kcs221118.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360015868311)**

**Saiba Mais:**  
[RH - Linha Protheus - GPE - Como configurar Lançamento Padrão para Folha de Pagamento do Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021101152-RH-Linha-Protheus-GPE-Como-configurar-Lan%C3%A7amento-Padr%C3%A3o-para-Folha-de-Pagamento-do-Protheus-)
