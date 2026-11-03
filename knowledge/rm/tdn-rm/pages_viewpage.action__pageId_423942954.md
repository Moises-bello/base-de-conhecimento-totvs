---
content_hash: 27e819727a40c5fdcfeb298e456c7b5bbc0a9991b0223ee5995d960d01f6f16e
fetched_at: '2026-06-29T00:09:29.335551+00:00'
page_id: '423942954'
product: rm
source: tdn-rm
title: 1747249 FOPCALCULO01-2560 - Cálculo de Férias - Log
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423942954
version: 1
---

# Cálculo de Férias

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Folha de Pagamento |
| **Função:** | Cálculo de Férias |
| **Situação/Requisito:** | Quando a base está parametrizada para Ativar Alterações da Reforma Trabalhista e o funcionário tem um saldo de férias restante do período aquisitivo aberto menor que 5 dias, no processo de cálculo não retornar nenhuma mensagem para o usuário informando que o período minimo de gozo é 5 dias. Isto é necessário, pois: Supondo que o funcionário possui 30 dias de férias a marcar. Quando é feito agendamento ou o cálculo de 20 dias de férias antecipadamente e durante o período aquisitivo houver 6 faltas reduzindo o saldo de férias para 24 dias por exemplo, no momento do cálculo não é apresentado nenhum alerta ou mensagem de que o saldo restante para gozo de férias no próximo período seja de 4 dias, contrariando a lei da reforma trabalhista de que o período mínimo é de 5 dias. |
| **Solução/Implementação:** | Tratativa para verificar se os dias restantes de férias são inferiores a 5 dias e, se for o caso, avisar o usuário pelo log. |
| **Tickets relacionados:** | 1747249 |
