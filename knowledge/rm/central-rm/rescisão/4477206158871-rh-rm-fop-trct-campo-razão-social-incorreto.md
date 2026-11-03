---
article_id: 4477206158871
category: Rescisão
content_hash: b97bef5d26854695174e3fa05c044405de67bbe0c8bf4a3521346b383150b92d
fetched_at: '2026-06-28T22:46:54.412687+00:00'
product: rm
section_id: 1500000834561
source: central-rm
title: 'RH - RM - FOP - TRCT: campo Razão Social incorreto'
type: support-article
updated_at: '2022-08-01T10:38:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4477206158871-RH-RM-FOP-TRCT-campo-Raz%C3%A3o-Social-incorreto
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:26 min****Ocorrência**Ao gerar o relatório Termo de Rescisão, o campo Razão Social está saindo incorretamente.  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Causa**Esse incidente ocorre pois, o campo **Razão Social** do TRCT leva o nome que está informado em: **Administração de Pessoal | Seções | Editar a Seção | campo Descrição.**  
**Solução**  
Para que relatório TRCT leve o nome da razão social da empresa será necessário verificar os procedimentos abaixo.  
  
1. Acesse: **Administração de Pessoal | Seções | Editar a Seção | campo Descrição** e verifique qual o nome da empresa que está sendo informado, pois esse campo que irá levar pro TRCT.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4483619543319/mceclip0.png)  
  
2. Logo, acesse: **Rescisão | TRCT | Portaria 1621/2010.**  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4477864011159/mceclip0.png)  
  
3. É necessário alterar a quebra de seção no momento da geração do TRCT. Portanto, avance a tela de parametrização do perfil e logo após altere a quebra de seção, conforme deseja.  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4478044951319/mceclip2.png)  
  
Esta parametrização servirá como filtro, ou seja, serão gerados TRCT cujas seções dos funcionários correspondam à quebra informada e os funcionários tenham dados compatíveis com a grade de seleção definida.  
  
**Glossário**  
**TRCT-** Termo de Rescisão de Contrato de Trabalho  
  
**Saiba Mais**  
[RH - RM - FOP - TRCT: parametrização de rubricas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360003040531-RH-RM-FOP-TRCT-parametriza%C3%A7%C3%A3o-de-rubricas)  
[Termo Rescisão Contrato de Trabalho](https://tdn.totvs.com/pages/releaseview.action?pageId=452719268)
