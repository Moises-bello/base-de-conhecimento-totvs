---
article_id: 13512642353303
category: Ativo Fixo - Transferência
content_hash: 922a1e7530502f4e76f66e52750b54de38ec62237d02bb39596a43cfaf3ea3df
fetched_at: '2026-06-28T22:41:52.191061+00:00'
product: protheus
section_id: 1500001536061
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAATF - ATFA060 - Valor do ativo
  com ICMS a informar na transferência  após ocorrer apropriação CIAP
type: support-article
updated_at: '2023-03-31T17:32:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/13512642353303-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-ATFA060-Valor-do-ativo-com-ICMS-a-informar-na-transfer%C3%AAncia-ap%C3%B3s-ocorrer-apropria%C3%A7%C3%A3o-CIAP
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **HH:MM:SS min****Ocorrência**

Após a transferência criou novo CIAP na filial destino não considerando as parcelas de apropriações e o saldo de ICMS  da filial de origem.

**Ambiente**

Cross Segmento - TOTVS Backoffice Linha Protheus - TOTVS  Ativo fixo   - Todas as versões

**Causa**

Na transferência do ativo não foi informado valor correto da NF considerando que já houve apropriação  de icms

**Solução**Para que seja seja gerado corretamente o saldo de icms na filial destino quando se faz uma  transferência é necessário informar o valor da NF considerando a apropriação que já houve na filial de origem.

Como na filial origem houve apropriações da manutenção CIAP e creditou o valor de ICMS, não é correto na transferência informar apenas o valor do ativo, quando a TES utilizada está como credita ICMS sim, pois calcula o ICMS de 18% em cima do valor informado e perde-se na transferência por já estar usado, o correto é informar o valor de ICMS (não integral) + Valor do custo (ativo).

Sendo: Valor do ICMS após apropriações / (dividido) pelo percentual do ICMS (18%) = Valor a ser informado.

Para que assim seja apresentado na filial destino o valor do ativo imobilizado e o ICMS correto conforme apropriações já feitas na filial origem.

Exemplo:

## Documento de Entrada NF = 1000,00

Filial Origem  
Valor ativo = 820,00  
Valor ICMS(18%) = 180,00  
2 Apropriações de 3,75 cada

## Valor ICMS = 172,50

Transferência   
172,50 / 18 % = 958,33

## Valor da nota a ser informado na Transferência = 958,33

Filial Destino  
Valor ativo = 820,00  
Valor ICMS(18%) = 172,50

Link da documentação com informações relacionada no item 06

[Transferências (ATFA060 - SIGAATF)](https://tdn.totvs.com/pages/releaseview.action?pageId=312159681)
