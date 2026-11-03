---
article_id: 1500002838202
category: SIGAEST - LEGAIS
content_hash: 9f17155ec2c83227b5bbc6f0a8884b466c9ed903a598fbd25734d886817b7c9b
fetched_at: '2026-06-28T22:38:51.944890+00:00'
product: protheus
section_id: 1500001538941
source: central-protheus
title: MP - SIGAEST - No Registro K200 do Bloco K os produtos que tem saldo de terceiro,
  em terceiro e próprio não está gerando "em estoque próprio"
type: support-article
updated_at: '2021-04-28T15:12:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500002838202-MP-SIGAEST-No-Registro-K200-do-Bloco-K-os-produtos-que-tem-saldo-de-terceiro-em-terceiro-e-pr%C3%B3prio-n%C3%A3o-est%C3%A1-gerando-em-estoque-pr%C3%B3prio
---

**Dúvida**Ao gerar o SPEDFISCAL ou MATR241, verifico que alguns produtos que tenho na condição de estoque próprio, de terceiro e em terceiro, está saindo no K200 apenas os "de terceiros" e "em terceiros", o "estoque próprio" não está indo para o K200. O que fazer para resolver?  
  
**Ambiente**Microsiga Protheus - Estoque/Custos - A partir da versão 12.1.17  
  
**Solução**Neste tipo de problema normalmente a causa-raiz está relacionado ao TES utilizado nos movimentos de poder de terceiros (normalmente quando envia para o terceiro). Vamos a um exemplo:

**1° - Nosso produto PA17 tem Saldo Inicial (MATA220) de 3 unidades;**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500002674241/mceclip0.png)

**2° - Recebemos uma remessa de 1 unidade de um terceiro (De terceiro para o meu poder) utilizando TES com** **F4\_ESTOQUE = S** e **F4\_PODER3 = R**;

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360103675493/mceclip1.png)

**3° - Note que neste momento o saldo é de 4 unidades, sendo 3 "em estoque próprio" e 1 "de terceiro em meu poder"**;

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500002634942/mceclip2.png)

**4° - Agora, faremos uma remessa para um terceiro das 3 unidades que temos em estoque próprio com uma TES com** **F4\_ESTOQUE = N (não atualiza)** e **F4\_PODER3 = R**;

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360101520934/mceclip3.png)

**5° - Com isso, ficamos com o mesmo saldo anterior. Ou seja, 4 Unidades no total, sendo 3 Em Terceiro e 1 De Terceiros (esse 3 "em terceiros" não tirou do saldo atual porque o movimento** **não atualizou estoque****)**;

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500002635562/mceclip4.png)

**6° - Ao emitir o Relatório do Bloco K (MATR241), veja que o PA57 traz o saldo de 3 Em Terceiros, 1 De Terceiro e não traz nada em Estoque Próprio;**

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360103676293/mceclip5.png)

Concluindo: mesmo que a remessa ao terceiro não movimentou o estoque, para o Bloco K, o saldo foi ao terceiro mesmo assim (é uma regra fiscal). A operação de fazer movimento sem controle de estoque é interna da empresa, porém para o fisco todos os movimentos são computados da forma com que são.

**Saiba mais:**

*[MP - SIGAEST- Como definir um tipo de produto que não seja padrão do sistema para que seja considerado no Bloco K (K200)?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033136554)*

*[MP - SIGAEST - Quais são as tabelas relacionadas para composição do saldo do registro K200 no bloco K?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021629091)*

*[MP - SIGAEST - Bloco K - Saldo negativo de alguns produtos no Registro K200](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360061935253)*

[*Clique aqui e veja mais artigos sobre Legais/Fiscais no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000033001-SIGAEST-LEGAIS)
