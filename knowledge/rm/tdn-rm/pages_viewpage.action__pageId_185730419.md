---
content_hash: 443f1a31a6728ab7cfd7d7c3d801f76015aa12d52bfe17866c29dcadf91a8472
fetched_at: '2026-06-29T00:05:57.902018+00:00'
page_id: '185730419'
product: rm
source: tdn-rm
title: RMFIS00002_Geração do registro 1400
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=185730419
version: 4
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | TOTVS Gestão Fiscal                      **Versão 12.1.1** |
| **Processo** | **:** | SPED Fiscal |
| **Subprocesso** | **:** | Geração do registro 1400 |
| **Data da publicação** | **:** | 13/02/2015 |

***Definição do Processo***

O objetivo deste documento é oferecer orientações sobre a geração do registro 1400 - INFORMAÇÃO SOBRE VALORES AGREGADOS.

***Regras Gerais***

O sistema Totvs Gestão Fiscal gera o registro 1400 com base nas informações do guia prático, segue trecho do manual disponível em:

<http://www1.receita.fazenda.gov.br/sistemas/sped-fiscal/download.htm>

“Registro 1400

Este registro tem como objetivo fornecer informações para o cálculo do valor adicionado por município.

Deve ser preenchido pelos seguintes contribuintes:

• empresas que adquirirem, diretamente de produtor, produtos agrícolas, pastoris, extrativos minerais, pescados ou outros produtos extrativos ou agropecuários;

• empresas que emitem documentos fiscais de entrada de produção própria, de produtos agrícolas, pastoris, extrativos minerais, pescados ou outros produtos extrativos ou agropecuários;

• empresas de transporte intermunicipal e interestadual;

• empresas de telecomunicação e comunicação;

• distribuidoras de energia;

• serviço de utilidade pública de distribuição de água;

• inscrição centralizada;

• demais casos que influenciem no valor agregado.”

***Parametrização Necessária***

 1**.** **Cadastro de Natureza de Operação**

É necessário cadastrar uma natureza pertinente a operação realizada, conforme regra mencionada acima. O sistema irá consistir o CFOP informado no lançamento:

Para lançamento de saída o CFOP deve ser: 5.25X.xx, 6.25X.xx, 5.3XX.xx, 6.3XX.xx

Para lançamento de entrada o tipo do IPI deve ser SEM IPI

Na aba Outros Dados, campo Tipo Natureza (Rotinas Legais) é necessário informar o tipo 21 – Compras a Extrat. Prod. Agrop. e Pescadores para nota de entrada ou tipo 22 – Receitas Prest de Serv. e Energia Elétrica

2**.** **Realizar o lançamento que possui a natureza parametrizada.**

Realizar o lançamento e informar a natureza de operação previamente parametrizada.

Informar a UF e município na pasta de “Prestação de Serviços” da situação tributária ou na pasta “Outros Dados” do item.

***Geração da Rotina***

Gerar a rotina SPED Fiscal no período do lançamento fiscal criado.
