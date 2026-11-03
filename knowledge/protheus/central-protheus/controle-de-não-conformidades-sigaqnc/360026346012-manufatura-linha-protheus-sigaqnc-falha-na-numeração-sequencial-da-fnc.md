---
article_id: 360026346012
category: Controle de Não Conformidades (SIGAQNC)
content_hash: efb6dc7fda8997308490e8eb432592827b83ed5b4d34eae37373858ce5949b5d
fetched_at: '2026-06-28T22:42:27.947209+00:00'
product: protheus
section_id: 360005876654
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQNC - Falha na numeração sequencial da FNC
type: support-article
updated_at: '2021-05-10T21:12:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026346012-Manufatura-Linha-Protheus-SIGAQNC-Falha-na-numera%C3%A7%C3%A3o-sequencial-da-FNC
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:01:40 min****Ocorrência**Ao incluir uma **FNC -****Ficha de Ocorrência e Não Conformidade** é apresentada mensagem de **falha no inicializador padrão**. Em alguns casos, a sequência é gerada, porém está incorreta.   
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) – Controle de Não Conformidades (SIGAQNC) – Todas as versões  
  
**Causa**Esta situação ocorre quando o inicializador padrão está incorreto ou porque as tabelas que controlam a numeração **QNSXE** e **QNSXF** não constam no banco de dados.  
  
**Solução**Para solucionar esta ocorrência, siga os procedimentos abaixo:  
1. No módulo **SIGACFG - Configurador**, na opção **Dicionário de dados**, verifique se o inicializador padrão do campo está com a expressão a seguir. Caso não estiver, realize o ajuste, salve e faça um novo teste:

```
IF(INCLUI,GETQNCNUM("QI2","QI2_FNC",,1,STRZERO(YEAR(DDATABASE),4),@AQNQI2),) 
```

2. Através do **APSDU** ou **Gerenciador de banco de dados**, verifique se as tabelas **QNSXE** e **QNSXF**constam em seu banco de dados. Caso não constar, é necessário acessar a pasta **.\protheus\_data\system** do seu servidor, localizar os arquivos **QNSXE** e **QNSXF** e importá-los para o seu banco de dados. Após importar estes arquivos, é necessário apagá-los da pasta **system**.  
  
3. Caso ainda assim a inconsistência com a numeração persistir, abrir *ticket* com as tabelas **QNSXE** e **QNSXF** completas, a data dos fontes **QNCXFUN** e **QNCA040 - Cadastro de Ocorrências/Não-Conformidades** e a evidência demonstrando a situação que está ocorrendo.  
  
**Importante**Caso deseje que, ao cancelar a tela de inclusão da **FNC**, o número em questão seja reutilizado para a próxima **FNC**, configure o parâmetro **MV\_QNCVSEQ - Define se devera ser recuperado Código Sequencial da Ficha Não-Conformidades e Plano de Ação após um cancelamento ou exclusão** como **S - Sim**.
