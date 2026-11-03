---
article_id: 4420346230551
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: bc80c3ad6402b9759c085e95c66185d03400ac9f80047c430a54fd679e81200d
fetched_at: '2026-06-28T22:37:20.222551+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus -  SIGAGCT - Ao medir um contrato
  parcialmente, é possível não gerar o Título PR com saldo restante da Parcela ?
type: support-article
updated_at: '2023-10-26T16:43:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4420346230551-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Ao-medir-um-contrato-parcialmente-%C3%A9-poss%C3%ADvel-n%C3%A3o-gerar-o-T%C3%ADtulo-PR-com-saldo-restante-da-Parcela
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **02 min** **Dúvida**

Ao medir um contrato parcialmente, para o qual já foi gerado um título provisório em Contas à Pagar ou Contas à Receber, existe alguma parametrização para NÃO  manter o valor restante no título provisório gerado?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão de contrato - Todas as versões

**Solução**

No modo padrão, **NÃO** existe uma parametrização quando um título provisório gerado, tipo (PR), ao ser medido parcialmente seja estornado ou não gerado o título de saldo restante.

*Exemplo:* ao incluir um contrato  no valor de $1000,00 com cronograma financeiro,  será gerado um título provisório no valor de $1000,00 em contas a pagar ( contrato de compras ) ou contas a receber (contrato de vendas). Caso a medição seja realizada parcialmente no valor de $800,00, será gerado um  título  efetivo ou pedido no valor de 800,00 e um título provisório com o saldo restante de $200,00, não havendo parametrização para não se gerar este título de $200,00 do saldo restante

***Obs:***

No funcionamento padrão do sistema, ao se realizar uma medição do contrato, o título provisório referente a parcela do cronograma que está sendo medida é excluído, ou se for medida parcialmente, é gerado um novo titulo provisório com o saldo restante da parcela. E se estornado o encerramento da medição, o título provisório fica conforme estava antes do encerramento.

***Saiba Mais:***

* [MP - SIGAGCT - Pontos de entrada para rotinas de Medição](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022685112-MP-SIGAGCT-Pontos-de-entrada-para-rotinas-de-Medi%C3%A7%C3%A3o)
* [Nova Medição - CNTA121 - Gestão de Contratos - P12](https://tdn.totvs.com/pages/viewpage.action?pageId=353284981)
* [Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001539581)
