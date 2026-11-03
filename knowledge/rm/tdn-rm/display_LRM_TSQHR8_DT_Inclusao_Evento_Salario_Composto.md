---
content_hash: 0f33dbcb2ff8e232dcf7c842fc2139d67625edd317abecf637280903aa9fc8c8
fetched_at: '2026-06-29T00:06:02.817755+00:00'
page_id: '198949110'
product: rm
source: tdn-rm
title: TSQHR8_DT_Inclusao_Evento_Salario_Composto
type: documentation
url: https://tdn.totvs.com/display/LRM/TSQHR8_DT_Inclusao_Evento_Salario_Composto
version: 4
---

# Salário Composto

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *C&P* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Salário Composto* |
| **Situação/Requisito:** | *Ao realizar a inclusão,exclusão ou edição de um evento no cadastro de salário composto, cujo evento já existe no histórico salarial, o sistema permitia o cadastro do evento, inseria um novo número de salário e emitia mensagem de erro.* |
| **Solução/Implementação:** | *Realizar a comparação do número do salário buscando informações do Histórico Salarial e não somente da Composição do Salário para verificar se um evento já esteve associado a um número de salário alguma vez.* |
| **Chamados relacionados:** | *TSQHR8* |
| **Versões/Release:** | *11.82.40* |
