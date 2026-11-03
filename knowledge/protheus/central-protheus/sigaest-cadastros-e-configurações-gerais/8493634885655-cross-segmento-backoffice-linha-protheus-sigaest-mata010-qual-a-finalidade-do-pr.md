---
article_id: 8493634885655
category: SIGAEST - CADASTROS E CONFIGURAÇÕES GERAIS
content_hash: 6bd26ca5b71c7bf09cef207da3a5134e3c4ba450610aa4bb1c458eff48fbe0a0
fetched_at: '2026-06-28T22:39:09.538191+00:00'
product: protheus
section_id: 1500001550022
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA010 - Qual a finalidade
  do produto fantasma?
type: support-article
updated_at: '2022-08-29T14:02:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8493634885655-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA010-Qual-a-finalidade-do-produto-fantasma
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:52 min** **Dúvida**Qual a finalidade do produto fantasma?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**

Um produto identificado como **fantasma** serve como um Kit que aglutina diversos produtos. Este tipo de produto não é produzido nem requisitado, mas sim, os seus componentes.

Esse recurso facilita o cadastro de estruturas que possuem uma série de componentes comuns.

**Exemplo:**

Para fabricar uma série de produtos é necessário utilizar um mesmo kit de 20 parafusos. Assim, ao invés de informar respectivamente os 20 parafusos em cada uma das estruturas, crie um produto fantasma que represente este conjunto de parafusos.

Procedimentos para criar um **produto fantasma**:

1. Cadastrar os produtos principais;  

   **Exemplo:**

   ARMÁRIO A

   ARMÁRIO B

   ARMÁRIO C
2. Cadastrar um produto fantasma que represente os componentes;  
   **Exemplo:** PAR01
3. Cadastrar a estrutura do produto fantasma com os seus componentes;  
   ![](https://tdn.totvs.com/download/attachments/235592323/1.jpg?version=1&modificationDate=1461845596000&api=v2)
4. Na estrutura dos produtos principais, indique apenas o produto fantasma.  
   ![](https://tdn.totvs.com/download/attachments/235592323/2.jpg?version=1&modificationDate=1461845597000&api=v2)

|  |
| --- |
| **Observações:**  Apesar do produto fantasma não ter seu empenho realizado durante a explosão da estrutura na abertura de uma ordem de produção, temos situações nas quais os clientes recebem esse material através de documento fiscal e efetuam o controle de seu estoque, seja por compra, devolução ou remesse de terceiros ou até mesmo por bonificação.  Deste modo, para os clientes que não possuem esse cenário e desejam bloquear a entrada desse tipo de materiais via nota fiscal de entrada, recomendamos que este tratamento seja realizado através de uma validação personalizada nesta rotina, ou que o assunto seja direcionado como sugestão de melhoria para o produto em nossa central colaborativa.    Logo no padrão não podemos deixar bloqueado esse tipo de movimento. |

**Relação do Produto Fantasma com o Bloco K do SPED**

No padrão do Protheus, produtos configurados como Fantasma **não aparecerão no Bloco K do SPED Fiscal**, devido a ser um produto facilitador no qual não tem requisição nem movimentação pura do mesmo, sendo apenas um facilitador de um acumulado de produtos.

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Cadastros e Configurações Gerais no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550022-SIGAEST-CADASTROS-E-CONFIGURA%C3%87%C3%95ES-GERAIS)
