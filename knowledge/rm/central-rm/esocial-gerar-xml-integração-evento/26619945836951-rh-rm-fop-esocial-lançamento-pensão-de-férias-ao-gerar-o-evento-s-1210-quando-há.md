---
article_id: 26619945836951
category: eSocial - Gerar XML/ Integração Evento
content_hash: b8b882ae0886435d41848b4aa52e245fa73941c23e31d923380a1bae89bfd30a
fetched_at: '2026-06-28T22:47:13.061512+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: 'RH - RM - FOP - eSocial - Lançamento pensão de Férias - Ao gerar o evento
  S-1210 quando há férias ocorre o erro: Não foi encontrado Movimentação da Pensão
  de Dependente e a informação é obrigatória para o eSocial (S-1.2)'
type: support-article
updated_at: '2026-06-01T17:41:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/26619945836951-RH-RM-FOP-eSocial-Lan%C3%A7amento-pens%C3%A3o-de-F%C3%A9rias-Ao-gerar-o-evento-S-1210-quando-h%C3%A1-f%C3%A9rias-ocorre-o-erro-N%C3%A3o-foi-encontrado-Movimenta%C3%A7%C3%A3o-da-Pens%C3%A3o-de-Dependente-e-a-informa%C3%A7%C3%A3o-%C3%A9-obrigat%C3%B3ria-para-o-eSocial-S-1-2
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26619989568535) Tempo aproximado para leitura: **00:05:00 min**  
  
**Ocorrência**

Ao gerar o evento S-1210 que contém lançamento de pensão de férias, ocorre o erro: Não foi encontrado Movimentação da Pensão de Dependente e a informação é obrigatória para o eSocial.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26619989569815)

**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - A partir das versões 12.1.23 e  superiores.  
  
**Causa**  
O movimento de pensão alimentícia não esta sincronizado com a ficha financeira.   
  
**Solução**

Para que as informações de pensão sejam geradas no XML S-1210, o sistema irá validar se consta evento com um dos **códigos de cálculo** aceitos para pensão; se o **tipo de movimento** na movimentação de Pensão de Dependentes está de acordo com o lançamento; se o **período do Movimentação da Pensão consta de  acordo com o envelope**; e a **data de pagamento**.

Os códigos de cálculos e o tipo de movimento que o sistema irá validar serão os que constam abaixo:

|  |  |
| --- | --- |
| **CÓDIGO DE CÁLCULO** | **TIPO DE MOVIMENTO** |
| **13** - Pensão Alimentícia Judicial | **0** - Movimento |
| **53** - Pensão Alimentícia Judicial informada(folha) | **0** - Movimento |
| **54** - Pensão Alimentícia Judicial informada(13º salário) | **2** - 13º.Salário |
| **113** - Pensão alimentícia sobre férias | **1** - Férias |
| **120** - Pensão alimentícia sobre 13º salário | **2** - 13º.Salário |
| **121** - Pensão Alimentícia Sobre Participação nos Lucros | **3** - Participação Lucros |
| **195** - DIF PENSÃO ALIMENTICIA JUDICIAL | **4** - Dif. Movimento |
| **196** - DIF PENSÃO ALIMENTICIA 13 SALARIO | **6** - Dif. 13o.Salário |
| **197** - DIF PENSÃO ALIMENTICIA FERIAS | **5** - Dif. Férias |
| **206** - Pensão Alimentícia Judicial RRA | **9** - RRA Digitado |
| **210 -** Pensão Alimentícia Judicial RRA Férias | **9 -** RRA Digitado |
| **214 -** Pensão Alimentícia Judicial RRA 13º Salário | **9 -** RRA Digitado |
| **319** - Pensão Alimentícia Férias na Rescisão | **7** - Férias Rescisão |
| **320** - Pensão Alimentícia Férias Informada | **1** - Férias |
| **321** – Pensão Alimentícia PLR Informada | **3** - Participação Lucros |
| **326** - Diferença Pensão Alimentícia Férias Rescisão | **8** - Dif. Férias Rescisão |
| **386** - Pensão Alimentícia Judicial Retificação | **10 -** Retificação Folha |
| **394 -** Diferença Pensão Alimentícia RRA Folha | **13 -** Dif. RRA Movimento |
| **395** - Diferença Pensão Alimentícia RRA 13o. Salário | **15** - Dif. RRA 13o.Salário |
| **396 -** Diferença Pensão Alimentícia RRA Férias | **14 -** Dif. RRA Férias |
| **397 -** Diferença Pensão Alimentícia RRA Férias Rescisão | **16 -** Dif. RRA Férias Rescisão |
| **406** - Pensão Alimentícia Férias Retificação | **11** - Retificação Férias |
| **407** - Pensão Alimentícia 13° Salário Retificação | **12** - Retificação 13 salário |
| **408** - Pensão Alimentícia Partic. Lucros Retificação | **3** - Participação Lucros |

