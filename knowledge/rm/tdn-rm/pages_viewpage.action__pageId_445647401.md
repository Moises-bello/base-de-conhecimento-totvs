---
content_hash: 3bdba530c2391fd8b63d8e40bc01fbb9ad7938311a66545d10096539bd7a7e17
fetched_at: '2026-06-29T00:09:54.805180+00:00'
page_id: '445647401'
product: rm
source: tdn-rm
title: Aba Integração bancária
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=445647401
version: 15
---

Nesta aba são apresentadas informações que integram os dados bancários do Lançamento Financeiro.

**Lançamentos a Receber**

Para lançamentos a receber é exibido somente o campo "Dados bancários" que deve ser cadastrado e alterado na visão do Cliente/Fornecedor. Os demais campos bancários estão disponíveis em *Anexo | Boleto* de lançamentos financeiros e na visão de Boletos.

**Lançamentos a Pagar**

Para lançamentos a pagar são exibidos os seguintes campos:

Dados bancários

Nosso Número

O campo Nosso Número é apresentado apenas para lançamentos a Pagar e é preenchido manualmente ou no retorno de pagamento.

Código de Barras e IPTE

No total o código de barras é composto por 44 dígitos numéricos, que representam o valor e a data de vencimento, entre outras informações do boleto, a composição e disposição desses números variam de banco para banco, podendo conter o número da agência, conta corrente, código do cliente.

O código de barras é composto por dois campos:

* Campo obrigatório, determinado pelo BACEN e comum a todos os bancos;
* Campo livre, determinado por cada banco de acordo com a modalidade de cobrança utilizada pelo cliente.

A composição é realizada da seguinte forma:

| Posição | Tamanho | Conteúdo |
| --- | --- | --- |
| 01 a 03 | 03 | Código do Banco na Câmara de Compensação |
| 04 a 04 | 01 | Código da Moeda = 9 (Real) |
| 05 a 05 | 01 | Digito Verificador (DV) do código de Barras |
| 04 a 09 | 04 | Fator Vencimento |
| 10 a 19 | 10 | Valor |
| 20 a 44 | 25 | Campo Livre |

 - Validação do Código de Barras/IPTE em lançamentos a Pagar

O sistema não permitirá a inclusão de mais de um lançamento com a mesma linha digitável (IPTE) ou alteração de data de vencimento e valor diferentes do gravado no IPTE inserido no lançamento. Mas para que o sistema faça essa consistência e validade desses dados, será preciso parametrizar o sistema por coligada. O parâmetro a ser marcado está em Contas a Pagar | Lançamentos | Inclusão a Pagar | Consiste IPTE/Código de Barras. Na configuração do valores opcionais será possível definir para cada um, que tenha ação diferente de "Nada", se o mesmo afeta o cálculo sobre o lançamento que será comparado ao valor lido do IPTE.

Observações:

* Se um lançamento um estiver cancelado e possuir IPTE o sistema fará a validação do lançamento cancelado e permitirá a cópia e inclusão de um novo com o mesmo IPTE, mas somente se o lançamento de origem estiver cancelado.

* A validação do valor é feita sobre o campo Valor Original do lançamento financeiro, descontadas as retenções, o Valor de INSS do Empregado e o Valor do IRRF, além de serem acrescentados ou descontados os valores opcionais parametrizados. Os valores de Juros, Multa, Desconto, Capitalização e Valores de Integração não são considerados na validação do valor para aumento ou dedução do Valor Original. Caso exista um valor a ser considerado que não se trate de retenções ou impostos, ele deve ser informado nos campos de valores opcionais.

Número da Autenticação

Este campo só será apresentado para lançamentos a Pagar e será  utilizado para gravar o número da Autenticação Bancária/Protocolo de pagamento eletrônico, cujo banco siga o Padrão CNAB240 da FEBRABAN, ou arquivos do Banco Itaú, Banco do Brasil, Caixa Econômica Federal ou Santander.

Os dados deste campo é apresentado no Segmento Z, posição 79 a 103 (conforme padrão do layout CNAB240 da FEBRABAN), do arquivo de retorno bancário e posição 15 a 78 do mesmo segmento.

O carregamento dos dados para esse campo no sistema dependerá da forma de retorno selecionado no sistema no momento da importação do arquivo. (Retorno de Pagamento, que atende todos os bancos com layout próprio e Retorno de Pagamento cnab240 que é padrão febraban).

QR-Code PIX

Este campo será apresentando para lançamentos a Pagar e será utilizado para gravar o número da leitura do QR-Code do boleto, caso utilize.

Caso a forma de pagamento do Dados Bancário do cliente/fornecedor seja "PIX QR-Code", o QR-Code PIX será obrigatório para geração do borderô
