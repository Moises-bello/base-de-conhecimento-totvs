---
article_id: 360024407172
category: ADVPL - Classe e Função
content_hash: 721e1691374b16884f590c049587c8995beeb802b0a3603098470ed89f2fea8d
fetched_at: '2026-06-28T22:40:14.102332+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - Através de alguma
  função advpl é possível saber se um usuário utiliza um outro módulo/rotina do sistema
type: support-article
updated_at: '2021-05-06T19:47:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024407172-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Atrav%C3%A9s-de-alguma-fun%C3%A7%C3%A3o-advpl-%C3%A9-poss%C3%ADvel-saber-se-um-usu%C3%A1rio-utiliza-um-outro-m%C3%B3dulo-rotina-do-sistema
---

**Dúvida**Através de alguma função ADVPL é possível saber se um usuário utiliza um outro módulo/rotina do sistema?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 12.1.17  
  
**Solução**Utilize a função GetUserInfoArray().  
  
Importante  
Em anexo o fonte T172MONIT.prx exemplifica como utilizar a função GetUserInfoArray() para monitorar/desconectar usuários utilizando a função KillUser().  
  
**Saiba Mais**  
[GetUserInfoArray - Retorna cada um do processos em execução no protheus](http://tdn.totvs.com/display/tec/GetUserInfoArray)
