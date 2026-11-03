---
article_id: 360058924314
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 55add322c1ce7209ac133a7c2e6e4da5fd9a429da97e0ec76f0393eb95111d84
fetched_at: '2026-06-28T22:39:56.385749+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE - Condições
  de Pagamento no TXT (Santana de Parnaíba)
type: support-article
updated_at: '2025-07-14T21:22:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058924314-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-Condi%C3%A7%C3%B5es-de-Pagamento-no-TXT-Santana-de-Parna%C3%ADba
---

**Dúvida**  
Como são configuradas os tipos de pagamentos no arquivo .TXT para Santana de Parnaíba?   
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.  
  
**Solução**Dentro da rotina MATA360, informar corretamente os conteúdos orientados abaixo:  
 **![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500000493461/mceclip4.png)**Possibilidades da prefeitura no arquivo TXT gerado:![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500000485281/mceclip0.png)

**001: A VISTA**-> Utilizar uma condição a vista no E4\_COND, exemplo: **00**

**002-060: PARCELADO** -> Utilizar uma condição parcelada no E4\_COND, exemplo: **20,30**Dois vencimentos -> 1º após 20 dias e 2º após 30 dias.  
  
**253: A PRAZO ->** Utilizar uma condição parcelada no E4\_COND, exemplo: **0 ou contendo %**  
Se gerada uma única duplicata na SE1 será destacado como 001: Data de Vencimento Fatura, se mais de uma duplicata ai sim será destacada como: 253: A PRAZO.  
  
**254: CONTRA APRESENTACAO** -> Utilizar uma condição parcelada no E4\_COND, exemplo: **20,**Único vencimento -> 1º após 20 dias.  
  
**255: CONFORME CONTRATO** -> Até o momento não houve a necessidade por nenhum cliente de utilizar esse conteúdo específico.  
  
Detalhes: [Link com o Manual da Prefeitura.](https://www.santanadeparnaiba.sp.gov.br/NFE/formulario/Formato%20do%20arquivo%20de%20Importa%C3%A7%C3%A3o%20Santana.pdf)
