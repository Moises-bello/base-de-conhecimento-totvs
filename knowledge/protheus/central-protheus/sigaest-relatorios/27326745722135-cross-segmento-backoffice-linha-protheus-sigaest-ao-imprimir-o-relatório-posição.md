---
article_id: 27326745722135
category: SIGAEST - RELATORIOS
content_hash: de126d0ab85d489f95d0245f491b9fbbd8158f56a07dc90edf0cc287026c5c6d
fetched_at: '2026-06-28T22:39:06.016334+00:00'
product: protheus
section_id: 1500001538841
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Ao imprimir o relatório
  Posição de Estoque (MATR260), os valores são exibidos com no máximo duas casas decimais.
  O que deve ser feito?
type: support-article
updated_at: '2025-03-12T12:41:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/27326745722135-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Ao-imprimir-o-relat%C3%B3rio-Posi%C3%A7%C3%A3o-de-Estoque-MATR260-os-valores-s%C3%A3o-exibidos-com-no-m%C3%A1ximo-duas-casas-decimais-O-que-deve-ser-feito
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27326733943959) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**

Ao imprimir o relatório Posição de Estoque com a configuração de campos para mais de duas casas decimais, os valores não estão sendo exibidos. Como posso fazer para que eles apareçam?

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27326733945239)

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

Para que os campos de Custos no relatório Posição de Estoque (MATR260) exibam corretamente valores com mais de duas casas decimais, é necessário verificar o parâmetro MV\_CENT.

Por padrão, esse parâmetro está configurado com o valor 2. Esse parâmetro determina o número de casas decimais a serem exibidas no relatório.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27326745706007)

 Esse parâmetro determina o número de casas decimais a serem exibidas no relatório, conforme exemplo abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27326745707159)

A utilização do parametro se dar por conta do número de casas decimais, por exemplo se utilizam 6 casas decimais, logo o parametro precisa conter o valor de 6 por exemplo.

**Saiba mais:**

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATR260 - Importância da pergunta "Saldo do produto a considerar?" para correta emissão do relatório](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018559171-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATR260-Import%C3%A2ncia-da-pergunta-Saldo-do-produto-a-considerar-para-correta-emiss%C3%A3o-do-relat%C3%B3rio)

[Posição de Estoque (MATR260 - SIGAEST)](https://tdn.totvs.com/pages/releaseview.action?pageId=448596591)
