---
article_id: 360026891251
category: Financeiro - Contas a Pagar - Comunicação Bancária CNAB
content_hash: 5788f79a9529cd68939c3ae5ac6c11c1e913f1acbb9c15c28e3f971ec7e4d0f8
fetched_at: '2026-06-28T22:37:56.419985+00:00'
product: protheus
section_id: 1500001550622
source: central-protheus
title: 'Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Qual função pode ser
  utilizada no ponto de entrada: FA200FIL'
type: support-article
updated_at: '2022-07-22T15:50:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026891251-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Qual-fun%C3%A7%C3%A3o-pode-ser-utilizada-no-ponto-de-entrada-FA200FIL
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:03:00min**

**Dúvida**Qual função pode ser utilizada no ponto de entrada: FA200FIL  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro – A partir da versão 12

**Solução**O ponto de entrada **FA200FIL** executa a substituição da pesquisa padrão do título do **arquivo de retorno**, na tabela do **Contas a Receber (SE1)**, que realiza o **IDCNAB** ou chave do título.

**Por exemplo**A chave de busca no padrão é o **IDCNAB**, através deste ponto de entrada poderá substituir a chave de busca **E1\_IDCNAB** pelo Nosso Número**(E1\_NUMBCO)**.

**Função: DBGoto**Utilizando o ponto de entrada pela função: **DBGoto**, é posicionado na tabela corrente em um determinado registro, conforme a ordem física (sequência sobre o **recno**).

**Função: Dbseek**Utilizando o ponto de entrada pela função: **Dbseek,** é feito a pesquisa pela área de trabalho ativa para encontrar um determinado registro, de acordo com a chave de pesquisa utilizada.
