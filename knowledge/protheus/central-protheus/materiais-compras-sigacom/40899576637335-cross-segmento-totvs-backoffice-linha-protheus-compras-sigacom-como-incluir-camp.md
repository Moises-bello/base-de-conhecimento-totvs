---
article_id: 40899576637335
category: Materiais - Compras (SIGACOM)
content_hash: c7b9df36cfe19bb92c3a339e00ae7d9751f56a8a0c396655a419c35c8183e1c0
fetched_at: '2026-06-28T22:41:07.304623+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - Compras (SIGACOM) - Como
  incluir campos adicionais no formulário enviado ao fornecedor no Novo Fluxo de Compras(PGCA010?
type: support-article
updated_at: '2026-06-02T12:11:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40899576637335-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-Compras-SIGACOM-Como-incluir-campos-adicionais-no-formul%C3%A1rio-enviado-ao-fornecedor-no-Novo-Fluxo-de-Compras-PGCA010
---

#### **Dúvida**

Como incluir campos adicionais no formulário enviado ao fornecedor no Novo Fluxo de Compras(PGCA010?

#### **Ambiente**

Cross Segmento – TOTVS Backoffice (Linha Protheus) – Compras (SIGACOM) – Importador XML – A partir da Versão 12

#### **Solução**

A Rotina **NFCA030 - Workflow Customizável** tem como finalidade permitir aos usuários incluir campos personalizados no corpo do e-mail enviado aos fornecedores, por meio da nova funcionalidade **Template WF (NFCA030)**. Além disso, possibilita a seleção de campos adicionais provenientes das tabelas:

**SC8 – Cotações** e **DHU – Cabeçalho da Cotação**. Essa flexibilidade visa atender às necessidades específicas de cada processo de cotação, proporcionando maior controle e adequação do conteúdo encaminhado aos fornecedores.

Para incluir um novo template WF, siga os passos abaixo:

* Clique em **Incluir** para iniciar a criação de um novo template.
* Preencha os campos obrigatórios conforme descrito a seguir:

Os campos que poderão ser configurados para exibição no template estão divididos nas seguintes seções:

* **Cabeçalho:** Área localizada na parte superior do workflow.
* **Itens:** Seção destinada aos detalhes dos itens relacionados à cotação.
* **Rodapé:** Área localizada na parte inferior do template.

**Editável:** Define se o campo poderá ser editado pelo usuário ou se será somente para visualização. Vale destacar que os campos das seções **Cabeçalho** e **Rodapé** são permitidos apenas para visualização.

**Obrigatório:** Indica se o preenchimento do campo é obrigatório para que a cotação possa ser respondida.

![incluir.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/40899726831127)

#### **Observação**

Caso não encontre essa rotina (NFCA030) em seu ambiente é necessário que realize a inclusão da mesma em seu Menu, conforme configuração abaixo.

![](https://tdn.totvs.com.br/download/attachments/680260500/image-2025-9-5_16-38-57.png?version=1&modificationDate=1765471779973&api=v2)

#### **Saiba Mais:**

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Novo Fluxo de Compras - NFC (PGCA010)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/19838751317655-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Novo-Fluxo-de-Compras-NFC-PGCA010)  
[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)  
[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
