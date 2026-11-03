---
article_id: 360025333891
category: Controle de Documentos (SIGAQDO)
content_hash: 99f16df21ef25c7870c53296841e8f81a63ae41e57a66c50c0d4d4b730bdb87d
fetched_at: '2026-06-28T22:42:29.198316+00:00'
product: protheus
section_id: 360005906113
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQDO - Não foi encontrada a referência para
  o arquivo na base de dados
type: support-article
updated_at: '2021-09-08T12:58:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025333891-Manufatura-Linha-Protheus-SIGAQDO-N%C3%A3o-foi-encontrada-a-refer%C3%AAncia-para-o-arquivo-na-base-de-dados
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:01:40 min****Ocorrência**Ao tentar visualizar um documento é apresentada a mensagem: **QDCDOCERR - Não foi encontrada a referência para o arquivo na base de dados**  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Controle de Documentos (SIGAQDO) - Todas as versões  
  
**Causa**A mensagem **QDCDOCERR** é apresentada quando ocorreu perda de vínculo do arquivo do documento armazenado no diretório da instalação do Protheus com o registro localizado na tabela **QDH - Documentos** no campo **QDH\_NOMDOC - Nome do Arquivo Docto**.  
  
**Solução**  
Para solucionar este erro, realize os seguintes passos:  
1. Abra o **APSDU**;  
2. Abra a tabela **QDH** e filtre pelo documento em questão, utilizando o campo **QDH\_DOCTO - Código do Documento**;  
3. Verifique o conteúdo do campo **QDH\_NOMDOC** do documento filtrado no passo anterior;  
4. Busque por este arquivo no diretório de armazenamento de arquivos no servidor. Este diretório fica abaixo da pasta **protheus\_data**. Para verificar o diretório completo, verifique o conteúdo do parâmetro **MV\_QPATHW - Define o diretorio onde contem os arquivos dos Documentos**;5. Caso confirmado que o arquivo não está na pasta, será necessário recuperá-lo e colocá-lo na pasta novamente. Em geral este tipo de situação ocorre devido à alguma manutenção no servidor ou reversão do **backup**. Esta análise deverá ser realizada pelo administrador do servidor, com base nas últimas alterações feitas antes do erro ser apresentado para os usuários.