Para lançamento de férias existem dois casos. Quando as férias são lançadas no mês competência atual e pagamento no mês caixa atual, ou em mês caixa atual e férias lançadas no próximo mês competência.

As validações para os casos são:

* **Férias mês competência atual e pagamento no mês caixa atual**

1. Acesse **Administração de Pessoal | Funcionários | Período aquisitivo | Recibo de férias** e as informações de:

**Mês competência :** 05/2024

**Data de pagamento (caixa):** 08/05/2024

**Vencimento:** 28/02/2023

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26640967896215)

Por se tratar de férias dentro da mesma competência e caixa, será necessário acessar o envelope e conferir se as informações estão iguais.

**Mês competência :** 05/2024

**Período:** 1

**Data de pagamento (caixa):** 08/05/2024

**Código de cálculo :** 113

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26640944272791)

2. Acesse a Movimentação da Pensão e confira se todos os dados constam condizentes com o envelope;

Baseando ao exemplo acima todas a informações abaixo precisam estar preenchidas corretamente;

**Mês de competência:** 05/2024

**Mês caixa:** 05/2024

**Período:** 1

**Valor:** Igual ao envelope/Recibo de férias

**Vencimento:** 28/02/2023

**Data de pagamento férias :** 08/05/2024

**Tipo de movimento:** Será 1, por ser código de cálculo 113.

**Valor:** Igual ao do envelope/ Recibo de férias.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26640967905047)

* **Férias com pagamento no mês caixa atual e lançamento no mês competência próximo mês**

1. Acesse **Administração de Pessoal | Funcionários | Período aquisitivo | Recibo de férias** e verifique as informações abaixo, Considerando que estou na competência 05/2024, ás férias terão inicio em 01/06/2024 com pagamento em 30/05/2024.

**Mês competência de lançamento das férias :** 06/2024

**Data de pagamento (caixa):** 30/05/2024

**Vencimento:** 28/02/2023

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26641023911575)

2. Acesse a Movimentação da Pensão e confira se todos os dados constam condizentes com o envelope;

Baseando ao exemplo acima todas a informações abaixo precisam estar preenchidas corretamente;

**Mês de competência:** 06/2024

**Mês caixa:** 05/2024

**Período:** O sistema lança de forma automática

**Valor:** Igual ao Recibo de férias

**Vencimento:** 28/02/2023

**Data de pagamento férias :** 30/05/2024

Tipo de movimento: No exemplo o mesmo será 1, por ser código de cálculo 113.

As demais informações a empresa irá preencher conforme cadastro do dependente.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26641023922583)

**Importante**

Por se tratar de férias com lançamento próximo mês, a mesma estará disponível apenas no recibo de férias, e não estará no envelope de pagamento, por este motivo é importante que não haja nenhuma alteração de valor na pensão de férias, pois se o mesmo for executado, não será possível ajustar o movimento de pensão e o mesmo ficará com o valor zerado, impedindo o ajuste do erro.

Para que não haja necessidade de alteração de valor de pensão de férias, sugerimos que inclua uma fórmula dentro do cadastro do dependente, afim de que quando lançar as férias, o lançamento e o movimento seja preenchido de forma automática.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26620888374423)

Vale lembrar que se houver a necessidade de alteração do valor de pensão de férias no recibo de férias, é possível realizar o lançamento de férias próximo mês para conseguir manusear o ajuste do movimento de pensão. Para mais informações sobre o lançamento de férias próximo mês[**CLIQUE AQUI**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007913092-RH-RM-FOP-F%C3%A9rias-Lan%C3%A7amento).

**Saiba mais**  
Para mais informações sobre o S-1210 acesse:

      • [S-1210 - Pagamentos de Rendimentos do Trabalho](http://tdn.totvs.com/display/LRM/S-1210+-+Pagamentos+de+Rendimentos+do+Trabalho)   
      • [Qual a diferença entre os eventos S-1200 e S-1210?](http://tdn.totvs.com/pages/viewpage.action?pageId=364907580)  
      • [Ao gerar o evento S-1210 ocorre o erro: Não foi encontrado Movimentação da Pensão de Dependente e a informação é obrigatória para o eSocial (S-1.2)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036360433-RH-RM-FOP-eSocial-Ao-gerar-o-evento-S-1210-ocorre-o-erro-N%C3%A3o-foi-encontrado-Movimenta%C3%A7%C3%A3o-da-Pens%C3%A3o-de-Dependente-e-a-informa%C3%A7%C3%A3o-%C3%A9-obrigat%C3%B3ria-para-o-eSocial-S-1-2)
