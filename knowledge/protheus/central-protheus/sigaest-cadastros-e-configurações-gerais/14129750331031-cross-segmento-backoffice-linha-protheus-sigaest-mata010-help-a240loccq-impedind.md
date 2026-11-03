---
article_id: 14129750331031
category: SIGAEST - CADASTROS E CONFIGURAÇÕES GERAIS
content_hash: 470453a17bda57fa4c4b32383a154ae65fee37edf4eea6c09eddac3719b0fb0d
fetched_at: '2026-06-28T22:39:09.487130+00:00'
product: protheus
section_id: 1500001550022
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA010 - HELP A240LOCCQ
  impedindo informar o Local Padrão igual ao MV_CQ
type: support-article
updated_at: '2023-04-25T10:33:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/14129750331031-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA010-HELP-A240LOCCQ-impedindo-informar-o-Local-Padr%C3%A3o-igual-ao-MV-CQ
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **HH00:03:00 min** **Dúvida**Ao tentar cadastrar ou mesmo alterar o Armazém Padrão (B1\_LOCPAD) para o Armazém de CQ (MV\_CQ) apresenta o **HELP A240LOCCQ** impedindo a conclusão, é possível efetuar esse cadastro?

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14130108389911)  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões

**Solução**Nesse cenário não se trata de um erro, no padrão o **HELP A240LOCCQ** é apresentado no cadastro de produtos, pois não é permitido o Local Padrão igual ao parâmetro MV\_CQ, para envio ao CQ é necessário configurar como indicado na FAQ com instruções padrões de utilização do CQ [(clique aqui)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025518774-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Rotina-MATA175-Instru%C3%A7%C3%B5es-padr%C3%B5es-sobre-Controle-de-Qualidade-no-Estoque?source=search) **para que siga o fluxo corretamente de envio de produtos ao Controle de Qualidade**.

Também na rotina **MOVIMENTAÇÕES MÚLTIPLAS (MATA241)** e **TRANSFERÊNCIAS MÚLTIPLAS (MATA261)** apresentam os **HELPS A240LOCCQ e A260LOCCQ** respectivamente. [Clique aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/13078285027095) e veja mais detalhadamente.

***Saiba Mais:***  
[Clique aqui e veja mais artigos sobre CADASTROS E CONFIGURAÇÕES GERAIS no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550022-SIGAEST-CADASTROS-E-CONFIGURA%C3%87%C3%95ES-GERAIS)

[SIGAEST - HELP A260LOCCQ e A240LOCCQ](https://centraldeatendimento.totvs.com/hc/pt-br/articles/13078285027095)

[SIGAEST - Rotina MATA175 - Instruções padrões sobre Controle de Qualidade no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025518774-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Rotina-MATA175-Instru%C3%A7%C3%B5es-padr%C3%B5es-sobre-Controle-de-Qualidade-no-Estoque?source=search)
