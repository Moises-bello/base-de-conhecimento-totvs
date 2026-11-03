---
article_id: 360018606391
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 5e90440b54da682d57bd231d2f604f4505ab32c92957e4f3a332ed00ea8456d9
fetched_at: '2026-06-28T22:38:31.326859+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: MP-FAT-Os parâmetros MV_HVERAOI e MV_HVERAOF devem ser alterados manualmente
  todo ano
type: support-article
updated_at: '2021-04-28T15:55:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018606391-MP-FAT-Os-par%C3%A2metros-MV-HVERAOI-e-MV-HVERAOF-devem-ser-alterados-manualmente-todo-ano
---

**Dúvida**

Os parâmetros **MV\_HVERAOI** e **MV\_HVERAOF** devem ser alterados manualmente todo ano?  
   
 **Ambiente**

Microsiga Protheus - a partir da versão 12.  
  
**Solução**

Os parâmetros **MV\_HVERAOI** e **MV\_HVERAOF** somente devem ser ajustados, se o ambiente utiliza o parâmetro **MV\_HORARMT**=3, neste caso sim, deverá ser ajustados todo ano, visto que a data de inicio e fim do Horário de Verão não é a mesma data todos os anos  e pode haver alteração de período, como foi o caso do Horário de Verão para 2018.

Dúvidas de configuração dos parâmetros, acesse a FAQ no TDN que também contém o boletim técnico referente aos parâmetros: **[Campo F2\_hora está sendo gravado com o horário incorreto resultando na Rejeição 578](http://tdn.totvs.com/pages/viewpage.action?pageId=267794836)**
