---
article_id: 9938568835863
category: Gestão de Transportes (TMS)
content_hash: 2d66cceff2e882d4cf88d4eb7a3cbcf37ac7623eecf8749b3cec1730c51a156e
fetched_at: '2026-06-28T22:45:27.322389+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Cadastros básicos para geração de viagem
type: support-article
updated_at: '2024-05-17T12:19:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9938568835863-Log%C3%ADstica-Linha-Protheus-TMS-Cadastros-b%C3%A1sicos-para-gera%C3%A7%C3%A3o-de-viagem
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:10 min** **Dúvida**Quais os cadastros principais para gerar viagem no **TOTVS Logística TMS**?  
  
**Ambiente**TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**Considerando que já possui documentos gerados, é necessário que possua os seguintes cadastros para gerar a viagem e realizar seu processo até o encerramento:

* **Atualizações/ Cadastros/ Fornecedores - MATA020**. É necessário cadastrar o fornecedor proprietário do veículo que será utilizado na viagem e o fornecedor relacionado ao motorista. Independente da frota do veículo e motorista, podendo ser própria, terceiro ou agregado, é necessário possuir um fornecedor.
* **Atualizações/ Transporte/ Motoristas - OMSA040.** Cadastre um motorista para utilizar na viagem, preenchendo os dados do motorista como nome e **CPF - Cadastro de Pessoa Física**, fornecedor e frota.
* **Atualizações/ Transporte/ Tipos de Veículos - TMSA530.** Cadastre os tipos de veículos necessários para sua operação. Considere a documentação [Tipos de Veículos (TMSA530 - SIGATMS)](https://tdn.totvs.com/pages/releaseview.action?pageId=545650447) para cadastrar os tipos de veículos.
* **Atualizações/ Transporte/ Veículos - OMSA060.** Cadastre um veículo para utilizar na viagem, preenchendo os dados do veículo como placa, motorista, frota, proprietário e tipo de veículo.
* **Atualizações/ Serviços/ TarefasxAtividades - DLGA080.**Cadastre uma tarefa com saída e chegada de viagem para a filial.
* **Atualizações/ Serviços/ ServiçosxAtividades - DLGA070.**Cadastre um **serviço operacional** que deve conter a tarefa configurada anteriormente.
* **Atualizações/ Logística/ Zonas - OMSA070.**Cadastre uma zona para vincular à rota, conforme documentação [Zonas (OMSA070 - SIGATMS)](https://tdn.totvs.com/pages/releaseview.action?pageId=464948751)
* **Atualizações/ Logística/ Setores por Zona - OMSA080.** Cadastre setores por zona para vincular à rota, conforme documentação [Setores Por Zona (OMSA080 - SIGATMS)](https://tdn.totvs.com/pages/releaseview.action?pageId=464948802)
* **Atualizações/ Logística/ Pontos por Setor - OMSA090.**Cadastre pontos por setor para vincular à rota, conforme documentação [Pontos Por Setor (OMSA090 - SIGATMS)](https://tdn.totvs.com/pages/releaseview.action?pageId=464948826)
* **Atualizações/ Logística/ Rotas - OMSA100.**Cadastre uma rota para ser utilizada na viagem, preenchendo a região de origem da rota e o serviço operacional cadastrado anteriormente.
