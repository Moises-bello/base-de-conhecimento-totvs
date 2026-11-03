---
article_id: 360024893694
category: TAF - REINF
content_hash: 050d87ed4a03594fead5ec2f3bbd9d5f31c992b60457727a435b9b41ad33bb32
fetched_at: '2026-06-28T22:41:34.617158+00:00'
product: protheus
section_id: 1500001536841
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - TAF - REINF - Controle de Numeração
  de Nota - Tabela C0R - Duplicidade Registro T001AE - Documento de Arrecadação '
type: support-article
updated_at: '2023-03-31T17:04:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024893694-Cross-Segmentos-Backoffice-Protheus-TAF-REINF-Controle-de-Numera%C3%A7%C3%A3o-de-Nota-Tabela-C0R-Duplicidade-Registro-T001AE-Documento-de-Arrecada%C3%A7%C3%A3o
---

**Dúvida**Duplicidade Registro T001AE - Documento de Arrecadação  
  
**Ambiente**  
Protheus – TAF – A partir da versão 12.1.33  
  
**Solução**

Para solução desta ocorrência realize os seguintes procedimentos:

Caso utilize o controle de numeração pelo License:

1) Acesse o configurador em seguida, utilize o caminho abaixo:  
  
Ambiente -> Cadastro -> Controle de Numeração (Rotina APCFG110)

2) Filtre pela tabela C0R e informe o próximo número a ser gravado na tabela (Para saber o próximo número a ser gravado, basta acessar a tabela C0R pela APSDU e verificar o último registro incluso, pelo campo C0R\_ID);

![inline1901384519.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360038414154/inline1901384519.png)

3) Após realizar o ajuste, basta extrair os dados novamente.

Caso utilize controle de numeração pelo SXE e SXF, basta deletar as linhas referente a tabela C0R para que o sistema acate a nova numeração.  Após isso, basta seguir os mesmos procedimentos mencionado nos primeiros passos.
