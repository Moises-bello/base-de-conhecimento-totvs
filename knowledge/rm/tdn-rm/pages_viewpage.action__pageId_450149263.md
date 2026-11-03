---
content_hash: 13bf1f7bd1e8b34682d8f31e70b035c3c0dd761b1490cb873b90f01f0ef8f1a5
fetched_at: '2026-06-29T00:09:55.746327+00:00'
page_id: '450149263'
product: rm
source: tdn-rm
title: FISCAL01-7603 DT Ajuste na carga dos Parâmetros de integração RM X TAF
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=450149263
version: 1
---

# Escrituração Fiscal - Estado Lançamento Fiscal

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Serviços |
| **Módulo:** | TOTVS Gestão Fiscal |
| **Função:** | Integração RM X TAF |
| **Situação/Requisito:** | O processo e integração do RM com o TAF não aceita o padrão de url fornecido para a comunicação com o SMART REINF |
| **Solução/Implementação:** | Ajustada a carga dos parâmetros de comunicação do TAF no RM para que suporte a URL completa do SmartClient. A partir de agora a porta não é mais obrigatória pois a url do SmartClient não possui esta informação. Os campos de usuário e senha permanecem inalterados.  O cliente poderá informar os parâmetros da seguinte maneira. SERVIDOR: [http://SERVIDOR/rest](http://servidor/rest "Follow link") PORTA: XXXX  SERVIDOR: SERVIDOR/rest - Neste caso o processo de envio acrescenta o http:// na frente do endereço. PORTA: XXXX  SERVIDOR:[https://SERVIDORSMARTCLIENT/rest/wstafst2](https://wsp-c9002c.dev-ing.smartfiscal.info/rest/wstafst2 "Follow link")  PORTA: SEM INFORMAÇÃO  Quando se tratar do protocolo https ele deve ser obrigatoriamente informado pois se não existe será preenchido como http e isto pode ocasionar erro de comunicação. |
| **Documento relacionado:** |  |
