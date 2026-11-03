---
article_id: 29586504205591
category: SIGAEST - CUSTOS
content_hash: 0b7ce20aa4e1db95ec35193aebe2c998dbdf7862280dc51518b3a07827f44f06
fetched_at: '2026-06-28T22:39:00.744934+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como é formado o CMV
  - custo medio da mercadoria vendida no Protheus?
type: support-article
updated_at: '2025-03-12T12:25:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/29586504205591-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-%C3%A9-formado-o-CMV-custo-medio-da-mercadoria-vendida-no-Protheus
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29586517955735) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**Como é formado o **CMV** da mercadoria? como é calculado o **CMV** no protheus, como é apurado esse calculo?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões  
  
**Solução**O Protheus atua com o calculo sobre a **média ponderada**, ou seja o custo médio **mensal/diario ou sequencial**.

**Saiba mais sobre as apropriações:**

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA330 - Quais são os Métodos de Apropriação para execução do Recálculo do Custo Médio?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033673914-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA330-Quais-s%C3%A3o-os-M%C3%A9todos-de-Apropria%C3%A7%C3%A3o-para-execu%C3%A7%C3%A3o-do-Rec%C3%A1lculo-do-Custo-M%C3%A9dio)

O custo efetivado na nota de saida é calculado de acordo **Médio** da movimentação (**B2\_CM1**) do produto.  
  
**Os casos de varejista ou comercio o CMV e calculado da seguinte forma:**  
-->(+) Saldo anterior (SB9) também conhecido como saldos iniciais  
-->(+) Notas fiscais de compras  
-->(=) A) base de calcalo1 = (Saldo anterior valor + Compras)  
-->(=) B) base de calculo2 = (Saldo anterior quantidade + quantidade compras)  
-->(=) C) Custo Médio = Base de calculo 1 / Base de calculo 2  
  
Esse calculo e efetuado pela rotina de recalculo do custo médio e atualiza o campo **D2\_CUSTO1** que é o **CMV** da operação.  
  
Finalizando, no Protheus o **CMV** é o valor que está no campo do **D2\_CUSTO1**, que é efetivado com base no Custo médio da movimentação **B2\_CM1**  
  
**Formação do custo de saida D2\_CUSTO1.**  
[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como é calculado o campo D2\_CUSTO1 ao efetuar Pedido de Venda?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500005465422-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-%C3%A9-calculado-o-campo-D2-CUSTO1-ao-efetuar-Pedido-de-Venda)  
  
**Método atendido legalmente de acordo IOB**   
<https://tdn.totvs.com/pages/releaseview.action?pageId=789992253>  
  
Em relação a utilização de formulas para rentabilidade da **planilha financeiras/Lucro Bruto/Margem de contribuição/Valor presente**, duvidas podera tratar diretamente com o time "**Protheus Faturamento**".  
<https://tdn.totvs.com/pages/releaseview.action?pageId=266963014>

**O CMV tem outra variaveis que precisam de atenção, como:**

1. O que significa o Custo da Mercadoria Vendida (CMV)?
2. Qual a finalidade do CMV na gestão empresarial?
3. Quais fatores compõem o cálculo do Custo da Mercadoria Vendida?
4. Quais métodos podem ser usados para calcular o CMV?
5. Por que o CMV é um indicador estratégico para o negócio?
6. Existe um valor ideal para o CMV? Como interpretá-lo?
7. De que maneira o CMV pode contribuir para um controle eficiente do estoque?

Neste boletim, abordamos a composição do Custo da Mercadoria Vendida (CMV) apurado e calculado no Protheus.

**Mas qual seria o setor da empresa que trata esse calculo?**

A área responsável por tratar os cálculos do Custo da Mercadoria Vendida (CMV) em uma empresa é, geralmente, o **Setor Contábil e Fiscal**, com possível apoio da **Controladoria**.

O **Setor Contábil** é encarregado de registrar corretamente os custos das mercadorias vendidas, garantindo a conformidade com as normas contábeis e tributárias. Ele assegura que os valores lançados no balanço patrimonial e na demonstração do resultado do exercício (DRE) estejam corretos e refletindo a realidade financeira da empresa.

O **Setor Fiscal**, por sua vez, desempenha um papel essencial na análise tributária do CMV, garantindo que os cálculos considerem corretamente os impostos incidentes, os créditos fiscais e a legislação vigente. Essa área evita inconsistências que possam impactar a apuração de tributos e o cumprimento das obrigações fiscais.

Além disso, em empresas de maior porte, a **Controladoria** pode atuar no acompanhamento e análise estratégica do CMV, avaliando sua variação ao longo do tempo e buscando otimizações que impactem diretamente na lucratividade e na tomada de decisões gerenciais.

Portanto, a **verificação e análise do CMV** na maioria das vezes são responsabilidades compartilhadas entre os setores **Contábil, Fiscal e Controladoria**, garantindo que os valores apurados sejam precisos e alinhados às melhores práticas contábeis e de gestão.

**Saiba mais:**

*[MP - SIGAEST - Como é calculado o campo D1\_CUSTO ao efetuar um Documento de Entrada?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500005383202)*

*[MP - SIGAEST - Como é calculado o campo D2\_CUSTO1 ao efetuar Pedido de Venda?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500005465422)*

*[MP - SIGAEST - Como é calculado o campo D3\_CUSTO1 ao efetuar Movimentos Internos?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500005527161)*

*[Clique aqui e veja mais artigos sobre Custos no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538901-SIGAEST-CUSTOS)*
