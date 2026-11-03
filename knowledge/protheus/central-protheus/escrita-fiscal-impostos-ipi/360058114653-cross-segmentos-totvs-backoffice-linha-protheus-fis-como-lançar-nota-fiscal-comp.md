---
article_id: 360058114653
category: Escrita Fiscal - Impostos - IPI
content_hash: bd00d194efa301a93ea588abe6149249abc334e2be5a6d9b863f4c938df16362
fetched_at: '2026-06-28T22:39:29.001536+00:00'
product: protheus
section_id: 1500001538641
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Como lançar nota
  fiscal Complemento de ICMS/IPI na Devolução de Venda?
type: support-article
updated_at: '2021-07-28T14:14:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058114653-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-lan%C3%A7ar-nota-fiscal-Complemento-de-ICMS-IPI-na-Devolu%C3%A7%C3%A3o-de-Venda
---

**Dúvida**Como lançar nota fiscal Complemento de ICMS/IPI na Devolução de Venda ?  
  
**Ambiente**Protheus - a partir da Versão 11.8  
  
**Solução**

Nos casos de complemento de Devolução, é necessário efetuar o cadastro do cliente como fornecedor e informar alguns campos da nota manualmente.

**Tipo da NF = Complemento de ICMS / Complemento de IPI**

* Informe o mesmo fornecedor/cliente (neste caso, cadastre o cliente como fornecedor )
* Informe um produto da NF original
* Digite o valor do imposto nos campo valor unitário e valor total
* Informe o TES
* Para vincular ao documento original, digite manualmente a NF original no campo**NF Orig.**, **Série Orig.**

Cadastro da TES de COMPLEMENTO

Aba Adm:

Tipo: Saída/Entrada  
Cred. ICM e Cred IPI = Não  
Gera Duplic. ICMS = Não, IPI = SIM  
Não atualiza Estoque e Não controla Poder de Terceiros  
Restante preencha como Default  
Aba Impostos

Calcula ICMS e IPI = SIM  
CFOP da NF Original  
Livros Fiscais: De acordo com o Imposto a ser complementado (ICMS/IPI) = Tributado

Escrituração

A escrituração desta nota será na coluna tributada e deve ser feita conforme determinação da TES e no campo OBSERVAÇÕES será informado à nota de origem a qual este complemento se refere.

Deve ser usado o item da nota fiscal original para não causar rejeição na transmissão da nota fiscal,

pois a sefaz valida o item da nota fiscal e a chave eletrônica.
