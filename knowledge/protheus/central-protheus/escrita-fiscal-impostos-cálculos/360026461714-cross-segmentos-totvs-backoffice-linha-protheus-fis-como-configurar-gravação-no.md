---
article_id: 360026461714
category: Escrita Fiscal - Impostos - Cálculos
content_hash: 803e8312589f581c713716d7f098f097d07d82f898b7e0be866d1863ef36704f
fetched_at: '2026-06-28T22:39:30.528298+00:00'
product: protheus
section_id: 1500001538621
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Como configurar gravação
  no campo F1_HORA / F2_HORA em Nota Fiscal Manual de saída?
type: support-article
updated_at: '2021-07-29T14:24:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026461714-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-configurar-grava%C3%A7%C3%A3o-no-campo-F1-HORA-F2-HORA-em-Nota-Fiscal-Manual-de-sa%C3%ADda
---

**Dúvida**

Como configurar ou parametrizar, gravação no campo F1\_HORA / F2\_HORA em Nota Fiscal Manual de saída MATA920?

**Ambiente**

Protheus – Livros Fiscais – A partir da versão 11.80  
  
**Solução**

Configurar parâmetros - MV\_HORANFE / MV\_HORARMT

1. No Configurador (SIGACFG),

Acesse Ambientes / Cadastros / Parâmetros (CFGX017). Crie e/ou altere o parâmetros a seguir:

Nome da variável: MV\_HORANFE  
TIPO: Lógico

Descrição: Utilizado para gravar o campo F1\_HORA no momento da inclusão do documento de entrada. .T. = Grava .F. = Não grava a hora.

Valor Padrão .F.  
.F. = Não grava informação no Sistema (conteúdo padrão);  
.T. = Grava a data da inclusão no Sistema.

Nome da variável: MV\_HORARMT   
TIPO: Caracter

Descrição: Horário gravado nos campos F1\_HORA/F2\_HORA

1=Horário do SmartClient;

2=Horário do servidor;

3=Fuso horário da filial corrente;

Valor Padrão 2

**Exemplo:**

**![MV_HORANFE.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360041306954/MV_HORANFE.png)![MV_HORAMRT.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360042140653/MV_HORAMRT.png)**
