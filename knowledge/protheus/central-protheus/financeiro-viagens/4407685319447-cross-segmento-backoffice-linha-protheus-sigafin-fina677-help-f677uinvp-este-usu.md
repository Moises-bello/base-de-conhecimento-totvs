---
article_id: 4407685319447
category: Financeiro - Viagens
content_hash: 845653855ea91c6f9baa5a2cbb00cb508aee3678aa709be0a30efc6b6a0708c6
fetched_at: '2026-06-28T22:38:21.354734+00:00'
product: protheus
section_id: 1500001539201
source: central-protheus
title: Cross Segmento BackOffice Linha Protheus - SIGAFIN - FINA677 - HELP F677UINVP
  Este usuário não é um substituto para prestação de contas do participante selecionado
type: support-article
updated_at: '2023-02-17T22:01:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4407685319447-Cross-Segmento-BackOffice-Linha-Protheus-SIGAFIN-FINA677-HELP-F677UINVP-Este-usu%C3%A1rio-n%C3%A3o-%C3%A9-um-substituto-para-presta%C3%A7%C3%A3o-de-contas-do-participante-selecionado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:05:00 min****Ocorrência**No módulo **Financeiro**, ao tentar alterar uma **prestação de contas** na FINA677 para outro participante, apresenta o HELP **F677UINVP** - Este usuário não é um substituto para prestação de contas do participante selecionado  
**Ambiente**Cross Segmento - TOTVS BackOffice (Linha Protheus) - TOTVS Financeiro - Todas as versões  
  
**Causa**Esse incidente ocorre, pois no cadastro do solicitante na rotina **APDA020 - Cadastro de Participantes** não está informando o Substituto da prestação de contas.  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
  
1 - Acesse o cadastro do participante da viagem na rotina **APDA020 - Cadastro de Participantes**   
2 - Na aba **Viagem**, informe no campo **Sub. Prst. Cta - RD0\_USRPRE** o código do usuário substituto que irá realizar a prestação de contas.

![APDA020_SUBSTITUTO.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4407673660055/APDA020_SUBSTITUTO.png)

**Importante**

3- Após o cadastro acima, para o erro não ocorrer, será preciso entrar no Protheus com a conta do Substituto realizar a prestação pela pessoa substituída na prestação de contas **FINA677**.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12490838061591)

Isso por que pela regra e logica empregada, se no cadastro **APDA020** um viajante tem um substituto associado, será ele (Substituto associado) quem deve entrar no sistema e gerar uma prestação de contas em nome de outra pessoa e em nome digo, apenas trocar o registro do viajante para que o processo siga na prestação.  ![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12490992673175)  
  
**Saiba mais**  
[Viagens - Financeiro - P12](https://tdn.totvs.com/display/public/PROT/Viagens+-+Financeiro+-+P12)
