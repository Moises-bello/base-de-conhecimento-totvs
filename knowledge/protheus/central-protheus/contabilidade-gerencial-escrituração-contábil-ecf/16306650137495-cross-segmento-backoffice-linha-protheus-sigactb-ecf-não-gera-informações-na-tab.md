---
article_id: 16306650137495
category: Contabilidade Gerencial - Escrituração Contábil - ECF
content_hash: e997eeeeab048d9dc322b01ca08796cdfd12f553ef9fc27d71ee27e7b0550222
fetched_at: '2026-06-28T22:40:47.744561+00:00'
product: protheus
section_id: 1500001537721
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - ECF - Não Gera Informações
  na Tabela CSK
type: support-article
updated_at: '2023-07-26T15:15:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/16306650137495-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-ECF-N%C3%A3o-Gera-Informa%C3%A7%C3%B5es-na-Tabela-CSK
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16306620637847) Tempo aproximado para leitura: 00:03:00**Ocorrência**Ao gerar a Revisão da ECF no CTBS001, o sistema carrega as informações na tela porém não alimenta a tabela CSK, fazendo o arquivo sair em branco.  
**Ambiente**Cross Segmento - TOTVS Backoffice  - Microsiga Protheus - Todas as versões  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:

Realizar a verificação nos campos CVN\_ENTREF e CVD\_ENTREF se estão iguais.

Acessar a rotina do Plano Referencial (CTBA025), localizar o Plano Referencial que ira utilizar e avaliar o campo Entidade:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16306418411031)

Após acesse a rotina Plano de Contas (CTBA020), e avalie se o campo Entidade no Plano Contas estão iguais:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16306506289047)
