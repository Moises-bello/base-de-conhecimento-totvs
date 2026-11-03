---
article_id: 360039555253
category: Escrita Fiscal - Impostos - ICMS
content_hash: 50e9a6252408fd0f0c9ed8667b49b2cf5142f81f7084e648bc0df22bfe5b35be
fetched_at: '2026-06-28T22:39:26.058450+00:00'
product: protheus
section_id: 1500001549842
source: central-protheus
title: MP - FIS - Qual a Configuração Para o Calculo do ICMS Dispensado?
type: support-article
updated_at: '2024-10-08T21:18:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360039555253-MP-FIS-Qual-a-Configura%C3%A7%C3%A3o-Para-o-Calculo-do-ICMS-Dispensado
---

**Dúvida**MP - FIS - Qual a Configuração para o cálculo do ICMS Dispensado?  
  
**Ambiente**  
Microsiga Protheus – Livros Fiscais – A partir da versão 11.80  
  
**Solução**

**Cadastro de TES:**

F4\_AGREG : D (Deduz Icms Vl Ct).

Parâmetro MV\_DBRDIF: Indica se o valor do ICMS a ser deduzido, quando o campo F4\_AGREG = D , deve ser sobre o valor da base reduzida ou valor de redução da base.

Exemplo de uma nota fiscal com ICMS Dispensado:

Valor mercadoria = R$ 1645,40

Redução de Base de ICMS = reduzir a 40%

**Primeiro Item:**

Quantidade = 19 unidades

Valor Unitário = R$ 86,60

Valor Total = R$ 1645,40

Base ICMS = R$ 658,16

Valor ICMS = R$78,98

Alíquota de ICMS = 12%

Valor total da Nota Fiscal = R$ 1.526,93

Valor do ICMS destacado = R$ 78,98

Valor ICMS Dispensado = R$ 118,47, apresentado nos dados adicionais

* **Rotinas envolvidas:**

MATA080, MATA103 , MATXFIS, MATA410

Informações Adicionais:

<https://tdn.totvs.com/pages/releaseview.action?pageId=506989770>
