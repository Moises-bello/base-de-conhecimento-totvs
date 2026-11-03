---
article_id: 360018927792
category: Contabilidade Gerencial - Integração EAI PIMS Protheus
content_hash: d01888eb42acaed06604ce4b974f67c0de237fa73065789190a95a6dc45641b5
fetched_at: '2026-06-28T22:40:54.121309+00:00'
product: protheus
section_id: 1500001537541
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB -  PROBLEMAS NA INTEGRAÇÃO
  EAI,TRANSAÇÃO NÃO EXECUTADA
type: support-article
updated_at: '2022-07-18T18:51:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018927792-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-PROBLEMAS-NA-INTEGRA%C3%87%C3%83O-EAI-TRANSA%C3%87%C3%83O-N%C3%83O-EXECUTADA
---

**Ocorrência**

Na inclusão de centro de custo retornar mensagem de problemas na integração EAI  
Esta mensagem pode ocorrer para outras inclusões ou processos que envolvam a integração via EAI

**Ambiente**

#### Cross Segmento - Backoffice Linha Protheus - CONTABILIDADE GERENCIAL – A partir da versão 11.80 **Causa** Com o ambiente configurado para integração EAI , esse incidente ocorre, pois a parametrização do MV\_EAIURL2 não esta correta.

**Solução**[Exemplo:  
Para esta ocorrência, verificar configuração do parâmetro mv\_eaiurl2 e configurações do adapter correspondente a integração que esta sendo executada.

Abaixo Informações extraídas do link que segue  sobre o EAI protheus

**MV\_EAIURL2** - Parâmetro que indica ao **EAI Protheus** para qual endereço de *Webservices* a mensagem será disparada. Este parâmetro é utilizado quando o **adapter** está cadastrado com o **Canal Envio** (XX4\_CHANEL) =EAI;

As rotinas que são responsáveis por realizar o processamento das mensagens enviadas e recebidas são cadastradas no ambiente do **Configurador** **Protheus**. Em *Ambiente/Schedule/Adapter E.a.i,* no **Cadastro de Adapter EAI** (**APCFG20)** é possível incluir, alterar e excluir um **adapter** no **Protheus**.

<http://tdn.totvs.com/display/framework/A+camada+do+EAI>
