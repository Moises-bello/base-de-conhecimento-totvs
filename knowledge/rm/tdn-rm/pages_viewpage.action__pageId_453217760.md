---
content_hash: ece3f70848237b36a5f8e84a7f9a90689c9b31b02ec237f290ff4fca092953b2
fetched_at: '2026-06-29T00:10:11.701367+00:00'
page_id: '453217760'
product: rm
source: tdn-rm
title: FISCAL01-7793 DT Ajuste na carga dos parâmetros de integração RM X TAF
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=453217760
version: 2
---

# Envio da NF-e

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Serviços |
| **Módulo:** | TOTVS Gestão Fiscal |
| **Função:** | Integração RM X TAF |
| **Situação/Requisito:** | Quando a integração do RM com o TAF é através do SMARTREINF está sendo acrescentado o prefixo http no endereço que já é está com https. |
| **Solução/Implementação:** | A carga dos parâmetros do TAF foi ajustada para que quando existir o prefixo no endereço do webservice, seja ele http ou https, nada seja acrescentado ao mesmo. Quando este prefixo não existir será concatenado o prefixo http. Portando quando se tratar de https continua sendo obrigatório informar o mesmo nos parâmetros de integração.  Em caso de erro na comunicação agora serão exibidos no log o Json enviado, o Json recebido e o webservice utilizado na comunicação. |
