---
article_id: 360040089154
category: Financeiro - Contas a Pagar
content_hash: 9ca8cd4938bfe003e7fd2876e7d747f95c2bd80f8742470b0a9388bc99c1992f
fetched_at: '2026-06-28T22:38:09.970148+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: MP - SIGAFIN – FINA080 – Criação de critério de conversão contábil para o LP
  530
type: support-article
updated_at: '2021-04-28T15:18:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360040089154-MP-SIGAFIN-FINA080-Cria%C3%A7%C3%A3o-de-crit%C3%A9rio-de-convers%C3%A3o-cont%C3%A1bil-para-o-LP-530
---

**Ocorrência**Como fazer o LP 530 respeitar a configuração do critério de conversão após criação de validação no plano de contas  
   
 **Ambiente**Microsiga Protheus – Financeiro – A partir da versão 11  
   
 **Causa**Ao baixar o título pela rotina FINA080, ao contabilizar o critério de conversão gerando o conteúdo 15 ao invés de utilizar o critério 13  
   
 **Solução**

1º - Ter o conteúdo do parâmetro MV\_CRITPLN=.T.

2º - Criar um calendário e amarrar a moeda 1 e a moeda 2 (Dolar) no calendário contábil

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360054032833/mceclip0.png)

3º - Na rotina “Plano de contas” criar uma conta analítica amarrada a uma conta sintética. Criar uma conta debito e uma crédito onde cada conta terá a sua sintética.

Segue um exemplo de criação de conta sintética.

![02_sintetica_debito.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360053156554/02_sintetica_debito.jpg)

Na aba “Conv.Moeda” alterar os campos abaixo para  “ 3-Mensal”

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360053156594/mceclip0.png)

Criação da conta analítica amarrada a conta sintética

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360054033073/mceclip1.png)

Na aba “Conv.Moeda” alterar os campos abaixo para  “ 3-Mensal”

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360054033093/mceclip2.png)

4º - Na rotina lançamento padrão CTBA080 segue um exemplo de criação do lançamento padrão 530.

Segue exemplo da aba “Cadastro”

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360053156634/mceclip3.png)

Segue exemplo da aba “Entidades”

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360054033253/mceclip4.png)

Segue exemplo da aba “Valores”

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360053156734/mceclip5.png)

5º - Criação do Câmbio

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360054033293/mceclip6.png)

Criar o câmbio para todos os meses do ano que estiver fazendo a contabilização.

No exemplo abaixo sempre irei selecionar o último dia do mês e inserir a taxa do câmbio onde no meu exemplo foi inserido a taxa=2,000 para o Dolar

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360053156774/mceclip7.png)

Segue um exemplo do cadastro de fevereiro, onde pegamos a data do último dia do mês

![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360053156794/mceclip8.png)

Após cadastrar todos os meses do ano

![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360053156814/mceclip9.png)

6º - Baixa o título onde a contabilização será online

![mceclip10.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360053156854/mceclip10.png)

Na tela de contabilização o critério de conversão será 13

![mceclip11.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360054033313/mceclip11.png)

Outras documentações do mesmo assunto:

[CTB0021\_Critérios\_de\_conversão\_da\_Contabilidade\_Gerencial](https://tdn.totvs.com/pages/releaseview.action?pageId=233753234)
