---
content_hash: a600eecb7de806af0d035d2ce55541efc8fb1fbf5935858fa832ddc70fca32e4
fetched_at: '2026-06-29T00:10:25.943462+00:00'
page_id: '506994215'
product: rm
source: tdn-rm
title: FISCAL01-10229 DT Cadastro de Eventos da EFD-Reinf - Front End R1000
type: documentation
url: https://tdn.totvs.com/display/LRM/FISCAL01-10229+DT+Cadastro+de+Eventos+da+EFD-Reinf+-+Front+End+R1000
version: 3
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | BackOffice |
| Módulo: | Gestão Fiscal |
| Função: | EDF Reinf |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-10229 |

## **02. SITUAÇÃO/REQUISITO**

Ao acessar o menu EFD-REINF → “Eventos Cadastrais” devem ser listados todos os Eventos do tipo R-1000. O cadastro poderá ser acionado somente pela Filial Matriz ou Filial SCP. Os campos seguirão o padrão de estrutura definidos para os Eventos da EFD-REINF.

A inclusão do registro R-1000 será realizada conforme a estrutura padrão dos eventos da EFD-REINF, porém com os detalhes abaixo.

* **Id. Evento Pai** não deve ser visível;
* **Tipo:** será preenchido com o código do evento R-1000 e não deve ser editável;
* **Início do Período:** deverá ser informado a data de início da vigência da EFD-REINF ou deste Evento;
* **Código da Filial:** não deve ser editáve

## **03. SOLUÇÃO**

Ao acessar o menu EFD-REINF → “Eventos Cadastrais” devem ser listados todos os Eventos do tipo R-1000. O cadastro poderá ser acionado somente pela Filial Matriz ou Filial SCP. Os campos seguirão o padrão de estrutura definidos para os Eventos da EFD-REINF.

A inclusão do registro R-1000 será realizada conforme a estrutura padrão dos eventos da EFD-REINF, porém com os detalhes abaixo.

* **Id. Evento Pai** não deve ser visível;
* **Tipo:** será preenchido com o código do evento R-1000 e não deve ser editável;
* **Alinhamento de alguns quadros**

## **04. DEMAIS INFORMAÇÕES**

O campo **Código da Filial** não foi incluído pois após análise, ficou entendido que a Código da Filial será a do Contexto(não havendo possibilidade inicial de troca de contexto) e mesmo que seja incluída o campo Código Filial as informações de contexto devem existir(o que ainda não acontece).
