---
content_hash: 6219ba0458439c5b662c0edf07c357f73a3935df374b084d81c2b34b1d0a0ceb
fetched_at: '2026-06-29T00:10:15.274849+00:00'
page_id: '463823367'
product: rm
source: tdn-rm
title: Autônomos e Externos 2/2
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=463823367
version: 13
---

# Objetivo:

---

Através deste cadastro serão definidos os eventos relativos aos rendimentos e descontos dos autônomos registrados em outros sistemas, como no BackOffice de outras linhas de produto ou através do BackOffice do RM e externos que devem ser informados ao Governo através do evento "S-1200 - Remuneração de trabalhador vinculado ao Regime Geral de Previdência Social".

---

**EVENTOS TRANSPORTADOR AUTÔNOMO**

**Provento de remuneração de frente utilizado na integração (S-1200)**

O sistema utiliza este evento para lançar o valor da remuneração de frete autônomo.

Lembrando que, o valor da remuneração de frete deverá desconsiderar a base de cálculo do IRRF e INSS.

**Exemplo:**

Valor Frete (carga): R$10.000,00 

Valor da base de cálculo de INSS 20%: R$2.000,00

Valor da base de cálculo de IRRF 10%: R$1.000,00

Neste campo deverá informar o código do evento que irá conter o valor de R$7.000,00 (Valor do Frete - Valor Base de Cálculo INSS - Valor Base de Cálculo IRRF). 

 

**Provento de remuneração de frente com incidência em IRRF utilizado na integração (S-1200)** 

O sistema utiliza este evento para lançar o valor da base de IRRF de remuneração de frete de autônomo.

**Exemplo:**

Valor Frete (carga): R$10.000,00 

Valor da base de cálculo de IRRF 10%: R$1.000,00

Neste campo deverá informar o código do evento que irá conter o valor de R$1.000,00 (Valor do Frete x 10%). 

**Provento de remuneração de frente com incidência em INSS utilizado na integração (S-1200)**

O sistema utiliza este evento para lançar o valor da base de INSS de remuneração de frete de autônomo.

**Exemplo:**

Valor Frete (carga): R$10.000,00 

Valor da base de cálculo de INSS 20%: R$2.000,00

Neste campo deverá informar o código do evento que irá conter o valor de R$2.000,00 (Valor do Frete x 20%). 

**Observação**: 

Estes eventos serão utilizados para demonstrar o pagamento somente quando a  categoria for:

711 - Contribuinte individual - Transportador autônomo de passageiros ou 

712 - Contribuinte individual - Transportador autônomo de carga, conforme manual do eSocial.

**Provento com incidência somente em IRRF utilizado na integração para autônomos de outros sistemas (S-1200)**

O sistema utiliza este evento para lançar o valor remuneração com incidência exclusiva em IRRF no cadastro do autônomo externo e autônomos do TOTVS Gestão Financeira.

**OBSERVAÇÃO:**O tratamento não abrange as categorias abaixo:

|  |  |
| --- | --- |
| 711 | Contribuinte individual - Transportador autônomo de passageiros |
| 712 | Contribuinte individual - Transportador autônomo de carga |

Veja mais detalhes em:  [Eventos S-1200 e S-1210 - Autônomos do TOTVS Gestão Financeira - Como realizar o pagamento de uma verba com incidência exclusiva em IRRF?](https://tdn.totvs.com/pages/viewpage.action?pageId=776112878)

**Gerar evento (S-1200) para autônomos externos sem o valor do desconto de INSS**  
Ao marcar este parâmetro, o sistema passa a realizar a geração do evento S-1200 para os autônomos que possuem lançamento(s) sem valor no campo VALORINSS da tabela PPAGTOAUTONOMOEXT.

**Observação**: 

Caso possua mais de um lançamento no período de apuração os valores serão somados.

---

eSocial

[Parametrizador](http://tdn.totvs.com.br/display/LRM/Parametrizador)
