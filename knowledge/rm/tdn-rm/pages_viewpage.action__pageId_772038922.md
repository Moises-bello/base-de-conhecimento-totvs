---
content_hash: a5719ea9148a279f2d9df0daa04c4c53f84aa15bb6462880012def2cafd99385
fetched_at: '2026-06-29T00:11:36.076655+00:00'
page_id: '772038922'
product: rm
source: tdn-rm
title: TCGI - Comissão - Metas - Cadastro
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=772038922
version: 10
---

Primeiro passo é liberar o perfil do usuário para usar o cadastro de Meta da Comissão ( 01.01.03.03 )

O cadastro tem como objetivo definir o tipo da meta da comissão e os itens da faixa de prêmios.

Tipo de Meta:

1. Quantidade de Imóveis:  O prêmio será pago por **quantidade** comercializada de imóveis em uma competência.
2. Valor de Imóveis: O prêmio será pago por **valor** comercializada de imóveis em uma competência.

Tipo de Cálculo da Meta

1. Todas as Coligadas: A meta é contabilizada em todas as coligadas com imóveis comercializados.
2. Coligada da Comissão: A meta é contabilizada apenas na coligada que a comissão foi gerada.
3. Empreendimento da Comissão: A meta é contabilizada apenas no empreendimento que a comissão foi gerada.
4. Meta da Comissão: A meta é contabilizada apenas nas comissões que tem a mesma meta cadastrada.

Tipo de Prêmio:

1. Percentual: Determina um percentual a ser pago por metas batidas na comissão.
2. Valor Fixo: Determina um valor fixo a ser pago por metas batidas na comissão.
3. Valor Fórmula: Determina um valor através de fórmulas que pode ser customizado para pagamento de metas batidas na comissão.

Código Fórmula Valida Meta

* Fórmula para validar se uma meta pode ser executada em apenas determinas condições .

Exemplos:

1. O **Corretor  A** tem uma meta **estabelecida de 12 unidades** vendidas, mas dessas 12, pelo menos **7 tem que ser do Empreendimento Norte** e **5 do Empreendimento Sul**. Ele **não** teria direito a Meta *vendendo apenas 12 unidades do Empreendimento Norte.*
2. Mesmo exemplo aplicaria para o **Corretor B**, que somente ganharia a meta em caso de venda do número determinado do Empreendimento **TOTVS Leste e TOTVS Oeste , chegando num total de 16 unidades vendidas**.

Número de Parcelas

* se deixar 0 vai pegar o numero de parcelas configurado da comissão do comissionado.

A meta poderá ser associada ao Cadastro de Regra ou de Regra da Modalidade
