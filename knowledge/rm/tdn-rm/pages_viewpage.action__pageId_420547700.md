---
content_hash: 2ac49fd2112c779572f6be7a20c487ad1b5709878a5841813b2cf79fd26c7372
fetched_at: '2026-06-29T00:09:13.445911+00:00'
page_id: '420547700'
product: rm
source: tdn-rm
title: 3830018 FOPROTINAS01-6230 DT - Ícone do Status de Férias Vencidas Incorreto
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=420547700
version: 1
---

# ÍCONE DO STATUS DE FÉRIAS DEVE ASSINALAR QUE AS FÉRIAS FORAM MARCADAS APENAS QUANDO NÃO RESTAR SALDO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Recursos Humanos |
| **Módulo:** | Folha de Pagamento |
| **Função:** | RM Portal - Subordinados |
| **Situação/Requisito:** | Ao acessar a tela de subordinados do RM Portal, é exibido ícone informando que foram marcadas as férias de um funcionário que ainda possui saldo de férias a marcar. Isso ocorre porque está sendo validado apenas se há um período de gozo marcado, mas não é validado se ainda há saldo restante de férias a marcar. |
| **Solução/Implementação:** | Foi feito ajuste para considerar o último período de gozo marcado ao invés do primeiro, e para validar se ainda há saldo de férias a marcar para definir o ícone a ser exibido. |
| **Tickets relacionados:** | 3830018 |
