---
article_id: 360056072793
category: RH - Benefícios
content_hash: 61835bb651ebcd95b21540fd2f4c3b5ae89c1e3c9679e951220df6ee3137e74a
fetched_at: '2026-06-28T22:44:03.811282+00:00'
product: protheus
section_id: 360001597251
source: central-protheus
title: RH - Linha Protheus - GPE - Como funciona a rotina de Planos Saúde Ativos
type: support-article
updated_at: '2025-08-28T17:44:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360056072793-RH-Linha-Protheus-GPE-Como-funciona-a-rotina-de-Planos-Sa%C3%BAde-Ativos
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34519521078807) Tempo aproximado para leitura: 00:04:00 min**

**Dúvida**Como funciona a rotina de Planos Saúde Ativos?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões   
  
**Solução**

Nos Planos de Saúde Ativos devem ser informados os planos de assistência médica e odontológica do funcionário, seus dependentes e agregados. Nesta rotina constam os registros ativos à serem calculados na folha de pagamento e será nesta tabela que estarão todas as informações de parametrização dos planos.

Dentro do padrão do ambiente Protheus temos a possibilidade de configurar os tratamentos de Plano de Saúde considerando as seguinte opções de Cálculo de Assistência Médica e Odontológica:  
  
1 - Faixa Salarial  
2 - Faixa Etária  
3 - Valor Fixo  
4 - % S/ Salario  
5 - Salarial/Etária  
6 - Salarial/Tempo

Localização no menu do ambiente: Atualizações > Benefícios > Plano de Saúde Ativos (GPEA001)  
  
Na estrutura do Plano de Saúde, todo dependente ou agregado **deve estar vinculado a um registro do Titular.**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/13605812449687)

**Principais Campos:**

