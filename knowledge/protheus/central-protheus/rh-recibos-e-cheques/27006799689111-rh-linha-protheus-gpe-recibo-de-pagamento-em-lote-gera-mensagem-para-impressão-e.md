---
article_id: 27006799689111
category: RH - Recibos e Cheques
content_hash: a1ede8262cb0adad9be167c67224f3410fd88cdb3751ce9692ccd08e7a9c67d5
fetched_at: '2026-06-28T22:43:29.600293+00:00'
product: protheus
section_id: 360011909573
source: central-protheus
title: RH - Linha Protheus GPE - Recibo de Pagamento em Lote gera mensagem Para impressão
  em lote somente deve ser selecionado 1 matricula
type: support-article
updated_at: '2024-10-11T19:23:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/27006799689111-RH-Linha-Protheus-GPE-Recibo-de-Pagamento-em-Lote-gera-mensagem-Para-impress%C3%A3o-em-lote-somente-deve-ser-selecionado-1-matricula
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27006816440855) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**  
No recibo de pagamento GPER030 ao realizar a geração em Lote sistema emite mensagem:  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/27006799652503)****Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) Gestão de Pessoal - Todas as versões  
  
**Causa**Esse incidente ocorre, pois o preenchimento dos campos Filial De, Filial Até, Matricula De e Matricula Até, precisam ser preenchido igualmente, apontando para o mesmo funcionário e mesma filia. Como a SRA é uma tabela exclusiva por empresa/filial, ao deixar o preenchimento de filial para geração de todas cadastradas no sistema, pode ocorrer de ter a mesma matricula em outras filiais, sendo gerado recibo para ambos os funcionário. Porém a impressão de recibo de pagamento em Lote é para geração de recibo de pagamento de vários período para um único funcionário, por isso a necessidade do preenchimento selecionando uma única filial e uma única matricula.    
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
**passo 1:** Acesse a rotina Recibo de Pagamento GPER030 em **Relatórios > Recibo/Cheques > Recibo de Pagamento**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27006816443287)  
  
**passo 2**: Verifique o preenchimento dos parâmetros dos campos **Filial De, Filial Até, Matricula De e Matricula Até**. Para que estejam selecionados somente uma única filial e única matricula.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27006799654551)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27006816449303)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27006816450455)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27006816450967)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27006816452887)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27006799660311)

**passo 3:** Após ajuste do preenchimento dos parâmetros clique em **Ok**. E o recibo de pagamento dos períodos selecionado para o funcionário serão gerados.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27006799662103)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27006799666071)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27006799673879)

**Saiba mais:**

[RH - Recibos e Cheques](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360011909573-RH-Recibos-e-Cheques)
