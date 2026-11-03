---
article_id: 360025373131
category: Gestão de Transportes (TMS)
content_hash: 11eb09d20d34447815cf6e1b752d19b2fc1ec792c6c29e98e3ad2923e1248d9b
fetched_at: '2026-06-28T22:45:29.333101+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Informações e parametrizações sobre MDF-e
type: support-article
updated_at: '2024-06-21T12:05:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025373131-Log%C3%ADstica-Linha-Protheus-TMS-Informa%C3%A7%C3%B5es-e-parametriza%C3%A7%C3%B5es-sobre-MDF-e
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24334396035479)** Tempo aproximado para leitura:**00:01:45 min****Dúvida**Quais as parametrizações e informações importantes sobre o **MDF-e - Manifesto Eletrônico de Documentos Fiscais?**  
  
**Ambiente**TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**  
**Cadastros**

* Cadastrar **Tarefa x Atividades - DLGA080**
  + Criar descrição para tarefas de saída e chegada na tabele **L2** do **SX5**;
  + Tarefa para atividade de saída da filial;
  + Tarefa para atividade de chegada da filial.
* Cadastrar **Serviços x Tarefas - DLGA070**
  + Criar descrição do serviço na tabela **L4** do **SX5**;
  + Relacionar as tarefas de saída e chegada ao serviço.
  + Cadastrar **Zona - OMSA070**;
  + Cadastrar **Setor por Zona - OMSA080**;
  + Cadastrar **Pontos por Setor - OMSA090**;
  + Cadastrar **Rota - OMSA100** utilizando o **Serviço**, **Zona** e **Setor** cadastrados anteriormente;
  + Cadastrar **Ocorrências - TMSA020**, para utilizar no encerramento da viagem.

**Parâmetros**

* **MV\_MDFEEXC -**Este parâmetro permite definir o prazo em horas para o cancelamento do **MDF-e** após autorizado;
* **MV\_MDFEDOC -** Este parâmetro permite definir os **Tipos de Documentos de Transporte** que não serão transmitidos à **SEFAZ - Secretaria de Estado da Fazenda**;
* **MV\_SERMAN -** Série do manifesto;
* **MV\_TMSHRVR -** Define se encontra-se no período de horário de verão;
* **MV\_TMSHRFL -** Define Filiais que não aderiram ao horário de verão e/ou possuem diferença de fuso;
* **MV\_ESTADO -** Define o estado da filial;
* **MV\_MDFECAN** - Habilita a exclusão do manifesto somente após a autorização do cancelamento do **MDF-e** pela **SEFAZ**.

**RDMAKE**

* **MDFSEFAZ3**  
  Responsável pela geração do **XML - *Extensible Markup Language****.*
* **RTMSR34**Responsável pela impressão do **DAMDF-e - Documento Auxiliar do Manifesto Eletrônico de Documentos Fiscais**

**Pontos de entrada:**

* [TME73LST](https://tdn.totvs.com.br/pages/releaseview.action?pageId=612546633)
* [TME73CAB](https://tdn.totvs.com.br/pages/releaseview.action?pageId=612546722)
* [TME73ALT](https://tdn.totvs.com.br/pages/releaseview.action?pageId=525023462)
* [TME73ENC](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025092012-MP-TMS-Ponto-de-entrada-TME73ENC-Sele%C3%A7%C3%A3o-do-MDF-e)
* [TME73BUT](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025385391-MP-TMS-Ponto-de-entrada-TME73BUT-Inclus%C3%A3o-de-bot%C3%B5es-no-painel-da-rotina-MDF-e)

**Saiba mais**[Logística - Linha Protheus - TMS - Procedimento para emitir um MDF-e para CT-e](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019631891-Log%C3%ADstica-Linha-Protheus-TMS-Procedimento-para-emitir-um-MDF-e-para-CT-e)
