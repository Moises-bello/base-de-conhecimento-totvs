---
content_hash: 65e5490e4a727fc681096f68b8232dc2a1188f72763724b843c745bc9ff71199
fetched_at: '2026-06-29T00:10:58.764061+00:00'
page_id: '606642939'
product: rm
source: tdn-rm
title: FISCAL01-15034 DT Log Rotina Estadual - PR ADRC-ST
type: documentation
url: https://tdn.totvs.com/display/LRM/FISCAL01-15034+DT+Log+Rotina+Estadual+-+PR+ADRC-ST
version: 5
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS Backoffice |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | Gestão Fiscal |
| Função: | Rotina Estadual ADRC-ST |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-15034 |

## **02. SITUAÇÃO/REQUISITO**

Criar Log para Rotina Estadual ADRC-ST

## **03. SOLUÇÃO**

Foi implementado junto a geração da Rotina Estadual ADRC-ST um Log para que o cliente posso verificar algumas inconsistências antes de enviar o Arquivo

**Inconsistências apontadas no Log:**

Registro 1000:

Alíquota Interna do ICMS no Anexo de Dados Fiscais por UF do Produto Zerada.  
Código CEST nos Dados Fiscais do Produto não preenchido.

Registro 1200:

CST não informado no Item do Lançamento Fiscal.  
Campo “OPERAÇÃO COM CONSUMIDOR FINAL” não habilitado para o Lançamento Fiscal vinculado ao Produto.
