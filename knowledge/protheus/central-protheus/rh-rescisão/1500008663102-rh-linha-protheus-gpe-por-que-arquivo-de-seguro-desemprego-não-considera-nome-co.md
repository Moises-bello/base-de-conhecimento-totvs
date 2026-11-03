---
article_id: 1500008663102
category: RH - Rescisão
content_hash: b94324ec5242940b01a6ad1ee166422ba1f831426f3782f85820fa8fa551a2f5
fetched_at: '2026-06-28T22:43:53.495864+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE - Por que arquivo de Seguro Desemprego não considera
  nome completo do campo RA_NOMECMP
type: support-article
updated_at: '2025-08-20T20:28:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008663102-RH-Linha-Protheus-GPE-Por-que-arquivo-de-Seguro-Desemprego-n%C3%A3o-considera-nome-completo-do-campo-RA-NOMECMP
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18943123429143)**Tempo aproximado para leitura: **01:30 min****Dúvida**Por que arquivo de Seguro Desemprego não considera nome completo do campo RA\_NOMECMP do cadastro do funcionário?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17.  
  
**Solução**O arquivo de Seguro Desemprego não considera o nome completo do campo RA\_NOMECMP quando o nome ultrapassa 40 caracteres (considerando espaço e letras). O tamanho do campo nome é conforme *layout* do Seguro Desemprego.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500012928342)  
Desta forma, se no campo Nome Completo, o nome do funcionário tiver mais de 40 caracteres, o Sistema irá buscar o nome do funcionário do campo Nome.

**Exemplo:**

**Cadastro funcionário:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18943100561815)

**Geração Seguro Desemprego.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18943123461015)

**Ao abreviar o nome campo RA\_NOMECMP com limite de 40 caracteres, o arquivo seguro desemprego considera o nome campo.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18943123469335)

**Geração Seguro Desemprego.**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/18943100586007)**

**Saiba mais:**

[RH - Linha Protheus - GPE - Como fazer a geração do arquivo de seguro desemprego](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500010783602-RH-Linha-Protheus-GPE-Como-fazer-a-gera%C3%A7%C3%A3o-do-arquivo-de-seguro-desemprego?source=search)
