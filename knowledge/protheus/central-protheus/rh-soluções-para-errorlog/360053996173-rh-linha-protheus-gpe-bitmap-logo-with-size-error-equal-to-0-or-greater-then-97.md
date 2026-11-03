---
article_id: 360053996173
category: RH - Soluções para error.log
content_hash: a565fd9b540cdfa5bbaf02af2be7f32dfeb16fb0a07b208f887e2bc5012ab881
fetched_at: '2026-06-28T22:44:09.046392+00:00'
product: protheus
section_id: 115003853987
source: central-protheus
title: RH - Linha Protheus - GPE - Bitmap logo with size error, equal to 0 or greater
  then 97 kB. in file
type: support-article
updated_at: '2022-04-26T12:01:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053996173-RH-Linha-Protheus-GPE-Bitmap-logo-with-size-error-equal-to-0-or-greater-then-97-kB-in-file
---

**Ocorrência**Ao emitir **relatórios com logotipo** gera *error log:* "***Bitmap* logo *with* *size error,* equal *to* 0 *or greater then* 97 kB. *in file****".***Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoas - Todas as versões  
  
**Solução**O arquivo de logotipo, para ser inserido em um relatório, deve possuir no máximo um tamanho de 97kb, com as medidas em 100 *pixels* de largura por 20 *pixels* de altura.  
  
Para solucionar o erro, siga os passos abaixo descritos:  
  
1. A imagem do logotipo, deve ser em **formato .bmp**  
2. O **tamanho precisa ser entre 0 e 97 kb**  
3. Deve-se usar no **formato 256 cores,**  
4. Largura de **100 *pixels*;**  
5. Alturas de **20 *pixels*;**  
6. O nome do arquivo se compõe de; **LGRL + Código da Empresa + Filial + .bmp**
