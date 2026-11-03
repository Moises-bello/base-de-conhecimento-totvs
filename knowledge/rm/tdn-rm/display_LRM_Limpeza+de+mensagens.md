---
content_hash: fe0739c7594a0c0a2e262720ccaf7fdb34eecc8c86ac1b490264eebc8207d7b5
fetched_at: '2026-06-29T00:11:40.465905+00:00'
page_id: '794393609'
product: rm
source: tdn-rm
title: Limpeza de mensagens
type: documentation
url: https://tdn.totvs.com/display/LRM/Limpeza+de+mensagens
version: 5
---

Funcionalidade para sanitizar a base de dados removendo as mensagens nas seguintes tabelas:

* GEAIMENSAGEM, as mensagens.
* GEAIROTAMENSAGEM, informação de rota de mensagem.
* GEAIEXECROTAMENS, informação de execução de rota de mensagem.
* GEAIROTALOGMENSAGEM, informação de log de rota de mensagem.

**Opções de exclusão:**

* Exclui mensagens processadas com sucesso  
  Opção padrão que remove todas as mensagens com status igual a Processadas com Sucesso, até a data do dia anterior da execução do processo de limpeza.  
  Ex: Caso a execução de limpeza seja solicitada para hoje, serão excluídas todas as mensagens até ontem.
* Exclui mensagens síncronas processadas com erro  
  Remove todas as mensagens com status igual a Processadas com Erro e tipo de entrega igual a síncrono, até a data do dia subtraído da quantidade de dias informados no campo de Número de dias corridos.  
  Exe: Caso a execução de limpeza seja solicitada para o dia 11/10/2023, serão excluídas todas as mensagens até 01/10/2023 (dia 11 menos 10 dias corridos, igual a 1).   
          Para limpar as mensagens do dia corrente, informe Zero(0), no campo Número de dias.  
  Obs: As mensagens síncronas são as mensagens definidas com o Tipo de Entrega igual a Síncrono!
* Exclui mensagens assíncronas processadas com erro   
  Remove todas as mensagens com status igual a Processadas com Erro e tipo de entrega igual a Assíncrono, até a data do dia subtraído da quantidade de dias informados no campo de Número de dias corridos.  
  Exe: Caso a execução de limpeza seja solicitada para o dia 11/10/2023, serão excluídas todas as mensagens até 01/10/2023 (dia 11 menos 10 dias corridos, igual a 1).   
          Para limpar as mensagens do dia corrente, informe Zero(0), no campo Número de dias.  
  Obs: As mensagens assíncronas são as mensagens definidas com o Tipo de Entrega igual a Assíncrono!  
          Esta opção também valida a quantidade de tentativas de execução, de acordo com a configuração informada.

Informações

Caso as tabelas contenham uma quantidade significativamente grande de registros, pode ser necessário configurar o Host,  aumentando o tempo de espera com o banco de dados (Time Out).

A tag DBSCommandTimeout, pode ser utilizada para aumentar o tempo de espera de um comando update, insert ou delete.  
A tag ConnectionTimeOut, para aumentar o tempo de espera para a conexão com a base de dados.

O processo de limpeza realiza 5 passos, o primeiro marca os registros para serem excluídos e os passos seguintes realizam a exclusão em cada tabela.  
Para SQLServer o processo é realizado em Lote.
