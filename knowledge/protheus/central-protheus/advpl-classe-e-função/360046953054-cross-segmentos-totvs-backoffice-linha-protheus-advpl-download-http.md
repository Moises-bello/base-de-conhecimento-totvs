---
article_id: 360046953054
category: ADVPL - Classe e Função
content_hash: 06ef452235fd8bb942c3d8457bfc8fb52ab952857cabe784c9602105ccec3185
fetched_at: '2026-06-28T22:40:18.292768+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - ADVPL - Download HTTP
type: support-article
updated_at: '2022-01-06T18:54:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046953054-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-Download-HTTP
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:03:00 min  
  
Dúvida** O protheus server HTTP suporta downloads? Qual o tamanho limite do arquivo a ser baixado  
  
**Ambiente**Cross Segmentos - Backoffice (Linha Protheus) – ADVPL – A partir da versão 11  
  
**Solução**É possível realizar download através do server HTTP, para isso precisamos setar um **PATH**na seção HTTP e a partir dai fazer o download do arquivo **zip** ou **rar**.  
 **Exemplo:**

```
[HTTP]  
Enable=1  
Port=86  
Path=C:\P1225\protheus_data\web\ ->aqui vc determina a pasta que deseja buscar o arquivo
```

**PATH** que foi definido

![Screenshot_37.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360067957194/Screenshot_37.jpg)

Link utilizado para download :

```
http://localhost:{PORTA}/download.zip
```

**Limitação tamanho do arquivo**

A limitação é configurada pela chave **MAXSTRINGSIZE** no server, por padrão o limite é **50MB**, habilitando por exemplo **MAXSTRINGSIZE=200**, ele consegue baixar ate **200MB.**

```
[general]
maxStringSize=200
```

**Saiba mais**  
[MaxStringSize](https://tdn.totvs.com/pages/viewpage.action?pageId=161349793)  
[Path](https://tdn.totvs.com/display/tec/Path+--+29362)
