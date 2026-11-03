---
article_id: 360019309111
category: NFe - Nota Fiscal Eletrônica
content_hash: 72a1cfa5a2e0e088848a34f8240137563c96f43183ca68e34b30c025b4801701
fetched_at: '2026-06-28T22:40:03.594697+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos -  Como gerar FCI
  no XML e DANFE
type: support-article
updated_at: '2025-06-26T14:39:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019309111-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Como-gerar-FCI-no-XML-e-DANFE
---

**Dúvida**Como gerar FCI no XML e DANFE ?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.

**Solução****1-**  Acessar o módulo **Configurador (SIGACFG)**, em seguida em **Ambiente /****Cadastros / Parâmetros** clicar em **alterar** MV\_FCIDANF = **.T. e** MV\_IMPADIC= **.T.**

![20201116_174728.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360099647253)

2. O cadastro da TES pode ter a situação tributária do ICMS no campo **Sit. Trib. ICM** **F4\_SITTRIB= 00-10-20-30-40-41-50-51-60-70-90**

**![F4_SITTRIB.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/11603345189655)**

3- Em ambos casos os produtos devem ter a origem no campo **B1\_ORIGEM=** **1, 2, 3, 4, 5, 6 e 8**

![B1_ORIGEM.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/11603500535319)

**Revenda:**

1- Preencher o campo **D1\_FCICOD (documento de entrada)** quando utilizar controle de lote, ou manualmente através do campo **C6\_FCICOD (pedido de venda).**

2- Lembrando para que o **D1\_FCICOD grave na D2\_FCICOD** deverá estar com o parâmetro habilitado **MV\_FISFRAS= .T.**

**Industrialização:**

Após efetuar todo o processo para gerar o arquivo do FCI o código é gravado no campo **CFD\_FCICOD.**

Se estiver configurado dessa forma é gerado o **FCI no XML e Danfe.**

* **Saiba Mais:**

A mensagem é gerada conforme a **resolução 88:**

“Resolução do Senado Federal nº 13/12, Número da FCI\_\_\_\_\_\_\_.".

**Não é levado o valor e o percentual, pois foi retirada essa informação na resolução 88.**

O FCI será destacado **na TAG infadprod no XML e no DANFE** em Descrição do **prod./serv.**

Para **sair apenas no XML** e não destacar no Danfe **MV\_IMPADIC= .F.**

O preenchimento na SD1, SC6 ou CFD precisam gravar o campo **D2\_FCICOD.**

* **Saiba mais:**

Para emitentes do Simples Nacional, será gerado no XML realizando a mesma configuração, neste caso não pode ser preenchido no TES a situação tributária do ICMS no campo **Sit. trib. ICM** **F4\_SITTRIB, apenas preencher no TES o campo  **F4\_CSOSN "Campo Cod. Sit. "****

Conforme o ***parecer do link abaixo e a documentação do desenvolvimento :***

*[´Clique Aqui](https://tdn.totvs.com/pages/releaseview.action?pageId=581866486)*

*[Clique Aqui](https://tdn.totvs.com/pages/releaseview.action?pageId=589524813)*
