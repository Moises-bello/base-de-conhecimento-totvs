---
content_hash: 7959d09b027eca772feff7382c7e36c6ba76cc4934b1436cae640810c105edd5
fetched_at: '2026-06-29T00:09:11.447106+00:00'
page_id: '403750797'
product: rm
source: tdn-rm
title: Cache Centralizado - Alterando o comportamento padrão
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=403750797
version: 3
---

# Sumário

---

Sumário|Revisão|Download dos arquivos

# Revisão

---

|  |  |  |
| --- | --- | --- |
| Versão do Documento | Modificação | Autor / Revisor |
|  | Criação do documento |  |
|  |  |  |

.panelContent, .panelContent p, .panelContent p span{
color: white !important;
background: #202020 !important;
}
]]>

# 1 Introdução

      Todo objeto de cache possui um comportamento padrão que é definido na implementação mesmo, porém é possível que esse comportamento seja alterado, esse recurso deve ser utilizado com critério e deve ser avaliado posteriormente pelo dono do cache se o comportamento padrão deve ou não ser alterado.

---

## 1.1.  Configuração

a) Crie um arquivo com o nome \_cache.config na pasta de instalação do RM, considere o layout do arquivo abaixo

<CacheConfigFile xmlns:i="<http://www.w3.org/2001/XMLSchema-instance>" xmlns="<http://schemas.datacontract.org/2004/07/RM.Lib.Cache>">

  <Caches>

    <CacheConfig>

      <Id>SqlCacheData.Cache</Id>

      <Limit>0</Limit>

      <Mode>Default</Mode>

      <Timeout>0</Timeout>

    </CacheConfig>

  </Caches>

</CacheConfigFile>

b) O Id do cache é identificado pelo arquivo de log do cache.

c) O Mode pode ser:

* Disabled: Desabilita o cache
* Default: Utiliza o modo padrão do cache definido pela TOTVS
* Memory: Sempre utiliza o cache em memória
* KVS: Sempre utiliza o cache KVS

d) A propriedade Limite, define o número máximo de itens que o cache poderá ter. A propriedade Timeout define o tempo limite de expiração do item no cache em segundos.

falsefalse

**Produto:** Framework

false

**Versão:** 12.1.20 ou Superior

false

Cache Centralizado - **Get Started**

falsefalse

**Status:** **Finalizado**

false

**Data:**

false

**Autores:**

false 250
