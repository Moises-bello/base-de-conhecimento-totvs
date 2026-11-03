---
article_id: 4406177869079
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: 338f5c5fb68e3d384be3c0a81d9299ce1ca4a4d418c156d66596815142ae0599
fetched_at: '2026-06-28T22:37:22.992656+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Impostos no Gestão
  de Contratos
type: support-article
updated_at: '2026-01-14T19:17:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4406177869079-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Impostos-no-Gest%C3%A3o-de-Contratos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19753944919959) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**  
Existe tratativa ou cálculo de Impostos no módulo de Gestão de Contratos ?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão de Contratos - Todas as versões  
  
**Solução**

No módulo de Gestão de Contratos e em suas rotinas padrões como a de Manutenção e Medição do Contrato, não possui nenhuma tratativa ou configuração para geração ou cálculo de impostos.

Na Inclusão do Contrato existem os campos informativos abaixo na aba "Informativos/Impostos":

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9372983960727)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9373206388887)

Porém esses campos são apenas informativos, e alguns deles, tem função apenas para serem impressos no relatório **Boletim de Medição (CNTR040).**

No Gestão de Contratos no caso de geração de título na medição, o título é gerado na medição da mesma forma como se fosse gerado o titulo manualmente, com as informações Valor, Fornecedor/Cliente e Natureza cadastradas e as informações de impostos dos títulos são gerados conforme o que há contido nestes cadastros que vão para o título gerado.

No SIGAGCT por padrão não existe nenhuma tratativa ou configuração pra impostos.

No caso de geração de Pedido na medição do contrato, é possível preencher a TES de entrada ou de saída nos campos: **CNB\_TE** (TES de Entrada), **CNB\_TS** (TES de Saída) nos itens do contrato ou na medição nos campos **CNE\_TE** ou **CNE\_TS** que é levado para o pedido gerado e o calculo dos impostos será realizado no pedido que é gerado através do encerramento da medição de acordo com essa informação de TES.

Considerando também os campos existentes nos cadastros de fornecedores/clientes, produtos e natureza que possuem informações de impostos que no momento do encerramento da medição, serão gerados  Pedidos de Compra ou Venda ou geração de Títulos.

Da mesma forma no SIGAGCT não há nenhuma tratativa ou configuração pra impostos.

Caso se necessite ou deseje a informação de algum campo adicional na geração de Título ou Pedido no encerramento medição, podem ser utilizados os pontos de entrada disponíveis caso desejado.

[Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Pontos de entrada para rotina de Medição](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022685112-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Pontos-de-entrada-para-rotina-de-Medi%C3%A7%C3%A3o?source=search)

Para a dúvidas em como realizar as configurações para cálculo de Impostos num titulo financeiro ou Pedido/NF orientamos a verificação respectivamente junto a Equipe dos Módulos Financeiro (Título) ou Fiscal (Pedido/NF) do suporte.

***Saiba Mais:***

[Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - O SIGAGCT possui campo de "Tipo de Operação" da "TES Inteligente" para ser passado para os Pedidos gerados na Medição ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/37676774818839-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-O-SIGAGCT-possui-campo-de-Tipo-de-Opera%C3%A7%C3%A3o-da-TES-Inteligente-para-ser-passado-para-os-Pedidos-gerados-na-Medi%C3%A7%C3%A3o)

[Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Pontos de entrada para rotina de Medição](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022685112-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Pontos-de-entrada-para-rotina-de-Medi%C3%A7%C3%A3o?source=search)

[Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Documentação Gestão de Contratos do TDN](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4441027145623)

[Guia de Referencia - Gestão de Contratos - Protheus 12](https://tdn.totvs.com/pages/viewpage.action?pageId=224127467)

[FAQs - Gestão de Contratos](https://tdn.totvs.com/x/O_tgDQ)

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001539581)
