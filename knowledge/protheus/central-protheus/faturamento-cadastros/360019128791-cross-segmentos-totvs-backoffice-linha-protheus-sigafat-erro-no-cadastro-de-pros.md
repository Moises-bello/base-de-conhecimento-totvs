---
article_id: 360019128791
category: Faturamento - Cadastros
content_hash: 670885080ce374bc3026cd383f8c41a7acab83b2556a050b32208284f2e5a2e9
fetched_at: '2026-06-28T22:38:35.580531+00:00'
product: protheus
section_id: 1500001539221
source: central-protheus
title: Cross Segmentos-TOTVS Backoffice (Linha Protheus)-SIGAFAT-Erro no cadastro
  de prospect
type: support-article
updated_at: '2022-08-11T14:30:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019128791-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Erro-no-cadastro-de-prospect
---

**Ocorrência**Ao incluir, alterar ou visualizar um prospect é gerado o erro: argumento #6, parâmetrolShowBarerro, previstoL->A on FWFORMVIEW:ADDUSERBUTTON(FWFORMVIEW.PRW)  
  
**Ambiente**

Cross Segmentos-TOTVS Backoffice (Linha Protheus)-SIGAFAT - a partir da versão 12.  
  
**Causa**

O erro ocorre na montagem dos botões da opção outras ações.

**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:

1. Efetue o download do pacote de atualização da rotina **TMKA260, ocorrência 41: [Principais Pacotes de Correção - Faturamento - SIGAFAT ( A410Limpa, NNR, \_FWMBPICTVAR, CHECKNEWX, MPUSERACCOUNT, BEFOREEXECUTE, Work area not, MATA030, CFILTERNATIVE, FEFO, Vencimento Lote, AFY811, FATJOBNFE, ACOLSCCUT, MARESDOFAT, Gatilho, C5\_MENNOTA)](http://tdn.totvs.com/pages/viewpage.action?pageId=235334710)**;  
2. Aplique o pacote no RPO através do TDS ou Ide;  
3. Reinicie o smartclient e refaça o processo.

OBS: Para aplicação de pacote, requer que o analista tenha conhecimento em estrutura de ambiente Protheus.

Sempre efetuar a aplicação do pacote em ambiente de homologação para validar e posteriormente, aplicar no ambiente de produção, efetuando o devido backup do ambiente.
