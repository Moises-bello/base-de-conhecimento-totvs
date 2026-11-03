---
article_id: 360061193954
category: SIGAEST - CUSTOS
content_hash: 3ed48fc36206bfccea7ff2439cd23ac739c1517e55ed1b6c3a5c0e790b5b2d1a
fetched_at: '2026-06-28T22:39:02.422887+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - Como alterar o custo de uma devolução
  de venda ou compra?
type: support-article
updated_at: '2025-10-10T11:25:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360061193954-Cross-Segmento-Backoffice-Linha-Protheus-Como-alterar-o-custo-de-uma-devolu%C3%A7%C3%A3o-de-venda-ou-compra
---

O Protheus permite alterar o custo em notas de devolução de venda ou compra via parâmetros MV\_CUSTDEV (para devolução de vendas) e MV\_ADEVCOM (para devolução de compras). MV\_CUSTDEV define se o custo da devolução será o atual ou da nota de origem, enquanto MV\_ADEVCOM ajusta custos negativos na devolução de compras em casos especificos de saldo negativo na devolução. Para custos específicos, é possível usar pontos de entrada na rotina MATA330 com suporte de desenvolvedor.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34605818052119) Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**  
Como eu posso alterar, o custo de uma nota de devolução de venda ou um nota de devolução de compra?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

Por alguma razão interna da empresa, existe a necessidade de que o custo de uma nota de devolução de compra ou de vendas, seja diferente o da nota de origem.

**Esse parametro não trata outros tipos de devoluções**, somente **Compra** e **Venda**, como por exemplo, a devolução de uma remessa, não é considerado, pois existe amarração com o poder de terceiros, e tudo que saiu com X deve voltar com X.

Como sugestão, poderá verificar o ponto de entrada **A103CUST - Manipula Custo de Entrada**, caso desejar buscar o custo atual de terceiros, mas ter ciencia que isso pode acarretar divergencia, porque terceiro tudo saia a X tem que voltar a X.  
Link: <http://tdn.totvs.com/display/PROT/A103CUST+-+Manipula+Custo+de+Entrada>   
  
Pontos de entrada disponíveis no MATA103:   
<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006469332-MP-SIGACOM-Pontos-de-entrada-do-Documento-de-Entrada-MATA103>

Hoje o sistema Protheus tem duas tratativas, para os dois cenários apresentados, através da utilização de parâmetros, de forma nativa.

**Primeiro, precisamos ter conhecimento que:** **Se é uma nota de devolução, porque eu quero que o custo seja diferente da nota de origem?**

Entendido o conceito, se deseja muda-lo, segue como efetuar:

**Devolução de Vendas:**

Existe o parâmetro **MV\_CUSTDEV:**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/13199448321815)**

tem funcionalidade para as notas de devolução de **vendas**.

Define se no recalculo do custo médio deverá considerar:  
-custo atual (T) ou o custo.  
-custo Origem (F) para as notas de devolução.  
A alteração deste parâmetro define de qual será a origem do custo da **devolução de vendas.**

**Exemplo hipotético:**

Dia 10/01/2023 foi efetuado a venda do produto A001, a um custo de 100 reais (D2\_CUSTO1).

Mas ao decorrer dos dias e ou períodos, o custo desse produto não é mais 100 e sim 150.

Então, através do parâmetro, você pode definir, se "todas" a notas de devolução de venda, devem ser custeadas com o valor de custo da "Origem" ou então o custo "Atual".

### **Nota:**

Toda devolução de nota fiscal de venda, precisa ter obrigatoriamente o campo D1\_NFORI preenchido com a nota fiscal de origem para que o sistema entenda e faça a amarração, vice e versa!!!.

**Devolução de Compras:**

Existe o parâmetro **MV\_ADEVCOM:**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/13199528302231)**

O parâmetro **MV\_ADEVCOM** é utilizado na rotina Recálculo do Custo Médio (MATA330) e efetua ou não o ajuste do custo de devolução de compras quando o custo final de fechamento **(B2\_VFIM1)** estiver com o **valor negativo**. 

Permite ajustar os custos de devoluções de compras quando o saldo final **(B2\_QFIM1)** for menor que o **valor do custo da nota de origem**. Assim, possibilita que o custo não fique negativo. (T=Sim / F= Não).

[Clique aqui e veja o Exemplo detalhado do comportamento MV\_ADEVCOM](https://tdn.totvs.com/x/EuNc)

Para tal, atentar-se a configuração da TES sob o campo **F4\_DEVZERO** 

![](https://centraldeatendimento.totvs.com/hc/article_attachments/13199728487447)

**Por alguma razão:** Eu preciso que o custo da minha devolução seja 999.

Nesse caso, sugerimos avaliar o boletim abaixo, que contem todos os pontos de entrada para execução do custo médio, e validar se algum atende a sua necessidade, mediante um desenvolvedor.

[MP - SIGAEST - MATA330 - Pontos de Entrada da rotina Recálculo do Custo Médio](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003970802-MP-SIGAEST-MATA330-Pontos-de-Entrada-da-rotina-Rec%C3%A1lculo-do-Custo-M%C3%A9dio)

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Custos no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000049222-SIGAEST-CUSTOS)
