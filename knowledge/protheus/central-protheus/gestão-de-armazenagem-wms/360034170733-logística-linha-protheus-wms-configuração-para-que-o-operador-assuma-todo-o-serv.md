---
article_id: 360034170733
category: Gestão de Armazenagem (WMS)
content_hash: 01f8753edca2c742aa3dbb5f86173bbcc87c1b23b3c76ff0fdba6793b75e7ba5
fetched_at: '2026-06-28T22:45:47.997262+00:00'
product: protheus
section_id: 206962247
source: central-protheus
title: Logística - Linha Protheus - WMS - Configuração para que o operador assuma
  todo o serviço de um documento
type: support-article
updated_at: '2025-10-31T19:57:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034170733-Log%C3%ADstica-Linha-Protheus-WMS-Configura%C3%A7%C3%A3o-para-que-o-operador-assuma-todo-o-servi%C3%A7o-de-um-documento
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36023930668055)**Tempo aproximado para leitura: **00:00:54 min****Dúvida**Qual é a configuração para que o operador assuma todo o serviço de um documento?  
  
**Ambiente**TOTVS Logística - TOTVS WMS (Linha Protheus) - Gestão de Armazenagem (WMS) - A partir da versão 11.80  
  
**Solução**Deve ser cadastrada uma **Regra de Convocação - WMSA350**, do tipo **limite**, indicando o funcionário e também apontando a execução da atividade do documento ou da carga exclusivamente para um único operador do coletor de dados - **DCQ\_DOCEXC - Doc Exclusiv**.  
  
A **regra de convocação** por documento exclusivo, quando aplicada em conjunto com a limitação por zona de armazenagem poderá impedir a convocação do documento por completo, caso existam movimentos em outras zonas de armazenagem, nas quais o operador não tem acesso.  
  
**Saiba mais**Informações adicionais podem ser obtidas no documento: [Configuração para que o operador assuma todo o serviço de um documento.](https://tdn.totvs.com/pages/viewpage.action?pageId=654945578)  
Também assista ao *Webinar* sobre o cadastro **Regras de Convocação**: [Webinar TOTVS | Regras para a Convocação WMS](https://www.youtube.com/watch?v=TgvM8CA5LpA)
