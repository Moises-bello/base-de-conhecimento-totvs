---
content_hash: 3b5ef120f88c1a5882e78bdc563acdbd16cd5fdd82a35f2021c7ebfebcb71cec
fetched_at: '2026-06-29T00:10:53.326694+00:00'
page_id: '578643071'
product: rm
source: tdn-rm
title: Totvs Gestão Financeira - Funções de Fórmulas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=578643071
version: 23
---

CHAVEPAGAMENTOPIX

Disponível a partir dos patches abaixo:

Patch 12.1.2306.240   
Patch 12.1.2310.181  
Patch 12.1.2402.116

Extrai de um QRCode Pix a chave de pagamento.  Essa chave de pagamento pode ser uma URL para QRCode dinâmico ou uma chave de endereçamento para QRCode estático.

Exemplo de como utilizar a função em uma fórmula, extraindo de um QRCode PIX gravado no lançamento:

CHAVEPAGAMENTOPIX(TABLAN('QRCODEPIX', 'S'))

Abaixo segue alguns exemplos do resultado de QRCode estático e QRCode dinâmico.

1. QRCode Dinâmico
   * QRCode PIX: 00020101021226770014BR.GOV.BCB.PIX2555api.itau/pix/qr/v2/d81aaa36-722e-4015-a9bd-6cf47aa83eb25204000053039865802BR5910TICKET LOG6009SAO PAULO62070503\*\*\*630481C9
   * Resultado da função: api.itau/pix/qr/v2/d81aaa36-722e-4015-a9bd-6cf47aa83eb2
2. QRCode Estático - Chave CPF
   * QRCode PIX: [00020126330014br.gov](http://00020126330014br.gov).bcb.pix01113160180107652040000530398654031005802BR5903PIX6006Cidade62070503\*\*\*6304A4EB
   * Resultado: 31601801076
3. QRCode Estático - Chave Telefone
   * QRCode PIX: 00020126360014BR.GOV.BCB.PIX0114+553199999999952040000530398654073000.005802BR5914TEste Telefone6009Fortaleza62070503\*\*\*63040A96
   * Resultado: +5531999999999
4. QRCode Estático - Chave E-mail
   * QRCode PIX: [00020126500014BR.GOV.BCB.PIX0128testeemail@testeemail.com.br](mailto:00020126500014BR.GOV.BCB.PIX0128testeemail@testeemail.com.br)5204000053039865406200.005802BR5911Teste Email6009Fortaleza62070503\*\*\*63041E42
   * Resultado: [testeemail@testeemail.com.br](mailto:testeemail@testeemail.com.br)
5. QRCode Estático - Chave Aleatória
   * QRCode PIX: 00020126580014BR.GOV.BCB.PIX0136dcta478j-196l-03fm-t6gh-4298er7845m25204000053039865406152.365802BR5921Teste Chave Aleatoria6014Belo Horizonte62070503\*\*\*6304A00E
   * Resultado: dcta478j-196l-03fm-t6gh-4298er7845m2
CHAVETXIDPIX

Disponível a partir dos patches abaixo:

Patch 12.1.2306.266  
Patch 12.1.2310.219  
Patch 12.1.2402.163  
Patch 12.1.2406.100

Extrai de um QRCode Pix o TX Id.  Essa identificador da transação é extraído somente de um QRCode estático.

Exemplo de como utilizar a função em uma fórmula, extraindo de um QRCode PIX gravado no lançamento:

CHAVETXIDPIX(TABLAN('QRCODEPIX','S'))

Abaixo segue alguns exemplos do resultado de QRCode estático.

1. QRCode Estático - Chave CPF
   * QRCode PIX: [00020126330014br.gov](http://00020126330014br.gov).bcb.pix01113160180107652040000530398654031005802BR5909Teste CPF6006Cidade62150511316018010766304E92C
   * Resultado: 31601801076
2. QRCode Estático - Chave Telefone
   * QRCode PIX: [00020126360014br.gov](http://00020126360014br.gov).bcb.pix0114+5531999999999520400005303986540415665802BR5914Teste Telefone6006Cidade62180514+553199999999963044568
   * Resultado: +5531999999999
3. QRCode Estático - Chave E-mail
   * QRCode PIX: [00020126500014br.gov.bcb.pix0128testeemail@testeemail.com.br](mailto:00020126500014br.gov.bcb.pix0128testeemail@testeemail.com.br)52040000530398654031525802BR5911Teste email6006Cidade62140510testeemail630495E5
   * Resultado: testeemail
4. QRCode Estático - Chave Aleatória
   * QRCode PIX: [00020126580014br.gov](http://00020126580014br.gov).bcb.pix0136dcta478j-196l-03fm-t6gh-4298er7845m25204000053039865405445225802BR5921Teste Chave Aleatoria6006Cidade62120508dcta478j630461ED
   * Resultado: dcta478j
TIPOPAGAMENTO

Retorna o tipo de pagamento de acordo com o contexto passado para o serviço do calculo do valor liquido. Tem como objetivo conceder um desconto ou acréscimo de acordo como será efetuada a forma de pagamento. Ex: Conceder um desconto caso o tipo de pagamento tenha sido por débito ou PIX.

São retornado os seguintes valores:

0 - Cartão de Crédito;

1 - Cartão de Débito;

2 - PIX

-1 - Nenhum

URLQRCODEPIX

OBSOLETO - Utilizar a função de fórmula CHAVEPAGAMENTOPIX conforme documentado nesta página.

VALORBASEJUROSEMULTA

Retorna o valor líquido do lançamento desconsiderando multa, juros e valores opcionais condicionado ao vencimento

Campos que são desconsiderado no retorno da fórmula:

Valor de multa;

Valor de juros;

Valor de multa INSS;

Valor de juros INSS;

Valor de multa IRRF;

Valor de juros IRRF;

Valor Desconto Condicional;

Valores opcionais que aumentam e que estejam parametrizado com dias de atraso maior que zero;

Valores opcionais que descontam e que estejam parametrizado até o vencimento.

**Exemplo:**

Lançamento

Valor Original: 1.000,00

Valor Multa: 100,00

Valor Juros: 60,00

Vencimento: 12/12/2020

Data atual: 15/12/2020

VALORLIQUIDO() - O resultado será 1.160,00

VALORBASEJUROSEMULTA() - O resultado será 1.000,00

VALORBRUTOBOLETO

Retorna o valor original do (s) lançamento (s) vinculados ao boleto.

**Exemplo:**

Lançamento

Valor Original: 1.000,00

Valor Multa: 100,00

Valor Juros: 60,00

Vencimento: 05/09/2024

Data: 12/09/2024

VALORBRUTOBOLETO() - O resultado será 1.000,00

VALORLIQUIDOBOLETO() - O resultado será 1.160,00

VALORTRBLAN

Retorna o valor do tributo no lançamento. Caso o título esteja baixado, obtém as informações da tabela de tributos da baixa.

**Parâmetros:**

* Código do tributo (texto)
VALORTRBLANBAIXA

Retorna o valor do tributo na baixa do lançamento.

**Parâmetros:**

* Código do tributo (texto)
VALORTRBLANBAIXAPF

Retorna o valor do tributo na baixa do lançamento em uma determinada data, considerando a Posição Financeira.

Apenas para lançamentos baixados.

**Parâmetros:**

* Código do tributo (texto)
* Data considerada (data)
VALORTRBLANPF

Retorna o valor do tributo no lançamento em uma determinada data, considerando a Posição Financeira.

**Parâmetros:**

* Código do tributo (texto)
* Data considerada (data)
