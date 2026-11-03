---
article_id: 5270644765591
category: PCO - Reprocessamentos
content_hash: 03d211d50424aba9c87ce0633035b483f94aa54aa5b514efd28a12370d6e44d0
fetched_at: '2026-06-28T22:37:06.973251+00:00'
product: protheus
section_id: 1500001551022
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGAPCO - PCOA009 - Help: PCONOLANCINTEGR,"Não
  existem pontos de lançamento para integração ..."'
type: support-article
updated_at: '2022-04-13T22:04:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5270644765591-Cross-Segmento-Backoffice-Linha-Protheus-SIGAPCO-PCOA009-Help-PCONOLANCINTEGR-N%C3%A3o-existem-pontos-de-lan%C3%A7amento-para-integra%C3%A7%C3%A3o
---

**Ocorrência**No módulo SIGAPCO, ao tentar reprocessar os lançamentos de integração, através da rotina PCOA009 **,***é acionado* o Help

***PCONOLANCINTEGR,***

***Problema:** "Não existem pontos de lançamento para integração cadastrados, ou não existe nenhum ativo. Verifique a rotina em Atualizações > Lançamentos > Pontos Lanc Integr.'*

*![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5270830082839/mceclip0.png)*

**Ambiente** Cross Segmento - Backoffice Linha Protheus - SIGAPCO - Planejamento e controle orçamentário  
  
**Versão**Todas.  
  
**Solução**Para solucionar esta ocorrência, execute os seguintes passos:

1. Verifique se os pontos de lançamentos de Integração estão configurados e ativos através da rotina PCOA041-Pontos de lançamento de Integração.![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5271008609687/mceclip1.png)

Caso não estejam ativos será necessário, marcar a opção uso, para que o ponto seja ativo, e preencher os campos conforme a a tabela de origem do ponto e regra do campo.

2. Confirme se o registro correspondente à entrada de integração que você configurou está ativo na rotina PCOA030

**![Captura de Tela (23)_LI.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/5422869760151/Captura_de_Tela__23__LI.jpg)**

Caso os processos não estejam ativos, será necessário, ativa-los marcando a opção de uso e preenchendo os campos conforme a tabela de origem, e regra do campo.

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5422763998231/mceclip0.png)**

**Saber mais:**

[MP - SIGAPCO - CAMPOS DO CABEÇALHO DO PONTO DE LANÇAMENTO DESABILITADOS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020505032-MP-SIGAPCO-CAMPOS-DO-CABE%C3%87ALHO-DO-PONTO-DE-LAN%C3%87AMENTO-DESABILITADOS?source=search)

[MP - SIGAPCO - Configuração on-line dos lançamentos por processo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018567972-MP-SIGAPCO-Configura%C3%A7%C3%A3o-on-line-dos-lan%C3%A7amentos-por-processo?source=search)
