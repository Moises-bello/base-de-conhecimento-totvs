---
content_hash: d3a5499f6b61468d118dc64fda1b80eee3180a1a4318fb2fb3bbb03edc1012e5
fetched_at: '2026-06-29T00:06:23.400757+00:00'
page_id: '224101743'
product: rm
source: tdn-rm
title: TTVD76_DT_Cancelamento_Movimento_Funcao_Processo
type: documentation
url: https://tdn.totvs.com/display/LRM/TTVD76_DT_Cancelamento_Movimento_Funcao_Processo
version: 2
---

# IDENTIFICAR CANCELAMENTO DE MOVIMENTO NA FUNÇÃO DE FÓRMULA PROCESSO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Fórmula* |
| **Situação/Requisito:** | *Cliente solicita que a função de fórmula PROCESSO tenha também a opção de identificar o módulo de Cancelamento de Movimento.* |
| **Solução/Implementação:** | *Tratamento para incluir na função de fórmula PROCESSO a identificação do módulo de Cancelamento de Movimento.*  *Quando a função estiver sendo executada de dentro deste módulo, o seu retorno será CANCELA\_MOVIMENTO.*  *Foi incluída também a identificação de execução do módulo de Importação de Movimento, com o retorno IMPORTA\_MOVIMENTO.* |
| **Chamados   relacionados:** | *TTVD76, TUBBH6* |
| **Versões/Release:** | *11.82.43, 12.1.10* |
