---
article_id: 360035662374
category: ADVPL - Classe e Função
content_hash: 39bb48a20463c04e933c00545f1429aded0c66fa08d4eb206ec0c276078e225b
fetched_at: '2026-06-28T22:40:17.134247+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Regra de privilégios
  em função customizada
type: support-article
updated_at: '2022-05-05T20:08:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035662374-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Regra-de-privil%C3%A9gios-em-fun%C3%A7%C3%A3o-customizada
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Temos uma função customizada que é chamada dentro de um ponto de entrada de botões nas ações relacionadas, nesta customização utilizamos uma **Mbrowse** onde não é acatado as regras de privilégios.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – Financeiro – A partir da versão 12.1.25  
  
**Solução**Neste caso é necessário modificar o parâmetros do mbrowse utilizando o método SetMainProc(), para que a regra de privilegio seja acatada no menu principal e nos demais correspondente.  
  
**Observação**  
Método **SetMainProc**() é interno disponível para esta situação.

```
mBrowse( 6,1,22,75,cAlias,,,,,, aCores,,,,,,,,cFilter,,,,,{|oBrw|oBrw:SetMainProc("U_MSZGCAD")})
```

**Saiba Mais**[**Mbrowse**](https://tdn.totvs.com/pages/viewpage.action?pageId=24346981)
