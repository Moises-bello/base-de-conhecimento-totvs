---
content_hash: 26dfabb43c0db039e04ae403d4eee9500df3e928553f450ea05561992eb2e78a
fetched_at: '2026-06-29T00:09:24.058577+00:00'
page_id: '423934423'
product: rm
source: tdn-rm
title: 3955462 PORTALMOBILE01-5820 DT Disponibilização de Processo Seletivo no portal
  - Data fim\ disponivel na internet
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423934423
version: 1
---

# Disponibilização de Processo Seletivo no portal - Data fim\ disponivel na internet

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | TOTVS Educacional |
| **Módulo:** | Processo Seletivo |
| **Função:** | Inscrição |
| **Situação/Requisito:** | Cliente informa que o processo seletivo tem o seguinte calendário de Inscrição: 01/01/2018 a 30/09/2018, com 2 formas de inscrição cadastradas nesse processo, sendo uma para internet e outra presencial. A forma de inscrição "presencial" está com o parâmetro "disponível para internet" desabilitado e com data de utilização entre 01/01/2018 a 30/09/2018, ou seja, disponível até a data fim do período de inscrição do processo seletivo. A forma de inscrição "Internet" está com o parâmetro "disponível para internet" marcado e com data de utilização entre 01/01/2018 a 19/09/2018, ou seja, 11 dias a menos que a data fim do período de inscrição do processo seletivo. Com o sistema configurado dessa forma, o candidato consegue acessar o processo seletivo pelo portal, preencher os dados pessoais, e somente no final da inscrição o mesmo não consegue selecionar a forma de inscrição, pois não existe nenhuma forma de inscrição disponível. Assim o Candidato efetua um preenchimento desnecessário, criando uma falha de disponibilidade do recurso. Solicita que o portal efetue essa consistência da data de inscrição online antes do candidato começar a digitar a inscrição do processo. |
| **Solução/Implementação:** | Foi realizado ajuste para realizar a consistência da forma de inscrição no portal, levando em consideração a data início e fim da mesma, em relação a data de inicio e fim da inscrição. Caso aconteça o cenário acima, o portal não exibirá mais a opção de inscrição. O processo seletivo continuará sendo exibido no portal mas sem a opção para realizar inscrição. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A |
| **Documento de Referência:** | N/A |
