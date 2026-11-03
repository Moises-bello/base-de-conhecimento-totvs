---
article_id: 360052504013
category: RH - Definições de Cálculo
content_hash: b95d86a7f89164d307e4b8ef46f35e1d60e1923e871634b5fea6392b1d957474
fetched_at: '2026-06-28T22:43:22.268014+00:00'
product: protheus
section_id: 360011913513
source: central-protheus
title: 'RH - Linha Protheus - GPE - Cadastro Auxílio Creche gera mensagem: Quando
  o campo "Aux. Creche" for preenchido com sim, deverá existir valor no campo "Valor
  Creche" ou então registro válido na tabela S015'
type: support-article
updated_at: '2026-06-26T17:37:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052504013-RH-Linha-Protheus-GPE-Cadastro-Aux%C3%ADlio-Creche-gera-mensagem-Quando-o-campo-Aux-Creche-for-preenchido-com-sim-dever%C3%A1-existir-valor-no-campo-Valor-Creche-ou-ent%C3%A3o-registro-v%C3%A1lido-na-tabela-S015
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26434645133975) Tempo aproximado para leitura: 00:02:00 min**

**Ocorrência**  
Na rotina de cadastro de dependentes aorealizar o cadastro das informações referente ao auxilio creche  gera a mensagem abaixo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360083325053)

**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17

**Causa**  
Esse incidente ocorre, pois no Cadastro do funcionário não consta o código do sindicato para poder validar junto com a tabela S015.

**Solução**  
Para que não ocorra mais a mensagem e a configuração do auxilio creche fique correta, realize os passos abaixo:

**1.** Passo o conteúdo do parâmetro **MV\_ACPGSLA** - Cálculo Auxilio creche, precisa estar com 1 - Calcula. Para configurar o parâmetro acesse o **Configurador SIGACFG > Ambientes > Cadastros > Parâmetros, pesquise pelo MV\_ACPGSLA e configure.**

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26434645139351)**

**2.** Cadastre a verba de **id 0721** em **Atualizações > Definições de cálculo > Verbas (GPEA040)**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26434621257495)

**3.** Acesse **Atualizações > Definições de Cálculo > Manutenção de tabelas (GPEA320),** e vincule o sindicato no cadastro da S015:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360083323033)

**4.** Acesse **Atualizações > Funcionários > Funcionários (GPEA010)** e vincule o sindicato no cadastro do funcionário que irá receber o auxilio creche na **aba Funcionais**:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360083323293)

**5.** Acesse **Atualizações > Funcionários > Dependentes** **(GPEA020)** ao incluir a informação no campo "Aux. Creche" deixando o campo "Valor" em branco é possível salvar o cadastro:

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360083323353)

**Saiba Mais**  
[RH - Funcionários](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360011909593-RH-Funcion%C3%A1rios)
