---
article_id: 360018778952
category: Escrita Fiscal - Impostos - ICMS
content_hash: 0d8890c572b21ba73ca6fc3cbbc7216e0ca7bf9feeb395245a329d600c0ddf44
fetched_at: '2026-06-28T22:39:25.569804+00:00'
product: protheus
section_id: 1500001549842
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Complemento de ICMS/IPI
  na devolução de compra
type: support-article
updated_at: '2025-01-31T13:30:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018778952-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Complemento-de-ICMS-IPI-na-devolu%C3%A7%C3%A3o-de-compra
---

**Dúvida**

Como fazer um Complemento de ICMS/IPI na devolução de compra?

**Ambiente**Protheus - Fiscal: Todas as versões  
  
  
**Solução**

Nos casos de complemento de Devolução, é necessário efetuar o cadastro do fornecedor como cliente e informar alguns campos da nota manualmente.

**Tipo da NF = Complemento de ICMS / Complemento de IPI**

* Informe o mesmo fornecedor/cliente (neste caso, cadastre o fornecedor como cliente)
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
  
Abaixo documentação complementar referente Complemento de ICMS e IPI:

<https://tdn.totvs.com/pages/releaseview.action?pageId=699814440>
