---
article_id: 360007337292
category: Contabilidade Gerencial - Escrituração-Contábil-ECD
content_hash: 82192e4b27d092ed41802bcea148c8ad83cbb9d0d94f0de63a068c5b16a131ed
fetched_at: '2026-06-28T22:40:45.655449+00:00'
product: protheus
section_id: 1500001548702
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB- ECD NÃO GERA REGISTROS
  I250
type: support-article
updated_at: '2026-04-09T19:59:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007337292-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-ECD-N%C3%83O-GERA-REGISTROS-I250
---

**Ocorrência**  
ECD - Arquivo não gera registros I250.

**Ambiente**  
Cross Segmento - Backoffice Linha Protheus - Contabilidade Gerencial – A partir da versão 12.  
  
**Solução**  
Para gerar o I250 :

* [Necessário que as tabelas contábeis estejam devidamente populadas e com o compartilhamento correto](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026989572-MP-SIGACTB-TABELAS-ECD-E-ECF-COMPARTILHAMENTO?source=search) principalmente as tabelas [CT2,CQ0,CQ1(..)CQ9, CTC,CTF,](http://tdn.totvs.com/display/PROT/CTB0012_Compartilhamento_de_tabelas_SIGACTB)
* Necessário que as   [tabelas ECD estejam com o  Compartilhamento correto](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026989572-MP-SIGACTB-TABELAS-ECD-E-ECF-COMPARTILHAMENTO?source=search)
* Verifique se procedure dinâmica está habilitada através do parâmetro [MV\_CTBSPRC.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007132632-MP-SIGACTB-Habilitar-procedures-din%C3%A2mica-na-gera%C3%A7%C3%A3o-da-ECD?source=search)
* Verifique como o do parâmetro [MV\_CTBSDOC](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025883891-MP-SIGACTB-ECD-I200-PORQUE-N%C3%83O-ESTA-CONSIDERANDO-O-NUMERO-DO-LOTE?source=search) está configurado
* parâmetro [MV\_FILTEMP que filtra as escriturações contábeis por empresas e filiais,](https://tdn.totvs.com/display/public/PROT/1250458+DSERCTR1-4887+DT+Filtro+por+empresa+ECD) levando em consideração apenas o modelo gestão corporativa
* veja se  os campo verifique se os campos X2\_AUTREC, X2\_TAMFIL, X2\_TAMUN, X2\_TAMEMP , das tabelas CT2, CTC, CTF, CQO,CQ1...CQ9 e CQA , CS0....CSZ e CW0 estão com o tamanho correto em comparação ao seu sigmat
* Veja se o campo CW0\_CHAVE está preenchido corretamente

Consulte link de documentação: <http://tdn.totvs.com/display/public/PROT/ECD0002_MV_CTBSPRC_PERFORMANCE_ECD>

* [Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBA960 - Processo de atualização de saldos.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/36347421005975-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA960-Processo-de-atualiza%C3%A7%C3%A3o-de-saldos)
* Verifique se o reprocessamento de saldo [Saldos não estão sendo atualizados de forma online.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019534772-MP-SIGACTB-Saldos-n%C3%A3o-est%C3%A3o-sendo-atualizados-de-forma-online-?source=search)
* Confira o compartilhamento das tabelas  [Reestruturação dos Saldos Contábeis](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018467872-MP-SIGACTB-Reestrutura%C3%A7%C3%A3o-dos-Saldos-Cont%C3%A1beis?source=search)
* Verifique se esta sendo preenchido  [Campo Filial das tabelas CQ não estão sendo alimentadas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018497311-MP-SIGACTB-CTBA190-Campo-Filial-das-tabelas-CQ-n%C3%A3o-est%C3%A3o-sendo-alimentadas-?source=search)
* Realize o [reprocessamento de saldos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006689012-MP-SIGACTB-Reprocessamento-n%C3%A3o-atualiza-saldos?source=search) , da data que esta correta até a data de hoje , em caso de duvidas veja [Como realizar o reprocessamento de saldos no SIGACTB](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007452371-MP-SIGACTB-CTBA-190-Como-realizar-o-reprocessamento-de-saldos-no-SIGACTB-?source=search)
