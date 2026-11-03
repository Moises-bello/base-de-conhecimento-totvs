---
content_hash: 5798e0f10f41ce5ed55d8ca596479041403fd633488f55827979349f6c1d9dab
fetched_at: '2026-06-29T00:09:01.678370+00:00'
page_id: '374317727'
product: rm
source: tdn-rm
title: 2741900 DSAUGHFATF-537 DT Erro na Mudança de Categoria do Paciente
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=374317727
version: 1
---

# Erro na Mudança de Categoria do Paciente

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Função:** | Mudança de Categoria do Paciente |
| **Situação/Requisito:** | Na mudança de categoria do paciente, sistema informava que a tabela de porte não estava configurada. No entanto, ao acessar a condição contratual do convênio destino, a mesma estava configurada. |
| **Solução/Implementação:** | Foi identificado que só havia uma vigência para o convênio destino e a mesma era posterior a data do lançamento do item na conta do convênio origem. Para tal, foi esclarecido esse ponto através do complemento da mensagem de erro do sistema |
