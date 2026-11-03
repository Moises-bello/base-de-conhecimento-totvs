---
article_id: 360021323352
category: Controle de Documentos (SIGAQDO)
content_hash: bdf50fcb3f7e51d2bd167fedfca853e905a91cc4a86ce4da6369b63ee2c9af0b
fetched_at: '2026-06-28T22:42:29.964388+00:00'
product: protheus
section_id: 360005906113
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQDO - Usuário não autorizado a gerar revisão
type: support-article
updated_at: '2023-04-20T18:33:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021323352-Manufatura-Linha-Protheus-SIGAQDO-Usu%C3%A1rio-n%C3%A3o-autorizado-a-gerar-revis%C3%A3o
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*Tempo aproximado para leitura: **00:01:30 min  
  
Ocorrência**Ao tentar incluir uma nova revisão, é apresentada a mensagem **Usuário não autorizado a gerar revisão**.   
  
**Ambiente**  
TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Controle de Documentos (SIGAQDO) - Todas as versões  
  
**Causa**Esta mensagem é apresentada devido à falta de permissão do usuário para gerar uma revisão.  
  
**Solução**  
1. Verificar no **QDOA020 - Cadastro de Tipo de Documento**, no botão **outras Ações > Niv. Resp**. quais etapas estão com a opção **Gera Revisão = Sim**. Apenas os usuários pertencentes à estas etapas poderão gerar revisão.  
  
2. Para verificar quais departamentos e funções são responsáveis por cada etapa, acesse a rotina **QDOA020,** edite o tipo de documento em questão e clique no botão **Outras Ações > Respons.**  
3. Ainda na rotina **QDOA020**, verifique se a coluna **Acumula Revisão** está preenchida como **Sim** para as etapas que tem a permissão para gerar revisão. Com o campo preenchido com **Sim**, caso for admitido um usuário novo que se enquadra nos responsáveis no tipo de **Documento**, ao gerar revisão, o **Protheus** verifica o campo e consulta novamente os usuários que estão na condição de responsáveis. Desta forma, usuários que não possuíam a permissão para gerar revisão na revisão anterior, serão acrescentados para a nova revisão.  
  
4. Caso desejar que o usuário digitador do documento, isto é, o usuário que incluiu o documento no Sistema, mas não necessariamente é o elaborador possa gerar revisões, configure o parâmetro **MV\_QDOREVD - Define se o Digitador pode Gerar Revisão. (1=SIM 2=NAO)** com conteúdo igual à **1**.
