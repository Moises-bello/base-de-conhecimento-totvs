---
content_hash: 66a9b8fcd3118aae4d49cd5586ffac05235e6d1e83eabb13871f4544806a358a
fetched_at: '2026-06-29T00:09:21.191816+00:00'
page_id: '422545858'
product: rm
source: tdn-rm
title: Consulta Autorização/Cancelamento Automático (JOB Server)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422545858
version: 4
---

A consulta das autorizações e Cancelamentos das NFS-e deve ser feita manualmente para cada registro ou para vários. Para otimizar o processo ele poderá ser agendado para um horário no qual não carregue o tráfego de dados na rede e que não existam usuários logados no RM.  
 Este processo geralmente é utilizado por emissores de grande quantidade de NFS-e e é aplicável quando o  RM está configurado em [Ambiente de Três Camadas](http://tdn.totvs.com.br/display/connect/2012/10/23/Como+Fazer+-+Configurando+um+Ambiente+3+Camadas)[.](http://tdn.totvs.com.br/display/rm/2012/12/06/Como+Fazer+-+Configurando+um+Ambiente+3+Camadas) Ainda para seu correto funcionamento deve ser habilitado e configurado o [Job Server](http://tdn.totvs.com.br/display/connect/2012/10/23/Como+Fazer+-+Configurando+um+Ambiente+3+Camadas).  
 Após ter configurado os pré-requisitos siga os passos abaixo:

1. Acesse a visão das NFS-e.
2. Efetue  o envio de todas a NFS-e.
3. Crie um filtro para selecionar somente as NFS-e que irão ser consultadas, execute-o e selecione todos os registros.
4. Nos Processos escolha Consulta Autorização/Cancelamento Automático JOB.
5. No wizard que será apresentado clique no botão Opções que está localizado no canto inferior esquerdo da Tela e desmarque a opção Aguardar Execução do Processo. Em seguida clique em Avançar.
6. Na tela seguinte informe os dados do agendamento como a Data e a  Hora. Clique em executar para concluir o processo.
7. Nada acontecerá com os registros das NFS-e de imediato. Elas só serão consultadas na hora agendada no Job.

O resultado da execução do Job pode ser consultado acessando a última execução do Job em Ambiente Z Gerenciamento de Jobs. Crie um filtro para o seu Job para facilitar sua consulta, edite-o e analise seu log para verificar o motivo de notas não terem sido autorizadas se for o caso.  
**Este processo será melhor aproveitado se ao ser criado Job não forem selecionados registros na visão. Desta forma será criado um Job que ficará rodando e se no horário agendado existirem NFS-e pendentes elas serão consultadas.**  
***Atenção!*** Aconselha-se criar um agendamento sempre para ser executado durante a noite ou em horários de menor uso do RM. Se a necessidade da autorização for imediata execute o processo normal de Consulta de Autorização da NFS-e.
