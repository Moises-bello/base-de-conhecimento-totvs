---
content_hash: 9020c5be488d9d5910e04d583fb5efefa55fa522a72d0497fbe709792776c0a9
fetched_at: '2026-06-29T00:10:30.091410+00:00'
page_id: '519195285'
product: rm
source: tdn-rm
title: Comparativo de Incidências de Rubricas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=519195285
version: 27
---

**Releases que contemplam este relatório**

* 12.1.24.255
* 12.1.25.198
* 12.1.26.139
* E superiores

**01. VISÃO GERAL**

Através deste relatório serão identificadas com maior facilidade possíveis diferenças entre as incidências marcadas no cadastro de eventos e o XML gerado - S1010  já com o Status 10- (aceito RET).

Este relatório pode ser gerado considerando todas as incidências ou individualmente por tipo de incidência (INSS ,IRRF, FGTS e Contribuição Sindical).

**02. EXEMPLO DE UTILIZAÇÃO**

   No primeiro acesso ir em segurança / perfil e dar permissão de acesso ao menu.

   Acessar **eSocial | Outros processos | Comparativo de Incidências de Rubricas**

Selecionando "Exibir a comparação de todos os campos" o sistema desabilita os demais campos de comparação.

  Podemos comparar todas as incidências ou selecionar uma incidências especifica para a comparação no relatório.

  Selecionando a opção de relatório "Exibir somente registros com erro" será exibido os registros com erros.

    Exemplo do relatório gerado somente com diferença comparando todos os campos.

   Exemplo do relatório gerado sem e com diferenças.

Caso exista alguma rubrica no Cadastro de Eventos do RM, cujo XML S-1010 ainda não esteja com o status 10-Aceito RET, elas serão informadas na aba **Inconsistências**.

 Após gerar o relatório, através do menu processos podemos gerar o gatilho das rubricas que estiverem divergentes.

**03.IMPORTANTE**

Quando existir mais de um evento para a mesma rubrica com o Status 10 (Aceito RET), o relatório irá considerar sempre o evento com a data de envio mais recente para comparação.

**04.TABELAS UTILIZADAS**

* PEVENTO
