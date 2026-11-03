---
content_hash: b11112695bdaaf6e16db083a303dcc050bf00ad4ae43ba79b6f62f4e8142471b
fetched_at: '2026-07-02T19:24:26.036555+00:00'
page_id: '519725180'
product: protheus
source: tdn-tec
title: DBAccess - Seção [Environment], chave SeekBind
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=519725180
version: 2
---

SeekBind

Esta chave de configuração permite ativar ou desativar o uso de *bind* de valores para as operações de *seek* que forem submetidas ao true.

---

## Valores válidos

| Valor | Descrição |
| --- | --- |
| 0 | Não utiliza bind |
| 1 (**Padrão**) | Habilita o uso de bind |

---

## Observações

* Especificar a chave na seção de configuração de um banco de dados tem efeito sobre o valor default de todos os ambientes nele configurados.
* Caso seja especificada dentro de uma seção de conexão específica [banco/ambiente], esta configuração será considerada para o ambiente em questão.
* Esta configuração passa a ser considerada a partir do true Build 20181212.
* O uso de bind provê um ganho de desempenho e performance na busca de registros. Somente devemos desligar seu uso para fins de diagnostico ou troubleshooting, quando estritamente ligados a estas operações.
* Caso a chave de configuração  esteja "ligada"/"desligada" e a chave SeekBind não tenha sido especificada, automaticamente o SeekBind será "ligado".

---

## Exemplos

  
textConfigurando SeekBind para todos os ambientes  
textConfigurando SeekBind apenas no ambiente de produção

---

## Veja também
