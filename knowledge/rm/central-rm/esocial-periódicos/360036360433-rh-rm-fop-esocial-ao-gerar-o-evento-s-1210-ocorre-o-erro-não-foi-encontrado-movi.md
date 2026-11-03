---
article_id: 360036360433
category: esocial - Periódicos
content_hash: 4cf3493eb51cb165a885cdd7476c1de767e966057cb2b0f7b99b5ea568d8606f
fetched_at: '2026-06-28T22:47:09.134167+00:00'
product: rm
section_id: 1500000860982
source: central-rm
title: 'RH - RM - FOP - eSocial - Ao gerar o evento S-1210 ocorre o erro: Não foi
  encontrado Movimentação da Pensão de Dependente e a informação é obrigatória para
  o eSocial (S-1.2)'
type: support-article
updated_at: '2026-04-17T18:14:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036360433-RH-RM-FOP-eSocial-Ao-gerar-o-evento-S-1210-ocorre-o-erro-N%C3%A3o-foi-encontrado-Movimenta%C3%A7%C3%A3o-da-Pens%C3%A3o-de-Dependente-e-a-informa%C3%A7%C3%A3o-%C3%A9-obrigat%C3%B3ria-para-o-eSocial-S-1-2
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21707985394199)**Tempo aproximado para leitura: **00:05:00 min**  
  
**Ocorrência**  
Ao gerar o evento S-1210 ocorre o erro: Não foi encontrado Movimentação da Pensão de Dependente e a informação é obrigatória para o eSocial.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21707597851543)

**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - A partir das versões 12.1.2302.235, 12.1.2306.182, 12.1.2310.116 e superiores.  
  
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

Para correta geração, realize os seguintes passos:

1. Acesse o envelope do funcionário e identifique o evento de pensão; Confira o código de cálculo, data de pagamento e valor. Em nosso exemplo as validações são:

**Mês competência :** 05/2024

**Período:** 1

**Data de pagamento (caixa):** 15/06/2024

**Código de cálculo :** 13

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26618647690263)

2. Acesse a Movimentação da Pensão e confira se todos os dados constam condizentes com o envelope.. Baseando ao exemplo acima:

**Mês competência:** 05/2024

**Mês caixa:** 06/2024

**Período:** 1

**Valor:** Igual ao envelope

Tipo de movimento: No exemplo o mesmo será 0, por ser código de cálculo 13.

As demais informações a empresa irá preencher conforme cadastro do dependente.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26618632886679)

3. XML gerado com sucesso.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26618647705239)

**Importante**  
Se o funcionário possuir mais que 1 dependente, deverá conferir todos os dependentes.

**Saiba mais**  
Para mais informações sobre o S-1210 acesse:  
      • [S-1210 - Pagamentos de Rendimentos do Trabalho](http://tdn.totvs.com/display/LRM/S-1210+-+Pagamentos+de+Rendimentos+do+Trabalho)   
      • [Qual a diferença entre os eventos S-1200 e S-1210?](http://tdn.totvs.com/pages/viewpage.action?pageId=364907580)  
      • [- S-1210 - Lançamento pensão de Férias](https://centraldeatendimento.totvs.com/hc/pt-br/articles/26619945836951)
