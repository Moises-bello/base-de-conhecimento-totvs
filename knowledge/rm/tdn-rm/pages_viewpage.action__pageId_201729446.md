---
content_hash: 5b805082d4352d413070ccdbc9937200cc785787749299b160ba52c46fc0eb45
fetched_at: '2026-06-29T00:06:06.262906+00:00'
page_id: '201729446'
product: rm
source: tdn-rm
title: TTDH85_DT_Geração_Histórico_Regime_Dependência
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=201729446
version: 1
---

# NOME DO REQUISITO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | Totvs Gestão Educacional |
| **Função:** | Geração de histórico do aluno |
| **Situação/Requisito:** | Ao executar processo de Geração de Histórico, marcando o parâmetro “Importar disciplina cursadas em regime de dependência” apresenta mensagem de erro Column 'ANO' não permite valores nulls. |
| **Solução/Implementação:** | O problema ocorre quando no histórico está faltando informações do ano anterior ao solicitado.     Durante a Geração de Histórico, ao marcar a opção “Importar disciplina cursadas em regime de dependência”, caso não encontre o registro do ano anterior no histórico, será apresentado o aviso abaixo para melhor entendimento da causa do erro.     \*\*\* AVISOS \*\*\*     Para a correta  Geração de Histórico do TOTVS Educacional no contexto do Ensino Básico, quando existir disciplina cursada em regime de dependência, é necessário que esteja cadastrado o período letivo anterior (contendo a disciplina reprovada) e o período letivo atual (contendo a mesma disciplina em Dependência).     Deve ser gerado o histórico do período anterior e em seguida o histórico do período atual. Verifique o histórico do aluno RA: 00123. |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | N/A |
| **Versões/Release:** | *11\_82\_41* |
