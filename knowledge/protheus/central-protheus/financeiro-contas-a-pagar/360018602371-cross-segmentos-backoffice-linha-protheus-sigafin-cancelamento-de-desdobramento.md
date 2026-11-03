---
article_id: 360018602371
category: Financeiro - Contas a Pagar
content_hash: ab15d591db5fba688a7ecc21a7b2943ee088bfc35e70d6b1f0899ff1c1f64555
fetched_at: '2026-06-28T22:38:07.053560+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Cancelamento de Desdobramento
type: support-article
updated_at: '2026-05-13T16:52:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018602371-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Cancelamento-de-Desdobramento
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32460334094231)**Tempo aproximado para leitura: **00:03:00 min**  
  
**Dúvida**  
Como cancelar um título com desdobramento do contas a pagar ou receber?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões.  
  
**Solução**

Quando é realizado o desdobramento de um título, o sistema gera um título totalizador, com o valor total já baixado, e cria as parcelas correspondentes (títulos desdobrados) em aberto. Esse procedimento visa garantir a rastreabilidade das informações, especialmente em processos de cancelamento do desdobramento.

Para controlar esse comportamento, foi disponibilizado o parâmetro **MV\_NRASDSD**, responsável por definir se a inclusão de títulos via desdobramento seguirá o processo antigo ou o processo atual do sistema.

**MV\_NRASDSD com conteúdo ".T." :** O desdobramento ocorre conforme o processo antigo. Nesse cenário:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37722506138903)

* O título originador é excluído após o desdobramento;
* As parcelas desdobradas podem ser excluídas manualmente;
* Não há rastreabilidade do vínculo entre o título original e os desdobramentos.

Para realizar a exclusão, acesse as funções do Contas a Receber ou Contas a Pagar, selecione o título desejado e, em seguida, utilize a opção de exclusão. O processo deve ser realizado individualmente, excluindo um título por vez. **Exemplo: em Funções do Contas a Receber:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40444968839703)

Caso esteja acessando diretamente a rotina do Contas a Receber, basta selecionar o título desejado e clicar em **Outras Ações > Excluir**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40444946910743)

**MV\_NRASDSD com conteúdo ".F." :** O desdobramento ocorre conforme o processo atual, com rastreabilidade, mantendo o título originador como totalizador. Nesse cenário:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37722501951127)

* O sistema permite a exclusão das parcelas apenas por meio da exclusão do título original (pai);
* Caso uma ou mais parcelas estejam pagas, ou baixadas, o sistema não permitirá a exclusão do título originador;
* Para cancelar o desdobramento, é necessário cancelar previamente as baixas de **todas** as parcelas (títulos desdobrados) e, somente após isso, realizar o cancelamento do desdobramento por meio do título original.

Neste cenário, é possível realizar o cancelamento do desdobramento pelo **Contas a Pagar** ou **Contas a Receber**, acessando **Outras Ações > Cancelar Desdobramento**.

Pelo menu **Funções**, essa opção não está disponível.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40444968845079)

 **Parâmetro válido para as rotinas de Contas a Pagar e Contas a Receber.**

**Saiba Mais**  
[Desdobramento (FINA050)](https://tdn.totvs.com/pages/viewpage.action?pageId=312159857)

[Para cancelamento do desdobramento do contas a receber, pelo FINA040, segue link abaixo com todos os detalhes:](https://tdn.totvs.com/pages/releaseview.action?pageId=306856119)
