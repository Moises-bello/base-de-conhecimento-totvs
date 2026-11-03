---
article_id: 33489674647319
category: SIGAEST - CADASTROS E CONFIGURAÇÕES GERAIS
content_hash: eb2c3161fb27f7762b7c03b1b8c27fcaa41d35215111e121b718776bdf65bc79
fetched_at: '2026-06-28T22:39:08.248741+00:00'
product: protheus
section_id: 1500001550022
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Failed Parse XML.
  on FWSERIALIZE:XMLMANGERDESERIALIZER(FWSERIALIZE.PRW)
type: support-article
updated_at: '2025-07-15T19:26:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/33489674647319-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Failed-Parse-XML-on-FWSERIALIZE-XMLMANGERDESERIALIZER-FWSERIALIZE-PRW
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33489674634007) Tempo aproximado para leitura: **00:02:00 min**  
  
**Ocorrência**  
Ao acessar uma rotina o sistema exibe o error.log:

`erro no parâmetroFwSerialize: XMLParse Error:Start tag expected, '<' not found`  
`[xmlReadMemory]Failed Parse XML. on FWSERIALIZE:XMLMANGERDESERIALIZER(FWSERIALIZE.PRW)`  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAEST - A partir da versão 12  
  
**Causa**  
Ao criar uma visão no Browse da rotina ([Como criar visões nas rotinas?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/33339946632215-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-criar-vis%C3%B5es-nas-rotinas)), o sistema realiza a gravação de um arquivo XML na pasta "Views" que fica dentro da pasta "Protheus Data" no diretório de instalação do Protheus.

Se houver algum erro na geração do arquivo XML, alguma modificação ou mesmo se estiver corrompido, ao tentar abrir o Browse da rotina onde a View foi criada, o sistema pode apresentar erros como o "Failed Parse XML".  
  
**Solução**  
Para solucionar essa ocorrência, você pode renomear o arquivo XML na pasta "Views" que fica dentro da pasta "Protheus Data", assim o sistema não irá mais consultá-lo, deixando de gerar o erro.

O único efeito em renomear/excluir o arquivo, seria ter que refazer a visão, fora isso não há alteração no comportamento da rotina, caso necessite de auxilio em recriar a visão, consulte "[Como criar visões nas rotinas?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/33339946632215-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-criar-vis%C3%B5es-nas-rotinas)"

**Saiba mais:**

[Clique aqui e veja mais artigos sobre CADASTROS E CONFIGURAÇÕES GERAIS no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550022-SIGAEST-CADASTROS-E-CONFIGURA%C3%87%C3%95ES-GERAIS)
