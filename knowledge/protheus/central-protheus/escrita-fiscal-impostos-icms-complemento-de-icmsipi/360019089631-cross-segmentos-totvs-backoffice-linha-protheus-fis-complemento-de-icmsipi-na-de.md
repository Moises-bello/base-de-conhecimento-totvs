---
article_id: 360019089631
category: Escrita Fiscal - Impostos - ICMS - Complemento de ICMS/IPI
content_hash: 88973a95d9a1999e63ff346d93c25148744b8935494bb7426195bad70fdbedce
fetched_at: '2026-06-28T22:39:21.254222+00:00'
product: protheus
section_id: 1500001538701
source: central-protheus
title: ' CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Complemento de
  ICMS/IPI na devolução de venda'
type: support-article
updated_at: '2021-07-13T18:37:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019089631--CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Complemento-de-ICMS-IPI-na-devolu%C3%A7%C3%A3o-de-venda
---

**Dúvida**Como fazer um Complemento de ICMS/IPI na Devolução de Venda?

**Ambiente**Protheus Fiscal - Todas as Versões.  
   
**Solução**

Nos casos de complemento de Devolução, é necessário efetuar o cadastro do cliente como fornecedor e informar alguns campos da nota manualmente.

**Tipo da NF = Complemento de ICMS / Complemento de IPI**

* Informe o mesmo fornecedor/cliente (neste caso, cadastre o cliente como fornecedor)
* Informe um produto da NF original
* Digite o valor do imposto nos campo valor unitário e valor total
* Informe o TES
* Para vincular ao documento original, digite manualmente a NF original no campo**NF Orig.**, **Série Orig.**

**Cadastro da TES de COMPLEMENTO**

**Aba Adm:**

* Tipo: Saída/Entrada
* Cred. ICM e Cred IPI = Não
* Gera Duplic. ICMS = Não, IPI = SIM
* Não atualiza Estoque e Não controla Poder de Terceiros
* Restante preencha como **Default**

**Aba Impostos**

* Calcula ICMS e IPI = SIM
* CFOP da NF Original
* Livros Fiscais: De acordo com o Imposto a ser complementado (ICMS/IPI) = Tributado

**Escrituração**

A escrituração desta nota será na coluna tributada e deve ser feita conforme determinação da TES e no campo **OBSERVAÇÕES** será informado à nota de origem a qual este complemento se refere.
