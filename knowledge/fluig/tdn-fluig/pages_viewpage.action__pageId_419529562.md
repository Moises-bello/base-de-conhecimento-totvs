---
content_hash: fe5a777b6c64603e4dcdb35ec328003704bf1b5dd1b17cab5d6ed2f90acf8e3a
fetched_at: '2026-06-28T21:35:26.802463+00:00'
page_id: '419529562'
product: fluig
source: tdn-fluig
title: ARQ - Problemas com caracteres especiais na publicação em ambiente Linux
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=419529562
version: 12
---

true.\*ndicenone

**Produto:** TOTVS Fluig Plataforma

**Ambiente:** Linux

# Ocorrência

Ao publicar arquivos com caracteres especiais, por exemplo acentuação, principalmente em ambiente Linux a publicação não tem sucesso e ocorre a mensagem abaixo no log:

Mensagem de erro

ERROR [com.datasul.technology.webdesk.foundation.servlet.StreamControlWCM] (default task-11) StreamControlWCM failed: java.lang.RuntimeException: javax.ejb.EJBException: java.nio.file.InvalidPathException: Malformed input or input contains unmappable characters: <caminho do arquivo>

# Solução

false11Passo 1

No arquivo de configuração host.xml **<instalação>/appserver/domain/configuration/host.xml** localize o trecho abaixo:

* <option value="-Dfile.encoding=utf8"/>
2Passo 2

E altere para:

* <option value="-Dfile.encoding=UTF-8"/>
3Passo 3

Abaixo deste trecho, adicione a nova linha:

* <option value="-DLC\_CTYPE=UTF-8"/>
4Passo 4

O conteúdo da tag jvm-options deve ficar:

Exemplo:

<jvm-options>  
<option value="-Dfile.encoding=UTF-8"/>  
<option value="-DLC\_CTYPE=UTF-8"/>  
<option value="-XX:MaxMetaspaceSize=1024m"/>  
<option value="-Djavamelody.disabled=true"/>  
  
  
<!-- Debug  
<option value="-Xdebug"/>  
<option value="-Xrunjdwp:transport=dt\_socket,address=8787,server=y,suspend=n"/>  
-->  
</jvm-options>
