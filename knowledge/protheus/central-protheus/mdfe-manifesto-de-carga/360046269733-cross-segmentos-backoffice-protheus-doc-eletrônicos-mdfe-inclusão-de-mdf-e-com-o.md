---
article_id: 360046269733
category: MDFe - Manifesto de Carga
content_hash: a092d0045368a6a242eb989c141f07ab90a73e1d641d526c200db9d7003d997b
fetched_at: '2026-06-28T22:40:08.178251+00:00'
product: protheus
section_id: 1500001549242
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - MDFE -  Inclusão
  de MDF-e com opção de Informações de Pagamento
type: support-article
updated_at: '2025-06-17T18:29:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046269733-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-MDFE-Inclus%C3%A3o-de-MDF-e-com-op%C3%A7%C3%A3o-de-Informa%C3%A7%C3%B5es-de-Pagamento
---

**Dúvida**Como gerar um MDFE com a opção de Informações de Pagamento  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - Todas as versões

**Solução**

**IMPORTANTE:**

**1° As Informações de Pagamento é somente para motoristas autônomos ou terceirizados.**

**Motorista próprio da empresa não tem a necessidade de informar essa opção.**

**2° Essas informações sairão somente no XML, não vai sair no DAMDFE.**

1- Realizar **atualização do TSS** do link abaixo:

[TSS Transmissão de Documentos Eletrônicos - Atualização do Repositório (RPO) do TSS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004215981)

2- Aplicar **patch e RDMAKE do MDFe MDFESEFAZ e o DAMDFE link abaixo:**

[Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Documentos Eletrônicos NFe (Rdmake NFESEFAZ, DANFE)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043005493)

Após atualização do ambiente basta acessar o módulo **Faturamento (SIGAFAT) / Atualizações / Cadastros / Veículos (OMSA060)**.

  Preencher o campo **Frota (DA3\_FROVEI)** com tipo**2 - TERCEIR0 / 3 - AGREGADO**para salva-lo como TAC agregado.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360065185173)

Para incluir o MDF-e com as Informações de Pagamento, basta acessar a rotina de MDF-e (Módulo Faturamento (SIGAFAT) / Atualizações / Nf-e e Nfs-e / MDF-e (SPEDMDFE), após informar os filtros da tela, clicar no botão **Incluir**.

![](https://tdn.totvs.com/download/attachments/545229144/image2020-3-30_15-10-9.png?version=1&modificationDate=1585591809299&api=v2)

![](https://tdn.totvs.com/download/attachments/545229144/image2020-3-30_15-10-43.png?version=1&modificationDate=1585591843435&api=v2)

Realizar todos os preenchimentos necessários como UF carregamento e descarregamento, veículo, seleção de documentos, municípios de carregamento e etc.

![](https://tdn.totvs.com/download/attachments/545229144/image2020-3-30_15-11-12.png?version=1&modificationDate=1585591872299&api=v2)

![](https://tdn.totvs.com/download/attachments/545229144/image2020-3-30_15-11-35.png?version=1&modificationDate=1585591896094&api=v2)

Após o  preenchimento das informações anteriores, clicar na aba **Informações de Pagamentos**, onde será apresentada a seguinte tela:

![](https://tdn.totvs.com/download/attachments/545229144/image2020-3-30_15-12-34.png?version=1&modificationDate=1585591954469&api=v2)

No grid **Informações de Pagamento**, serão informados os seguintes dados:

* Nome do Responsável pelo Pagamento;
* CPF ou CNPJ ou Id Estrangeiro do Responsável pelo Pagamento;
* Valor Total do Contrato;
* Forma de pagamento (Á vista ou À Prazo);
* CNPJ da IPEF ou Código do Banco e Código da Agencia.

![](https://tdn.totvs.com/download/attachments/545229144/image2020-3-30_15-19-45.png?version=1&modificationDate=1585592385257&api=v2)

**Importante: Caso seja preenchido o CNPJ da IPEF não será necessário o preenchimento dos campos de Código do Banco e Código da Agência. Este dois últimos deverão ser preenchidos caso o CNPJ da IPEF não seja informado.**

Para cada linha adicionada na grid de Informações de Pagamento serão atualizados e adicionados novos grupos (grid) de **Componentes do Pagamento** e **Parcelas do Pagamento**.

Na grid **Componentes do Pagamento**, serão informados os seguintes dados:

* **Tipo do Componente** (1- Vale Pedágio; 2 - Impostos, taxas e contribuições; 3 - Despesas (bancárias, meios de pagamento, outras) / 99 - Outros);
* **Valor do Componente**;
* **Descrição do Componente** (necessário somente quando informado tipo de componente 99 - Outros).

![](https://tdn.totvs.com/download/attachments/545229144/image2020-3-30_15-32-2.png?version=1&modificationDate=1585593122401&api=v2)

Na grid **Parcelas do Pagamento**, serão informados os seguintes dados:

* **Número da Parcela;**
* **Valor da Parcela**;
* **Vencimento da Parcela.**

![](https://tdn.totvs.com/download/attachments/545229144/image2020-3-30_15-34-58.png?version=1&modificationDate=1585593298933&api=v2)

**Importante**: Esta grid (**Parcelas do Pagamento**) será preenchido somente quando for informado a forma de pagamento **À Prazo** na grid de **Informações de Pagamentos**.

Em seguida, clicar no botão **Salvar**.

![](https://tdn.totvs.com/download/attachments/545229144/image2020-3-30_15-37-34.png?version=1&modificationDate=1585593454122&api=v2)

Apos realizar a TRANSMISSÃO do MDFE

Clicar no botão **Schema** para visualizar o XML do documento com as novas *tags* referentes as informações de pagamentos.

![](https://tdn.totvs.com/download/attachments/545229144/image2020-3-30_15-45-55.png?version=1&modificationDate=1585593955563&api=v2)

**Segue trecho do XML com a *TAG* preenchida.**

![](https://tdn.totvs.com/download/attachments/545229144/image2020-3-30_15-46-46.png?version=1&modificationDate=1585594006502&api=v2)
