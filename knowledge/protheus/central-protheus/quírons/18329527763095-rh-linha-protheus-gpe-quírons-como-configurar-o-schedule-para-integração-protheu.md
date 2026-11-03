---
article_id: 18329527763095
category: Quírons
content_hash: b7eae8effcb9744a4fb7ca322065b5f8d18eacfe3b66aebbfb08c6dbc2ccd83d
fetched_at: '2026-06-28T22:42:52.136818+00:00'
product: protheus
section_id: 9033517492119
source: central-protheus
title: RH - Linha Protheus - GPE - Quírons - Como configurar o Schedule para integração
  Protheus x Quírons
type: support-article
updated_at: '2025-04-16T11:03:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18329527763095-RH-Linha-Protheus-GPE-Qu%C3%ADrons-Como-configurar-o-Schedule-para-integra%C3%A7%C3%A3o-Protheus-x-Qu%C3%ADrons
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18329561569303) Tempo aproximado para leitura: **00:03:00 min****Dúvida**Como configurar o ***Schedule*** para **integração** **Protheus x Quírons?**  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**O cadastro do ***Schedule*** para **integração** é utilizado para validar os **registros gerados na tabela RJP** e integrá-los do Protheus para o Quirons.  
O cadastro deve ser feito no **Configurador**, seguindo os passos abaixo:  
  
**1 -** Acessar **Ambiente > Schedule > Schedule:**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31451742343703)  
  
  
**2 -** Primeiramente, deve ser criado um **Agente** para o **Grupo de Empresas** que terá integração com o Quírons. Para isso, clique na opção Agentes localizada no menu à esquerda:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31451771739543)  
  
  
**3 -** Clique em **Novo** e preencha os campos conforme abaixo:  
**> Descrição:** campo livre, é o nome do seu Agente  
**> *Status*:** habilitado  
**> IP:** deve ser informado o IP do servidor onde o *Schedule* será executado  
**> Porta:** deve ser informada a porta TCP do appserver.ini do serviço encarregado de executar o *Schedule*  
**> Número de *threads:*** a quantidade de *threads* impacta diretamente na performance do Produto, ou seja, informar um número que não seja comportado pelo seu servidor terá efeito reverso: trará mais lentidão e travamentos ao processo, portanto, deve ser feita uma análise criteriosa pelo time interno de TI  
**> Empresa:** deve ser selecionado o Grupo de Empresas que terá integração com o Quírons  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31451771739927)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31451742346391)  
  
  
**4 -** Por fim, deve ser criado o **Agendamento** para que a integração seja executada. Para isso, clique na opção Agendamentos localizada no menu à esquerda:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31451771740951)  
  
  
**5 -** Clique em **Novo** e preencha os campos conforme abaixo:  
**> Rotina:** deve ser informado GPEM923  
**> Dia/Horário:** a primeira vez que o job será executado  
**> Periodicidade:** determina como os *jobs* devem ser executados. Para o Quírons, não existe restrição em deixar selecionada a opção Sempre Ativo, ou seja, sempre que existirem registros novos na tabela RJP, o Protheus tentará integrar os dados para o Quírons  
**> Empresa:** selecione o Grupo de Empresas que terá integração com o Quírons  
**> Filial:** selecione as Filiais do Grupo de Empresa que terão integração com o Quírons  
**> Módulo:** deve obrigatoriamente ser selecionado 7 - Gestão de Pessoal  
**> Usuário:** será preenchido automaticamente com o usuário logado no CFG no momento do cadastro  
**> Descrição:** pode ser utilizado para nomear o *job*, porém, não é de preenchimento obrigatório  
**>** Por fim, confira os detalhes do seu agendamento. Se não for necessário nenhum ajuste, basta **Concluir.**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31451771741591)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31451771742103)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31451771742999)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31451742350487)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31451742351255)  
  
  
**6 -** Com isso, o *job* está pronto para iniciar as integrações entre o Protheus e Quírons:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31451771745815)  
  
  
**7 -** No appserver.ini, é possível verificar a busca de dados na RJP:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31451742354071)**Saiba Mais:**  
[Schedule - Como agendar a execução de rotinas](https://tdn.totvs.com/pages/releaseview.action?pageId=271167961)[Integração | Protheus SIGAGPE x Quírons](https://tdn.totvs.com/pages/releaseview.action?pageId=793200883#Integra%C3%A7%C3%A3o|ProtheusSIGAGPExQu%C3%ADrons|-05.CARGAINICIAL)  
[Artigos sobre Quírons](https://centraldeatendimento.totvs.com/hc/pt-br/sections/9033517492119-Qu%C3%ADrons)
