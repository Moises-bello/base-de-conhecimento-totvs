---
content_hash: e5bc46862f8f2c1fba67224644dd9492feed1895c7711e2bb67dd05c76357a3a
fetched_at: '2026-07-02T19:24:25.761540+00:00'
page_id: '506150000'
product: protheus
source: tdn-tec
title: Seção [Environment], chave FGLSQLReplay
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=506150000
version: 7
---

FGLSQLReplay

## Descrição

A chave de configuração FGLSQLReplay permite ativar uma camada de logs que passa a registrar no console.log do true toda emissão de statements submetidos ao Banco de Dados em uso.

Por se tratar de uma feature de troubleshooting, sua ativação pode afetar a performance do ambiente.  
Utilize apenas se necessário ou caso receba a recomendação dos times de suporte e desenvolvimento da TOTVS.

---

## Valores válidos

| Valor | Descrição | Observação |
| --- | --- | --- |
| 0 | Desativa o registro de log dos statements. | Default |
| 1 | Ativa o registro de log dos statements. |  |

---

## Exemplo

Trecho do log apresentando em console:
