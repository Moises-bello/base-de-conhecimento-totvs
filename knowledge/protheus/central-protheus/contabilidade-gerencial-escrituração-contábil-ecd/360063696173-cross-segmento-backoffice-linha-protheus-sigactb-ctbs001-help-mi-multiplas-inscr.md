---
article_id: 360063696173
category: Contabilidade Gerencial - Escrituração-Contábil-ECD
content_hash: 036001147eac20b4a158156a23ffe91563d147602d77e7b80b9a9fd09a801c77
fetched_at: '2026-06-28T22:40:45.634310+00:00'
product: protheus
section_id: 1500001548702
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGACTB- CTBS001 - HELP: MI-
  MULTIPLAS INSCRIÇÕES'
type: support-article
updated_at: '2021-04-28T22:07:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360063696173-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBS001-HELP-MI-MULTIPLAS-INSCRI%C3%87%C3%95ES
---

**Ocorrência**Ao exportar a ECD (CTBS001), na tela de Outras Inscrições, apresenta o seguinte mensagem:

HELP: MI- MULTIPLAS INSCRIÇÕES

Problemas: Atualize o sistema executando o UPDDISTR do ECD.

![image.png](https://mail.google.com/mail/u/0?ui=2&ik=3ae937b27b&attid=0.6&permmsgid=msg-a:r810336508686026221&th=177f7e2e331cce99&view=fimg&sz=s0-l75-ft&attbid=ANGjdJ8yZCRf71pEaDCxEDdphCIKskrKWJGPLlHf1usJYekEJ8mI7b8YjFCqAkx9yGr1PFAz9PKdZFCIeZtVYZrnEwvBkY78Qk3odIn0SM1j1nzenZq7tEyqI0zQ8QI&disp=emb&realattid=ii_kltd3eya8)  
**Ambiente**Cross Segmento - Backoffice Linha Protheus  – Contabilidade Gerencial – CTBS001 – A partir da versão 12  
  
**Causa**Sistema não encontrou a Tabela CSS (Múltiplas inscrições) no ambiente

**Solução**Antes da atualização referente o leiaute 9. Certifique-se que o pacote acumulado do **SIGACTB** + diferencial estão atualizados no ambiente.

Pacote acumulado (caso não tenha atualizado) + dicionário (criação da CSS + acumulado)

<https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/CTB_EXPEDICAO_CONTINUA>

**Tabela CSS**- Foi criada no leiaute 8.

Arquivo SDFBRA.TXT :

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360104598873/mceclip0.png)

**Saiba mais**

<https://tdn.totvs.com/display/public/PROT/ECD>

<https://tdn.totvs.com/pages/releaseview.action?pageId=544728585>
