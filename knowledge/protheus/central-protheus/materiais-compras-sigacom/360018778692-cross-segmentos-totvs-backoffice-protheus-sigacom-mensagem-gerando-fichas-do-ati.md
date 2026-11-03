---
article_id: 360018778692
category: Materiais - Compras (SIGACOM)
content_hash: 8a0abeab0bc64f1f398de57045895b880f8d3da903cffa7f1aeb42a9d8158092
fetched_at: '2026-06-28T22:41:20.169898+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Mensagem "Gerando fichas
  do Ativo" no Documento de entrada com integração com Ativo Fixo
type: support-article
updated_at: '2024-08-27T17:49:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018778692-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Mensagem-Gerando-fichas-do-Ativo-no-Documento-de-entrada-com-integra%C3%A7%C3%A3o-com-Ativo-Fixo
---

**Dúvida**Ao realizar a inclusão do documento de entrada para aquisição e desmembramento de bem do Ativo, o sistema 'prende' os registros, impedindo que outros usuários utilizem a rotina simultaneamente.  
Qual o motivo do sistema apresentar a mensagem "Gerando fichas do Ativo", *Multlock* - SQL registro bloqueado por outro usuário?  
  
**Ambiente**Microsiga Protheus – Compras – A partir da versão 12  
  
**Solução**Esta mensagem ocorre, pois internamente o sistema possui a função A103Trava (MATA103X), esta função executa o *MultLock* nas tabelas de fornecedor (SA2) e saldos (SB2), para atualização durante as operações do documento de entrada. Trata-se de uma função restrita do DbAccess que bloqueia os registros posicionados pela rotina 'documento de entrada' e faz com que estes sejam liberados somente após o processamento da primeira nota em fila.  
Portanto, não é recomendável a manutenção para retirada desta trava de registro, pois perde-se a integridade da fila de processamento.

Para melhorar a performance da geração dos ativos pelo documento de entrada foi criado um parâmetro de Threads:

**[MV\_A12DTHR - DT Job para geração de ficha de ativo com desmembramento através do MATA103](https://tdn.totvs.com/pages/releaseview.action?pageId=665275186)**

***Saiba Mais:***

[DT Job para geração de ficha de ativo com desmembramento através do MATA103](https://tdn.totvs.com/x/MkunJw)

[Funções de Travamento Restritas](http://tdn.totvs.com/x/XAdXAQ)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
