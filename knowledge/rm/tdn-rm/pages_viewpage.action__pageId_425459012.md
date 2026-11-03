---
content_hash: 8a551522e982a5ea3b6fe8b5644c5e0274ea58a6668e6efdf5e326c51e802355
fetched_at: '2026-06-29T00:09:33.396891+00:00'
page_id: '425459012'
product: rm
source: tdn-rm
title: TOTVS DBAccess - Configuração do DBAccess.ini em bases Oracle
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459012
version: 7
---

```
TOTVS DBAccess - Configuração do DBAccess.ini em bases Oracle
```

---

A configuração do DBAccess.ini é necessária  em integrações com o sistema protheus, que utilizam bases de dados Oracle.

**Pré-Condições:**

```
1- Ter instalado o SGBD Oracle
2- Ter instalado TOTVS DBAccess
```

**Configurando o arquivo:**

```
1- Acesse o diretório de instalação do TOTVS DBAccess e edite o arquivo DBAccess.ini. (caminho padrão de instalação: C:\Program Files (x86)\DBAccess)
2- Inclua o bloco abaixo no arquivo e clique em salvar:
```

```
[ORACLE]
```

```
Clientlibrary= caminho da oci.dll (padrão em  : C:\app\product\dbhome_1\BIN\oci.dll) environments=ambiente1,ambiente2,ambienteEtc,...
```

```
Observação:
```

```
O arquivo oci.dll  está na pasta BIN do  home Oracle. Exemplo: C:\app\product\dbhome_1\BIN\oci.dll+_*
```
