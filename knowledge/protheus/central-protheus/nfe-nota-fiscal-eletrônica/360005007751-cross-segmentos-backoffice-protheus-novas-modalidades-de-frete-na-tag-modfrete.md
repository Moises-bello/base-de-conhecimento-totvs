---
article_id: 360005007751
category: NFe - Nota Fiscal Eletrônica
content_hash: 276e03ebc979f3d4b26f13a3be222d86ad35d2adc667c0a2041893411b04238a
fetched_at: '2026-06-28T22:40:00.154092+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Novas modalidades de frete  na TAG
  modFrete
type: support-article
updated_at: '2025-06-23T11:54:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360005007751-Cross-Segmentos-Backoffice-Protheus-Novas-modalidades-de-frete-na-TAG-modFrete
---

**Dúvida**Como utilizar as novas modalidades de frete  na TAG modFrete?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - Todas as versões

Cross Segmentos - TSS - a partir da versão 12

**Solução**

 À partir da **versão 4.0 da NF-e** foi **alterada e acrescentada** novas modalidades de frete.

* **Conforme a nota técnica do link abaixo:**

[Nota Técnica 2016.002 - v 1.61 (publicada em 10/09/2018)](https://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=zfWxcJtOf98=)

Ao clicar no link acima será aberto um PDF com NT.

**Página 51**

**0=**Contratação do Frete por conta do Remetente (CIF);

**1=**Contratação do Frete por conta do Destinatário (FOB);

**2=**Contratação do Frete por conta de Terceiros;

**3=**Transporte Próprio por conta do Remetente;

**4=**Transporte Próprio por conta do Destinatário;

**9=**Sem Ocorrência de Transporte.

**Novas opções:**

* **R = Por conta remetente**(Corresponde opção 3 )
* **D = Por conta destinatário**(Corresponde opção 4 )

 1- Para nota de saída gerar de acordo com a nova regra da Sefaz deve ser preenchido o campo no pedido de vendas **C5\_TPFRETE "Tipo Frete"**

![Tipo_frete.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/11926549113879)

2- Para nota de entrada gerar de acordo com a nova regra da Sefaz deve ser preenchido o campo no pedido de vendas **F1\_TPFRETE "Tipo Frete"**

![20210712_171640.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4404120902167)

* **Saiba mais:**

Parecer da Consultoria de segmentos da TOTVS no link abaixo:

**[Clique Aqui](https://tdn.totvs.com/display/ConSeg/NFe+-+Modalidades+do+Frete+-+Obrigatoriedade+de+Informar+Transportadora)**

No Danfe será destacado conforme as opções abaixo:

**"C"**= **0=**Contratação do Frete por conta do Remetente (CIF);

**"F"** =**1=**Contratação do Frete por conta do Destinatário (FOB);

**"T"=** **2=**Contratação do Frete por conta de Terceiros;

**"R"** =**3=**Transporte Próprio por conta do Remetente;

**"D"** =**4=**Transporte Próprio por conta do Destinatário;

**"S"** = **9=**Sem Ocorrência de Transporte
