---
content_hash: 17fbbe6e9adc4177ab6ef8dba98c82f5d159d7fc150f24b0dd9592d7d064e2d5
fetched_at: '2026-06-29T00:09:28.062559+00:00'
page_id: '423938642'
product: rm
source: tdn-rm
title: Atualização do Participante nos Lançamentos Contábeis
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938642
version: 2
---

*Atenção!*  
   
Esta funcionalidade só está disponível para as bases já migradas para o Novo Modelo do BackOffice.  
   
O processo de Atualização do Participante nos Lançamentos Contábeis consiste em rastrear a origem da contabilização em sistemas externos que através das suas movimentações enviam a contabilização para o Gestão Contábil e identificar o Cliente/Fornecedor ou Filial utilizado na origem, depois verificar se eles estão cadastrados como Participante e por último atualizar o campo "Participante" das partidas dos respectivos lançamentos contábeis. Esta atualização será realizada conforme dados informados no cadastro do Participante, tais como Data Inicial e Data Final de relacionamento que deve abranger a data do lançamento, o processo válido para o relacionamento e o período indicado para execução do processo.

Caso seja necessário efetuar manutenção nos dados de algum Participante já cadastrado, o status deste passará para 'Atualização Pendente', mesmo que a associação deste com os lançamentos contábeis já tenha sido realizada anteriormente, sendo necessário executar este processo para atualização das associações e do status, que passará para 'Atualizado'.

**Importante:** O processo de geração do SPED Contábil somente será executado se o status de todos os Participantes cadastrados na base estiver igual à 'Atualizado'.

Quando o processo for executado e a *data* dos lançamentos a serem atualizados *não* estiver entre o período de relacionamento com o Participante e a contabilização estiver com o campo Participante preenchido, o sistema irá remover o vínculo com estes lançamentos, limpando o campo Participante.

Quando o processo for executado e caso seja necessário atualizar o Participante em Lançamentos/Partidas que estejam agrupadas (**veja Agrupamento de Lançamentos**), o sistema irá realizar um 'desagrupamento', removendo dos lançamentos/partidas agrupadas as partidas que deverão ser atualizadas, gerando então novas partidas desagrupadas no mesmo lançamento, contendo as mesmas informações originais, mas com o campo Participante devidamente preenchido e ao mesmo tempo atualizará os valores remanescentes da partida agrupada.

**Considerações:**

* Partidas originadas do RM Saldus não terão o campo Participante atualizado automaticamente por este processo, esta atualização deverá ser feita manualmente pelo usuário.
* Inicialmente este processo atualizará as contabilizações originadas de sistemas que já migraram para o novo modelo de BackOffice:  
     
  RM Nucleus - Movimento  
  RM Bonum - Avaliação de Bens / Leasing   
  RM Classis - Contabilização Contrato / Parcela  
  RM SGI - Módulo de Financiamento  
  RM Fluxus - Aplicação Financeira / Baixa Lançamento
