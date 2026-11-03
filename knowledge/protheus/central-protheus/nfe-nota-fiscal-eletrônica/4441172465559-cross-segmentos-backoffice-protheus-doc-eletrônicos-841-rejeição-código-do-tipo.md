---
article_id: 4441172465559
category: NFe - Nota Fiscal Eletrônica
content_hash: f5ef686b2a325a5ea60d157c7397e415bf9267e7cced69aa53fa1c803e7f47f7
fetched_at: '2026-06-28T22:40:05.341974+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 841 Rejeição: Código
  do Tipo de Veículo Inexistente'
type: support-article
updated_at: '2025-07-15T12:03:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4441172465559-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-841-Rejei%C3%A7%C3%A3o-C%C3%B3digo-do-Tipo-de-Ve%C3%ADculo-Inexistente
---

**Dúvida**Como solucionar a rejeição 841 - Rejeição : Código do Tipo de Veículo Inexistente

**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - Todas as versões

Cross Segmentos - TSS - a partir da versão 12

**Solução**

Verificar se o código do tipo de veículo ***(campo: tpVeic)*** consta na Tabela de Tipo e Espécie de Veículo Observação 1: Tabela de Tipo e ***Espécie de Veículo*** publicada na aba ***“Documentos”, opção “Diversos” do Portal Nacional da NF-e (www.nfe.fazenda.gov.br)***

1. Acessar o módulo **Configurador (SIGACFG)**, em seguida em **Ambiente /** **Cadastros / Parâmetros** clicar em **editar.** Preencher o parâmetro ***MV\_VEICNV no configurador o parâmetro*** com o grupo de produto de ***Veículos:***

**![MV_VEICNV.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/33476543108759)**

2. Preencher no cadastro de produto no campo ***Grupo "B1\_GRUPO"***  informado no parâmetro ***MV\_VEICNV.***

![B1_GRUPO.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/33476532703767)

3. Acesse a rotina de ***Livros Fiscais -> Atualizações -> Movimentos -> NF-e Manual de Entrada / Saída > Complementos.***

![20220504_172710.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/33476532705175)

4. Selecione opção ***Veículos automotores.***

![veiculo.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/33476543119255)

5. Preencher no *complemento de veículo o campo abaixo de acordo **com a Tabela de Tipo e Espécie de Veículo campo Tipo de Veículo CD9\_TPVEIC.***

[Tabela de Tipo e Espécie de Veículo](https://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=nt7Q2CXVChI=)  
Divulga tabela de tipo e espécie de veículo

![20220505_102229.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/5890352252311)

* **Validação da Sefaz:**

**![841_Rejei__o.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/5889076702487)**
