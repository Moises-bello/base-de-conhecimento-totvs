---
article_id: 360021312352
category: Gestão de Transportes (TMS)
content_hash: 28a342a337f43d8521c446f104aed43eb0f7970e988da3efc97308b2cc0ba7d3
fetched_at: '2026-06-28T22:45:27.710895+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Encerramento de Processo sem Viagem
type: support-article
updated_at: '2023-08-28T11:48:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021312352-Log%C3%ADstica-Linha-Protheus-TMS-Encerramento-de-Processo-sem-Viagem
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17081367269399)*** Tempo aproximado para leitura: **00:01:50 min  
  
Dúvida**Como encerrar um documento sem a necessidade de gerar uma viagem de entrega?  
  
**Ambiente**TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**Para executar o processo, é necessário saber qual é a filial, número e série do Documento a ser encerrado. Para isso, é possível consultar através da rotina **TMSA500 - Manutenção de Documentos**, onde o mesmo estará com o *Status* **Aberto*.***

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360018339192)

Para apontarmos a ocorrência, seguiremos os seguintes passos:

* Na rotina **TMSA020 -****Tabela de Ocorrências**, verifique se existe alguma ocorrência com as seguintes informações:  
  - **Tipo - DT2\_TIPOCO** = 01 - Encerra Processo  
  - **Categoria - DT2\_CATOCO** = 1 - Por Docto  
  - **Oco.Ativa -** **DT2\_ATIVO** = 1 - Sim
* Caso não exista alguma, cadastre.
* Acesse a rotina **TMSA360 -****Registro de Ocorrências** e clique no botão **apontar**.
* Selecione a filial do documento a ser encerrado.
* Preencha os seguintes campos:  
  - **Data Ocorre. -** **DUA\_DATOCO,**podendo ser o dia atual.  
  - **Hora Ocorre. - DUA\_HOROCO,** podendo ser a hora atual.  
  - **Cod. Ocorre. - DUA\_CODOCO**, sendo o código de ocorrência existente informado nos itens 1 e 2.  
  - **Filial - DUA\_FILDOC**, **Documento -** **DUA\_DOC** e **Série - DUA\_SERIE,** do documento a ser encerrado.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360018339232)

* Após preenchimento, clicar em **salvar**.
* Ao voltarmos para a rotina **Manutenção de Documentos** e consultarmos o Documento, podemos verificar que agora, o *Status* dele mudou para **Entregue**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360018339272)

Para entendermos os *Status* dos Documentos, segue abaixo descrição:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360018339292)
