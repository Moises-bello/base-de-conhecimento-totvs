---
content_hash: c36389fd2171307aa7c9ed4f67c8f1f6acdc5649a66e82573081dcc2800e0dd6
fetched_at: '2026-06-29T00:09:09.223163+00:00'
page_id: '393353477'
product: rm
source: tdn-rm
title: 3561185 FOPROTINAS01-5403 DT - Valor de FGTS de diferença por dissídio duplicado
  na GRRF
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=393353477
version: 6
---

# VALOR DE FGTS DE DIFERENÇA POR DISSÍDIO DEVE SER LEVADO APENAS UMA VEZ NA GRRF

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Recursos Humanos |
| **Módulo:** | Folha de Pagamento |
| **Função:** | GRRF |
| **Situação/Requisito:** | Valor de FGTS referente a uma diferença por dissídio está sendo levado em duplicidade para compor a base de cálculo da multa rescisória sobre o FGTS. Consequentemente, os lançamentos financeiros decorrentes da GRRF estão sendo gerados com valor incorreto. |
| **Solução/Implementação:** | Foi realizado ajuste para não considerar a base de diferença por dissídio e a base de diferença por dissídio 13º na composição da base para o cálculo da multa rescisória de FGTS. Essas duas bases são compostas pelo somatório dos valores dos eventos de base de cálculo com CC 69 e 111 (dissídio) e CC 109 (dissídio 13º), respectivamente. Elas não precisam compor a base de cálculo da multa na GRRF, uma vez que cada um desses códigos de cálculo é uma base de cálculo equivalente a um ou mais proventos/descontos lançados no envelope do funcionário, que já são considerados na Base de FGTS e FGTS 13º (que já compõem a base de cálculo da multa como remuneração do mês atual) e nos lançamentos financeiros da GRRF como "Valor FGTS Mês Rescisão".  Também foi realizado ajuste para considerar o código de cálculo 180 (Diferença de 13º salário por dissídio) na base de FGTS 13º na GRRF, de modo a levar o valor calculado em diferença de 13º por dissídio. O código de cálculo 66 (Dif. 13º Salário) já era considerado. |
| **Tickets relacionados:** | 3561185 |
