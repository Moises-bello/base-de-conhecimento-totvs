---
article_id: 360021393251
category: Controle de Documentos (SIGAQDO)
content_hash: c88a6afbcb6823f22f8755753ded3bffb7a5f319017b5068ed94a1fab62ebcc1
fetched_at: '2026-06-28T22:42:29.169242+00:00'
product: protheus
section_id: 360005906113
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQDO - Help QD_DOCNEXT ao visualizar ou alterar
  arquivo externo
type: support-article
updated_at: '2023-04-11T16:28:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021393251-Manufatura-Linha-Protheus-SIGAQDO-Help-QD-DOCNEXT-ao-visualizar-ou-alterar-arquivo-externo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:13 min****Ocorrência**Sistema apresenta o *help***QD\_DOCNEXT** ao tentar visualizar ou alterar um arquivo vinculado a um documento do tipo **Externo** na rotina **QDOA050 - Cadastro de Documentos**.  
  
**Ambiente**  
TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Controle de Documentos (SIGAQDO) - Todas as versões  
  
**Causa**O *help* **QD\_DOCNEXT** ocorre quando por algum motivo o arquivo perdeu o vínculo com o documento, não possui permissão para leitura e/ou gravação ou o arquivo foi corrompido.  
  
**Solução**Para verificar a causa do *help*, siga as orientações à seguir:  
1. Verifique se o arquivo indicado no campo **QDH\_NOMDOC - Nome Arquivo** para este documento está no diretório informado no parâmetro **MV\_QPATHW - Define o diretório onde contem os arquivos dos Documentos**;  
2.  Se o *SmartClient* está sendo executado como administrador;  
3. Se o *Appserver* está sendo executado como administrador;  
4. Se o usuário que está executando o *Appserver* ou *SmartClient* no Sistema Operacional, possui restrição de acesso para leitura e gravação no servidor e também no diretório indicado no parâmetro **MV\_QPATHWT - Define o diretório do Client onde ficarão os Documentos gerados pelo Sistema**;  
5. Se os itens acima estiverem corretos, será necessário gerar uma revisão deste documento com o parâmetro **MV\_QDUPEXT: Define se Visualiza/Altera/Exclui o documento externo na inclusão/alteração e copia o documento anterior na geração de revisão**igual a **1** para que possa adicionar o arquivo novamente.   
  
**Importante**O procedimento descrito no item 5 do tópico **Solução** somente deve ser realizado para corrigir o incidente pontualmente. Caso a situação venha a se repetir com vários documentos ou com muita frequência, será necessário abrir um **ticket** com o suporte **TOTVS** para investigação da causa.
