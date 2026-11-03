---
article_id: 360048227073
category: Escrita Fiscal - Impostos - ICMS - Icms St
content_hash: aa7530d4e1a2e6a96ad34deb1b8ed26e98a2ea1cfef82bdc59468fb4989212b4
fetched_at: '2026-06-28T22:39:20.359738+00:00'
product: protheus
section_id: 1500001538721
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Como calcular ICMS
  ST para movimentações geradas pelo Módulo SIGAEIC, quando o campo Agrega Valor possuir
  preenchimento Tipo B?
type: support-article
updated_at: '2021-07-13T18:25:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360048227073-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-calcular-ICMS-ST-para-movimenta%C3%A7%C3%B5es-geradas-pelo-M%C3%B3dulo-SIGAEIC-quando-o-campo-Agrega-Valor-possuir-preenchimento-Tipo-B
---

**Dúvida**Como calcular ICMS ST para movimentações geradas pelo Módulo SIGAEIC, quando o campo Agrega Valor possuir preenchimento Tipo B?  
   
 **Ambiente**Protheus - Fiscal -  A partir da versão 11.80  
  
**Solução**

Para obter o cálculo de ICMS – ST considerando as movimentações geradas pelo Módulo SIGAEIC, quando o campo Agrega Valor (F4\_AGREG) possuir preenchimento = B, observe a configuração do parâmetro a seguir:

**MV\_TIPOB** = Informe os Estados que deverão realizar o cálculo do ICMS-ST, quando for utilizado o tipo B do TES.

* Descrição do Tipo B: O valor da mercadoria não contém o valor do ICMS, portanto, os valores do ICMS e da mercadoria serão agregados ao total do documento. Este agregador de valor não calcula nenhum imposto, portanto mantém o que for informado pelo usuário ou transmitido por outro sistema.
