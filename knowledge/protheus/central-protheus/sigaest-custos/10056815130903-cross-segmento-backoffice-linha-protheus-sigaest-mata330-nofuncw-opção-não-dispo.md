---
article_id: 10056815130903
category: SIGAEST - CUSTOS
content_hash: 3102b0dc6a151c4fd0ed7352103344adb9b45a1d7e95ee3748dcf9c93a32d220
fetched_at: '2026-06-28T22:39:02.193468+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: 'Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA330 - NOFUNCW
  - Opção não disponível no Protheus. Função: DIFFTIME2Called by ENG51GETPROCESSES'
type: support-article
updated_at: '2022-11-07T19:46:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10056815130903-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA330-NOFUNCW-Op%C3%A7%C3%A3o-n%C3%A3o-dispon%C3%ADvel-no-Protheus-Fun%C3%A7%C3%A3o-DIFFTIME2Called-by-ENG51GETPROCESSES
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:35 min****Ocorrência**Ao executar o Recálculo do Custo Médio, ocorre o seguinte error.log:

InterFunctionCall: cannot find function DIFFTIME2 in AppMap on ENGSPSSTATUS(CFGX051F.PRW)

**![](https://atendimento.totvs.com/attachments/token/S6nDbDPGFuYWabF34eWLN00fU/?name=image004.png)**

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Causa**Função DIFFTIME2 é chamada dentro do fonte ENGPHLOAD, que é um fonte de engenharia. O erro acontece quando esta função não está contida no fonte.

**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
1. Atualize a versão da Central de Atualizações do Protheus - V.1.4.8  
<https://suporte.totvs.com/portal/p/10098/download?e=946864>

OBS: Sempre efetuar aplicações de pacotes primeiramente em ambiente de homologação com backup prévio do RPO.

Após aplicação do pacote, basta executar novamente o Recálculo do Custo Médio para que tenha sucesso já que a função já estará contemplada no fonte.

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Custos no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538901-SIGAEST-CUSTOS)
