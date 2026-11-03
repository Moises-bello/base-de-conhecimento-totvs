---
content_hash: bf59ce3235ebbb674d03994cf29ba608ae5f8ff33574f4bd094001c92a720677
fetched_at: '2026-06-29T00:09:47.178537+00:00'
page_id: '435104973'
product: rm
source: tdn-rm
title: Incluir Avanço de Obra para Medições Manuais e por fórmula
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435104973
version: 5
---

Pré-Condições

Ter incluído um Avanço de Obra (POC) de um dos tipos abaixo:

* Manual
* Fórmula
Incluindo um Avanço Manual

**Passo 1-** Clique no ícone [Incluir Avanço], localizado na lista localizada abaixo do formulário do registro.  
**Passo 2-** Preencha os campos conforme a necessidade de avanço e clique em salvar. Os campos são:

**Id do Andamento -** Identifica o andamento da obra  
**Data Inicial -** Data inicial de validade do percentual deste avanço  
**Data Final -** Data final de validade do percentual desse avanço  
**Percentual -** Percentual de avanço da obra. Se mais de um avanço foi inserido, seus percentuais não podem ultrapassar 100%

ObservaçãoSe um novo avanço for incluído, automaticamente o sistema preencherá os campos **[Data Inicial]** e **[Data Final]** com datas do próximo mês após o avanço anterior inserido.Incluindo um Avanço por Fórmula

**Passo 1 -**Clique no ícone **[Incluir Avanço],**localizado na lista localizada abaixo do formulário do registro.  
**Passo 2 -** Preencha os campos conforme a necessidade de avanço e clique em salvar. Os campos são:

**Id do Andamento -** Identifica o andamento da obra  
**Data Inicial-**Data inicial de validade do percentual deste avanço  
**Data Final -** Data final de validade do percentual desse avanço  
**Percentual -** Percentual de avanço da obra. O campo percentual seguirá as regras abaixo:

1. 1. O campo percentual é bloqueado para preenchimento, pois será preenchido com o valor de retorno do registro de Fórmula vinculado ao Avanço da Obra.
   2. O sistema controlará o total do percentual. Se o checkBox **[Permitir que a medição total da obra ultrapasse 100%]** foi selecionado, o sistema não validará o  total da soma dos percentuais de todos os registros inseridos na lista.
Observações

1. Se um novo avanço for incluído, automaticamente o sistema preencherá os campos **[Data Inicial]**e **[Data Final]** com datas do próximo mês após o avanço anterior inserido.
2. Há a necessidade de acionar o botão **[Fórmula]** para que os percentuais sejam aplicados aos avanços inseridos.
