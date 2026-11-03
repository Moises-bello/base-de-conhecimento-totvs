---
content_hash: 77deaff32aedf637b5747ecf012472e3112dd5c3ee252916c7b80e2daf0b5cba
fetched_at: '2026-06-29T00:09:09.702928+00:00'
page_id: '393364528'
product: rm
source: tdn-rm
title: 3501515 FOPCALCULO01-4409 Validação de Aviso Prévio Trabalhado Cadastrado
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=393364528
version: 1
---

# Aviso Prévio Trabalhado

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Folha de Pagamento |
| **Função:** | Funcionários | Anexos | Movimento | Férias |
| **Situação/Requisito:** | Quando o funcionário tem aviso prévio trabalhado cadastrado para mês posterior a competência atual da base, ao cadastrar férias dentro do período do aviso prévio trabalhado do funcionário, o sistema não está validando o aviso prévio trabalhado cadastrado, permitindo o cadastro, cálculo e lançamento de férias, sem apresentar nenhum aviso, causando conflito de processos. |
| **Solução/Implementação:** | Foi efetuada uma correção na regra de validação do lançamento de férias e agora o sistema impede que férias sejam marcadas no período coincidente ou posterior do aviso prévio. |
| **Tickets relacionados:** | 3501515 |
