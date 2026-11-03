---
article_id: 360021108932
category: Controle de Documentos (SIGAQDO)
content_hash: bd3214aab1d11c1ce79637562e5289fa1b36e0888937d6a4ef5cdee5ac6869f3
fetched_at: '2026-06-28T22:42:29.062679+00:00'
product: protheus
section_id: 360005906113
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQDO - Exclusão de documento
type: support-article
updated_at: '2024-05-27T16:35:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021108932-Manufatura-Linha-Protheus-SIGAQDO-Exclus%C3%A3o-de-documento
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16257912044311)**Tempo aproximado para leitura:**00:01:25 min****Dúvida**Como excluir um documento cadastrado no módulo **SIGAQDO - Controle de Documentos**?  
  
**Ambiente**  
TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Controle de Documentos (SIGAQDO) - Todas as versões  
  
**Solução**Na rotina **QDOA050 -****Cadastro de Documentos**, selecione o documento que deseja excluir e clique no botão **Outras Ações** > **Excluir**. Será aberta uma mensagem para o usuário confirmar a exclusão.   
  
**Importante**Somente é possível excluir um documento se:

* O mesmo não tiver sido distribuído;
* Que esteja em fase de **Em Elaboração** que compreende as etapas de **Digitação**, **Elaboração**, **Revisão**, **Aprovação**, **Homologação**, **Elaboração com Críticas** e **Digitação com Crítica;**
* O usuário que for somente **Digitador não poderá excluir** o documento. Precisará ser **Digitador e ter mais uma responsabilidade** no documento;
* Que o usuário com responsabilidade possua a permissão de alterar o documento cadastrada na rotina **QDOA020 - Tipo de Documento;**

Após a fase de **Em Elaboração** (**Digitação**, **Elaboração**, **Revisão**, **Aprovação**, **Homologação**, **Elaboração com Críticas** e **Digitação com Crítica)**, e/ou após a fase de **Distribuição**, apenas a opção de **Cancelamento** está disponível.

**Saiba mais**Para complementar a regra de exclusão do **Protheus**, pode ser implementado o ponto de entrada **Q050DEL** conforme documentação disponível no *link*: [Q050DEL - Exclusão de Documento](http://tdn.totvs.com/pages/viewpage.action?pageId=6801891)  
Para mais detalhes sobre como **cancelar** um documento, acesse o artigo: [Manufatura - Linha Protheus - SIGAQDO - Cancelamento de documento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021108292-MP-QUA-Como-cancelar-um-documento-)
