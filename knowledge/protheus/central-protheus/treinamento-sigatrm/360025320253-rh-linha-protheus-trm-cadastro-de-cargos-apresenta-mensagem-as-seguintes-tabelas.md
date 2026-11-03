---
article_id: 360025320253
category: Treinamento (SIGATRM)
content_hash: 0a24824947278e019ed937f6c4e89661a6af8009a6e4067e1b862a5b3cf7018c
fetched_at: '2026-06-28T22:43:02.564035+00:00'
product: protheus
section_id: 206971527
source: central-protheus
title: RH - Linha Protheus - TRM - Cadastro de Cargos apresenta mensagem - As seguintes
  tabelas devem ter o compartilhamento menor ou igual a SQ3 (Cargos). É necessário
  modificá-las através do configurador
type: support-article
updated_at: '2021-04-06T17:07:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025320253-RH-Linha-Protheus-TRM-Cadastro-de-Cargos-apresenta-mensagem-As-seguintes-tabelas-devem-ter-o-compartilhamento-menor-ou-igual-a-SQ3-Cargos-%C3%89-necess%C3%A1rio-modific%C3%A1-las-atrav%C3%A9s-do-configurador
---

**Dúvida**Cadastro de Cargos apresenta mensagem - As seguintes tabelas devem ter o compartilhamento menor ou igual a SQ3 (Cargos). É necessário modificá-las através do configurador  
  
![](https://p23.zdusercontent.com/attachment/888110/yq5sIPUUlNeSI1VeQhyEYzN3p?token=eyJhbGciOiJkaXIiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0..c5alVWdHV9xku48yWYJiDg.gcMSTOoPXWKRPZd0GBNyvKvznMWlB5o5T0X9sL-AoluXnG4nT_x1QJeqksnFLAyxIDvHzZ-9AYS3HnzZXqLgiC1hw_iumCov73r60sopAMl7zuxvuH6Lp8nnxJFxuKp2Ry1MAb9s1Do0LZFq_vqvKWmlQzOmG3GeB6afMrUvIsjVm97JvB3xS8BMVnWtUqafbd9-jxcrJSqq7TUyNBKyKtTdhU-g2wkvdLhAnhnvy7ullimJrhsZO71zrT4KCr0Ab97tOTEcWva4cBwqB-u-P00caheACL9V6iUR3U_ku0Y.JeJL3f-OXfoo7zkE0xTu_A)  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Treinamento - A partir da versão 11.80  
  
**Solução**Para solucionar essa dúvida, realize os seguintes passos:  
  
1. Para que seja possível mudar o compartilhamento via configurador, faça um Backup das tabelas e apague os registros;  
2. Ajuste o Compartilhamento das tabelas via configurador, considerando sempre como base a SQ3. **Por exemplo, se ela for totalmente compartilhada (C C C), as demais tabelas não podem ser exclusivas (E E E);**3. Volte o Backup dos dados feito no passo 1 e ajuste a coluna **Filial** se necessário, conforme novo compartilhamento.
