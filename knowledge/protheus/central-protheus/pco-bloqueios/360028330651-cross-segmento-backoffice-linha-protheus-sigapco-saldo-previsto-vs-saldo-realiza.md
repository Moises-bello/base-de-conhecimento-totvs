---
article_id: 360028330651
category: PCO - Bloqueios
content_hash: d8f89a776ee4d1fdbc868abc95d14b5932689c26a47bc68c6cb3b87618e8e049
fetched_at: '2026-06-28T22:37:13.494519+00:00'
product: protheus
section_id: 1500001550782
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAPCO - Saldo Previsto Vs Saldo
  Realizado no bloqueio. (PCOA530)
type: support-article
updated_at: '2022-10-28T12:43:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028330651-Cross-Segmento-Backoffice-Linha-Protheus-SIGAPCO-Saldo-Previsto-Vs-Saldo-Realizado-no-bloqueio-PCOA530
---

**Dúvida**Qual a composição do valor do Saldo Previsto e Saldo Realizado exibido na tela do bloqueio?  
  
   
 **Ambiente**Protheus – PCO – A partir da versão 11.80  
  
**Solução**O Saldo Previsto, considera à soma algébrica do(s) Saldo(s) informado no filtro da configuração do cubo.

                       Imagem com filtro de Saldo = OR e entidade = 3101 e 1001![](https://centraldeatendimento.totvs.com/hc/article_attachments/360028334272/mceclip0.png)

Considerando as respectivas entidades da configuração, que montará a chave (AKT\_CHAVE).

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360028333171/mceclip1.png)

Que esta apontado na Configuração Prevista, no Cadastro Tipo de Bloqueio.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360028333691/mceclip2.png)

O Saldo Realizado possui o mesmo critério todavia esta apontado na Configuração Realizada, no Cadastro Tipos de Bloqueios Cubo.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360028337132/mceclip3.png)

Observe o saldo com a chave contendo o tipo de saldo RE:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360028337292/mceclip4.png)

Com base nos dados acima segue demonstração da tela de bloqueio, considerando um titulo a pagar de R$10.000,00:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360028337592/mceclip6.png)

Saldo Previsto = (AKT\_MVCRD1 = 1000 + AKT\_MVDEB1 = 6000)  
Saldo Previsto = 1000 + (-6000) = -5.000,00

Saldo Realizado =  (AKT\_MVCRD1 = 27000 + AKT\_MVDEB1 = 0)  
Saldo Realizado = 27000 + 0 = 27000

Para um Orçamento negativo de -5000,00 que já foi realizado 27000,00 ocorre uma solicitação de contingência de 32000,00.

A rotina permite customizar a própria regra através de Pontos de Entrada

Fonte (PCOA530)

Pontos de entrada

PCOCONTG - Controle do saldo de contingencia.

<http://tdn.totvs.com/pages/releaseview.action?pageId=83165322>

PCODESVC - Permite desvio da funcionalidade padrão de solicitação de contingência.

<http://tdn.totvs.com/pages/releaseview.action?pageId=185749538>

PCOA5301 - Manipular o texto padrão do bloqueio

<http://tdn.totvs.com/pages/releaseview.action?pageId=6073549>

PCOFECBL - Criar para o botão fechar.

<http://tdn.totvs.com/display/public/mp/PCOFECBL+-+Cria+regra++--+107509>

PCOA5307 - Pós - Validação de Saldo de Contingência

<http://tdn.totvs.com/pages/releaseview.action?pageId=331863847>

PCOA5306 - Validar inclusão de contingências duplicadas.

<http://tdn.totvs.com/display/public/mp/PCOA5306+-+Contingencias+duplicadas+--+24721>

PCOA5303 - Manipular campos customizados. ALJ

<http://tdn.totvs.com/display/public/mp/PCOA5303+-+Campos+customizados+--+12561>

PCOA5304 - Manipular campos customizados ALI

<http://tdn.totvs.com.br/display/public/mp/PCOA5304+-+Campos+customizados+--+12562>

P530EWF - Altera e-mail

<http://tdn.totvs.com/display/public/mp/P530EWF+-+Altera+e-mail+--+95208>

PCOA5305 - Valor de Contingência

<http://tdn.totvs.com.br/display/public/mp/PCOA5305+-+Valor+de+contingencia+--+12563>
