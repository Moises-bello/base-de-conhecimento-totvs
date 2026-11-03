---
content_hash: 6c2cc3090ce532ad7b678fb0c4fd64ecaf4862a2f3208ba7b09e0ae5fc289f78
fetched_at: '2026-06-29T00:06:30.028433+00:00'
page_id: '235308996'
product: rm
source: tdn-rm
title: TUIPQ8_DT_SUBORDINADOS_PORTAL
type: documentation
url: https://tdn.totvs.com/display/LRM/TUIPQ8_DT_SUBORDINADOS_PORTAL
version: 123
---

# VISÃO DE SUBORDINADOS RM PORTAL

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Visão de subordinados do portal* |
| **Situação/Requisito:** | *Ao abrir a página de subordinados do RM Portal para um chefe com uma grande quantidade de subordinados, era exibido um erro de timeout, impedindo o acesso à página.* |
| **Solução/Implementação:** | *Foi otimizada a rotina da visão de subordinados, mas caso a quantidade de dados a serem carregados seja muito grande, é necessário ajustar o arquivo "web.config" do portal. Procure a linha semelhante à linha abaixo:*  *<httpRuntime requestValidationMode="2.0" maxRequestLength="100000" />*  *E altere para ficar da seguinte forma:*  *<httpRuntime requestValidationMode="2.0" maxRequestLength="100000" executionTimeout="6000" />*  *Nota: os valores podem variar.*  *Ao final da alteração, a tag "httpRuntime" deve possuir a propriedade "executionTimeout" com a quantidade de tempo que deseja como limite (lembrando que o valor deve ser informado em segundos. ex.: 600 = 10 minutos)* |
| **Chamados relacionados:** | TUIPQ8, TUIX64 |

divs
