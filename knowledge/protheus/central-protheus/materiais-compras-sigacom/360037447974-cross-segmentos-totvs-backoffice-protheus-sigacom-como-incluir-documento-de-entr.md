---
article_id: 360037447974
category: Materiais - Compras (SIGACOM)
content_hash: 6490533cd701fadc017f56cac2e90a3fecec3ce5c52ce6a93844d99dca9d5266
fetched_at: '2026-06-28T22:41:07.687395+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como incluir Documento
  de Entrada com Solicitação de Compras e Pedido de Compras?
type: support-article
updated_at: '2025-10-13T19:18:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037447974-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-incluir-Documento-de-Entrada-com-Solicita%C3%A7%C3%A3o-de-Compras-e-Pedido-de-Compras
---

**Dúvida**

Como incluir Documento de Entrada com Solicitação de Compras e Pedido de Compras?  
  
**Ambiente**A partir da versão 11.80  
  
**Solução**

Pode-se incluir um Documentos de Entrada a partir de uma Solicitação de Compras realizando o vínculo entre os documentos desde a Solicitação de Compras passando pelo Pedido de Compras e então gerando a NF de Entrada a partir deste pedido conforme os passos abaixo abaixo:

***Obs.:*** Lembrando que para as inclusões de cada um dos documentos (Solicitação de Compras, Pedido de Compras ou Documento de Entrada) sem o vinculo entre eles, basta realizar o processo de inclusão manual sem realizar o vinculo do Doc anterior na opção "Outras Ações" e preenchendo manualmente os campos obrigatórios do cabeçalho e Itens de cada Rotina/Documento.

Na inclusão manual de uma NF de Entrada, o Armazém do Item é trazido conforme o Armazém padrão do cadastro do Produto do Item. Caso se deseje um armazém diferente, basta alterar o armazém para o que se deseja no campo referente do Item da NF.

Para inclusão vinculando os Documentos dos processos anteriores (Solic Compras e Pedido de Compras) :

- Incluir uma Solicitação de Compras pela rotina Solicitação de Compras **MATA110.**

Utilizar a opção **Incluir**:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360049093834)

É aberta a tela para preenchimento do campos. Nesta rotina é obrigatório apenas o campo Quantidade (**C1\_QUANT**):

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360049979693)

Ao confirmar é gerada a Solicitação de Compras:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360049979773)

- Incluir um Pedido de Compras pela rotina Pedido de Compras (**MATA121).**

Utilizar a opção **Incluir**:

![mceclip29.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360049983913)

É aberta a tela para preenchimento do campos.

Nesta rotina são obrigatórios os campos **Cond. Pagto**, **Fornecedor**, **Produto**, **Quantidade**, **Prc Unitário** e **Vlr. Total** indicados abaixo, mas neste procedimento vamos preencher apenas dos campos do cabeçalho **Cond. Pagto** e **Fornecedor:**

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360049980573)

Após o preenchimento dos campos no cabeçalho **Cond. Pagto** e **Fornecedor,** posicionar o cursor nos itens e utilizar a opção **Outras Ações >Solicit**:

![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360049980993)

Selecionar os itens da SC gerada e usar a opção **Salvar**:

![mceclip11.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360049981613)

Observar que foram trazidos os itens da Solicitação de Compras.

Preencher os campos **Prc Unitário** e **Vlr. Total** e confirmar a inclusão do Pedido na opção **Salvar**:

![mceclip13.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360049095874)

Verificar o Pedido de Compras incluso:

![mceclip16.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360049096354)

Status da Solicitação de compras Após o Vinculo com Pedido:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/13510930556695)

Num do Pedido Gravado na Visualização da Solicitação de Compras.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/13510934535575)

- Incluir uma NF de Entrada pela rotina Documento de Entrada (**MATA103).**

Utilizar a opção **Incluir**:

![mceclip30.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360049984133)

É aberta a tela para preenchimento do campos.

Preencher os campos obrigatórios do cabeçalho **Numero**, **Série e** **Fornecedor** indicados abaixo:

![mceclip18.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360049982773)

Após o preenchimento dos campos no cabeçalho**,** posicionar o cursor nos itens e utilizar a opção **Outras Ações >Pedido**:

![mceclip21.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360049096874)

**Obs:** Caso se deseje atender apenas 1 item do Pedido, pode usar a opção **"Outras Ações >Item Ped"**, preenchendo anteriormente o produto contido no item do pedido desejado:

Selecionar o Pedido existente e confirmar na opção **Salvar**:

![mceclip22.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360049983173)

Observar que foram trazidos os itens do Pedido de Compras.

Preencher o campo obrigatório da **TES** e confirmar o vínculo na opção **Salvar**:

![mceclip24.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360049097154)

Observar no browse a NF de Entrada inclusa no sistema:

![mceclip26.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360049983473)

Status do Pedido de Compra , Após Vinculo com o Documento de Entrada:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/13511256247703)

Num do Pedido Gravado na Visualização do Documento de Entrada.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/13511621733399)

***Obs:***

As tabeles principais do Documento de Entrada são:

- SF1 (Cabeçalho do Documento de Entrada)

- SD1 (Itens do Documento de Entrada).

**Saiba Mais:**

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como realizar a inclusão de um Documento de Entrada - MATA103](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4407604558615)

[DOCUMENTO DE ENTRADA GERAL - CENTRALIZADORA de COMPRAS](https://tdn.totvs.com/x/H3PQHw)

[Base de Conhecimento - SIGACOM - Compras](https://tdn.totvs.com/display/public/PROT/SIGACOM+-+Compras)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