* **Planos Ativos do Titular/****Funcionários (tabela RHK):**

**Tipo:**Informe se o plano corresponde a Assistência Médica ou Odontológica;

**Cód Fornece:**Informe o código do fornecedor da assistência médica ou odontológica;

**Tipo do Plano**: Informe o tipo de cálculo do plano

**Cód. Plano**: Informe o código do plano correspondente ao fornecedor e tipo de plano selecionado anteriormente;

**Verb Titular:**Informe a verba de desconto na folha, desvinculando a verba de desconto com identificador de cálculo 049 Assistência Médica;

**Per. Início/ Per. Final**: Período de Vigência do plano de saúde. Caso o período final esteja em branco serão considerados vigentes.

* **P****lanos Ativos dos Dependentes** **(Tabela RHL):**

**Sequência:**Sequência do dependente vinculado à tabela de dependentes (SRB);

**Nome:** Este campo é preenchido automaticamente de acordo com a sequência selecionada do cadastro de dependente;

**Cód. Fornece:**Informe o código do fornecedor da assistência médica ou odontológica;

**Tipo do Plano:**Informe o tipo de cálculo do plano;

**Cód. Plano:** Informe o código do plano correspondente ao fornecedor e tipo de plano selecionado

**Verb. Dep.**: Informe a verba de desconto na folha para os dependentes

**Per. Inicio/Per. Final:**Período de vigência do plano de saúde: O período de vigência dos dependentes deve respeitar ao do Titular, ou seja, o intervalo deve estar dentro do intervalo do titular.

* **Planos Ativos dos Agregados** **(Tabela RHM):**

**Sequência**: Sequenciador automático do agregado;

**Nome:**Informe o nome do Agregado. **Não esta vinculado a nenhuma tabela do sistema**;

**Cód Fornec.:**Informe o código do fornecedor da assistência médica ou odontológica;

**Dt Nasci:**Informe a data de nascimento do agregado;

**CPF Agregado:** Informe o CPF do agregado, lembrando que para maiores de 18 anos o CPF é obrigatório para DIRF;

**Tipo do Plano:**Informe o tipo de cálculo do plano;

**Cód. Plano:** Informe o código do plano correspondente ao fornecedor e tipo de plano selecionado

**Per. Início/Per. Final:** O período de vigência dos agregados deve respeitar ao do Titular, ou seja, o intervalo deve estar dentro do intervalo do titular.

O cadastro de agregados passa a ser realizado nesta tabela, **RHM** e a exclusão do mesmo perde sua referência dentro do sistema, sendo considerado apenas para a geração da **DIRF**.

Para cada tipo de Plano, caso o agregado se repita, devem ser informadas novamente todas as suas informações, pois para a **DIRF** o tratamento ocorre de forma isolada.

As alterações realizadas nos campos **CPF (RHM\_CPF)**e **Data de Nascimento (RHM\_DTNASC)**não serão gerados no Histórico de Planos Ativos (**RHN**).

**Importante:**

* O titular sempre será o “pai” do dependente/agregado.
* A verba informada entre os planos de Assistência Médica e Odontológica **devem ser diferentes**, possibilitando a validação do sistema, caso contrário, será apresentada inconsistência. Para os planos do mesmo tipo a verba pode ser igual ou diferente, para casos em que o funcionário esteja vinculado em dois planos diferentes.
* O campo do **período inicial** é **obrigatório** e o período final em caso de permanecer em branco será considerado que não possui um período final para o plano. Os planos dos dependentes e agregados devem estar dentro do período estipulado para o Titular.
* O sistema permite que os dependentes estejam vinculados a planos de operadoras diferentes das utilizadas pelo titular, porém será necessária a inclusão de um registro na grid de titulares. Neste caso, o plano do cadastro de titulares deve estar configurado para que não realize nenhum desconto para o funcionário. Definiu-se que para não realizar o desconto do titular deve ser cadastrado nas definições de tabelas um registro com os valores zerados.

**Para saber mais:**[RH - Linha Protheus - GPE - Cancelamento do Plano de Saúde/Odontológico](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwjlUajUUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBkWh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA1MDA4NjM3My1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ2FuY2VsYW1lbnRvLWRvLVBsYW5vLWRlLVNhJUMzJUJBZGUtT2RvbnRvbCVDMyVCM2dpY28GOwhUOg5zZWFyY2hfaWRJIiljMTJiYjQ1ZS0wZTZjLTRiNWQtYWE3My1hMjFlYjFmNTg1M2YGOwhGOglyYW5raQw6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIhRwbGFub3MgZGUgc2F1ZGUGOwhUOhJyZXN1bHRzX2NvdW50aQLpAw%3D%3D--e0fb9b0baad982e9a677eb06aafdd8792944eec6)  
[RH - Linha Protheus - GPE - Cálculo do Plano de Saúde Proporcional a data de Aquisição](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwh9VDDVUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBqmh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA1ODk5OTkzMy1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQyVDMyVBMWxjdWxvLWRvLVBsYW5vLWRlLVNhJUMzJUJBZGUtUHJvcG9yY2lvbmFsLWEtZGF0YS1kZS1BcXVpc2klQzMlQTclQzMlQTNvBjsIVDoOc2VhcmNoX2lkSSIpN2Y5NmM3MTItMjRlZS00ZjAzLWI3OTMtZWI5NmIxNDIxYjYwBjsIRjoJcmFua2kMOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSIUcGxhbm9zIGRlIHNhdWRlBjsIVDoScmVzdWx0c19jb3VudGkC6QM%3D--d3b50b6617900a153dd991ac86864a07f952e440)  
[RH - Linha Protheus - GPE - Como excluir/cancelar o cálculo do plano de saúde/odontológico](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwhGzObUUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBqWh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA1NDE4MDkzNC1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ29tby1leGNsdWlyLWNhbmNlbGFyLW8tYyVDMyVBMWxjdWxvLWRvLXBsYW5vLWRlLXNhJUMzJUJBZGUtb2RvbnRvbCVDMyVCM2dpY28GOwhUOg5zZWFyY2hfaWRJIikxM2E4MzQ2MS04YzBhLTQ3NDQtOGFhMy0xMDU0YjlkNzhmZTQGOwhGOglyYW5raQc6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIhRwbGFub3MgZGUgc2F1ZGUGOwhUOhJyZXN1bHRzX2NvdW50aQLpAw%3D%3D--40b9f7d87ff24da98c45ed526b023b3fa4a42a38)  
[RH - Linha Protheus - GPE - Como fazer reajuste de valores do plano de saúde e odontológico](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwj6btbUUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBpWh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA1MzEwODQ3NC1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ29tby1mYXplci1yZWFqdXN0ZS1kZS12YWxvcmVzLWRvLXBsYW5vLWRlLXNhJUMzJUJBZGUtZS1vZG9udG9sJUMzJUIzZ2ljbwY7CFQ6DnNlYXJjaF9pZEkiKTEzYTgzNDYxLThjMGEtNDc0NC04YWEzLTEwNTRiOWQ3OGZlNAY7CEY6CXJhbmtpDDoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiFHBsYW5vcyBkZSBzYXVkZQY7CFQ6EnJlc3VsdHNfY291bnRpAukD--1ea00b98d0ced4b5cba3413f7529265c7a88c145)  
[RH - Linha Protheus - GPE - Cálculo do plano de saúde proporcional após encerramento do plano](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwheUyTVUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBrGh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA1ODIxMzIxNC1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQyVDMyVBMWxjdWxvLWRvLXBsYW5vLWRlLXNhJUMzJUJBZGUtcHJvcG9yY2lvbmFsLWFwJUMzJUIzcy1lbmNlcnJhbWVudG8tZG8tcGxhbm8GOwhUOg5zZWFyY2hfaWRJIik3Zjk2YzcxMi0yNGVlLTRmMDMtYjc5My1lYjk2YjE0MjFiNjAGOwhGOglyYW5raQk6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIhRwbGFub3MgZGUgc2F1ZGUGOwhUOhJyZXN1bHRzX2NvdW50aQLpAw%3D%3D--af735b4ffb2640277a940258548b30ea4cda6fbd)  
[RH - Linha Protheus - GPE - Como descontar plano de saúde/odontológico apenas para o dependente](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgXlafACgk6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBqmh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzk5NDE3ODY1MzEwOTUtUkgtTGluaGEtUHJvdGhldXMtR1BFLUNvbW8tZGVzY29udGFyLXBsYW5vLWRlLXNhJUMzJUJBZGUtb2RvbnRvbCVDMyVCM2dpY28tYXBlbmFzLXBhcmEtby1kZXBlbmRlbnRlBjsIVDoOc2VhcmNoX2lkSSIpN2Y5NmM3MTItMjRlZS00ZjAzLWI3OTMtZWI5NmIxNDIxYjYwBjsIRjoJcmFua2kPOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSIUcGxhbm9zIGRlIHNhdWRlBjsIVDoScmVzdWx0c19jb3VudGkC6QM%3D--fd1b60daf0d2da219ba72d5d11c2e8c7fcf4b1d7)
