---
article_id: 115004893528
category: Financeiro - Contas a Pagar - Comunicação Bancária CNAB
content_hash: 28749795f46ed322d30b8f6ea949128d983d75afa4c1d42b61ae37ceaf998788
fetched_at: '2026-06-28T22:37:54.951169+00:00'
product: protheus
section_id: 1500001550622
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus  - SIGAFIN - CNAB - Qual a estrutura
  do CNAB modelo 2
type: support-article
updated_at: '2023-05-03T23:30:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/115004893528-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-CNAB-Qual-a-estrutura-do-CNAB-modelo-2
---

**Dúvida**Qual a estrutura do CNAB modelo 2?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – Financeiro – Versão 12

**Solução**O formato do arquivo caracteriza-se por ser segmentado possuir um *HEADER* de arquivo, *HEADER* de lote, Detalhe(s), *TRAILLER* de lote e *TRAILLER* de arquivo.

O identificador do tipo de registro estará sempre na oitava coluna de cada linha de registro.

**Os códigos abaixo foram definidos pela FEBRABAN:**

**0** = *HEADER* DE ARQUIVO  
**1** = *HEADER* DE LOTE  
**3** = DETALHE  
**5** = *TRAILLER* DE LOTE  
**9** = *TRAILLER* DE ARQUIVO

São 240 caracteres por linha.

**Saiba Mais:**

Contas a Pagar - Modelo 2 - Arquivo de Layout Remessa  
<https://tdn.totvs.com/pages/releaseview.action?pageId=370611737>

Contas a Pagar - Modelo 2 - Arquivo de Layout Retorno  
<https://tdn.totvs.com/pages/releaseview.action?pageId=370611748>

**Veja mais**

* [Página Centralizadora do CNAB](http://tdn.totvs.com/display/PROT/CNAB)
* [Como Parametrizar o sistema para a geração do CNAB](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006611532-MP-SIGAFIN-CNAB-Como-parametrizar-o-sistema-para-gera%C3%A7%C3%A3o-do-CNAB-)
* [Principais mensagens do CNAB](http://tdn.totvs.com.br/pages/viewpage.action?pageId=353280222)
