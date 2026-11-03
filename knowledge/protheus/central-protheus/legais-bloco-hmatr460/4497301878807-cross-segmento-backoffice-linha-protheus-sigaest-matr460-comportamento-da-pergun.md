---
article_id: 4497301878807
category: LEGAIS - BLOCO H/MATR460
content_hash: 726250a5c6bdd98ecae18ad10bfc2a581d463d086a21fcc2ca781341eb846ba4
fetched_at: '2026-06-28T22:42:15.101682+00:00'
product: protheus
section_id: 1500001538741
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATR460 - Comportamento
  da pergunta "Prods c/ Saldo Zerado" no P7
type: support-article
updated_at: '2022-02-25T14:32:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4497301878807-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATR460-Comportamento-da-pergunta-Prods-c-Saldo-Zerado-no-P7
---

**Ocorrência**

Esta documentação visa explicar o comportamento deste pergunte e alguns cenários em que ele pode causar dúvidas

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

A pergunta Prods c/ Saldo Zerado refere-se a exibir ou não produtos com saldo físico zerado. Essa pergunta deve ser parametrizada com muitos critérios, principalmente na questão da filtragem dos armazéns que serão considerados no relatório.

**1° Cenário - P7 imprimindo "Estoque Inexistente" com a pergunta "Prods c/ Saldo Zerado" = Não, porém quando parametrizada = Sim ele traz o saldo zerado e o custo do produto**

Normalmente os usuários parametrizam o P7 para todos os armazéns. Quando ele deixa o pergunte de saldo zerado = Não e o P7 imprime "Estoque Inexistente" muito provavelmente isso ocorre porque todos os armazéns estão com saldo físico zerado, logo, quando é desligada essa pergunta, o P7 não pode imprimir saldo físico zero, então não vai imprimir nem o saldo financeiro (custo).

Exemplo:

Produto: PA251

**SB2**:

![](https://totvssuporte.zendesk.com/attachments/token/nFTyzBKSMllUOAU6L410DO1I1/?name=inline1454752602.png)​

**P7 com a pergunta "Lista Saldo Zerado" = Não**

![](https://totvssuporte.zendesk.com/attachments/token/eK5P9bT3b2AqYE2mt8u5wwP3S/?name=inline-1755807707.png)​

![](https://totvssuporte.zendesk.com/attachments/token/tH5KSsEx5uJeCdQ89oP3WXdyC/?name=inline-566579417.png)​

Estoque inexistente porque de fato nos armazéns do produto (01 e 02) o saldo físico é zero e deixamos para não listar produto com saldo zerado

**P7 com a pergunta "Lista Saldo Zerado" = Sim**

![](https://totvssuporte.zendesk.com/attachments/token/CybmmgqQBJ9Xh1sigbzjAxRsn/?name=inline888185543.png)​

![](https://totvssuporte.zendesk.com/attachments/token/iu7GLaeV21jj4tzOmc1QxtsIY/?name=inline-909248330.png)​

Neste caso, trouxe o saldo físico zero e o custo do armazém 02. Se o armazém 01 tivesse qualquer outro custo, também seria considerado em sua composição.

**2° Cenário - P7 está considerando custo de um armazém que o saldo físico está zerado com a pergunta "Prods c/ Saldo Zerado" = Não**

O comportamento padrão do P7 neste caso é que imprima o custo de um armazém com saldo físico zerado. Vamos exemplificar abaixo o porquê deste comportamento.

**SB2**:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4496838990231/mceclip0.png)

**P7 com a pergunta "Lista Saldo Zerado" = Não**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4496903919383/mceclip1.png)

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4496917288727/mceclip2.png)

Perceba que o P7 está parametrizado com todos os armazéns, então o relatório está analisando o custo por filial (já que está olhando todos os armazéns). **Nesse caso, é coerente que mesmo que ele não imprima o saldo físico zerado do armazém 02, ele considere o custo de -40 uma vez que todos os armazéns estão sendo considerados na composição (e seu custo deve ser considerado).**

**P7 com a pergunta "Lista Saldo Zerado" = Sim**

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4496991676951/mceclip3.png)

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4497015591191/mceclip4.png)

Vemos que o comportamento é o mesmo, já que o que está "mandando" é a filtragem de todos os armazéns, como temos um com saldo e um sem saldo, ele vai trazer a somatória (100 do armazém 01).

**P7 com a pergunta "Lista Saldo Zerado" = Sim e Armazém De/Até 01**

**![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4497074900759/mceclip5.png)**

**![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4497059903127/mceclip6.png)**

Neste caso ele imprimiu o custo de R$ 1000,00 porque amarramos apenas o Armazém 01.

**P7 com a pergunta "Lista Saldo Zerado" = Sim e Armazém De/Até 02**

**![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4497088318231/mceclip7.png)**

**![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4497098900375/mceclip8.png)**

Neste caso, amarrando apenas o armazém 02 e listando saldo zerado, ele vai imprimir o saldo zerado e o custo apenas do armazém 02.

**P7 com a pergunta "Lista Saldo Zerado" = Não e Armazém De/Até 02**

**![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4497182236951/mceclip9.png)**

**![mceclip10.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4497185970327/mceclip10.png)**

O "Estoque Inexistente" é pelo fato de que não há saldo fisico no armazém 02, então realmente não vai trazer o saldo financeiro dele.

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre o relatório P7 (MATR460)*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538741-LEGAIS-BLOCO-H-MATR460)
