---
article_id: 360007600152
category: Contabilidade Gerencial - Plano de Contas
content_hash: cde1c30343cfd0fd9f09398f50462dc36f766a55a922a770ae6e049ac4bf3d93
fetched_at: '2026-06-28T22:40:33.411070+00:00'
product: protheus
section_id: 1500001549022
source: central-protheus
title: 'MP-SIGACTB-InterFunctionCall: cannot find function CTB020CSUP'
type: support-article
updated_at: '2021-04-28T15:26:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007600152-MP-SIGACTB-InterFunctionCall-cannot-find-function-CTB020CSUP
---

**Ocorrência**InterFunctionCall: cannot find function CTB020CSUP in AppMap on {|a,b,c,d| FWInitCpo(a,b,c),lRet:=((Ctb020CSup())),FWCloseCpo(a,b,c,lRet),lRet }(PROTHEUSFUNCTIONMVC.PRX)

**Ambiente**Protheus – Contabilidade Gerencial – A partir da versão 11.80  
   
 **Causa**

Erro ao incluir uma conta Contábil: InterFunctionCall: cannot find function CTB020CSUP

**Solução**

Para a correção, segue link com a patch de correção disponibilizada: <https://suporte.totvs.com/portal/p/10098/download?e=638403>  
   
 Solicito que efetue os seguintes processos:   
 - Aplique a Patch do Pacote (Aceitando somente fontes atualizados)  
 - Copie o arquivo SDFBRA para dentro da pasta Systemload.  
 - Execute o Compatibilizador UPDDISTR.

Antes de executar o UPDDISTR é necessário excluir os arquivos de LOG.  
 Dentro da pasta System:

mpupdlog.log

mpupdlog.fpt

mpwizard.hlp

Dentro da pasta Appserver:

mpupddistri.tsk

mpupddistri.old

Por favor, verifique a validação do campo CT1\_CTASUP conforme padrão.   
 ​SX3 - CT1\_CTASUP = "Ctb020CSup()"  
Verificar no SX3-Dicionario de dados no campo X3\_Valid está igual CTB020CSup()

\*Homologar em ambiente de testes.
