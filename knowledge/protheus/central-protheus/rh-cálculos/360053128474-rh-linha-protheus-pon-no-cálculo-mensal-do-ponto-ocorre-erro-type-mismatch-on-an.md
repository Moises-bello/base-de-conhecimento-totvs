---
article_id: 360053128474
category: RH - Cálculos
content_hash: ce4dfc68461b8a7dfdb0cad5634e578db697468eb673a9e0ffa80b51dc6bd0d8
fetched_at: '2026-06-28T22:44:51.647275+00:00'
product: protheus
section_id: 32419138773655
source: central-protheus
title: 'RH - Linha Protheus - PON - No cálculo mensal do Ponto ocorre erro: type mismatch
  on .AND. on PNM070PROC(PONM070.PRX)'
type: support-article
updated_at: '2026-02-10T20:11:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053128474-RH-Linha-Protheus-PON-No-c%C3%A1lculo-mensal-do-Ponto-ocorre-erro-type-mismatch-on-AND-on-PNM070PROC-PONM070-PRX
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38308812760983)****Tempo aproximado para leitura: 00:01:00 min**  
  
**Ocorrência**  
Ao efetuar o cálculo mensal do Ponto ocorre erro: ***type mismatch on .AND. on*** **PNM070PROC(PONM070.PRX)**  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Causa**  
Esse incidente ocorre, pois a aplicação está esperando conteúdo da variável **lMantBH** que é obtida através do parâmetro **MV\_MANTBH** como lógico e no ambiente está configurada como caractere.  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:

1. Acesse o Configurador em SIGACFG > Ambiente > Cadastros > Parâmetros;
2. Localize o parâmetro **MV\_MANTBH** e altere o mesmo;
3. No campo **Tipo** deve estar como **Lógico**, assim como na figura abaixo. Caso não consiga alterar pelo configurador, pode alterar pelo dicionário **(SX6)**;  
   ![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360088049034)

Após o ajuste no tipo do parâmetro, o erro será corrigido.  
  
  
**Saiba mais:**  
[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)
