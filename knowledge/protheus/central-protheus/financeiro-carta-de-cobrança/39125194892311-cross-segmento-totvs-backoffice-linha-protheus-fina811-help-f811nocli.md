---
article_id: 39125194892311
category: Financeiro - Carta de Cobrança
content_hash: a9f779aedd65861ed4449dc281c4a8fe3fdcba4197ed61bc022206280daf6d42
fetched_at: '2026-06-28T22:37:28.929688+00:00'
product: protheus
section_id: 35058223754903
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice (Linha Protheus) - FINA811 - Help: F811NOCLI'
type: support-article
updated_at: '2026-03-18T13:34:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39125194892311-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-FINA811-Help-F811NOCLI
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39125194881047) Tempo aproximado para leitura: **00:05 min**  
  
**Dúvida**  
Como resolver a ocorrência do Help: F811NOCLI ao executar a rotina de carta de cobrança?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFIN - Todas as Versões.

**Solução**  
O Help **F811NOCLI** ocorre quando o sistema não identifica registros válidos do Clientes para o processamento devido à parametrização de filtros restritivos. Na rotina em questão, os campos de intervalo de valores estão configurados de forma que o limite superior não abrange os registros desejados.

Para corrigir o comportamento, certifique-se de que os parâmetros de intervalo de valores estejam preenchidos corretamente, permitindo que o sistema considere todos os registros da base.

## **Passos**

1. Acesse a rotina que apresenta a mensagem no módulo **Financeiro (SIGAFIN)**;
2. No momento de informar os **Parâmetros** (Filtros) da rotina, localize os campos de intervalo de valor;
3. Configure o campo **Valor De** com o conteúdo `0`;
4. Configure o campo **Valor Até** com o conteúdo `9999999999`;
5. Além do preenchimento dos demais campos;
6. Clique em **OK** para confirmar os parâmetros e processe a rotina novamente.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39125204860567)

**Saiba mais**

[Cross Segmentos - Backoffice Linha Protheus - FINA811 - Como configurar o e-mail para envio do boleto de cobrança?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/37735211248151-Cross-Segmentos-Backoffice-Linha-Protheus-FINA811-Como-configurar-o-e-mail-para-envio-do-boleto-de-cobran%C3%A7a)

[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA811 - Como realizar o envio da carta de cobrança](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6777494398231-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA811-Como-realizar-o-envio-da-carta-de-cobran%C3%A7a)
