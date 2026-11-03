---
article_id: 4415588154007
category: ADVPL - Ponto de Entrada
content_hash: e8504d5721ad831dea9726ff14497cd14513e913984ec115c0ee05c2f18c1924
fetched_at: '2026-06-28T22:40:11.755792+00:00'
product: protheus
section_id: 1500001549122
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - MPDOCPTH: Permitir
  a alteração do caminho padrão de armazenamento do banco de conhecimento.'
type: support-article
updated_at: '2022-06-21T17:54:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4415588154007-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-MPDOCPTH-Permitir-a-altera%C3%A7%C3%A3o-do-caminho-padr%C3%A3o-de-armazenamento-do-banco-de-conhecimento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura:**00:01:00 min****Dúvida**É possível alteração do path (caminho) padrão de armazenamento do banco de conhecimento?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 12.1.27  
  
**Solução**Existe o ponto de entrada **MPDOCPTH**.   
O ponto de entrada deve retornar o path de armazenamento do banco de conhecimento.   
Por exemplo: o retorno "/shareddocs" fará o path de referência ser alterado para a pasta "/shareddocs" a partir do **rootpath** do **Protheus**.   
Se o ponto existir, o banco de conhecimento passará a fazer a leitura e gravação de documentos a partir da pasta especificada.  
**Nota:**  
Não será feita qualquer criação de pasta ou consistência da existência da mesma.   
Se já houverem documentos armazenados nas pastas padrões do banco de conhecimento, **NÃO** será efetuado qualquer tipo de ajuste por parte do sistema.  
Eventuais ajustes e remanejamento de documentos ficarão a cargo do criador do ponto de entrada.  
**Exemplo:**

```
#include "totvs.ch"  
  
User function MPDOCPTH()  
  
Local cPath:=""  
  
cPath:="/shareddocs"//caminho a partir do rootpath do Protheus.  
  
Return cPath
```

**Saiba Mais**[Ponto de Entrada MpDocument](https://tdn.totvs.com/display/public/PROT/DFRM4-3676+DT+Ponto+de+Entrada+-+MpDocument)
