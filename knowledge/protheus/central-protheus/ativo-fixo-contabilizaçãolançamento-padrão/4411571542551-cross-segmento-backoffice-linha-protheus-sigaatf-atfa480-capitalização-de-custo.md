---
article_id: 4411571542551
category: Ativo Fixo - Contabilização/Lançamento padrão
content_hash: cbe27f6891968e07d1f5662bd6769b96e8dff9f74ce7e0aca445c6027cc62c83
fetched_at: '2026-06-28T22:41:42.381573+00:00'
product: protheus
section_id: 1500001536421
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGAATF- ATFA480 - Capitalização
  de Custo de Empréstimo '
type: support-article
updated_at: '2021-11-04T13:52:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411571542551-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-ATFA480-Capitaliza%C3%A7%C3%A3o-de-Custo-de-Empr%C3%A9stimo
---

**Dúvida**Capitalização de Custo de Empréstimo (ATFA480)  
  
**Ambiente**Cross Segmento - TOTVS Backoffice Linha Protheus - Ativo Fixo- Todas as versões  
  
**Solução**

Custo de empréstimo são os juros e outros custos que a entidade incorre em conexão com o empréstimo de recursos.   
Um ativo qualificável é um ativo que, necessariamente, demanda um período de tempo substancial para ficar pronto para seu uso ou venda pretendidos.

Pré-requisito:

As configurações definidas a seguir são premissas para a execução do Assistente de Custo de Empréstimo.

1. No Configurador (SIGACFG) acesse Ambientes/Cadastros/Parâmetros (CFGX017). Configure os parâmetros a seguir:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411570973079/mceclip0.png)

2. Ter ativos em andamento com os tipos 03 e 13, classificação Ativo Imobilizado.

3. Ter ativos com a classificação Custo de Transação(T).  
4. Ter executado o Cálculo mensal de depreciação.  
5. Executar o Assistente Custo de Empréstimo (ATFA480 )na mesma data do último calculo de depreciação  
6. Para execução dessa rotina, é preciso que esteja implementado no ambiente a melhoria do Adiantamento Gerencial.

Na rotina ATFA480

![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411586812823/mceclip9.png)

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411571295255/mceclip5.png)

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411577976983/mceclip4.png)

![mceclip10.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411586821271/mceclip10.png)

![mceclip11.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411586827671/mceclip11.png)

Será realizado o cálculo da taxa de capitalização dos bens selecionados.

O custo de capitalização será calculado da seguinte maneira: Taxa de Capitalização = ( a + b -c ) / d .Sendo:  
a = Soma dos juros do período  
b = Soma da amortização do custo de transação  
c = Soma dos rendimentos das aplicações  
d = Saldo dos Contratos de Financiamento

O valor de capitalização será o valor de aquisição do ativo qualificável multiplicado pela taxa de capitalização

Exemplo:

a = 100,00

c = 12

d = 3000,00

(100 - 12)/3000

88/3000= 0,02933

2000,00 (aquisição) x 0,02933 = 58,67

Com os resultados são gerados novos bens, relacionados aos bens selecionados no item 13, com a Classificação E(Custo de Empréstimo).

![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411578217879/mceclip8.png)

A contabilização da inclusão dos bens pode ser feita pelo lançamento padrão 803 –Ativo Fixo -Aquisição–Adiantamento.

**Saiba mais**

[CPC 20: Custos de Empréstimos (IAS 23)](https://tdn.totvs.com/pages/viewpage.action?pageId=63275466)
