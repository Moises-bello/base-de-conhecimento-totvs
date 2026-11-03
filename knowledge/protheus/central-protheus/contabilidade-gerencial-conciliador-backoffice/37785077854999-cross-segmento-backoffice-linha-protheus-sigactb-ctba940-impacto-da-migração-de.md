---
article_id: 37785077854999
category: Contabilidade Gerencial - Conciliador BackOffice
content_hash: d82e83211f54a3ad5fd4e64de67c950620450a672d65fd73ed7e108f292ed9ba
fetched_at: '2026-06-28T22:40:30.982374+00:00'
product: protheus
section_id: 31314114896791
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBA940 - Impacto da
  migração de banco de dados no Conciliador Backoffice
type: support-article
updated_at: '2026-01-19T20:29:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37785077854999-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA940-Impacto-da-migra%C3%A7%C3%A3o-de-banco-de-dados-no-Conciliador-Backoffice
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37785077845527) **Tempo aproximado para leitura: 00:10 min**  
  
**Dúvida**  
Como tratar a normalização dos campos UUID (`MSUIDT`) nas tabelas de conciliação (`QLD`) e rastreamento contábil (`CV3`) durante a migração de banco de dados?

**Ambiente**  
Cross Segmento - Backoffice Linha Protheus - Contabilidade Gerencial – A partir da versão 12.1.33.

**Solução**  
Os campos `MSUIDT`são utilizados para criar identificadores únicos para registros, apresentando formatações distintas (maiúsculas, minúsculas, com ou sem hifens) dependendo do banco de dados utilizado (SQL Server, PostgreSQL ou Oracle).  
Nas tabelas de itens de conciliação (`QLD`) e rastreamento de lançamentos (`CV3`), o sistema grava cópias desses identificadores.   
Ao realizar a migração de banco de dados, é imprescindível normalizar esses registros para garantir a integridade das conciliações e dos rastreamentos já existentes.  
Para consultar as regras específicas de formatação de cada banco e os procedimentos técnicos de normalização, acesse a documentação no link abaixo

[**Impacto da migração de banco de dados no Conciliador Backoffice**](https://tdn.totvs.com/pages/viewpage.action?pageId=1032878148)

**Reforça-se que este procedimento é crítico e deve ser executado obrigatoriamente por um** **DBA****, sempre precedido de um** **backup completo** **do ambiente para mitigar riscos de perda de dados.**

**Saiba Mais:**  
[Conciliador Protheus - Configuração e Instalação](https://tdn.totvs.com.br/pages/releaseview.action?pageId=638741736)  
[Conciliador Backoffice - CTBA940 - P12 - Contabilidade Gerencial](https://tdn.totvs.com.br/display/public/PROT/Conciliador+Backoffice+-+CTBA940+-+P12+-+Contabilidade+Gerencial)  
[CTBA940 - Conciliador BackOffice](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6451317698583-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA940-Conciliador-BackOffice)  
[Campos UUID no DBAccess](https://tdn.totvs.com/display/tec/Campos+UUID+no+DBAccess)
