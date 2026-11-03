---
content_hash: 1deeafe86a42ca037f55ec2bcf927e566267c4b30b9450e0c3b6d1b37f4728f2
fetched_at: '2026-06-29T00:09:18.687618+00:00'
page_id: '421388749'
product: rm
source: tdn-rm
title: Processos específicos para Geração do Nosso Número
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421388749
version: 3
---

**Banco Cooperativo do Brasil S.A. – BANCOOB – 756**

Para gerar o nosso número é necessário preencher o campo "Código do Cedente" e o "Dígito do Cedente", que estão disponíveis no cadastro de conta corrente.  
Caso o campo "Dígito do Cedente" não esteja preenchido, o sistema não irá considerar o último dígito do campo "Código do Cedente" como dígito. O sistema irá considerar "0" (Zero).

**Banco Bilbao Vizcaya Argentaria Brasil S.A. – 641**

Para gerar o nosso número é necessário preencher o campo "Código do Cedente" e o "Dígito do Cedente", que estão disponíveis no cadastro de conta corrente.  
Caso o campo "Dígito do Cedente" não esteja preenchido, o sistema não irá considerar o último dígito do campo "Código do Cedente" como dígito. O sistema irá considerar "0" (Zero).

**HSBC Bank Brasil S.A. – 399 – Banco Múltiplo**

O campo "Tipo de Cobrança" deve ser preenchido para identificar o tipo de cobrança do título.  
Para cobrança "Não Registrada" existem duas modalidades para o cálculo do Nosso Número. Modalidade "CNR" e modalidade "CNR Fácil".   
Para utilizar a modalidade "CRN" é preciso preencher o campo "Tamanho do Nosso Número" com o valor "13". O campo "Tamanho do Nosso Número" se encontra no Anexo "Layout Bancário" dentro do cadastro do banco HSBC.  
Para utilizar a modalidade "CRN Fácil" é preciso preencher o campo "Tamanho do Nosso Número" com o valor "6". O campo "Tamanho do Nosso Número" se encontra no Anexo "Layout Bancário" dentro do cadastro do banco HSBC.  
Caso o campo "Tamanho do Nosso Número" não esteja preenchido com os valores "6" ou "13" será apresentado um erro informando que não é possível gerar o Nosso Número.  
O banco HSBC informa que o nosso número pode ter até 6 ou 13 dígitos, dependendo da modalidade. Informando por exemplo "13" no campo "Tamanho do Nosso Número", não quer dizer que o nosso número terá 13 dígitos.  
O dígito informado no campo "Tamanho do Nosso Número" Serve somente para controle de qual modalidade está sendo utilizada.

**Banco Rural S.A. – 453**

O campo "Código do Cedente" não será mais utilizado para informar os dados para a geração do nosso número. Para gerar o nosso número de maneira correta preencha os campos do cadastro de "Conta Corrente" corretamente.  
Foi criado o campo "Outros Dados / Tipo de Conta" na aba "Dados Adicionais" do cadastro de "Conta Corrente". Esse campo é de preenchimento obrigatório na geração de nosso número do banco Rural. Para saber como preencher esse campo consulte o manual do banco.

**Banco Santander Banespa – 033**

O banco Banespa foi adquirido pelo Santander. Os antigos clientes do Banespa ainda estão utilizando o layout de geração do "Nosso Número" de acordo com a especificação do antigo Banespa. Portanto é preciso configurar a geração do nosso número do Santander, para que seja utilizado o modelo antigo do Banespa.  
O campo "Tamanho do Nosso Número" no anexo "Layout Bancário" deve ser usado para informar a quantidade de dígitos, somente do número seqüencial do Nosso Número.  
 Este campo não está associado ao tamanho final do "Nosso Número". Sendo assim, o banco Banespa possui um "Nosso Número" onde a quantidade de dígitos do seqüencial é "7", e o banco Santander também possui o seqüencial com "7" dígitos. Mas para diferenciá-los o "Nosso Número" do banco Santander deverá ser informado no campo "Tamanho do Nosso Número" com "8" dígitos, e não "7". Esse que será informando quando o "Nosso Número" a ser gerado for o do banco Banespa.  
 Mesmo o "Tamanho do Nosso Número" configurado com "8" dígitos, ao gerar o "Nosso Número" do Santander o mesmo terá somente "7" dígitos no seqüencial.  
O Santander possui outro modelo de "Nosso Número" com o seqüencial de "12" dígitos. Esse será considerado quando o "Tamanho do Nosso Número" for diferente de "7' e "8".

**Banco Itaú S.A. – 341**

O código da "Agência" utilizado para o cálculo do dígito do Nosso Número é composto por "quatro" caracteres, se for vinculada uma agência na Conta/Caixa que possua o código com mais de quatro caracteres o sistema só considera os quatro caracteres da esquerda para a direita.  
O código do "Cedente" utilizado para o cálculo do dígito do Nosso Número é composto por "cinco" caracteres, se for vinculada uma Conta Corrente na Conta/Caixa que possua o código do cedente com mais de cinco caracteres o sistema só considera os cinco caracteres da esquerda para a direita.  
O "Número do Documento" utilizado para o cálculo do dígito do Nosso Número é composto por "oito" caracteres, se for informado um número do documento que possua mais de oito caracteres o sistema só considera os oito caracteres da direita para a esquerda.  
Para carteira 198, é através da função de fórmula DAC198ITAU que será calculado o dígito verificador do NOSSONUMERO.
