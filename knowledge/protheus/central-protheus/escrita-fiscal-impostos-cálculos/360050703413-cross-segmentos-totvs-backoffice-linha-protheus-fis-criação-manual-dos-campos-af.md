---
article_id: 360050703413
category: Escrita Fiscal - Impostos - Cálculos
content_hash: f6a692958ed08a12e68048ada71333e38f909e9b607218ba9ba1e31988f01ca4
fetched_at: '2026-06-28T22:39:30.568572+00:00'
product: protheus
section_id: 1500001538621
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Criação manual dos
  campos AFRMM (Adicional ao Frete para Renovação da Marinha Mercante)
type: support-article
updated_at: '2021-07-29T14:31:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050703413-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Cria%C3%A7%C3%A3o-manual-dos-campos-AFRMM-Adicional-ao-Frete-para-Renova%C3%A7%C3%A3o-da-Marinha-Mercante
---

**Dúvida**Como criar e qual a configuração dos campos para  AFRMM (Adicional ao Frete para Renovação da Marinha Mercante)  
  
**Ambiente**Protheus - a partir da versão 12.1.17  
  
**Solução**

*Os tributos da marinha mercante foram criadas por um desenvolvimento participativo e por este motivo estes campos não fazem parte do dicionário padrão do sistema.*  
  
*Será necessário a criação dos referidos campos manualmente.*  
  
*Tabela: SF1  
Campo: F1\_AFRMIMP  
Tipo : Numérico  
Tamanho: 14  
Decimal: 2  
Título: Vlr. AFRMM  
Descrição: Valor de AFRMM  
Picture: @E 99,999,999,999.99  
Valid: MAFISREF("NF\_AFRMIMP","MT100",M->F1\_AFRMIMP)  
Contexto: Real  
Uso: Usado em todos os módulos*  
  
*Tabela: SD1  
Campo: D1\_AFRMIMP  
Tipo: Numérico  
Tamanho: 14  
Decimal: 2  
Título Vlr. AFRMM  
Descrição : Valor de AFRMM  
Picture: @E 99,999,999,999.99  
Valid: MAFISREF("IT\_AFRMIMP","MT100",M->D1\_AFRMIMP)  
Contexto: Real  
Uso: Usado em todos os módulos*  
  
*Tabela: SF3  
Campo: F3\_AFRMIMP  
Tipo: Numérico  
Tamanho 14  
Decimal: 2  
Título: Vlr. AFRMM  
Descrição : Valor de AFRMM  
Picture: @E 99,999,999,999.99  
Valid: MAFISREF("NF\_AFRMIMP","MT100",M->F3\_AFRMIMP)  
Contexto: Real  
Uso: Usado em todos os módulos*  
  
*Tabela: SFT  
Campo: FT\_AFRMIMP  
Tipo: Numérico  
Tamanho: 14  
Decimal: 2  
Título: Vlr. AFRMM  
Descrição: Valor de AFRMM  
Picture: @E 99,999,999,999.99  
Valid: MAFISREF("IT\_AFRMIMP","MT100",M->FT\_AFRMIMP)  
Contexto: Real  
Uso: Usado em todos os módulos*  
  
*Para a versão 12.1.30 este tributo será tratado exclusivamente pelo configurador de tributos, pois apenas desta forma poderemos fazer a adequação de dicionário necessária."*
