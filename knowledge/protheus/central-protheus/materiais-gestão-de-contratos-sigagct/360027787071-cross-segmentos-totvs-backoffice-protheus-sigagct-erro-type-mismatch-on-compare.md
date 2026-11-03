---
article_id: 360027787071
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: 84f446e716c83353b06b7ddc1a1f55f3378750d198441aad2543d784ea608bc0
fetched_at: '2026-06-28T22:37:20.040718+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Erro "type mismatch
  on compare on CN120GRVPED ou "type mismatch on compare on CN121GERDOC" No encerramento
  da medição
type: support-article
updated_at: '2026-06-22T20:02:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027787071-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Erro-type-mismatch-on-compare-on-CN120GRVPED-ou-type-mismatch-on-compare-on-CN121GERDOC-No-encerramento-da-medi%C3%A7%C3%A3o
---

**Ocorrência**  
Ao encerrar a medição ocorre a falha / erro de "type mismatch on compare on CN120GRVPED" ou "type mismatch on compare on CN121GERDOC"   
  
**Ambiente**  
Microsiga Protheus – Gestão de contratos – A partir da versão 12   
  
**Causa**

Esse incidente ocorre, pois o "Tipo" do parâmetro no dicionário SX6 ou conteúdo MV\_CNDPCAL estão diferentes do padrão.

No arquivo de error.log completo da ocorrência pode ser verificada a variável "NGCTDPCAL" com um tipo diferente de "numérico" que é o padrão do sistema (no caso do exemplo da imagem abaixo está como "C" de "Caracter"):

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29217763779479)

**Solução**

Para solucionar essa ocorrência, realize os seguintes passos:  
1. É necessário que seja **alterado o "Tipo" do parâmetro** para **"Tipo "Numérico" (na tabela SX6, campo X6\_TIPO = N)**, e deixando o conteúdo como 1, 2 ou 3, conforme a necessidade.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4433465320855)

***Saiba Mais:***

[GCT0105- Como corrigir o erro " type mismatch on compare on CN120GRVPED(CNTA120.PRW)"](https://tdn.totvs.com/pages/releaseview.action?pageId=327321955)

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001539581)
