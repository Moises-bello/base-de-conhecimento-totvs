---
article_id: 5458822012311
category: Faturamento - Cadastros
content_hash: 188c4a73b6c947600ddad3f251c0f151e6b973691b3b0799c228a2eda5e88189
fetched_at: '2026-06-28T22:38:35.327070+00:00'
product: protheus
section_id: 1500001539221
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - Sigafat - O campoA1_XXXX
  refira à pasta:5, mas não existe. on FWFORMFIELD:PREPAREFIELDS(FWFORMFIELD.PRW)
type: support-article
updated_at: '2022-04-19T13:43:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5458822012311-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-Sigafat-O-campoA1-XXXX-refira-%C3%A0-pasta-5-mas-n%C3%A3o-existe-on-FWFORMFIELD-PREPAREFIELDS-FWFORMFIELD-PRW
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**Ao incluir ou alterar um registro no cadastro de cliente , utilizando a rotina crma980, ocorre o erro:

O campoA1\_XXXX refira à pasta:5, mas não existe. on FWFORMFIELD:PREPAREFIELDS(FWFORMFIELD.PRW) 04/02/2022 16:14:28 line : 408"  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Sigafat- Todas as versões  
  
**Causa**O sistema reclama que o campo apontado  não foi direcionado corretamente a pasta 5 do cadastro de cliente.

Por exemplo:

O campoA1\_CONTATO2 refira à pasta:5, mas não existe. on FWFORMFIELD:PREPAREFIELDS(FWFORMFIELD.PRW) 04/02/2022 16:14:28 line : 408"

Neste exemplo acima , o sistema informa que o campo a1\_contato2, campo de usuário, não está endereçado a pasta correta do cadastro do cliente, sendo necessário verificar a pasta correta e endereçar o campo.

Esta inconsistência pode ocorrer com qualquer campo ou tabela do sistema.  
  
**Solução**  
Verifique o **X3\_FOLDER** do campo em questão, se está preenchido com uma pasta que não existe na tabela "Clientes (SA1)".

Segue abaixo a estrutura de pastas da SA1:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5457345888919/mceclip0.png)

Pegando como exemplo, o campo padrão a1\_contato, ele se encontra na pasta cadastrais:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5458259247767/mceclip1.png)

Ajustando o campo na pasta correta, o erro deixa de ocorrer.
