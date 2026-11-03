---
content_hash: ef1f095a9448469d43db03bdc28b65af8664c217a929e2262fcbba902ecdafcb
fetched_at: '2026-06-29T00:08:11.577975+00:00'
page_id: '243630110'
product: rm
source: tdn-rm
title: TVCVKS_DT_Envelope
type: documentation
url: https://tdn.totvs.com/display/LRM/TVCVKS_DT_Envelope
version: 113
---

# Envelope de pagamento

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e projetos* |
| **Módulo:** | *Folha de pagamento* |
| **Função:** | *Envelope de pagamento* |
| **Situação/Requisito:** | Interpretação da Demanda: Cliente informa que lançou folha para funcionário, e a soma dos eventos que incide FGTS aplicada a alíquota de recolhimento (8%) apresenta um determinado valor. Porém ao gerar o lançamento financeiro do tipo 15 – FGTS conforme SEFIP o sistema está arredondando o valor para mais ou para menos, ficando assim o valor incorreto. Desta forma de apenas um funcionário a diferença é de centavos, porém esta diferença somada a todos os funcionários está impactando no fechamento do cliente. Mesmo desmarcando a flag Trunca Valores de FGTS/INSS o sistema continua considerando o arredondamento. |
| **Solução/Implementação:** | Ajuste realizado para que o sistema passe a truncar o valor de FGTS (valor folha) na aba incidências, dentro do envelope do funcionário, para que este valor seja coerente com o valor gerado pelo SEFIP, pois o SEFIP trunca os valores e o envelope estava arredondando |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | TVCVKS TVEB28 |
| **Requisito (ISSUE):** |  |

divs
