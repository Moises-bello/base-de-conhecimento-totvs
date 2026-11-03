---
article_id: 360020588711
category: LEGAIS - BLOCO H/MATR460
content_hash: 4a2450973a703caf1abb393dce6724cf9cfb5bc79b83767ca907a40b01bd8ddd
fetched_at: '2026-06-28T22:42:15.024439+00:00'
product: protheus
section_id: 1500001538741
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Bloco K deve considerar
  o armazém de trânsito?
type: support-article
updated_at: '2025-03-12T12:22:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020588711-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Bloco-K-deve-considerar-o-armaz%C3%A9m-de-tr%C3%A2nsito
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29879991233047) Tempo aproximado para leitura: **00:01:00 min**

**Dúvida**Na apresentação do Bloco K deve-se considerar os saldos em armazém de trânsito?

**Ambiente**  
Microsiga Protheus – Estoque/Custos – A partir da versão 11.80  
  
  
**Solução**

O parâmetro de sistema MV\_LOCTRAN (armazém de transito) faz o tratamento juntamente com a Nota fiscal de Entrada. Documento de entrada que é o fato gerador de informações fiscais e saldos do produto, conforme configurações de TES.

Esses fatores caracterizam posse do produto, gerando até mesmo registro no C170. Assim deve ser considerado no Bloco k, registro K200.

**Saiba mais:**

*[MP - SIGAEST - Dicas de Análise dos Saldos no Relatório MATR460 (P7)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360061829673)*

*[MP - SIGAEST - Parâmetros (SX6) relacionados ao relatório MATR460 - Registro de Inventário Modelo 7](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500001351901-MP-SIGAEST-Par%C3%A2metros-SX6-relacionados-ao-relat%C3%B3rio-MATR460-Registro-de-Invent%C3%A1rio-Modelo-7)*

*[MP - SIGAEST - Validação do Parâmetro MV\_R460TPC](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500001352161-MP-SIGAEST-Valida%C3%A7%C3%A3o-do-Par%C3%A2metro-MV-R460TPC)*

*[Clique aqui e veja mais artigos sobre Bloco H e MATR460 (P7) no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000033001-SIGAEST-LEGAIS)*
