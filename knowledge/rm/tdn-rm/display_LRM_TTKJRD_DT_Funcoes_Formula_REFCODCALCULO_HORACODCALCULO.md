---
content_hash: d08c919ae1a59c82bf4c9cf259de007248bc759ecf8ccc7cf063a526435837bb
fetched_at: '2026-06-29T00:06:16.918565+00:00'
page_id: '212901899'
product: rm
source: tdn-rm
title: TTKJRD_DT_Funcoes_Formula_REFCODCALCULO_HORACODCALCULO
type: documentation
url: https://tdn.totvs.com/display/LRM/TTKJRD_DT_Funcoes_Formula_REFCODCALCULO_HORACODCALCULO
version: 1
---

# FUNÇÕES REFCODCALCULO E HORACODCALCULO COM OBJETO DE UMA ANULANDO OBJETO DA OUTRA

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Fórmulas* |
| **Situação/Requisito:** | *Ocorrência de erro na execução de fórmula que utiliza a função REFCODCALCULO e chama outra fórmula que contém a função HORACODCALCULO.*  *Nesta situação estava retornando a mensagem de "Referência de objeto não definida para uma instância de um objeto.".* |
| **Solução/Implementação:** | *Ajuste no cálculo das funções REFCODCALCULO e HORACODCALCULO, para que objetos de uma não influencie nos objetos da outra.*  *Ou seja, não efetuar o clear na lista de objetos.* |
| **Chamados   relacionados:** | *TTKJRD* |
| **Versões/Release:** | *11.82.42* |
