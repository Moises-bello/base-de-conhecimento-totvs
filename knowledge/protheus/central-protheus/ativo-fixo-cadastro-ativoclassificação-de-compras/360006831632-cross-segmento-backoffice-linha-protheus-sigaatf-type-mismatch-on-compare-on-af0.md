---
article_id: 360006831632
category: Ativo Fixo - Cadastro Ativo/Classificação de Compras
content_hash: ee92167ec40b57959d7a6ad67bae0df9e158da8f9884543c0995c5ccf583833b
fetched_at: '2026-06-28T22:41:48.448167+00:00'
product: protheus
section_id: 1500001547662
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAATF - type mismatch on compare
  on AF012ALNOK
type: support-article
updated_at: '2026-06-15T12:19:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006831632-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-type-mismatch-on-compare-on-AF012ALNOK
---

**Ocorrência**  
THREAD ERROR ([27800], Cruz\_Alta\_3, 001-CONTCONTPC) 29/06/2018 16:27:16  
type mismatch on compare on AF012ALNOK(ATFA012.PRW) 06/02/2018 11:54:27 line : 3269  
  
**Ambiente**Protheus – Ativo Fixo – A partir da versão 12.1.17  
  
**Causa**Erro ocorre no momento da inclusão de novo ativo fixo.  
  
**Solução**  
Verificamos que o erro ocorre na linha onde é validado os parâmetros MV\_ZRADEPR e MV\_ULTDEPR ​.   
  
- Por favor, verifique se o parâmetro MV\_ZRADEPR existe em seu ambiente e se o mesmo está com o tipo "lógico". Segue anexo exemplo. .F.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4416020268567)​  
  
- Verifique se o parâmetro MV\_ULTDEPR existe em seu ambiente e se o mesmo está com o tipo "data". Segue anexo exemplo.  
  
![](https://totvssuporte.zendesk.com/attachments/token/6QjM7LXpR1yqfnTCiixHqNSma/?name=inline-308978118.png)​  
  
Caso não estejam dessa forma, crie ou altere-os para que não ocorre o erro.  
  
Atenciosamente,
