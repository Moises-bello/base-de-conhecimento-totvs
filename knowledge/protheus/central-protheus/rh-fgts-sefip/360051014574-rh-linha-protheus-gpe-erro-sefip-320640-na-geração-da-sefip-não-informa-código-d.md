---
article_id: 360051014574
category: RH - FGTS / SEFIP
content_hash: a2cfe83c70fd13a82abb4b3db9a114571ad9e1cd889856ef14059e97d3b1c2f2
fetched_at: '2026-06-28T22:43:41.416095+00:00'
product: protheus
section_id: 360003115651
source: central-protheus
title: RH - Linha Protheus - GPE - Erro SEFIP 320640 na geração da SEFIP não informa
  código de movimentação de retorno do afastamento.
type: support-article
updated_at: '2021-07-17T03:19:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051014574-RH-Linha-Protheus-GPE-Erro-SEFIP-320640-na-gera%C3%A7%C3%A3o-da-SEFIP-n%C3%A3o-informa-c%C3%B3digo-de-movimenta%C3%A7%C3%A3o-de-retorno-do-afastamento
---

**Dúvida**Erro SEFIP 320640 na geração da SEFIP não informa código de movimentação de retorno do afastamento.

![image2018-4-11_11-16-12.png](https://tdn.totvs.com/download/attachments/351391115/image2018-4-11_11-16-12.png?version=1&modificationDate=1523456622000&api=v2)  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17.  
  
**Solução****1.**Para que o sistema entenda que o afastamento deve ter um código de movimentação no retorno é necessário que realize a seguinte configuração;  
  
**2.** Na tabela **S046** preencha o campo código de retorno para os códigos de movimentos que possuem código de retorno.

![image2018-4-11_11-20-36.png](https://tdn.totvs.com/download/attachments/351391115/image2018-4-11_11-20-36.png?version=1&modificationDate=1523456620000&api=v2)  
  
**3.** Em tipos de ausências acesse o cadastro da ausência cadastrada e informe o código de movimento que foi cadastrado na tabela **S046**.

![](https://tdn.totvs.com/download/attachments/351391115/image2018-4-11_11-22-9.png?version=1&modificationDate=1523456619000&api=v2)  
  
**4.**Calcule a folha para o funcionário e gere a **SEFIP**, desta forma o sistema irá levar o código de retorno para o txt e não haverá inconsistência **320640** no validador.

**Saiba mais:**<https://tdn.totvs.com/display/public/PROT/FGTS>
