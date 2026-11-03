---
article_id: 360018012532
category: Contabilidade Gerencial - Compartilhamento Tabelas
content_hash: bc0b3bef222de2bb16bb8c36eb0b005cfbdf904eebb497462995648fc21d00a0
fetched_at: '2026-06-28T22:40:57.805654+00:00'
product: protheus
section_id: 1500001537461
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB- CTBA105 Exclusão dos
  registros das tabelas CTK e CV3
type: support-article
updated_at: '2026-05-04T18:18:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018012532-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA105-Exclus%C3%A3o-dos-registros-das-tabelas-CTK-e-CV3
---

**Dúvida**  
SIGACTB: Exclusão dos registros das tabelas CTK e CV3  
  
**Ambiente**  
Protheus – Contabilidade Gerencial – A partir da versão 12.  
  
  
**Solução**

A tabela **Arquivo Contra Prova (CTK)** é responsável por guardar dados que serão usados no momento da contabilização para gerar os registros de **Movimento Contábeis (CT2)**. Deve certificar-se que a contabilização esta totalmente efetuada e conferida para uma posterior limpeza desta tabela.

 A tabela **CV3-Rastreamento Contábil** é utilizada para o rastreamento do registro de origem a partir do lançamento contábil nas rotinas **Lançamento Contábil (CTBA101)**, **Lançamento Contábil Automático (CTBA102)** e **Lançamento Contábil Parametrizado (CTBA103)**. Em hipótese alguma deve-se executar a exclusão dos registros desta tabela, pois, sua exclusão inviabiliza este processo.

Para melhor entendimento do funcionamento do rastreio contábil poderá verificar a documentação com exemplo da chave utilizada pelo rastreio:

[Cross Segmento - Backoffice Linha Protheus - CTBA105 Como é composta a chave de rastreamento na tabela CV3.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022784291-Cross-Segmento-Backoffice-Linha-Protheus-CTBA105-Como-%C3%A9-composta-a-chave-de-rastreamento-na-tabela-CV3-)

Saiba mais:

[Cross Segmentos - Backoffice Linha Protheus - SIGACTB - CTBA102 - Exclusão de lançamento contábil gera error.log : Invalid data type on (F3\_DTLANC)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/9144446577687-Cross-Segmentos-Backoffice-Linha-Protheus-SIGACTB-CTBA102-Exclus%C3%A3o-de-lan%C3%A7amento-cont%C3%A1bil-gera-error-log-Invalid-data-type-on-F3-DTLANC-)

[CTBA105 - Contabilização Off-Line não valida a linha do lançamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059273293-MP-SIGACTB-CTBA105-Contabiliza%C3%A7%C3%A3o-Off-Line-n%C3%A3o-valida-a-linha-do-lan%C3%A7amento?source=search)

[Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBA102 RASTREAR LANÇAMENTOS E RASTREAMENTO CONTABIL](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025839472-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA102-RASTREAR-LAN%C3%87AMENTOS-E-RASTREAMENTO-CONTABIL)

<https://tdn.totvs.com/pages/releaseview.action?pageId=6068533>
