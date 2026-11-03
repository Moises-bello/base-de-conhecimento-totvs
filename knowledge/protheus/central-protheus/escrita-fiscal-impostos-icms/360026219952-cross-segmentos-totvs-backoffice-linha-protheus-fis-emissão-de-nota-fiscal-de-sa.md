---
article_id: 360026219952
category: Escrita Fiscal - Impostos - ICMS
content_hash: 8cab48ebcd89c725495118229379eb9ad950327e106d79766aa4dba8d9d2a7f1
fetched_at: '2026-06-28T22:39:25.653484+00:00'
product: protheus
section_id: 1500001549842
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Emissão de nota fiscal
  de saldo credor ou devedor de ICMS
type: support-article
updated_at: '2021-07-20T14:34:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026219952-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Emiss%C3%A3o-de-nota-fiscal-de-saldo-credor-ou-devedor-de-ICMS
---

**Dúvida**

Como realizar emissão de nota fiscal de saldo credor ou devedor de ICMS?

**Ambiente**

Protheus – Livros fiscal – A partir da versão 11.80]  
  
**Solução**

Cadastro de TES:

**Credita ICMS**(F4\_CREDICM) = Não

**Calcula ICMS**(F4\_ICM) = Não

**Cod. Fiscal**(F4\_CF) = informe o CFOP

**L.Fisc. ICMS**(F4\_LFICM) = ICMS Zerado/Outros/Isento - A escrituração da nota fiscal deve ser analisada pelo departamento fiscal de sua empresa.

**Agrega Valor**(F4\_AGREG) = Não

**TRF. Deb/Crd**(F4\_TRFICM) = SIM – esse campo leva o valor do ICMS transferido para linha 21 (transf. Cred) ou 22 (transf. Deb) da parte de Informações Complementares da apuração de ICMS.

**Fórmula** (F4\_FORMULA): Criar uma fórmula (menu Atualizações>Cadastros>Fórmulas com conteúdo Transferência de saldo (credor/devedor) conforme art. XXXX do RICMS) para ser amarrada à TES.

**Ajuste CIAP** (F4\_AJUSTE) = Sim

**Cadastro de um Produto:**

Para gerar a nota é necessário criar um produto **Transferência de Saldo de ICMS** para ser selecionado no momento do lançamento da nota.

* Incluir/emitir nota fiscal tipo NORMAL e informe o produto, quantidade 1, valor unitário e o total, sendo o valor do ICMS, e informe a TES criada para transferência.
* Após a inclusão da Nota Fiscal de Transferência, acesse a rotina de **Apuração do ICMS**e inclua manualmente em **Outros Créditos** ou **Outros** **Débitos** o valor do ICMS Transferido.
