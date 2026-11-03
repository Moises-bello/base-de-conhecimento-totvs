---
article_id: 4441193552663
category: NFe - Nota Fiscal Eletrônica
content_hash: 087d5df1f08684bbe6b6876a476e664a5d14f7d679717bdbfc73338c73fe575b
fetched_at: '2026-06-28T22:40:05.347172+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 842 Rejeição: Código
  da espécie de Veículo Inexistente'
type: support-article
updated_at: '2025-07-15T12:06:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4441193552663-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-842-Rejei%C3%A7%C3%A3o-C%C3%B3digo-da-esp%C3%A9cie-de-Ve%C3%ADculo-Inexistente
---

**Dúvida**Como solucionar a 842 Rejeição: Código da espécie de Veículo Inexistente  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - Todas as versões

Cross Segmentos - TSS - a partir da versão 12

**Solução**

Verificar se o código da espécie de veículo ***(campo: espVeic)*** consta na Tabela de Tipo e Espécie de Veículo Observação 1: Tabela de Tipo e ***Espécie de Veículo*** publicada na aba ***“Documentos”, opção “Diversos” do Portal Nacional da NF-e (www.nfe.fazenda.gov.br)***

1. Acessar o módulo **Configurador (SIGACFG)**, em seguida em **Ambiente /** **Cadastros / Parâmetros** clicar em **editar.** Preencher o parâmetro ***MV\_VEICNV no configurador o parâmetro*** com o grupo de produto de ***Veículos:***

**![MV_VEICNV.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/33476576096919)**

2. Preencher no cadastro de produto no campo ***Grupo "B1\_GRUPO"***  informado no parâmetro ***MV\_VEICNV.***

![B1_GRUPO.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/33476636466967)

3. Acesse a rotina de ***Livros Fiscais -> Atualizações -> Movimentos -> NF-e Manual de Entrada / Saída > Complementos.***

![20220504_172710.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/33476576101399)

4. Selecione opção ***Veículos automotores.***

![veiculo.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/33476576102167)

5. Preencher no *complemento de veículo o campo abaixo de acordo **com a Tabela de Tipo e Espécie de Veículo campo Espécie de Veiculo  CD9\_ESPVEI.***

[Tabela de Tipo e Espécie de Veículo](https://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=nt7Q2CXVChI=)  
Divulga tabela de tipo e espécie de veículo

![20220505_102229.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/33476576103063)

* ***Validação da Sefaz:***

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5895374222999)
