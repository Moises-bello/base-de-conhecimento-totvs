---
article_id: 17718737772823
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: 4977b935053554957122498b1adf1c244d4b9ae899d49b9fa34ed80cb94d1c65
fetched_at: '2026-06-28T22:37:22.730335+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Erro "Existem alguns
  campos obrigatórios no item que não foram informados" ao Encerrar Medição na Geração
  do Pedido de Compras ou de Vendas
type: support-article
updated_at: '2023-09-21T19:16:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/17718737772823-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Erro-Existem-alguns-campos-obrigat%C3%B3rios-no-item-que-n%C3%A3o-foram-informados-ao-Encerrar-Medi%C3%A7%C3%A3o-na-Gera%C3%A7%C3%A3o-do-Pedido-de-Compras-ou-de-Vendas
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17718693623703) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**Ao Encerrar Medição ocorre Erro "Existem alguns campos obrigatórios no item que não foram informados" na Geração do Pedido de Compras ou de Vendas

![](https://totvssuporte.zendesk.com/attachments/token/fLI3731G6QzRfSU7koEpXACW3/?name=image.png)

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão de Contratos - Todas as versões

**Solução**Como o log em questão reporta, ele mesmo está relacionado a algum campo existente no ambiente em questão que está marcado como "Obrigatório" no Comfigurador e que não está sendo preenchido.

Dessa forma, devem ser analisados nos campos existentes da tabela SC7 (Pedido de Compras) ou SC5/SC6 (Pedido de Vendas) do ambiente em questão algum campo que esteja configurado como 'Obrigatório" no Configurador (exceto os que são obrigatórios já no padrão do sistema) e assim no(s) mesmo(s) deve(m) ser retirada essa obrigatoriedade para uso no padrão do sistema.

Por padrão, o sistema preenche apenas os campos do Pedido que são obrigatórios no padrão original do sistema.

Demais campos da tabela SC7 ou SC5/SC6 de Pedido que foram colocados como obrigatório além dos que já são poe padrão, para seus preenchimentos na geração do Pedido pelo Medição, podem ser preenchidos através de customização de Ponto de Entrada.

Abaixo segue artigo disponível com os pontos de entrada da Rotina de medição contendo o que pode ser utilizado para preenchimento de campos nos Pedidos gerados:

- [Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Pontos de entrada para rotina de Medição](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022685112-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Pontos-de-entrada-para-rotina-de-Medi%C3%A7%C3%A3o?source=search)

- CN121PED - [DT\_PE\_CN121PED\_Tratamento\_especifico\_antes\_da\_geração\_do\_pedido\_de\_compra](https://tdn.totvs.com/pages/viewpage.action?pageId=271385565)

***Saiba Mais:***

[Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Pontos de entrada para rotina de Medição](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022685112-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Pontos-de-entrada-para-rotina-de-Medi%C3%A7%C3%A3o?source=search)

CN121PED - [DT\_PE\_CN121PED\_Tratamento\_especifico\_antes\_da\_geração\_do\_pedido\_de\_compra](https://tdn.totvs.com/pages/viewpage.action?pageId=271385565)

[Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001539581)
