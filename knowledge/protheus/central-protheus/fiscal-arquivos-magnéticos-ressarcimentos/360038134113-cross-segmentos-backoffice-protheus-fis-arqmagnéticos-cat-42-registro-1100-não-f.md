---
article_id: 360038134113
category: Fiscal Arquivos Magnéticos - Ressarcimentos
content_hash: b2ca4c2d199c9ad3a4994662b6e8edd39468857bd7724f6c2b968fd084adb9ea
fetched_at: '2026-06-28T22:42:12.689378+00:00'
product: protheus
section_id: 1500001546642
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - CAT 42 - Registro
  1100: Não foi encontrado um código correspondente em outro registro do tipo "0200"'
type: support-article
updated_at: '2022-08-18T17:55:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360038134113-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-CAT-42-Registro-1100-N%C3%A3o-foi-encontrado-um-c%C3%B3digo-correspondente-em-outro-registro-do-tipo-0200
---

**Ocorrência**Ao validar o arquivo da CAT 42 está ocorrendo o seguinte erro:  
Registro 1100: Não foi encontrado um código correspondente em outro registro do tipo "0200"  
  
**Ambiente**Protheus – Livros Fiscais – A partir da versão 11.80  
  
**Causa**Esse erro ocorre, pois o tamanho dos campos **B1\_DESC** e**F2V\_DESPRO**está diferente.  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
1. Acesse o Configurador (SIGACFG) e verifique o tamanho do campo **B1\_DESC** na tabela **SB1** (Descrição Genérica do Produto);  
2. Depois, verifique o tamanho do campo **F2V\_DESPRO** na tabela **F2V** (Ress.ICMSST-Saldos Apuração);  
3. Altere o tamanho do campo **F2V\_DESPRO** para que fique igual ao tamanho do campo **B1\_DESC**;  
4. Após a correção do campo, processe novamente a apuração e geração do arquivo.

Obs.: Se o conteúdo do campo **B1\_DESC** estiver com tamanho maior do que o tamanho do campo **F2V\_DESPRO** o produto não será gravado na tabela **F2V**e consequentemente não gerará o registro 0200.
