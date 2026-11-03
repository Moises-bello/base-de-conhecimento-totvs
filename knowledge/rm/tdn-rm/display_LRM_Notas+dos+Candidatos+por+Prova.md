---
content_hash: 9dc3dd6e0240832dfa3c8090d2445b5829a10c9edb3a0b7456373557f184699c
fetched_at: '2026-06-29T00:09:29.842095+00:00'
page_id: '425458308'
product: rm
source: tdn-rm
title: Notas dos Candidatos por Prova
type: documentation
url: https://tdn.totvs.com/display/LRM/Notas+dos+Candidatos+por+Prova
version: 2
---

Esse serviço deverá ser usado, principalmente, em Processos Seletivos Agendados. Nessa modalidade de processo seletivo os candidatos, na maioria das vezes irão fazer a prova "no papel". Ou seja, não será usado o RM Executor e nem o gabarito será transcrito para um arquivo a ser lido. Sendo assim, sempre que houver a necessidade de informar a nota de um candidato manualmente, a entrada de "Notas dos Candidatos por Prova" será uma das opções a ser utilizada. A entrada "Notas das Provas por Candidato" também poderá ser usada.  
 Na visão deste serviço exibirá as provas cadastradas no TOTVS Avaliação e Pesquisa que possuem execuções pendentes de candidatos. Ou seja, toda prova que esteja para ser feita por alguma pessoa inscrita na prova será exibida. O usuário poderá selecionar a prova que deseja executar o processo "Entra nota de candidato por prova". Em seguida será exibida a listagem com todas as pessoas inscritas e será permitido digitar a nota de cada uma delas, podendo filtrar os candidatos por Local do processo seletivo e/ou Área ofertada. Quando sistema for parametrizado para não realizar importação de notas de candidatos ausentes no dia da prova, não será permitido a entrada de nota para candidatos ausentes no dia prova.  
 Para Classificar candidatos com este tipo de lançamento de nota, deverá executar o processo de classificação de candidatos, deve-se escolher a opção de classificação por Nota- Entrada Manual de notas.  
    
 Quando este serviço for acionado especificamente do Totvs Educacional irá ocorrer contextualização de filial. Isso quer dizer que, "apenas" provas que possuem candidatos que pertençam a processos seletivos VISÍVEIS para todas as filiais ou provas pendentes da filial logada é que serão exibidas na visão.
