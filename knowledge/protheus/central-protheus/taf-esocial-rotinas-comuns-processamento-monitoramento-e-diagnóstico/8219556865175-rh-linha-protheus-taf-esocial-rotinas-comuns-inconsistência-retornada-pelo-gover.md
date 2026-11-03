---
article_id: 8219556865175
category: TAF - eSocial - Rotinas comuns (Processamento, Monitoramento e Diagnóstico)
content_hash: a59d51198b59eedd22444d098fa8f637d14a08ad158c9b843aad9e0be17cba05
fetched_at: '2026-06-28T22:45:21.045538+00:00'
product: protheus
section_id: 1500001536781
source: central-protheus
title: 'RH - Linha Protheus - TAF - eSocial - Rotinas Comuns - Inconsistência retornada
  pelo governo, Código da Resposta: 401 - Conteudo do evento invalido.'
type: support-article
updated_at: '2024-05-29T14:46:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8219556865175-RH-Linha-Protheus-TAF-eSocial-Rotinas-Comuns-Inconsist%C3%AAncia-retornada-pelo-governo-C%C3%B3digo-da-Resposta-401-Conteudo-do-evento-invalido
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23699423512855) Tempo aproximado para leitura: **00:05:00 min****Ocorrência**

Ao transmitir um evento do eSocial, é retornado o *Código da Resposta: 401 - Conteudo do evento invalido.*

Exemplo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8218888367767)  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - eSocial - TAF eSocial - Rotinas Comuns - Todas as

versões.

**Solução**

Ao tentar transmitir um evento para o eSocial, o governo realiza a validação das informações, e estrutura do XML.

Validando ou invalidando o mesmo, seguindo as regras do leiaute do eSocial.

Se o eSocial identificar erro, ele retornará a mensagem:

***Código da Resposta: 401 - Conteudo do evento invalido.***

Porém, essa mensagem, sempre será acompanhada do **Código da Ocorrência**, este código que informa o real erro identificado pelo governo e onde localiza-lo.

Analisando nosso exemplo, o *Código da Ocorrência neste caso é o 312:*

*![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8219382095255)*

Se precisar de apoio, do nosso suporte, ou se realizar uma pesquisa, em busca de documentação, informe o Código da Ocorrência, e um trecho do erro reportado por ele.
