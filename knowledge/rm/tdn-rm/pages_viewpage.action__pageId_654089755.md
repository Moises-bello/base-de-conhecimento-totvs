---
content_hash: dfd135155af7f75c41eeced67f53f15c45ab51c99f09758a60175e300ef313aa
fetched_at: '2026-06-29T00:11:12.518831+00:00'
page_id: '654089755'
product: rm
source: tdn-rm
title: 12640963 FISCAL01-16837 DT - Geração indAquis 7 evento R-2055 Sped \ EFD-Reinf
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=654089755
version: 5
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | EFD-Reinf |
| País: | Brasil |
| Ticket: | 12640963 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-16837 |

## **02. SITUAÇÃO/REQUISITO**

Ao gerar o evento R-2055 de um lançamento de entrada de produtor rural pessoa física onde o participante não está parametrizado como   
Entidade executora do Programa de Aquisição de Alimentos - PAA (no cadastro do Cliente/Fornecedor) e com a Natureza de Operação = 1.501.01 -   
Entrada de mercadoria recebida com fim especifico de exportação, a tag indAquis é gerada com valor 1 e deveria ser gerada com valor 7.

## **03. SOLUÇÃO**

Geração da Tag "indAquis"  
7 - Aquisição de produção de produtor rural pessoa física ou segurado especial para fins de exportação:   
O Participante NÃO DEVE estar parametrizado como Executora de PAA (no cadastro do Cliente/Fornecedor)   
e a Natureza de Operação DEVE ser de Exportação  
No Lançamento de Entrada o CFOP Iniciado com 3 é referente a Importação e não é Exportação conforme o documento,   
então não é correto considerar o CFOP iniciado com 3..

Para esta situação o correto é considerar as CFOPs:

1.501 - Entrada de mercadoria recebida com fim específico de exportação.  
2.501 - Entrada de mercadoria recebida com fim específico de exportação.

Disponível a partir da biblioteca 12.1.31
