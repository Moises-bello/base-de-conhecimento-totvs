---
article_id: 360042778873
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 8877289b9b7e4fa5d59c90aa4f224276bf85799c897cec0edf3f5b91a09020e8
fetched_at: '2026-06-28T22:38:40.020728+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Recálculo do preço de venda
  no Pedido de vendas (MATA410)
type: support-article
updated_at: '2026-03-03T12:07:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360042778873-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Rec%C3%A1lculo-do-pre%C3%A7o-de-venda-no-Pedido-de-vendas-MATA410
---

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7492068256279)Tempo aproximado para leitura: **00:05:00 min**

**Ocorrência**  
No módulo Faturamento, sempre que alterada a tabela de preços, a condição de pagamento, quantidade ou incluído um novo produto no pedido, os preços de venda podem ser recalculados?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - A partir da versão 12  
  
**Causa**  
Por padrão o desconto no Pedido de Venda é aplicado sempre sobre o Preço de Lista (C6\_PRUNIT) para se obter o Valor Unitário (C6\_PRCVEN) já com desconto. Quando alteradas informações no pedido de vendas (incluindo a quantidade), o sistema aciona a função interna de Recálculo do campo que valida o Preço de Tabela menos os Descontos aplicados.  
  
**Solução**  
Os parâmetros envolvidos no comportamento de recálculo da rotina de pedidos de venda são:

1. **MV\_ALTPREC** (Alteração dos preços dos itens do PV.)

**T** - Sempre altera (padrão);

**L** - Apenas quando não existir lib/fat para o item;

**F** - Apenas se não fat. para o item; deixar em branco - não altera.

2. **MV\_PVRECAL** (Indica se desabilita o recálculo da tabela de preço no pedido de venda.)

**.T.** - Desabilita recálculo;

**.F.** - Habilita recálculo.

3. **MV\_TABCENT** (Indica se a tabela de preços ira respeitar o cliente e a loja de entrega.)

**1** - Sim - respeita;

**2** - Não - não respeita (padrão).

4. **MV\_NDESCTP** (Desconsidera ou não a diferença do preço de lista como desconto)

**.T.** - Desconsidera;

**.F.** - Considera.

5. **MV\_DESCLOT** (Habilita desconto escalável)

**.T.** - Habilitado;

**.F.** - Desabilitado.

**Observação 1**: O recálculo disparado pela alteração de quantidade (C6\_QTDVEN) é um processo nativo da regra de negócio do produto. Não existe um parâmetro que impeça o recálculo especificamente ao alterar a quantidade, pois o sistema precisa validar se o novo volume de itens altera a faixa de preço ou descontos da tabela vinculada.

**Observação 2**: As informações aqui descritas também são válidas para a rotina **Televendas** (**TMKA271**) do módulo Call Center.  
  
**Saiba mais**:

[Atualização de Preço no Pedido de Venda (MATA410 - SIGAFAT)](https://tdn.totvs.com/x/Rk0AHw)
