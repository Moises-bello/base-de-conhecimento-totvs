---
article_id: 15371876879767
category: SIGAEST - MOVIMENTAÇÕES
content_hash: f5092be42a596b616e4041373311863231d70fcb4cfc04db9109c46ae6940b72
fetched_at: '2026-06-28T22:38:55.803746+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA185 - Cabeçalho
  não apresenta o campo Centro de Custos
type: support-article
updated_at: '2023-07-19T18:34:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/15371876879767-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA185-Cabe%C3%A7alho-n%C3%A3o-apresenta-o-campo-Centro-de-Custos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15371940183959) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Ao acessar a rotina ***Baixas da pré-requisição (MATA185)*** não apresenta no cabeçalho o campo Centro de Custos em **algumas movimentações de Baixa**, por quê?

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15372126099863)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15372644643991)

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões

**Solução**Esse cenário não se trata de erro, ocorre devido ao incluir uma Solicitação ao Armazém na rotina MATA105 e ***não informar*** o campo ***Centro de Custos (CP\_CC)*** na linha de itens não exibe o campo no cabeçalho, dessa forma no momento da Baixa da SA é definido o Centro de Custo da Baixa.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15373293723415)

Para os cenário em que são informados mais de um Centro de Custo para cada linha de item, exibe o alerta abaixo. Ao clicar em Sim, pode-se efetuar os ajustes caso desejar linha a linha dos Centros de Custos ou confirmar mantendo o registro inicial.

**\*OBS.:** Nesse cenário também **não** será apresentado o campo Centro de Custos no cabeçalho da baixa de Pré-Requisições.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15372841669015)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15372884173207)

***Saiba Mais:***  
*[Clique aqui e veja mais artigos sobre MOVIMENTAÇÕES no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)*
