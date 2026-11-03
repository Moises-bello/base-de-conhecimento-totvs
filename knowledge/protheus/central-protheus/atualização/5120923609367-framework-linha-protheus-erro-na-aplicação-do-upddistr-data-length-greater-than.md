---
article_id: 5120923609367
category: Atualização
content_hash: e2a3aa29534d62d270bca32f6787dee80706d9200ecf405d6ea75c75d82579a5
fetched_at: '2026-06-28T22:42:21.171940+00:00'
product: protheus
section_id: 360000076747
source: central-protheus
title: Framework - Linha Protheus - Erro na aplicação do UPDDISTR.  Data length greater
  than the MaxStringSize configuration
type: support-article
updated_at: '2024-03-26T12:37:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5120923609367-Framework-Linha-Protheus-Erro-na-aplica%C3%A7%C3%A3o-do-UPDDISTR-Data-length-greater-than-the-MaxStringSize-configuration
---

**Ocorrência:****Na aplicação do upddistr o sistema interrompe a execução e gera um erro.log**

 [TOPAPI] TC\_DBInsert - Data length greater than the MaxStringSize configuration

**Ambiente:**

MP-Frame - TOTVS Backoffice (Linha Protheus) - TOTVS Atualizações - Todas as versões  
  
**Causa:**

Ocorre por conta de falta de comprimento na aplicação.   
  
**Solução:**

Para solucionar essa ocorrência, realize os seguintes passos:  
1. Para os serviços do Dbaccess e appserver;  
2. Incluir no dbacces.ini e appserver.ini a chave "MaxStringSize =500",  ou altera-la para "500" se já existir ;

```
[general]
maxStringSize=500
```

3. Como validar que a chave esta ativa no APPSERVER e no DBACCESS. Ao executar a aplicação como console (-console) é possível efetuar a validação na abertura conforme imagem abaixo.

DBACCESS.EXE

![image.png](https://chat.google.com/u/0/api/get_attachment_url?url_type=FIFE_URL&content_type=image%2Fpng&attachment_token=AAUuIGvJT6y1n2%2BLYi9MOkkczoz31YJF8gOvLGJkmNAW3QilSiqU8w7VjG2j2JmiTZse7soJGhuKtzzOeQNs2Pg7F0CUFl4IQvQ%2F7kgpra8ZE8fVGxA46n%2BhZYPDNvQzLG6FQxqPBVbL2mwiKao9mJtiEnBiBU1Za7ypFBGVZy9l983P1C6J0cxORrXneEad%2BHg1VaCziaEBJBKWyzMSx5oVVz718m2Frkt9s2tpA3JVz26z%2BILR%2BtAGxAO1cEALKKegSFaD6%2FR4aTjPFmeRmZzpbc%2FcKTqtrzFTWrUCjtHD9gXH6H6s%2F4rv18UvFDV3aN%2BIDBAXJT%2FFerKTGvUWzZ%2B%2Bm60vT%2FNBi8%2FOSU4PWBXCH8tIeXTysOob3QHw1VL8HNmqto%2B5y92X3CEIfUO%2Bf%2Fn5Ib93Hf9T9rRWcJT3Fg%3D%3D&sz=w512)

APPSERVER.EXE

![image.png](https://chat.google.com/u/0/api/get_attachment_url?url_type=FIFE_URL&content_type=image%2Fpng&attachment_token=AAUuIGs4K43QfMhaW%2BYzQt5j5n%2BBAKoQFc52fstB4DMJGJ3PChpvl9U5a06OrejZB5V4Z1LDydZ%2Fh3PGTd91WyNmwkQBuOqyUef5SSF4tTaQIYpiImqk%2BiSrhmQNK9o7xRHWHDUFvcmPD52D3yZ01BkcAK3k3MUODwe1%2BsfgrQi4TNhjjyk%2BTmKoyWUxLvQE837tXJ97nGAD0cwmReJ96g3F646OnSePjB2W790hHMdLsLakttfwt6Nlgpfpb3KpLRkvqlJDLxmqRpoBlrjUErkOkHnyIJwF7lbEYIxlOlIvTdggnXPBGIiSgUNhQKmMss4rCzYQZoB%2BwjjzeHNJRh5rrQMjw3p2nnsmbU9AFShtYeBLEiD3B1JdyaNTbQ9za99qdcvmqEk6WlebA0wbEXG9KHkt4JPHKcCtBoiM1g%3D%3D&sz=w512)

OBS.: Possível validar no console.log das aplicações.

. Iniciar os serviços e reaplicar o Upddistr.

**Detalhe:**

MaxStringSize.

https://tdn.engpro.totvs.com.br/pages/viewpage.action?pageId=161349793
