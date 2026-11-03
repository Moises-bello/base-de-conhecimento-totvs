---
content_hash: 8c8037c8f5117fd87a3dfe4def80ac2c11871a0c1cb9dbeaa53fb4b491afb190
fetched_at: '2026-06-29T00:10:37.150688+00:00'
page_id: '536709999'
product: rm
source: tdn-rm
title: DT - Incorporação - Contrato de Venda - Reajuste
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=536709999
version: 1
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Construção & Projetos |
| Módulo: | Totvs Incorporação |
| Função: | Venda |
| Ticket: | - |
| Requisito/Story/Issue (informe o requisito relacionado) : |  |

## **02. SITUAÇÃO/REQUISITO**

Ao realizar Reajuste cadastrando a cotação como Acumulada e informando que o reajuste será mensagem era retornado uma mensagem de erro:

**ERRO: Erro ao tentar salvar lançamentos no RM Fluxus: Arithmetic overflow error converting numeric to data type numeric.**

**Tempo de Processamento venda [37560] grupo [9]: 00:00:09.0090000**

**Fim Reajuste: 12/12/2019 15:13:46**

**Tempo Total de Processamento: 00:00:12**

## **03. SOLUÇÃO**

Realizado um tratamento da mensagem de erro para que seja apresentado algo mais amigável para usuário:

**Início do Reajuste: 12/02/2020 10:28:14**  
**Reajustando Venda [37560] Grupo [11]...**  
**ERRO: Favor verificar se o tipo de índice dos componentes de correção monetária do plano de financiamento, corresponde a cotação definida no cadastro de moeda/índice.**

**Tempo de Processamento venda [37560] grupo [11]: 00:00:08.1652252**  
**Fim Reajuste: 12/02/2020 10:28:23**  
**Tempo Total de Processamento: 00:00:08.9996852**
