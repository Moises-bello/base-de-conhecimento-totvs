---
article_id: 360025891612
category: Comércio Exterior - Easy Import Control - Siscomex
content_hash: 253c6c6f70b834d4b80f625174b6a26433ad6f65dc7d76e87e5657f14a746b68
fetched_at: '2026-06-28T22:39:45.318615+00:00'
product: protheus
section_id: 1500001538441
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC- Declaracao nao
  aceita - Usuario nao cadastrado como representante legal do importador para as atividades
  de importacao
type: support-article
updated_at: '2022-06-02T13:57:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025891612-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Declaracao-nao-aceita-Usuario-nao-cadastrado-como-representante-legal-do-importador-para-as-atividades-de-importacao
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:02:00 min**

**Ocorrência**  
No módulo SIGAEIC, ao tentar realizar a integração de L.I. com o Siscomex é retornada a mensagem:  
"Declaração não aceita - Usuário não cadastrado como representante legal do importador para as atividades de importação"

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:02:00 min**  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Import Control* – Todas versões

**Causa**Certificado não associado ao importador informado no processo (Representante legal).

**Solução**Validação do Siscomex sob o Certificado utilizado para integrar as informações ao mesmo, o E-CPF deve estar associado ao importador do Processo.  
Caso a mensagem seja apresentada deve-se verificar se o importador utilizado no processo esta correto e se o certificado utilizado para a integração esta associado a este importador junto ao Siscomex.
