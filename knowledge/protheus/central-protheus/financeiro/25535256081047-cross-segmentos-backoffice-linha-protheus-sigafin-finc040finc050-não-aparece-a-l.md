---
article_id: 25535256081047
category: Financeiro
content_hash: d5e1760087e6b232d501df758f683cd97bff96a289972f5546519b4281b1f54f
fetched_at: '2026-06-28T22:38:03.237891+00:00'
product: protheus
section_id: 1500001550522
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINC040/FINC050 - Não
  aparece a linha referente a baixa do título a pagar ou receber na consulta posição
  cliente/fornecedor
type: support-article
updated_at: '2024-08-30T20:05:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/25535256081047-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINC040-FINC050-N%C3%A3o-aparece-a-linha-referente-a-baixa-do-t%C3%ADtulo-a-pagar-ou-receber-na-consulta-posi%C3%A7%C3%A3o-cliente-fornecedor
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25535261899671) Tempo aproximado para leitura: **00:15:00 min****Dúvida**Não aparece a linha referente a baixa do título a pagar ou receber na consulta posição cliente FINC040 / fornecedor FINC050   
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Solução**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/25535261902103)**

Para solucionar essa dúvida, realize os seguintes passos:  
O que faz o sistema a amarrar a tabela SE1/SE2 com a tabela SE5 é a chave filial+prefixo+numero+parcela+tipo+cliente/fornecedor+loja

Essa chave deverá ter o mesmo conteúdo entre as tabelas SE1 ou SE2 e SE5.

Deverá ter o mesmo conteúdo, como a mesma quantidade de carácter de cada campo.

Vamos fazer um exemplo de erro de base, onde o título a receber foi baixado, porém não aparece a linha de baixa

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/25535256055703)](https://centraldeatendimento.totvs.com/hc/article_attachments/25535256055703)

 1 - Vamos comparar o conteúdo de cada campo que faz parte da chave entre as tabelas SE1/SE2 e SE5

Via APSDU vamos abrir

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/25535261905687)](https://centraldeatendimento.totvs.com/hc/article_attachments/25535261905687)

Abrimos a tabela SE1

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/25535256057879)](https://centraldeatendimento.totvs.com/hc/article_attachments/25535256057879)

Abrimos a tabela SE5

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/25535261907223)](https://centraldeatendimento.totvs.com/hc/article_attachments/25535261907223)

E neste caso os conteúdos estão corretos

2 - Vamos comparar o tamanho de todos os campos que fazem parte da chave

Na APSDU, iremos abrir a opção "Estrutura"

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/25535261908247)](https://centraldeatendimento.totvs.com/hc/article_attachments/25535261908247)

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/25535256061463)](https://centraldeatendimento.totvs.com/hc/article_attachments/25535256061463)

Nesta opção podemos ver o tamanho de cada campo da tabela SE1, veja que o campo parcela eu tenho um tamanho de 2 carácter

Posicionando na tabela SE5 e clicando em "arquivo > estrutura"

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/25535261913751)](https://centraldeatendimento.totvs.com/hc/article_attachments/25535261913751)

Conseguimos observar que o campo E5\_PARCELA possui um tamanho diferente da tabela E1\_PARCELA

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/25535256063639)](https://centraldeatendimento.totvs.com/hc/article_attachments/25535256063639)

E por isso do erro de não mostrar a baixa do título.

Esse problema poderá ocorrer em qualquer campos da chave que esteja com diferença de conteúdo ou de tamanho.

**Sabia mais**

Outros cenário com problemas de base.

[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA340 - HELP: NOTITSEL](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021352991-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA340-HELP-NOTITSEL)

[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA330 - HELP:NOTITSEL](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500012361522-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA330-HELP-NOTITSEL)

[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Help: TITNAOXADO ao cancelar a baixa do título](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053001473-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Help-TITNAOXADO-ao-cancelar-a-baixa-do-t%C3%ADtulo)

[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - CTBAFIN - Contabilização duplicando ou gerando gravação incorreta do campo da tabela Sequência de Baixa (E5\_SEQ)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/18890795067927-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-CTBAFIN-Contabiliza%C3%A7%C3%A3o-duplicando-ou-gerando-grava%C3%A7%C3%A3o-incorreta-do-campo-da-tabela-Sequ%C3%AAncia-de-Baixa-E5-SEQ)

[TOTVS Diagnóstico de Dicionários](https://tdn.totvs.com.br/pages/releaseview.action?pageId=725728577)
