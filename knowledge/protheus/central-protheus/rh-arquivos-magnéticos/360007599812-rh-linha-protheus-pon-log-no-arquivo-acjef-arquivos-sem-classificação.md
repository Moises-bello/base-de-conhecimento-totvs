---
article_id: 360007599812
category: RH - Arquivos Magnéticos
content_hash: 1349b4ad241a2991800db40a2bc2011fdda59e0b4481530dbe54e228723f22e8
fetched_at: '2026-06-28T22:44:55.295656+00:00'
product: protheus
section_id: 32302371669783
source: central-protheus
title: RH - Linha Protheus - PON - Log no arquivo ACJEF - Arquivos sem classificação
type: support-article
updated_at: '2025-11-12T18:53:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007599812-RH-Linha-Protheus-PON-Log-no-arquivo-ACJEF-Arquivos-sem-classifica%C3%A7%C3%A3o
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33772881215255) Tempo aproximado para leitura: 01:00:00 min  
  
Dúvida**Log no arquivo ACJEF - Arquivos sem classificação.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**Para solucionar essa dúvida, realize os seguintes passos:  
**1.** Verifique se as tabelas **SP4, SP9 e SX5** possuem o mesmo compartilhamento na **SX2** e, consequentemente, possuem o campo filial corretamente cadastrado **em branco (Se o compartilhamento for C-C-C):**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/30099552744471)  
  
Ou preenchido **(Se o compartilhamento for E-E-E)**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/30099594102295)

**2**. Acesse a tabela **SP4** e confira se todos os eventos de hora extras cadastrados estão com a classificação correta como 01 - Hora Extra, se não estiverem, classifique corretamente, exemplo:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/30099594103063)  
  
**3**. Gere novamente o arquivo ACJEF.

\*\* Importante: Os 8 primeiros tipos de horas extras são obrigatórios ao sistema e, em cada tipo deve haver um evento diferente, ou seja, não podemos repetir um mesmo código de evento em mais de um [tipo de hora extra](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060489314).

**Atenção:**  
Com a entrada em vigor da Portaria nº 671/2021, os arquivos AFDT e ACJEF foram substituídos pelo AEJ (Arquivo Eletrônico de Jornada). Os Programas de Tratamento de Registro de Ponto (PTRP) têm até 11/01/2023 para se adequarem ao novo leiaute. Portanto, até 10/01/2022 o PTRP ainda pode gerar os arquivos AFDT e ACJEF (alteração trazida pela Portaria MTP nº 3.717, de 9 de novembro de 2022 que ampliou o prazo contido na Portaria MTP nº 671, de 8 de novembro de 2021). Portanto, só poderá ser utilizado estes arquivos AFDT e ACJEF da portaria antiga 1510 somente até 10/01/2022.

**Saiba mais:**[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)[Pacote de Expedição Contínua Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)
