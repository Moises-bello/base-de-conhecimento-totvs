---
article_id: 14303895151127
category: Fiscal Arquivos Magnéticos - SPED Contribuições
content_hash: a7a98b6e1d7eb421b38714bd5e28643179f5d4830cb20e567529c57b71b7ef46
fetched_at: '2026-06-28T22:42:04.875411+00:00'
product: protheus
section_id: 1500001535081
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - SPED Contribuições
  - F100 - NAT_BC_CRED -  Campo obrigatório quando o CST PIS ou CST COFINS for referente
  a operação com direito a crédito.
type: support-article
updated_at: '2023-05-03T12:27:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/14303895151127-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-SPED-Contribui%C3%A7%C3%B5es-F100-NAT-BC-CRED-Campo-obrigat%C3%B3rio-quando-o-CST-PIS-ou-CST-COFINS-for-referente-a-opera%C3%A7%C3%A3o-com-direito-a-cr%C3%A9dito
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **02:00 min****Ocorrência**Ao validar o arquivo txt do SPED Contribuições gerado pelo Protheus ocorre o erro de validação quanto registro **F100 - Campo obrigatório quando o CST PIS ou CST COFINS for referente a operação com direito a crédito.**  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Causa**Esse incidente ocorre, pois a configuração do sistema está incorreta para para o cadastro de Natureza utilizado na escrituração do documento. Dessa forma, no campo 15 do F100, a natureza do crédito é gerada em branco.  
  
**Solução**Para que o campo **15 - NAT\_BC\_CRED**  do **F100 - Demais Documentos e Operações Geradoras de Contribuição e Créditos**  seja apresentado é preciso preencher o campo abaixo no cadastro de naturezas utilizado na escrituração do Documento.  
   
![](https://totvssuporte.zendesk.com/attachments/token/R5pFIsChf1nfHSnTlizr9sg3z/?name=image.png)  
Com o preenchimento no cadastro de naturezas e reprocessada a apuração do PIS COFINS, o campo CL2\_CODBCC será devidamente alimentado e o campo 15 do F100 gerado com a informação correta.
