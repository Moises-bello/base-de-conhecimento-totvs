---
article_id: 360021393131
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: 1bc131391dbc8dbfa5053f0a4862b3dd6468bf6c5c9b5950e57e97f1af3f369a
fetched_at: '2026-06-28T22:42:00.922860+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - Como gerar
  o registro 1500 e 1510
type: support-article
updated_at: '2025-02-11T20:58:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021393131-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Como-gerar-o-registro-1500-e-1510
---

**Dúvida**Como gerar os registros 1500 e 1510 - Nota fiscal/Conta de energia elétrica (código 06) – Operações Interestaduais.  
  
**Ambiente**Microsiga Protheus - Livros Fiscais - A partir da versão 11.80.  
  
**Solução**Neste registro serão relacionados todos os documentos de notas fiscais de operações interestaduais, a partir do livro fiscal do seguinte modelo: Nota Fiscal/Conta de Energia Elétrica, Modelo 6.  
  
I. Escriture o documento Fiscal com espécie "**NFCEE**" e calcula imposto ICMS ou IPI;

II. Após escrituração da **NF**, preencha o complemento de "Energia Elétrica", por meio das rotinas **Documentos Fiscais de Entrada** **(MATA910)** e de **Saída** **(MATA920):**

**Importante:****Complemento de Nota Fiscal Automático**   
Ponto de Entrada **MATUCOMP**: Utilizado para alterações automáticas nos complementos dos documentos fiscais após a emissão das Notas Fiscais.  
  
Para informações sobre o Ponto de entrada **MATUCOMP**, acesse: [MATUCOMP - Alterações automáticas](http://tdn.totvs.com/pages/releaseview.action?pageId=6077107)  
  
O parâmetro **MV\_ATUCOMP** deve ser configurado para que seja possível utilizar o **Ponto de Entrada MATUCOMP (MV\_ATUCOMP = T)**.  
  
III. Realize a geração do Arquivo magnético **SPEDFISCAL**.

![image2016-6-5_17_55_40.jpeg](https://centraldeatendimento.totvs.com/hc/article_attachments/360017972031/image2016-6-5_17_55_40.jpeg)
