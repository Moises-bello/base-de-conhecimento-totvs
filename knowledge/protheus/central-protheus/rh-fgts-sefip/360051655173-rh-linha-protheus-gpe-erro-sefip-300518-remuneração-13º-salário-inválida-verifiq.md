---
article_id: 360051655173
category: RH - FGTS / SEFIP
content_hash: d414bc1ef887b50cf5438246f3402d645d2ecfcfcb529e98ff123fe8b1bd93b0
fetched_at: '2026-06-28T22:43:41.258392+00:00'
product: protheus
section_id: 360003115651
source: central-protheus
title: RH - Linha Protheus - GPE - Erro Sefip  300518 - Remuneração 13º Salário Inválida.
  Verifique se  está preenchido corretamente
type: support-article
updated_at: '2025-08-14T17:42:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051655173-RH-Linha-Protheus-GPE-Erro-Sefip-300518-Remunera%C3%A7%C3%A3o-13%C2%BA-Sal%C3%A1rio-Inv%C3%A1lida-Verifique-se-est%C3%A1-preenchido-corretamente
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34185641688343) Tempo aproximado para leitura: 00:01:30 min  
  
Ocorrência**Ao gerar o arquivo do SEFIP ocorre o seguinte erro 300518 - Remuneração 13º Salário Inválida. Verifique se está preenchido corretamente.

![](https://totvssuporte.zendesk.com/attachments/token/2DZj0WlvvHpHy2P0iB6V4m3Dh/?name=inline463532883.png)  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Causa**Esse incidente ocorre, pois o parâmetro MV\_SOMAVIS está como falso. 

**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
**1**. Deixe o parâmetro **MV\_SOMAAVIS** como **.T.**.  
Segue abaixo a documentação referente ao parâmetro que é responsável por levar o 13º salário sobre aviso indenizado para o arquivo SEFIP.

[RH - Linha Protheus - GPE - Envio de valores de INSS em rescisões com aviso indenizado (MV\_SOMAVIS)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052994253-MP-GPE-Envio-de-valores-de-INSS-em-rescis%C3%B5es-com-aviso-indenizado-MV-SOMAVIS-?source=search)

**Saiba mais:**[FGTS](https://tdn.totvs.com/display/public/PROT/FGTS)
