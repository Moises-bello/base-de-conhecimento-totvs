---
content_hash: a9da5d1444efb0a29c3f69b19509dfa64818589b4ae9af561abbc062826e5e00
fetched_at: '2026-06-29T00:09:24.444317+00:00'
page_id: '423937909'
product: rm
source: tdn-rm
title: Informações do Cálculo do MRPII
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423937909
version: 1
---

**Informações do Cálculo do MRPII**   
Através da janela de edição do item da ordem de produção, ao clicar no botão "Calcula" será feito o cálculo do caminho crítico ou cálculo do MRPII. Este cálculo visa informar a data prevista de início e término das atividades.   
Interferem no cálculo do MRPII:  
**Lote de Transporte** Definido na janela de edição do posto de trabalho, na pasta Estrutura, subpasta Lote de Transporte. É possível cadastrar vários lotes de transporte para uma única estrutura, pois a mesma pode ser transportada para postos diferentes. Ao calcular o MRPII, os lotes de transporte podem interferir na data início/fim das atividades dependentes. A dependência é criada através da prioridade informada para as atividades na janela de edição da atividade (propriedades relativas à estrutura).  
**Lote de Produção** Definido na janela de edição de estrutura, na pasta "Atividades", subpasta "Equipamentos Utilizados na Atividade" ou na subpasta "Postos aonde realizo as Atividades". Isso significa que o lote de produção deve ser definido por equipamento ou por posto. O lote de produção indica a quantidade produzida pelo equipamento ou pelo posto, nas atividades e estruturas. A capacidade produtiva do lote de produção é a quantidade máxima que o equipamento ou o posto produz. O tipo do lote de produção pode ser mínimo ou múltiplo. Lote mínimo é aquele onde é necessário produzir uma quantidade mínima para não haver prejuízo. Lote múltiplo é aquele onde é possível produzir uma quantidade múltipla de um número qualquer.  
No cálculo do MRPII, os lotes de produção podem interferir na data início/fim das atividades dependentes.  
No cálculo do MRPII, o calendário da linha interfere na data início/fim das atividades, pois o mesmo considera os turnos de funcionamento e as paradas definidas. Caso a atividade inicie em um turno e não seja possível concluí-la no mesmo turno, a mesma é deslocada para o próximo turno de trabalho.
