---
article_id: 4414516581911
category: RH - Leitura e Apontamento
content_hash: 8d8ab0f770f3b688930ab437f4fafa257fc7bd0fc82f373b2f94d6d564066af8
fetched_at: '2026-06-28T22:44:46.018873+00:00'
product: protheus
section_id: 32419281460119
source: central-protheus
title: RH - Linha Protheus - PON - Significado dos campos RFE_FLAG e RFE_NATU da tabela
  RFE
type: support-article
updated_at: '2025-10-03T18:45:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4414516581911-RH-Linha-Protheus-PON-Significado-dos-campos-RFE-FLAG-e-RFE-NATU-da-tabela-RFE
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19448323540375) Tempo aproximado para leitura: **00:01:30 min** **Dúvida**Qual o significado dos campos RFE\_FLAG e RFE\_NATU da tabela RFE?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões.  
  
**Solução**Os campos **RFE\_FLAG** e **RFE\_NATU** são campos utilizados após o processamento das marcações.  
  
O campo RFE\_FLAG indica se a marcação presente na tabela RFE foi processada ou não, sendo:  
**> RFE\_FLAG = 1** significa que a marcação **foi processada**  
**> RFE\_FLAG = 0** significa que a marcação **não foi processada.**  
  
O campo RFE\_NATU indica qual natureza da marcação lida, sendo:  
**> RFE\_NATU= 0** significa que o crachá **foi identificado e pertence a um Funcionário**  
**> RFE\_NATU = 1** significa que o crachá **é de Visitante**  
**> RFE\_NATU = 2** significa que o crachá **é de Acesso**  
**> RFE\_NATU = 3** significa que o crachá **não foi identificado**  
  
Inicialmente ao realizar a leitura de um arquivo de marcações do ponto, refeições, acesso ou de visitantes, o conteúdo do **RFE\_FLAG** será **0** e **RFE\_NATU = 3**. Após o sistema processar essa marcação, em caso de sucesso o RFE\_FLAG terá seu conteúdo alterado para 1 e o RFE\_NATU será alterado para sua finalidade. 

**> Exemplo de Marcação de Ponto:**  
Com a Leitura das Marcações, teremos a princípio:  
RFE\_FLAG = 0  
RFE\_NATU = 3  
Após o processamento, teremos:  
RFE\_FLAG = 1  
RFE\_NATU = 0  
Isso significa que a marcação foi processada, ou seja, o sistema conseguiu identificar o funcionário que realizou a marcação e ela foi para a Tabela de Marcações - SP8. Em casos do sistema não encontrar o funcionário, a marcação ficará com o mesmo conteúdo inicial, ou seja, RFE\_FLAG = 0 e RFE\_NATU = 3.

**> Exemplo de Marcação de Refeição:**Com a Leitura das Marcações de Refeição, teremos a princípio:  
RFE\_FLAG = 0  
RFE\_NATU = 3  
Após o processamento, teremos:  
RFE\_FLAG = 1  
RFE\_NATU = 0  
Isso significa que a marcação foi processada, ou seja, o sistema conseguiu identificar o funcionário que realizou a marcação de refeição e ela foi para a Tabela de Marcações de Refeição - SP5. Em casos do sistema não encontrar o funcionário, a marcação ficará com o mesmo conteúdo inicial, ou seja, RFE\_FLAG = 0 e RFE\_NATU = 3.

**> Exemplo de Marcação de Acesso:**Com a Leitura das Marcações de Acesso, teremos a princípio:  
RFE\_FLAG = 0  
RFE\_NATU = 3  
Após o processamento, teremos:  
RFE\_FLAG = 1  
RFE\_NATU = 2  
Isso significa que a marcação foi processada, ou seja, ela foi para a Tabela de Acessos e Visitantes - SPZ. Neste caso o sistema não busca o acesso do visitante em si para realizar a identificação para o preenchimento do campo RFE\_NATU, ele apenas marca como uma marcação de acesso.

**> Exemplo de Marcação de Visitante:**  
Com a Leitura das Marcações de Visitante, teremos a princípio:  
RFE\_FLAG = 0  
RFE\_NATU = 3  
Após o processamento, teremos:  
RFE\_FLAG = 1  
RFE\_NATU = 1  
Isso significa que a marcação foi processada, ou seja, ela foi para a Tabela de Acessos e Visitantes - SPZ. Neste caso o sistema não busca o visitante em si para realizar a identificação para o preenchimento do campo RFE\_NATU, ele apenas marca como uma marcação de visitante.  
  
  
****Saiba mais:**[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)**[Campos RFE\_FLAG e RFE\_NATU](https://tdn.totvs.com/display/public/PROT/Campos+RFE_FLAG+e+RFE_NATU)
