---
article_id: 1500003985082
category: Gestão de Frotas
content_hash: 781f149f2492ea0d95f19865b276fc095024e644e323b5a9fdc70d910ef5abd6
fetched_at: '2026-06-28T22:42:39.332393+00:00'
product: protheus
section_id: 360012117873
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Como é definida a filial gravada no Abastecimento
type: support-article
updated_at: '2021-08-13T16:49:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003985082-Manufatura-Linha-Protheus-MNT-Como-%C3%A9-definida-a-filial-gravada-no-Abastecimento
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023739612/time.png)**Tempo aproximado para leitura: **00:03:00 min****Dúvida**Como é definido a filial de gravação do abastecimento?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Gestão de Frotas - Versão 12  
  
**Solução**O processo de abastecimento pode ser efetuado tanto para veículos de mesma filial, como também para veículos de qualquer outra filial, através de uma **Importação de Abastecimento - MNTA716**, um **Abastecimento Manual - MNTA655** ou um **Abastecimento em lote - MNTA656**. Para que esse cadastro seja possível, ao registrar o abastecimento, deve ser informada a placa do veículo, que pode ser de uma outra filial. As situações possíveis para inclusão de um abastecimento realizado numa filial diferente do veículo são:  
  
**Situação 1:**Mesmo nível de compartilhamento entre **Abastecimento - TQN** e **Veículos - ST9**Nessa situação, será gravado o campo de **Filial - T9\_FILIAL**, conforme a filial do veículo abastecido. Porém, será considerada a situação do veículo, através do campo **Situação do Bem - T9\_SITBEM**, que deve estar ativo nessa filial.

| Filial do veículo - ST9 | Filial do abastecimento - TQN | Gravação |
| --- | --- | --- |
| M RJ 01 | M RJ 02 | M RJ 01 |
| S SC 01 | M RJ 01 | S SC 01 |
| M RJ | S SC | M RJ |
| S SC | M RJ | S SC |
| EM BRANCO | EM BRANCO | EM BRANCO |

**Situação 2:** Níveis diferentes de compartilhamento entre **TQN** e **ST9**Quando as duas tabelas possuírem níveis diferentes de compartilhamento, existem duas outras regras de gravação, quando o posto for conveniado ou interno:

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Posto conveniado** | Quando o posto possuir algum convênio, utiliza-se o campo **Filial - TQF\_CODFIL** do posto no qual foi realizado o abastecimento. O campo **TQF\_CODFIL** sempre possuirá a informação completa de **Empresa**, **Unidade de Negócio** e **Filial**, porém, na gravação da filial do abastecimento, será respeitado o nível de compartilhamento da tabela **TQN**.  Exemplo:   | Filial do veículo (ST9) | Filial do abastecimento (TQN) | Filial do posto (TQF) | Gravação | | --- | --- | --- | --- | | M RJ | M RJ 01 | M RJ 01 | M RJ 01 | | S SC 01 | M RJ | M RJ 01 | M RJ | | M RJ 01 | EM BRANCO | S SC 01 | EM BRANCO | | M RJ 01 | S SC 01 | M RJ 01 |  | |
| **Posto interno** | Caso o nível de compartilhamento entre **Tanques de combustíveis - TQI** e **TQN** seja igual, utiliza-se o campo **Filial - TQI\_FILIAL** do tanque de abastecimento. Caso não localizar o tanque ou o compartilhamento for diferente entre as tabelas, segue-se a mesma regra do **Posto conveniado**. O campo **TQF\_CODFIL** sempre possuirá a informação completa de **Empresa**, **Unidade de Negócio** e **Filial**, porém, na gravação da filial do abastecimento, será respeitado o nível de compartilhamento da tabela **TQN**.  Exemplo:   | Filial do veículo (ST9) | Filial do abastecimento (TQN) | Filial do tanque (TQI) | Filial do posto (TQF) | Gravação | | --- | --- | --- | --- | --- | | M RJ | M RJ 01 | M RJ 01 | M RJ 01 | M RJ 01 | | S SC 01 | M RJ | M RJ | M RJ 01 | M RJ | | M RJ 01 | EM BRANCO | EM BRANCO | S SC 01 | EM BRANCO | | M RJ 02 | M RJ | M | M RJ 01 | M RJ 01 | |
