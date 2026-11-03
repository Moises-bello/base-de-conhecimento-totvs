---
content_hash: 76d097215c3c233f9cdb578c3f1c76a7d3b945df2b9bb611d18b1da88750b251
fetched_at: '2026-06-29T00:10:38.746725+00:00'
page_id: '544724661'
product: rm
source: tdn-rm
title: LGPD - Serviços SOAP e Rest
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=544724661
version: 9
---

## 

## **CONTEÚDO**

1. **Visão Geral**
2. **Lista de dataservers com restrições**

## **01. VISÃO GERAL**

Com base na [Lei Nº 13.709/18](http://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/L13709.htm) , implementamos algumas regras de restrição a dados consumidos através de dataservers por meio dos serviços SOAP e Rest. 

Estas restrições se aplicam aos registros retornados (restrição de linha) ao consultar dados através destes serviços e implicam que um usuário só poderá ter acesso às informações que lhe pertencem, ou seja, informações que fazem referência a sua pessoa. 

Para os serviços via SOAP as restrições de aplicam aos métodos "ReadView" e "ReadRecord" e para os serviços Rest por meio da função "Get".

Estas restrições serão aplicadas aos dataservers listados abaixo (item 02) e para que o usuário tenha acesso a todas as informações do sistema através destes serviços, será necessário conceder permissão através dos perfis do sistema para cada dataserver de acordo com sua funcionalidade no menu do TOTVS Educacional.

## **02. LISTA DE DATASERVERS COM RESTRIÇÕES**

| Funcionalidade | Nome do DataServer | Item de permissão | Status |
| --- | --- | --- | --- |
| Aluno | EduAlunoData | [01.01.01.19] Visualizar informações do aluno sem restrição por Webservice | Ativo |
| Professor | EduProfessorData | [01.01.04.21] Visualizar informações do professor sem restrição por Webservice | Ativo |
| Ocorrências do aluno | EduOcorrenciaAlunoData | [01.01.01.09.04] Visualizar informações de 'Ocorrência de aluno' sem restrição por Webservice | Ativo |
| Contratos do aluno | EduContratoData | [04.01.01.19] Visualizar informações do contrato sem restrição por Webservice | Ativo |
| Responsáveis do contrato | EduResponsavelContratoData | \*\*As informações são retornadas no dataserver EduContratoData | Inativo |
| Parcelas do contrato do aluno | EduParcelaData | [04.01.01.05.06] Visualizar informações das parcelas do contrato sem restrição por Webservice | Ativo |
| Responsáveis da parcela do contrato | EduResponsavelData | [04.01.01.05.06] Visualizar informações das parcelas do contrato sem restrição por Webservice | Ativo |
| Bolsas do contrato do aluno | EduBolsaAlunoData | [04.01.01.04.04] Visualizar informações das bolsas do contrato sem restrição por Webservice | Ativo |
| Boleto | EduBoletoData | [04.01.02.02] Visualizar informações de boleto do aluno sem restrição por Webservice | Ativo |
| Lançamentos / Boletos da parcela | EduLancBoletoParcelaData | [04.01.02.02] Visualizar informações pelo readview do lançamento / boleto da parcela sem restrição por Webservice | Ativo |
