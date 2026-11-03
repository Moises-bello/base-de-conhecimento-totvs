---
content_hash: 2b9925902198d5968c631ccd9c5eae0aa8a66a0a8e3c782894f8ad0ab7c00e2d
fetched_at: '2026-06-29T00:11:16.996602+00:00'
page_id: '675549823'
product: rm
source: tdn-rm
title: 13581792 FISCAL01-17576 - DT - NFS-e Campinas - Inscrição Municipal da Obra
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=675549823
version: 2
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | NFS-e |
| País: | Brasil |
| Ticket: | [13581792](https://totvssuporte.zendesk.com/agent/tickets/13581792 "View ticket on the Zendesk portal") |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-17576 |

## **02. SITUAÇÃO/REQUISITO**

A cliente está realizando a emissão de NFS-e para o município de Campinas/SP, porém a seguinte mensagem de inconsistência no TSS está sendo apresentada:

\*Element 'InscricaoMunicipalObra': This element is not expected. Expected is ( CodigoAtividade ).

* Após a análise por parte da equipe de TSS, fomos informados que o mesmo foi alterado e está exigindo o preenchimento de tais dados para que a emissão do documento seja realizada com sucesso. Seguem dados técnicos da implementação:  
  <https://tdn.totvs.com/pages/viewpage.action?pageId=243641191>

* <https://jiraproducao.totvs.com.br/browse/DSERTSS2-9828>

## **03. SOLUÇÃO**

O layout da NFS-e foi alterado para que os campos **InscricaoMunicipalObra** e **ServicoObra** sejam gerados no layout único de integração com o TSS. O campo **InscricaoMunicipalObra** será gerado com base em campo complementar do cadastro do projeto.

**Regras:**

* A tag deverá ser gerada somente quando o campo complementar estiver preenchido.
* Sempre que o município do projeto for diferente do município de prestação, devemos ignorar o valor preenchido no campo complementar e gerar a tag com 000000000 (9 zeros), caso seja o mesmo município devemos gerar com o valor preenchido no campo complementar.

O campo **ServicoObra** deverá ser gerado a partir de um campo complementar do item do Movimento.

**Regra:**

Gerar a tag somente quando o campo complementar estiver preenchido.

**Exemplo:**

*<construcao>*

*<inscmunobra>000000000</inscmunobra>*

*<codservobra>27</codservobra>*

*</construcao>*

Disponível a partir da versão 12.1.33
