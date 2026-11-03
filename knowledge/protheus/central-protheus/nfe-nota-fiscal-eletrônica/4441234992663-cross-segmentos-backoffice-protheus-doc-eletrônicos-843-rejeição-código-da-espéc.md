---
article_id: 4441234992663
category: NFe - Nota Fiscal Eletrônica
content_hash: 6ae2d471b2510ad8580db3779658d2e8864f3999e37c429dfcf16693e6cd4775
fetched_at: '2026-06-28T22:40:05.353096+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 843 Rejeição: Código
  da espécie de Veículo incompatível com o tipo do Veículo'
type: support-article
updated_at: '2025-07-15T12:02:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4441234992663-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-843-Rejei%C3%A7%C3%A3o-C%C3%B3digo-da-esp%C3%A9cie-de-Ve%C3%ADculo-incompat%C3%ADvel-com-o-tipo-do-Ve%C3%ADculo
---

**Dúvida**

Como corrigir a Rejeição 843: Código da espécie de Veículo incompatível com o tipo do Veículo

**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - Todas as versões

Cross Segmentos - TSS - a partir da versão 12

**Solução**

Verificar se o código da espécie de veículo ***(campo: espVeic)*** é compatível com o tipo de veículo ***(campo: tpVeic)*** conforme ***Tabela de Tipo e Espécie de Veículo publicada na aba “Documentos”, opção “Diversos” do Portal Nacional da NF-e (www.nfe.fazenda.gov.br)***

1. Acessar o módulo **Configurador (SIGACFG)**, em seguida em **Ambiente /** **Cadastros / Parâmetros** clicar em **editar.** Preencher o parâmetro ***MV\_VEICNV no configurador o parâmetro*** com o grupo de produto de ***Veículos:***

**![MV_VEICNV.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/33476527328535)**

2. Preencher no cadastro de produto no campo ***Grupo "B1\_GRUPO"***  informado no parâmetro ***MV\_VEICNV.***

![B1_GRUPO.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/33476537794711)

3. Acesse a rotina de ***Livros Fiscais -> Atualizações -> Movimentos -> NF-e Manual de Entrada / Saída > Complementos.***

![20220504_172710.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/33476537795991)

4. Selecione opção ***Veículos automotores.***

![veiculo.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/33476537797911)

5. Preencher no *complemento de veículo os campos abaixo de acordo **com a Tabela de Tipo e Espécie de Veículo campos Tipo de Veículo CD9\_TPVEIC e Espécie de Veiculo  CD9\_ESPVEI.***

[Tabela de Tipo e Espécie de Veículo](https://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=nt7Q2CXVChI=)  
Divulga tabela de tipo e espécie de veículo

![20220505_102229.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/33476537798679)

* ***Validação da Sefaz:***

***![843_rejeicao.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/5896361940631)***
