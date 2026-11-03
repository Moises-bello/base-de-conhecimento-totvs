---
content_hash: c68a30083285b731c08159d9f164aed2b724ef0923f514be947796538adefb98
fetched_at: '2026-06-29T00:09:07.685250+00:00'
page_id: '384587787'
product: rm
source: tdn-rm
title: 3351575 FOPROTINAS01-5202 DT - Erro quando chefe cadastra férias de funcionário
  no RM Portal
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=384587787
version: 2
---

# RM PORTAL DEVE VALIDAR PERÍODO AQUISITIVO DO FUNCIONÁRIO, NÃO DO CHEFE

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Recursos Humanos |
| **Módulo:** | RM Portal |
| **Função:** | Gestão de Férias |
| **Situação/Requisito:** | Quando chefe tenta marcar férias do funcionário em RM Portal >> Portal RH >> Equipe >> Gestão de Férias, está sendo validado o período aquisitivo do chefe. O correto seria validar o período aquisitivo do funcionário para o qual o chefe está marcando as férias. |
| **Solução/Implementação:** | Foi realizado ajuste no formulário de sugestão de férias para utilizar os parâmetros passados na URL quando salvar os dados do período de gozo, ao invés de utilizar o contexto. |
| **Tickets relacionados:** | 3351575 |
