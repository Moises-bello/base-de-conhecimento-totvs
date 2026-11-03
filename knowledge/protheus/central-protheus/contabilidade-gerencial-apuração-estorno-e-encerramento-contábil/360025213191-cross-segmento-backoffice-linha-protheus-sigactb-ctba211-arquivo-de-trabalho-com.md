---
article_id: 360025213191
category: Contabilidade Gerencial - Apuração, Estorno e Encerramento Contábil
content_hash: f4d02b05f7a2812b12e17db08ff101a1761df410e9762c74ac37fc953f0c1017
fetched_at: '2026-06-28T22:41:05.081041+00:00'
product: protheus
section_id: 1500001548342
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBA211: Arquivo de
  trabalho com o saldos finais já existe'
type: support-article
updated_at: '2023-11-10T15:19:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025213191-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA211-Arquivo-de-trabalho-com-o-saldos-finais-j%C3%A1-existe
---

**Ocorrência**

Arquivo de trabalho com o saldos finais já existe

Arquivo encontrado :\_LPxxxxx.dtc  
Carregar novamente saldos ?

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360023622231)  
  
**Ambiente**  
Microsiga Protheus – Contabilidade Gerencial  – A partir da versão 11.80  
  
**Causa**

Situação é apresentada quando o sistema encontra Registro de apuração na Tabela CW0

Ex.:

Foi realizada a apuração com os parâmetros abaixo

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360023592632)

Devido algum ajuste na conta se faz necessário realizar mais uma apuração no mesmo periodo, para  algum range de conta , posteriormente a mensagem é apresentada

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360023592772)

**Solução**

A apuração pode ser executada mesmo que a mensagem seja apresentada.

O sistema não irá apagar na CT2 ou das tabelas CQx os lançamento de apurações já existente,  o sistema irá apagar da Tabela CW0  o registro de apuração(data) e substituir pela ultima apuração realizada

Após esta execução da apuração o sistema ira considerar e ultima apuração, com isso ao tentar executar o estorno o sistema apresentara somente a ultima data apurada

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360023596492)

[MP\_SIGACTB CHAVE DE APURAÇÃO CTBA211](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024134092-MP-SIGACTB-CHAVE-DE-APURA%C3%87%C3%83O-CTBA211?source=search)

Campos que são alimentado ao realizar a apuração : [\_LP e \_DTLP](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024630411-MP-SIGACTB-PREENCHIMENTO-DO-CAMPO-LP-e-DTLP?source=search)

Tabelas :

* ​[CW0](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024134092-MP-SIGACTB-CTBA007-CTBA211-CHAVE-DE-APURA%C3%87%C3%83O-CW0-?source=search)
* [CT2,CQ0, CQ1, CQ2, CQ3, CQ4, CQ5, CQ6, CQ07 CQ8, CQ9](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018270032-MP-SIGACTB-Como-realizar-compartilhamento-de-tabelas-no-Contabilidade-Gerencial-SIGACTB-?source=search)
