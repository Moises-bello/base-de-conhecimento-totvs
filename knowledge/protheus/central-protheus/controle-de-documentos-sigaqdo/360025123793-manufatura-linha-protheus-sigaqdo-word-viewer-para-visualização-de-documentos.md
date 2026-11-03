---
article_id: 360025123793
category: Controle de Documentos (SIGAQDO)
content_hash: 3a778e80d676072dc5e8ef399dc3a54d646dce4a9a11ca21be1f142528832aff
fetched_at: '2026-06-28T22:42:29.982075+00:00'
product: protheus
section_id: 360005906113
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQDO - Word Viewer para visualização de documentos
type: support-article
updated_at: '2025-06-26T14:19:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025123793-Manufatura-Linha-Protheus-SIGAQDO-Word-Viewer-para-visualiza%C3%A7%C3%A3o-de-documentos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33070502710807) Tempo aproximado para leitura: **00:02:30 min**  
 **Dúvida**Como configurar o **Microsoft Word Viewer** para a visualização de documentos no módulo **Controle de Documentos - SIGAQDO**?   
  
**Ambiente**  
TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Controle de Documentos (SIGAQDO) - Todas as versões  
  
**Solução**Para utilizar o **Microsoft Word Viewer**, siga os passos a seguir:  
  
1. Na rotina de **QAXA010 - Cadastro de Usuários**, altere o registro do usuário e preencha o campo **Tipo Word - QAA\_TPWORD** com o conteúdo **2 - WordView**.  
  
2. Copie o arquivo **ADVVIEW.EXE** disponível no anexo, para as pastas do **smartclient** e **system** da instalação do **Protheus**, que respectivamente estão nos diretórios: **\bin\SmartClient** e **\Protheus\_Data\system**.  
  
3. Instale o *software* **Microsoft Word Viewer 2003** no computador de todos os usuários que utilizarão este visualizador. Deve ser utilizado o mesmo diretório de instalação para todos os usuários. Sugerimos que seja instalado no diretório **C:\Office**.  
  
4. Preencha os parâmetros conforme listado a seguir:

* **MV\_QDPVIEW - Define o diretório onde o WordView foi instalado**= C:\Office\ .
* **MV\_QDVIEW - Define se o WordView será usado para consultar os Documentos gerados pelo Sistema** **= S.**
* **MV\_QDPRVW - Determina se será utilizado o Preview na visualização dos documentos, sendo: 1 - Não , 2 - Sim** **= em branco.**
* **MV\_QPATHWT - Define o diretório do Client onde ficarão os  documentos gerados pelo Sistema** **= GETTEMPPATH().**

**Importante**Como a ferramenta **Totvs Office Viewer** foi descontinuada pela **Microsoft**, o parâmetro **MV\_QDPRVW** deve ter conteúdo igual a **1**.  
  
**Observação**  
A solução apresentada neste artigo é válida até a *release* 12.1.2310. Para a *release* 12.1.2410 ou superiores, a [Integração com Wordview](https://tdn.totvs.com/pages/releaseview.action?pageId=306850272) foi descontinuada. Como solução, na rotina de **QAXA010 - Cadastro de Usuários** deverá utilizar o campo **QAA\_TPWORD** com o conteúdo **3 - MS Word ou 4 - Interna no ERP.**  
**Complemento**  
[Manufatura - Linha Protheus - SIGAQDO - Habilitar leitura de documento em PDF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/8930709565847-Manufatura-Linha-Protheus-SIGAQDO-Habilitar-leitura-de-documento-em-PDF)  
  
**Saiba mais**  
Para mais informações referente a ferramenta **Totvs Office Viewer** consulte o artigo [Manufatura - Linha Protheus - SIGAQDO - DLL não localizada em \SYSTEM\MODELOS\](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026252314-MP-QUA-DLL-n%C3%A3o-localizada-em-SYSTEM-MODELOS-)  
  
**Anexo**Copie o arquivo **ADVVIEW.EXE** para as pastas do **smartclient** e **system** da instalação do **Protheus**.
