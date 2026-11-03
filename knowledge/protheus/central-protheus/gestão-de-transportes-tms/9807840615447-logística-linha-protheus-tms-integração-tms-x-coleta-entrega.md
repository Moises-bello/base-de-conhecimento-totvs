---
article_id: 9807840615447
category: Gestão de Transportes (TMS)
content_hash: ee000b77000a2f4f9d5e6b6aefaf6ac2cbac176c26a46e9dd755d52fcb19934e
fetched_at: '2026-06-28T22:45:29.360836+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Integração TMS x Coleta Entrega
type: support-article
updated_at: '2023-08-14T14:27:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9807840615447-Log%C3%ADstica-Linha-Protheus-TMS-Integra%C3%A7%C3%A3o-TMS-x-Coleta-Entrega
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16673672773015) Tempo aproximado para leitura: **00:02:50 min** **Dúvida**Como funciona e como configurar a integração do **TMS x Coleta Entrega**?   
  
**Ambiente**TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**O **TOTVS Coleta Entrega** permite que Sistemas externos produzam diversas melhorias a serem apontadas via *mobile*. A utilização da integração entre o módulo **TOTVS Logística TMS** e o **TOTVS Coleta Entrega**, permite diversas ações além de complementar o processo de **Apontamento do Comprovante de Entrega**, conforme abaixo:

* Obter os dados obrigatórios para a transmissão do evento de comprovante de entrega para a **SEFAZ - Secretaria da Fazenda**;
* **Diário digital**: O registro dos eventos que ocorrem com os motoristas durante a execução de viagem de coletas e entregas;
* **Informação em tempo real**: Saber o que está acontecendo naquele exato momento com motorista/entrega, e como os eventos que estão ocorrendo podem impactar as próximas tarefas.
* **Comunicação**: Facilitar, simplificar, agilizar, unificar canais e tornar fluído o processo de pedir orientação e ajuda de acordo com a situação com a qual o motorista se depara durante a execução de suas tarefas.
* **Digitalização documentos**: Além de obtenção de dados obrigatórios para a transmissão do evento de comprovante de entrega para a **SEFAZ**, possibilidade de registro de outras fotos complementares , como documento/carga entregue, evidências de inconformidades que gerarão reentregas ou devoluções, informações de geolocalização e rubrica digital.
* Registro de ocorrências no módulo **TOTVS Logística TMS**, para **confirmação** dos processos de coleta e/ou entrega bem como registro de ocorrências para processos **não concluídos com sucesso**, como ocorrências que reportam retorno de documento/carga;
* Acesso a digitalização do documento comprovante de entrega digitalizado no módulo **TOTVS Logística TMS**;

A integração permite maior proximidade entre motoristas e planejadores por meio de automações e troca de mensagens em tempo real.  
  
Esta funcionalidade/integração será liberada no dicionário oficial da *release* 12.1.2310 e atende uso nas Viagens Modelo 2 e Modelo 3.  
  
Para acessar detalhes do processo de integração do **TMS x Coleta Entrega**, verifique a documentação [Integrações Coleta Entrega](https://tdn.totvs.com/pages/releaseview.action?pageId=697715345) e suas documentações associadas.  
Para uso desta funcionalidade, deve ser atualizado seu ambiente na seguinte ordem, para evitar possíveis erros de atualização:

* **Pacote: 010555** - Para atualização de dicionário de dados, criação de novas tabelas, campos, índices e gatilhos.
* **Pacote: 011015** - Utilizado na integração do **TOTVS Logística TMS x****Portal Logístico.**
* **Pacote: 011339** **-** Utilizado na integração do **SIGAFAT - Faturamento x** **TOTVS Logística TMS**
* **Pacote: 011212**- Para atualização menu (Em caso de uso pelo faturamento, deve-se obrigatoriamente alterar o módulo dos fontes via Configurador (SIGACFG) do menu)
* Caso deseje utilizar layout padrão, os mesmos podem ser baixados automaticamente. Caso haja necessidade, podem ser baixados manualmente:
  + [01 - TMS COLETA ENTREGA](http://manifest.engpro.totvs.com.br/01.lay)
  + [03 - OMS COLETA ENTREGA](http://manifest.engpro.totvs.com.br/03.lay)
  + [04 - TMS PORTAL LOGISTICO](http://manifest.engpro.totvs.com.br/04.lay)
  + [05 - FAT COLETA ENTREGA](http://manifest.engpro.totvs.com.br/05.lay)
* Pacotes **DLOGTMS02-22574** com os fontes atualizados das rotinas envolvidas das versões 12.1.27, 12.1.33 e 12.1.2210 em anexo.

**Anexo**
