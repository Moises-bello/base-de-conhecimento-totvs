---
content_hash: 65a1204fd2f77279bf21aeab880d6487a75d2ae836ffa376945fd158a1150fd5
fetched_at: '2026-06-29T00:09:53.659925+00:00'
page_id: '440854853'
product: rm
source: tdn-rm
title: Eventos S-1200 e S-1210 na contratação de MEI - Microempreendedor Individual
  - Autônomos cadastrados no Financeiro ( a partir da versão 12.1.21)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=440854853
version: 22
---

false

**A partir das Versões:**

* 12.1.22.216
* 12.1.23.143
* 12.1.24

# Objetivo:

---

 O objetivo deste documento é trazer informações de como enviar os eventos S-1200 (Remuneração de trabalhador vinculado ao Regime Geral de Previdência Social) e S-1210 (Pagamentos de Rendimentos do Trabalho) na contratação de MEI - Microempreendedor Individual -Autônomos cadastrados no Financeiro.

---

O manual de orientação do e-Social cita:

“Na contratação de MEI - Microempreendedor Individual, **quando este prestar serviços de hidráulica, eletricidade, pintura, alvenaria, carpintaria e de manutenção ou reparo de veículos**, a pessoas jurídicas, o contratante deverá enquadrá-lo na categoria 741 da Tabela 1 – Categoria de Trabalhadores. Neste caso, o MEI deve ser tratado como contribuinte individual, sem sofrer, no entanto, a retenção da contribuição previdenciária devida por esta espécie de segurado, e ser identificado pelo CPF e NIS. Nos demais casos de contratação de MEI por pessoa jurídica, o contratante nada informará no eSocial.”

**Observação:**Existem dois itens no texto acima que devem ser destacados:

01) **“... sem sofrer, no entanto, a retenção da contribuição previdenciária devida por esta espécie de segurado”** – No lançamento financeiro do cliente fornecedor não deverá haver valor para cálculo do desconto do segurado.

02) **“... e ser identificado pelo CPF e NIS. Nos demais casos de contratação de MEI por pessoa jurídica, o contratante nada informará no eSocial.”** – Será gerado o S-1200 para o cliente fornecedor que estiver marcado como pessoa física com CPF e NIS cadastrados ou  cliente fornecedor que estiver marcado como pessoa jurídica com o porte da empresa MEI - Microempreendedor Individual com CPF no campo complementar e NIS cadastrados.

1true1MEI - Autônomos cadastrados no Financeiro - Pessoa FísicaMEI - Microempreendedor Individual - Autônomos cadastrados no Financeiro - Pessoa Física

Passos para o envio das informações para o eSocial:

 No cliente fornecedor preencher os campos:

**Observação: a partir da versão 12.1.25.00, será disponibilizado o anexo do eSocial, que irá substituir o item Integrações | eSocial**

Informar o valor original

Em tributos clicar para calcular valores de IRRF e INSS

 Entrar em Exibir Dados para Cálculo do INSS

 Zerar a Base (Valor) para cálculo do INSS do Empregado

Clicar no cálculo para zerar o valor calculado anteriormente

Após salvar não haverá valor a ser informado a título de desconto de INSS segurado

Para a geração do S-1210 - Pagamentos de Rendimentos do Trabalho o lançamento financeiro do cliente fornecedor deve estar baixado

No parametrizador deve existir eventos previamente cadastrados para serem informados no eSocial

Será gerado S-1200 - Remuneração do Trabalhador da seguinte forma:

Será gerado S-1210 - Pagamentos de Rendimentos do Trabalho da seguinte forma:

true1MEI - Autônomos cadastrados no Financeiro - Pessoa JurídicaMEI - Microempreendedor Individual - Autônomos cadastrados no Financeiro - Pessoa Jurídica

Passos para o envio das informações para o eSocial:

Crie o campo complementar no cliente fornecedor com os seguintes dados abaixo:

Nome da coluna: CPFCOMPLEMENTAR

Descrição: CPFCOMPLEMENTAR

Tamanho:11

Tipo: Alfanumérico

**Observação: a partir da versão 12.1.25.00, será disponibilizado o anexo do eSocial, que irá substituir o campo complementar.**

 No cliente fornecedor preencher os campos:

**Observação: a partir da versão 12.1.25.00, será disponibilizado o anexo do eSocial, que irá substituir o item Integrações | eSocial**

Informar o valor original

Em tributos clicar para calcular valores de IRRF

Para a geração do S-1210 - Pagamentos de Rendimentos do Trabalho o lançamento financeiro do cliente fornecedor deve estar baixado

No parametrizador deve existir eventos previamente cadastrados para serem informados no eSocial

Será gerado S-1200 - Remuneração do Trabalhador da seguinte forma:

Será gerado S-1210 - Pagamentos de Rendimentos do Trabalho da seguinte forma:
