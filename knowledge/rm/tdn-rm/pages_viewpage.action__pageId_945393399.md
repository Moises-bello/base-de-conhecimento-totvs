---
content_hash: 654d08db715bafd41bce8e78c950f3d449fb072cf5268d18e0130c198fab9943
fetched_at: '2026-06-29T00:12:09.346918+00:00'
page_id: '945393399'
product: rm
source: tdn-rm
title: DT - Atestado Médico - Restrição de perfil no novo atestado
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=945393399
version: 4
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS -  Folha de Pagamento |
| Linha deIm Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | Atestado Médico - Restrição de perfil no novo atestado |
| País: | Brasil |
| Issue: | [DRHROTRM-13797](https://jiraproducao.totvs.com.br/browse/DRHROTRM-13797) |

## **02. LIBERAÇÃO**

Lembrando que, será a partir dos patches:

* 12.1.2406.278
* 12.1.2410.232
* 12.1.2502.146 e superiores

## **03. SITUAÇÃO/REQUISITO**

Ao registrar um atestado para um colaborador com múltiplos vínculos em filiais diferentes, o sistema considerará as permissões de acesso do usuário. Dessa forma, o atestado deverá ser inserido apenas para a matrícula (chapa) vinculada à filial à qual o usuário tem permissão de acesso.

## **04. SOLUÇÃO**

Implementamos uma regra de filtro por perfil: caso o usuário tenha um filtro que limite o acesso a apenas uma filial e registre um atestado para um colaborador com múltiplos vínculos, o atestado será vinculado exclusivamente à matrícula (chapa) pertencente à filial para a qual o usuário possui permissão de acesso.

## **05.****ASSUNTOS RELACIONADOS**
