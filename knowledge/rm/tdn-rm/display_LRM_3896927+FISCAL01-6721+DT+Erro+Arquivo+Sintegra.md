---
content_hash: 75250e10545d0727782826ff18ad183ea38470581442f02e9112f9091ff0343a
fetched_at: '2026-06-29T00:09:24.035614+00:00'
page_id: '423929070'
product: rm
source: tdn-rm
title: 3896927 FISCAL01-6721 DT Erro Arquivo Sintegra
type: documentation
url: https://tdn.totvs.com/display/LRM/3896927+FISCAL01-6721+DT+Erro+Arquivo+Sintegra
version: 1
---

Tempo aproximado para leitura:**02 min**

****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Serviços |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | Rotina Estadual Sintegra |

**02. SITUAÇÃO/REQUISITO**

Erro Arquivo Sintegra, ao validar a rotina do Sintegra ocorre:  
Registro 60 analítico sem o registro mestre correspondente.

**03. SOLUÇÃO**

Ajustada a geração do Arquivo Sintegra.  
O erro na geração da Rotina que continha Lançamentos Fiscais parcelados sem Desconto onde a Base de Dados  
estava parametrizada com mascara de numero de documento maior que 6 dígitos.
