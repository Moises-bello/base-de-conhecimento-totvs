---
content_hash: 081ed7b67dcb653b98d38383b2fc3640e390c1ca5b0c25393d586554d5a01f3f
fetched_at: '2026-06-29T00:10:26.246278+00:00'
page_id: '514425487'
product: rm
source: tdn-rm
title: FISCAL01-10227 Cadastro de Eventos - Regras gerais
type: documentation
url: https://tdn.totvs.com/display/LRM/FISCAL01-10227+Cadastro+de+Eventos+-+Regras+gerais
version: 3
---

****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | BackOffice |
| Módulo: | Gestão Fiscal |
| Função: | Regra Geral - EFD Reinf |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-10227 |

**02. SITUAÇÃO/REQUISITO**

Os Eventos devem seguir o padrão de cadastros do ERP, contudo podem existir particularidades entre os Eventos e neste caso deve ser verificada a regra na documentação especifica do Evento.

Inclusão:

Ao ser incluído o Evento assumira o Status de "Não transmitido".

Edição:

Quando o Evento estiver com Status de "Não Transmitido" o status não será alterado, quando o Evento estiver com o Status "Inconsistente" ou "Rejeitado" o Status será alterado para "Não Transmitido". Qualquer outro status o Evento assumirá o Status de "Alterado".

Exclusão:

O cadastro do Evento poderá ser excluído somente quando status for Não Transmitido, Inconsistente ou Rejeitado. 

Regras:

* Quando o Evento estiver com status de "Pendente" ou "Pendente Exclusão" todos os campos precisão permanecer bloqueados para Edição inclusive os campos nos cadastros de origem do Evento;
* Quando o Evento estiver com status de Excluído o mesmo deverá ser bloqueado para Edição, mas os campos de origem não serão bloqueados;
* Os campos **Cód. Coligada** e **Cód. da Filial**não devem ficar visíveis para o usuário;
* Nenhum histórico pode ser alterado, excluído ou incluído;
* Os campos **Identificador,** **Status,** **Tipo,** **Ambiente,** **Data da Última Transmissão, Número do Protocolo, XML de envio, XML de retorno** não devem ser editáveis;
* O campo **Id. Evento Pai** só poderá ser alterado quando o Status for "Não Transmitido", "Inconsistente" ou "Rejeitado".

**03. SOLUÇÃO**

Foram incluídas as seguintes validações gerais:

* Um evento só pode ser excluído se o status for “Não Transmitido”, “Inconsistente” ou “Rejeitado”;
* Em todos os eventos os campos data inicial e data final podem ser editadas, sendo que a data inicial somente se o status se o status for “Não Transmitido”, “Inconsistente” ou “Rejeitado” e a data final somente se o status for “Não Transmitido”, “Inconsistente”, “Rejeitado”, “Autorizado” ou “Alterado”; O campo IdProcessoJudicial só pode ser editado pelo evento R-1070;
* Se um evento for editado e o status atual for “Inconsistente” ou “Rejeitado” passará a ser “Não Transmitido”, se o status for “Alterado”, “Autorizado”, “Pendente” ou “Pendente Exclusão” passará a ser “Alterado”, caso seja “Não Transmitido” ou “Excluído” eles serão mantidos;
* Um novo Evento a ser cadastro será incluído com o status default de “Não Transmitido”;
* Somente o Evento R-1070 poderá incluir informação no campo IdProcessoJudicial;
* Ao incluir um Evento Filho, ele deverá respeitar o período de vigência do Evento Pai;
* Ao incluir um Evento Filho, ele deverá conter o Id.Evento Pai;
* A data inicial deve ser menor que a data final;

**04. DEMAIS INFORMAÇÕES**

Documentação completa do requisito:
