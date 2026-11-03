---
article_id: 14005233167895
category: SIGAACD - Automação e Coleta de Dados
content_hash: 573f6854a4312252e4a5a0eafb4609a21adde06c06849783d8876bcefb944917
fetched_at: '2026-06-28T22:39:13.806614+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - Relatório de ordem
  de separação ACDA100R não imprime o código de barras
type: support-article
updated_at: '2026-02-24T19:22:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/14005233167895-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Relat%C3%B3rio-de-ordem-de-separa%C3%A7%C3%A3o-ACDA100R-n%C3%A3o-imprime-o-c%C3%B3digo-de-barras
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38613941655959) Tempo aproximado para leitura: **00:01:25min**  
  
**Dúvida**

Dentro da rotina ACDA100 - Ordem de Separação no botão "Imprimir" o sistema gera um relatório de ordem de separação ACDA100R:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14004865195287)

Porém o mesmo não respeita o pergunte "imprime Cod. Barras?":

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14004921777559)

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**

O relatório ACDA100R utiliza um componente mais antigo, na qual a impressão de código de barras não estava mais sendo suportado.  
   
Para disponibilizar aos clientes a mesma funcionalidade, foi criado um novo relatório (ACDR100) que utiliza outro componente e no qual a impressão do código de barras ocorre da maneira esperada. A decisão sobre qual relatório será utilizado pode ser feita pelo cliente, através do parâmetro MV\_ACDR100.  
   
Para este cenário, recomendamos que o parâmetro seja configurado como .T. para que o relatório seja impresso da forma esperada:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14005128366615)

Após alteração do parâmetro o relatório já apresenta o código:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14005133022359)

Obs.: O campos que é apresentado na coluna OP do **relatório ACDR100 é CB7\_OP**, e não passa em nenhum momento o campo **CB8\_OP.**

Caso deseje para pegar as Op's dos itens, é necessário baixar o fonte do relatório no portal do cliente e customizar.

[Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - ACDA100R - Fonte de relatório para customizar a impressão do relatório de Ordem de Separação](https://centraldeatendimento.totvs.com/hc/pt-br/articles/16765702564887-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-ACDA100R-Fonte-de-relat%C3%B3rio-para-customizar-a-impress%C3%A3o-do-relat%C3%B3rio-de-Ordem-de-Separa%C3%A7%C3%A3o)

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Automação e Coleta de Dados*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550002-SIGAACD-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados)
