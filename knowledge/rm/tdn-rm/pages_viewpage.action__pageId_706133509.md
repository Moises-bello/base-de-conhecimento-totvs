---
content_hash: 2270600ee87fa891a006bbb7b36ace1377757d6867387b292c8ba175623b30bf
fetched_at: '2026-06-29T00:11:22.608845+00:00'
page_id: '706133509'
product: rm
source: tdn-rm
title: Processo - Serviço Rest
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=706133509
version: 30
---

Documentações RestAs documentações à seguir, foram criadas porque existem particularidades nas chamadas RESTs.  
Para os outros serviços RESTS, deve-se seguir as recomendações da Framework TOTVS.Dicas

Para auxiliar na compreensão de como preencher os parâmetros (obtidos pela chamada do ***GetSchema*** do processo) para execução do processo, execute o processo com sucesso via MDI e utilize as informações da execução disponíveis no monitor de Jobs (**Ambiente | Monitor de Jobs**).  Na lista de Jobs, edite o respectivo Job, e visualize os parâmetros que foram informados para a execução do processo na aba Processo:

Exemplo de dados da aba Processo

Ou visualize essas informações em formato XML acessando o menu **Anexos | XML de parâmetros de Jobs - Última utilização - (WebServices).** Dependendo do tipo do parâmetro do processo, só será possível visualizar essas informações em detalhes utilizando a opção de parâmetros em formado XML.

Ex: As informações de preenchimento de ***PrimaryKeyList*** e ***PrimaryKeyNames*** estão detalhadas somente no formato XML:

Exemplo de dados do anexo XML de parâmetros de Jobs - Última utilização - (WebServices)

O body da seguinte requisição foi preenchido seguindo as dicas:

Exemplo da requisição para execução do processo EduGeracaoUsuariosData

Url: http://localhost:8051/rest/restprocess/executeProcess/EduGeracaoUsuariosData

Body

## **Páginas:**
