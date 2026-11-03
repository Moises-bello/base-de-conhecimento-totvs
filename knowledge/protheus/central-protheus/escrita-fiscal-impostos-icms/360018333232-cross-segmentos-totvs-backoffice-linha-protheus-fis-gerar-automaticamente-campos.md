---
article_id: 360018333232
category: Escrita Fiscal - Impostos - ICMS
content_hash: 3381cc98ee5f19eb82175449ebfe1a82122cc6478feed91ef9780600ef7bd242
fetched_at: '2026-06-28T22:39:24.227759+00:00'
product: protheus
section_id: 1500001549842
source: central-protheus
title: 'CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Gerar automaticamente
  campos na SF6: F6_CODREC/ F6_CODPROD/ F6_DETREC/ F6_REF'
type: support-article
updated_at: '2021-07-28T02:41:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018333232-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Gerar-automaticamente-campos-na-SF6-F6-CODREC-F6-CODPROD-F6-DETREC-F6-REF
---

**Dúvida**Como gerar automaticamente na GNRE os campos: F6\_CODREC/ F6\_CODPROD/ F6\_DETREC/ F6\_REF  
  
**Ambiente**Protheus - Versão 12.1.17  
  
  
**Solução**

1) Para geração do código da Receita automaticamente no Campo: F6\_CODREC , configurar os Parâmetros abaixo

**MV\_GNRENF** = .T., para não exibir a Guia na Tela

**MV\_GNDIFUF**

Tipo: Caracter

Descrição: Informe código da receita por Operação ICMS complementar EC 87.

Por Estado separados por barra '\'.  
Exemplo SP100080

DIFAL - Venda para Não Contribuinte:

**MV\_GNFPDUF**

Tipo: Caracter

Descrição: Informe código da receita por Operação Fundo de Combate Pobreza EC 87

Por Estado separados por barra '\'.  
Exemplo SP100080

FECP DIFAL  - Venda para Não Contribuinte

**MV\_RECEINF**

Tipo  
  
Caractere

Descrição  
  
Informe código da receita por Operação

100099 Subst. Tributária por Operação.

Exemplo Conteúdo: 100099

Venda com ICMS-ST por operação

**MV\_GNFECP**

Tipo Caractere

Descrição: Informe código da receita por Operação

100129 FECP Substituição Tributária

Exemplo Conteúdo: 100129

Venda com FECP-ST por operação

A nota fiscal deve possuir Modelo 55, Espécie SPED

2) Para gravar corretamente o Campo: **F6\_CODPROD**:

Cadastrar o campo B5\_CODGNRE (Código do Produto para GRNE) no Complemento do Produto para preencher o campo F6\_CODPROD (GNRE - Guia Nacional de Recolhimento), automaticamente e alterar nos Parâmetros no Faturamento da nota fiscal:

Gera título por produto = Sim  
Gera Guia por produto = Sim

**MV\_GNRENF** = .T.

3) Para gerar automaticamente os Campos: F6\_DETREC e F6\_REF: configurar conforme exemplos abaixo:

**MV\_DETGNRE** = MT000018/  
**MV\_GNRENF** = .T.  
**MV\_GNREREF** = MT1/
