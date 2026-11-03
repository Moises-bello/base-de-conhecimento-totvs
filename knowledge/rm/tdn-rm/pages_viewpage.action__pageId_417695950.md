---
content_hash: 1689431a4ffa84a54a092d1e9ff6af614d40716c2dcc1b2b899b11ce0b11db81
fetched_at: '2026-06-29T00:09:12.348479+00:00'
page_id: '417695950'
product: rm
source: tdn-rm
title: Eventos S-1200 e S-1210 na contratação de MEI - Microempreendedor Individual
  - Autônomos cadastrados no Financeiro
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=417695950
version: 6
---

# Objetivo:

---

       O objetivo deste documento é trazer informações de como enviar os eventos S-1200 (Remuneração de trabalhador vinculado ao Regime Geral de Previdência Social) e S-1210 (Pagamentos de Rendimentos do Trabalho) na contratação de MEI - Microempreendedor Individual -Autônomos cadastrados no Financeiro.

---

O manual de orientação do e-Social cita:

“Na contratação de MEI - Microempreendedor Individual, **quando este prestar serviços de hidráulica, eletricidade, pintura, alvenaria, carpintaria e de manutenção ou reparo de veículos**, a pessoas jurídicas, o contratante deverá enquadrá-lo na categoria 741 da Tabela 1 – Categoria de Trabalhadores. Neste caso, o MEI deve ser tratado como contribuinte individual, sem sofrer, no entanto, a retenção da contribuição previdenciária devida por esta espécie de segurado, e ser identificado pelo CPF e NIS. Nos demais casos de contratação de MEI por pessoa jurídica, o contratante nada informará no eSocial.”

**Observação:**Existem dois itens no texto acima que devem ser destacados:

01) **“... sem sofrer, no entanto, a retenção da contribuição previdenciária devida por esta espécie de segurado”** – No lançamento financeiro do cliente fornecedor não deverá haver valor para cálculo do desconto do segurado.

02) **“... e ser identificado pelo CPF e NIS. Nos demais casos de contratação de MEI por pessoa jurídica, o contratante nada informará no eSocial.”** – Será gerado o S-1200 para o cliente fornecedor que estiver marcado como pessoa física com CPF e NIS cadastrados.

Passos para o envio das informações para o eSocial:

Criar um campo complementar de cliente fornecedor com o CODCATEGORIAESOCIAL – para registro do código da categoria do eSocial com o tipo inteiro.

 No cliente fornecedor preencher os campos:

No lançamento financeiro do cliente fornecedor deve estar com baixa importante para a geração do S-1210 - Pagamentos de Rendimentos do Trabalho

Informar o valor original

Em tributos clicar para calcular valores de IRRF e INSS

 Entrar em Exibir Dados para Cálculo do INSS

 Zerar a Base (Valor) para cálculo do INSS do Empregado

Clicar no cálculo para zerar o valor calculado anteriormente

Após salvar não haverá valor a ser informado a título de desconto de INSS segurado

No parametrizador deve existir eventos previamente cadastrados para serem informados no eSocial

Será gerado S-1200 - Remuneração do Trabalhador da seguinte forma:

Será gerado S-1210 - Pagamentos de Rendimentos do Trabalho da seguinte forma:

falsefalse

**Produto:** Folha de Pagamento

false

**Rotina:** eSocial

false

**Versões:**

|  |
| --- |
| 12.1.20 |
| 12.1.19 |

falsefalse

**Status:** Finalizado

false

**Data:**

false

**Autor:**
