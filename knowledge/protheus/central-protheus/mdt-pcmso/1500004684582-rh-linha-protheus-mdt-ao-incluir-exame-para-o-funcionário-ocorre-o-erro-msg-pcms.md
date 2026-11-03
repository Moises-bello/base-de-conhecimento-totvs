---
article_id: 1500004684582
category: MDT - PCMSO
content_hash: 2427eba887628a47755fd57cd18952b5ee5bb978d441f4f93140a7db9645a79b
fetched_at: '2026-06-28T22:44:28.308883+00:00'
product: protheus
section_id: 360010945214
source: central-protheus
title: 'RH - Linha Protheus - MDT - Ao incluir exame para o funcionário ocorre o erro:
  MSG_PCMSO "Não existe um número de PCMSO para esta data de Exame"'
type: support-article
updated_at: '2025-09-03T12:52:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004684582-RH-Linha-Protheus-MDT-Ao-incluir-exame-para-o-funcion%C3%A1rio-ocorre-o-erro-MSG-PCMSO-N%C3%A3o-existe-um-n%C3%BAmero-de-PCMSO-para-esta-data-de-Exame
---

**Ocorrência**Ao incluir exame para o funcionário ocorre o erro: **MSG\_PCMSO** "Não existe um número de **PCMSO** para esta data de Exame".  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as versões  
  
**Causa**Esse erro ocorre porque não existe **programação de exame** para o período (ano) que está sendo incluído o exame. O código **PCMSO** é o código do registro cadastrado na programação.  
  
Quando um atendimento ou lançamento de um exame for incluído e o sistema não localizar um **PCMSO** para a data do exame, será apresentado a mensagem **MSG\_PCMSO** "Não existe um número de PCMSO para esta data de Exame".  
  
Qualquer outro exame oriundo de uma necessidade avaliada para o médico poderá ser incluído dentro de qualquer data deste período, pois existe um PCMSO relacionado a este controle. Quando a empresa deseja lançar um exame aleatório sem relação com o PCMSO deverá utilizar a opção **Assistencial** e não **Ocupacional**, desta forma o sistema não irá validar.  
  
**Solução**Quando se cadastra um exame para um funcionário com a origem **Ocupacional,** deve existir um **PCMSO** para ser relacionado a **Ficha Médica** do trabalhador. Não trata-se de um erro e sim um conceito do produto. Normalmente o **PCMSO** é anual, e o Medico realiza avaliação de todos os exames necessários para segurança e saúde do colaborador.  
  
**Exemplo 1:** Cenário onde ocorre o erro.  
Note que na minha rotina geração da programação de exames localizada no caminho: **Atualizações > PCMSO > Gerar Programação** (MDTA190). Não existe nenhuma programa no período de 2021.![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500006212661)  
  
Ao tentar incluir um exame para o funcionário com a data de 22/03/2021 o campo Num. PCMSO não é preenchido ocorrendo o aviso: **MSG\_PCMSO** "Não existe um número de PCMSO para esta data de Exame".  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500006097402)  
  
**Exemplo 2:** Cenário onde não ocorre o erro.  
Note que na minha rotina geração da programação de exames localizada no caminho: **Atualizações > PCMSO > Gerar Programação** (MDTA190), existe uma programa no período de 2021.

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500006097702)  
  
Ao tentar incluir um exame para o funcionário com a data de **22/03/2021** o campo Num. PCMSO é preenchido e não ocorre erros.  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500006213061)  
  
**Observação**  
Para saber como funciona a rotina **Gerar Programação** (MDTA190) consulte os artigos:

* **[MP - MDT - Como Gerar Programação (MDTA190)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059737173)**
* **[MP - MDT - Como cadastrar e definir os exames que serão apresentado no PCMSO (Programa de Controle Médico de Saúde Ocupacional)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059540413)**

**Saiba Mais**  
[Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Artigos PCMSO](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360010945214-MDT-PCMSO)  
[ChatBot Carol Assistant](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022200991)
