---
article_id: 14818789197079
category: TAF - eSocial - Atualização
content_hash: c3a8437d5215a83a629019ac21c300c7f112e7f008e8befa3658a39725c64919
fetched_at: '2026-06-28T22:45:13.314838+00:00'
product: protheus
section_id: 1500001547902
source: central-protheus
title: RH - Linha Protheus - TAF - eSocial - Atualização - Error.log Incorrect syntax
  near '1'
type: support-article
updated_at: '2026-06-23T11:52:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/14818789197079-RH-Linha-Protheus-TAF-eSocial-Atualiza%C3%A7%C3%A3o-Error-log-Incorrect-syntax-near-1
---

**Ocorrência**

O erro abaixo, exibido no arquivo error.log, pode ocorrer ao executar certas rotinas, como consultas de colaboradores ou integração com o TAF, em diferentes eventos ou tabelas:

**Exemplo do erro apresentado:**

```
"THREAD ERROR ([73600], xxxxxx, RH-06) 24/03/2023 15:47:04 :   
Error : 102 (37000) (RC=-1) - [Microsoft][SQL Server Native Client 11.0][SQL Server]Incorrect syntax near '1'.   
Error : 8180 (37000) (RC=-1) - [Microsoft][SQL Server Native Client 11.0][SQL Server]Statement(s) could not be prepared.
```

**Ambiente** TOTVS RH - TOTVS RH (Linha Protheus) - eSocial - TAF eSocial - Atualização - À partir da release 12.1.33

**Causa**A causa desse erro está relacionada ao conteúdo incorreto da chave DBDATABASE no arquivo appserver.ini.

**Solução**

Para corrigir o problema:

1. Abra o arquivo appserver.ini do Protheus para edição.
2. Habilite a chave TafDbLegacy=1 no ambiente desejado (environment):

**Exemplo:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/14818042842519)**

Para saber mais sobre o TAFDbLegacy, acesse o TDN abaixo:

<https://tdn.totvs.com/display/public/TAF/TafDbLegacy>

3. Após habilitar a chave acima, acesse os outros appserver's, como REST, Protheus, DBAccess, Master e Slave (se houver), e verifique se a chave DBDATABASE está definida como MSSQL7.

**Exemplo:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/14818474381975)**

4. Caso esteja definida como MSSQL7, remova o "7", deixando apenas DBDATABASE=MSSQL.

**Exemplo correto:**

```
DBDATABASE=MSSQL
```

5. Após realizar as alterações, é necessário interromper e reiniciar os serviços para que as mudanças tenham efeito.

Essas etapas devem resolver o problema relatado e garantir a correta execução das rotinas no ambiente Protheus. Certifique-se de seguir as instruções cuidadosamente e verificar se as alterações foram implementadas com sucesso.
