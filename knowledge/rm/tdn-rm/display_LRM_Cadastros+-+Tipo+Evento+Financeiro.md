---
content_hash: 799b53d692d3a00aa41796c277e7f7597cbd5e17ad7414f87d6a52f2f251a95b
fetched_at: '2026-06-29T00:09:50.157430+00:00'
page_id: '435105418'
product: rm
source: tdn-rm
title: Cadastros - Tipo Evento Financeiro
type: documentation
url: https://tdn.totvs.com/display/LRM/Cadastros+-+Tipo+Evento+Financeiro
version: 3
---

O Tipo de Evento Financeiro é usado para classificar os eventos financeiros do módulo de aluguel do TOTVS Incorporação.

Cadastro localizado em: **Aluguel | Cadastros | Tipo de Evento Financeiro.**

Na versão 12.1.2, o cadastro de Tipo de Evento Financeiro contempla as seguintes novidades:

* Foram criados os campos:

* + **Campo integração;**
  + **Campo integração (Subtrai).**

* Criada uma nova Finalidade de tipo de evento que é a de Locação.
* A Finalidade **Padrão** criada na 12.1.1 foi renomeada para **Diversos** na versão 12.1.2.

Veja abaixo a descrição dos campos deste cadastro:

**Tipo de evento financeiro:** Código do tipo de evento criado.  
 **Descrição do tipo de evento:** Descrição do tipo de evento criado.  
 **Finalidade do tipo de evento**, possui os tipos de evento possíveis de serem criados. Abaixo temos os tipos disponíveis são:

* + **Diversos**: Utilizado por eventos financeiros cadastrados manualmente pelo usuário. Eventos com este tipo são criados manualmente.
  + **Rescisão**: Utilizado por eventos financeiros gerados pelo processo de rescisão de contrato de locação.
  + **Locação**:: Este tipo de Evento deve ser informado nos Contratos de Locação, para que após a geração dos Lançamentos Financeiro seja criado automaticamente um evento financeiro com as informações do respectivo contrato. Tipos de evento locação são criados apenas pelo Contrato de Locação.
  + **Luva**: Utilizado pelo processo de luva do contrato de locação. Eventos com este tipo são criados manualmente.

**Campo integração:** Campo usado para informar o Valor de Integração com objetivo de somar, que será gravado no lançamento do TOTVS Gestão Financeira.  
**Campo integração (Subtrai):** Campo usado para informar o Valor de Integração com objetivo de subtrair, que será gravado no lançamento do TOTVS Gestão Financeira.
