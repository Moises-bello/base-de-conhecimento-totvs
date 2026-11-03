---
content_hash: 2482e1bbbb873b54e33633717b03aac8502bde4cf1198a461e22fac2f12e491b
fetched_at: '2026-06-29T00:10:20.271676+00:00'
page_id: '490337861'
product: rm
source: tdn-rm
title: 5642109 FISCAL01-8888 DT Layout TAF - Alteração nos Registros T003 e T013
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=490337861
version: 5
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Serviços |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | Geração do Registro T003 e T013 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-8888 |

## **02. SITUAÇÃO/REQUISITO**

1- Ao executar o processo "Geração de registros - TAF Fiscal" foi apresentado a seguinte mensagem:  
T003. Erro ao gravar valor do campo INSCR\_MUNICIPAL . Valor: '020714600270'. Erro:   
O valor excedeu o tamanho do campo e foi truncado.

Atualmente o sistema gera esse campo considerando apenas 10 caracteres. Porém o layout único do   
TAF informa que esse campo possui o tamanho 20.

2-  O campo numero do documento do registro T0013 está sendo trucando para 9 dígitos.

## **03. SOLUÇÃO**

* Ajustado o Layout para truncar o campo INSCR\_MUNICIPAL em 20 Posições.

* Ajustado o campo Número do Documento do Registro T013 para gerar sem   
  cortar em 9 posições, limitando apenas em 60 posições conforme Layout TAF.
