---
article_id: 35109743233175
category: Materiais - Compras (SIGACOM)
content_hash: f5e873fb27f357cbf20777f8e194a9fd9f7e6cabb816ed75fe5e349c3e58df70
fetched_at: '2026-06-28T22:41:09.067506+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - NFC - Como carregar
  a observação da Solicitação de compras na cotação?
type: support-article
updated_at: '2026-02-05T18:21:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35109743233175-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-NFC-Como-carregar-a-observa%C3%A7%C3%A3o-da-Solicita%C3%A7%C3%A3o-de-compras-na-cota%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35109713163031) Tempo aproximado para leitura: **00:05:SS min**  
  
**Dúvida**

Como carregar a observação da Solicitação de compras na cotação?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS COMPRAS - Versão 12

**Solução**

Para utilizar as observações da Solicitação de Compras (**C1\_OBS**) nas Cotações geradas pelo Novo fluxo de Compras no campo **C8\_OBS**, deve habilitar o parâmetro **MV\_PGCOBC1.**

* **MV\_PGCOBC1** - A observação da SC1 deve ser carregada na Cotação e PC, no NFC? .T. - Para Sim / .F. - Não (default)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35110101240599)

Segue abaixo GIFs de todos os campos de observação do Novo Fluxo de Compras sendo preenchidos e seus resultados.

1ª parte: Incluir Sc preenchendo o campo **C1\_OBS** que aparece na tela de Necessidade de Compra no campo **Observação da Solicitação** quando o **MV\_PGCOBC1** está habilitado

O campo **Observação para o fornecedor** precisa ser preenchido manualmente, não existe a possibilidade de gatilhar a observação da solicitação para esse campo. Essa observação será levada na observação do item da cotação do formulário WF

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36089220224791)

2ª parte: Ao gerar a cotação, abre um Modal de envio do WF que tem o campo **Observação**. Essa observação aparecerá no corpo do email do WF na linha **Mensagem**.

O fornecedor pode preencher uma informação no campo **Observação do Fornecedor** que será levada para o campo **C8\_OBSFOR**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36089253103639)

3ª parte: Na visualização do item da cotação no NFC podemos ver

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36089253106199)

Resumindo...

C1\_OBS (TESTE) --> campo **Observação da Solicitação** --> C8\_OBS

campo **Observação para o fornecedor** (obs para workflow) **-->** campo **Observação para o fornecedor** do formulário  --> linha item cotação

campo **Observação**da tela de envio do WF (mais um teste obs) --> linha **Mensagem** do corpo do email

campo **Observação do Fornecedor** do formulário (obs fornecedor formulário workflow) ---> **C8\_OBSFOR**

**Saiba mais em :**

[Novo Fluxo de Compras: Guia de Referência](https://tdn.totvs.com.br/pages/releaseview.action?pageId=680260500)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
