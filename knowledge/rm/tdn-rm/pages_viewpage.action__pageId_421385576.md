---
content_hash: 9e93434455e4f4e6783311c94de14f7a353071474488da90dca14f80b820934d
fetched_at: '2026-06-29T00:09:16.844242+00:00'
page_id: '421385576'
product: rm
source: tdn-rm
title: WebService de Importação de Dados de Folha Tarefa para Coletor
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385576
version: 2
---

---

Para execução do processo de importação de dados de Avanço Físico dos coletores é necessário que se tenha acesso ao sistema mobile e realizar todo o processo de apontamento, Folha Tarefa e encerramento das mesmas. O comportamento do sistema se dará através das informações exportadas do Sistema Mobile para TOP – TOTVS Obras e Projetos, onde entre esses dois sistemas temos um conector intermediário chamado WebService, pois é ele o responsável por receber os dados recebidos pelo Mobile e conferir se todas as informações foram transmitidas corretamente e caso esteja positivo e enviado uma mensagem para o Mobile que a exportação foi feita com sucesso. Com as informações ainda no WebService é feito um tratamento nas informações e repassadas para o TOTVS Obras e Projetos concluído o processo.  
 Pré-Requisito para execução do processo: Estar autenticado no sistema e realizar os apontamentos e encerramento das folhas tarefa necessárias, para que na hora da exportação possamos conferir as alterações que chegarem no TOTVS Obras e Projetos.

Passo a passo:

1. Selecionar no Mobile o sincronismo;
2. Aguardar mensagem de informação de sucesso na transmissão de dados;
3. Acessar o TOTVS Obras e Projetos e conferir na folha tarefa % alterado está correto com o que foi apontado no móbile e status da folha tarefa depois de encerrada.
