---
article_id: 23078248814103
category: Contabilidade Gerencial - Escrituração-Contábil-ECD
content_hash: 1ddf22c72bed6a7ae966a9eebc8785760c632669cfed13f66962e2f2cd599d41
fetched_at: '2026-06-28T22:40:52.668683+00:00'
product: protheus
section_id: 1500001537561
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB- CTBS001 - ECD O bloco
  I não foi importado pois contém erros
type: support-article
updated_at: '2024-04-29T11:54:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23078248814103-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBS001-ECD-O-bloco-I-n%C3%A3o-foi-importado-pois-cont%C3%A9m-erros
---

**Ocorrência**

**O bloco I não foi importado pois contém erros**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23078248779415)  
**Ambiente**  
Cross Segmento - TOTVS Backoffice Linha Protheus - Contabilidade gerencial - Todas as versões  
  
**Causa**Erro é apresentado pois no mesmo arquivo foram apresentados erros em alguns registro I

Erro no I200 -Registro obrigatório não encontrado, ao avaliar o arquivo o registro I150 , não tinha sido gerado

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23078248781847)

Erro no I250 HIST Conteudo do campo inválido

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23078248788375)

Erro no I050 - COD\_NAT Campo obrigatório não preenchido

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23078264362775)

**Solução**Necessario corrigir os erros apresentado em todos os registro I .

* Erro no I200 - Necessário investigar o motivo pelo qual  o registro não foi gerado no arquivo
* [I200 e I250](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007337292-MP-SIGACTB-ECD-N%C3%83O-GERA-REGISTROS-I250?source=search) são gerados com base nas tabelas CTC e CTF
* [I150 e I155](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007744371-MP-SIGACTB-ECD-Registro-Blocos-I150-e-I155-?source=search).são gerados com base nas tabelas CQ0 e CQ1
* Erro no I250 HIST - Necessário avaliar o que esta incorreto no histórico do lançamento :  [ESPECIAL NO HISTÓRICO](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047562333-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-ECD-ECF-CAR%C3%81CTER-ESPECIAL-NO-HIST%C3%93RICO?source=search)
* Erro no I050 - COD\_NAT - Necessário preencher a  [NATUREZA CONTA CONTABIL](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006887272-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA020-NATUREZA-CONTA-CONTABIL-ECD-ECF?source=search)
