---
content_hash: d634e55503b52476dc25be94e1e1608b25dc5014d70c45fc775ae0ab19b8e54a
fetched_at: '2026-06-29T00:08:57.910989+00:00'
page_id: '357598159'
product: rm
source: tdn-rm
title: 96301 EDUCACIONAL01-191 Currículo Lattes campo Obtenção de título
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=357598159
version: 1
---

# CURRÍCULO LATTES

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Educacional. |
| **Módulo:** | TOTVS Gestão Educacional. |
| **Função:** | Importação do currículo Lattes |
| **Situação/Requisito:** | Na importação do currículo Lattes do professor, o sistema não estava importando o campo “Obtenção de título”. |
| **Solução/Implementação:** | Alterado a importação do currículo Lattes do professor, para gravar o campo “Obtenção de título” de acordo com o que está no arquivo xml da Plataforma Lattes, tag ANO-DE-OBTENCAO-DO-TITULO.  **OBS.:** A Plataforma Lattes até o momento não exporta o mês de obtenção do título, portanto no sistema Totvs Educacional somente iremos importar o ano.  Caso um dia o link [http://lattes.cnpq.br](http://lattes.cnpq.br/) passe a exportar o mês de obtenção do título, então será alterado futuramente no Totvs Educacional. |
| **Conversores e Parâmetros:** | N/A. |
| **Tickets relacionados:** | N/A. |
| **Requisito:** | N/A. |
| **Documento de Referência:** | N/A. |
