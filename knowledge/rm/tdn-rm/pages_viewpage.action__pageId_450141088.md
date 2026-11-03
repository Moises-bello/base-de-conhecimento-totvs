---
content_hash: ee8096fc475665307c8f51dcfe8e6718ec059a515f3ac30d40d4b395402294ef
fetched_at: '2026-06-29T00:09:55.686566+00:00'
page_id: '450141088'
product: rm
source: tdn-rm
title: FISCAL01-7353 DT Escrituração - Calcular valores para Fecp e Fecpst
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=450141088
version: 3
---

# Escrituração Fiscal - Estado Lançamento Fiscal

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Serviços |
| **Módulo:** | TOTVS Gestão Fiscal |
| **Função:** | Processo de Escrituração Fiscal |
| **Situação/Requisito:** | Calcular o FECP Proprio no Item e no Lançamento durante a Escrituração. Ajustar o FECPST para subtrair o FECP Proprio. Deverá ser considerado o parametro da regra de ICMS para calcular ou não os FECP e FECPST |
| **Solução/Implementação:** | Foi alterado o processo de escrituração do Lançamento Fiscal para calcular os valores de Fecp e FecpST em campos separados.  Para o cálculo serão considerados os parâmetros Operação com FCP e Operação com FCP da regra de ICMS.    A escrituração irá buscar a alíquota para cálculo do Fecp no anexo dados fiscais do produto para as uf envolvidas na incidência do imposto.    Campo no item do lançamento    No lançamento |
| **Documento relacionado:** |  |
