---
article_id: 35487580271511
category: Financeiro - Smart View
content_hash: 50d650e3e7259146651f061f27038fa34a7654ea899694b5752cbb47f27f17db
fetched_at: '2026-06-28T22:37:44.718474+00:00'
product: protheus
section_id: 32632656432151
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Coleta de Logs para
  Análise de erros nos relatórios SmartView
type: support-article
updated_at: '2026-01-09T20:50:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35487580271511-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Coleta-de-Logs-para-An%C3%A1lise-de-erros-nos-relat%C3%B3rios-SmartView
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35487580259351) Tempo aproximado para leitura: **00:15 min**  
  
**Dúvida**  
Durante a geração de relatórios SmartView no financeiro, são apresentados erros em tela. Como avaliar os logs gerados e coletá-los para validação?

**Erros comuns**

*- O ERP TOTVS teve um comportamento inesperado.*  
*- connectors.native.internal-server-error*  
*- connectors.native.failed-to-deserialize*  
*- 400 BadRequest*  
*- 500 InternalServerError*  
*- Http failure response for*  
*- Relatório não existe ou não cadastrado corretamente na tabela de/para*  
*- O conteúdo retornado pelo ERP TOTVS não condiz com o padrão esperado.*  
*- Não foi possível consultar as informações de configuração do DiscoveryEndpoint*  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro – A partir da release 12.1.2310  
  
**Solução**

Caso algum relatório do **Smart View** apresente **erro em tela** ou qualquer tipo de **inconsistência durante a execução**, é fundamental realizar a **coleta dos logs do ambiente**.

Esses registros são essenciais para uma **análise precisa** e para a **identificação da causa do problema**, permitindo correlacionar as informações técnicas por meio das **chaves e parâmetros utilizados na execução**.

**IMPORTANTE**

As validações dos relatórios SmartView funcionam com linguagens avançadas e, com isso, é extremamente importante certificar-se das atualizações mais recentes em seu ambiente.

1. [**Pacote Acumulado (conforme sua versão)**](https://tdn.totvs.com/pages/releaseview.action?pageId=531017758)
2. [**Pacotes LIB**](https://suporte.totvs.com/portal/p/10098/download#000006/368/TFLIB/search/searchAll)
3. [**Pacotes DBAccess**](https://suporte.totvs.com/portal/p/10098/download#000006/368/TFDBA/search/searchAll)
4. [**Binário AppServer**](https://suporte.totvs.com/portal/p/10098/download#000006/368/TFAPP/)
5. [**Binário SmartClient / WebApp**](https://suporte.totvs.com/portal/p/10098/download#000006/368/TFSC/)
6. [**Central de Atualizações**](https://suporte.totvs.com/portal/p/10098/download?e=946864#000006/368/TFSC/)

Um ponto fundamental nas atualizações é a **validação da equivalência entre o RPO principal e o RPO do REST**, especialmente quando este estiver **alocado em um servidor separado**.

É importante **manter seu produto sempre atualizado**, utilizando a **última versão disponível no Portal de Clientes (Central de Download)**. Dessa forma, você garante que todas as **melhorias e correções** disponibilizadas estejam contempladas no ambiente.

Reforçamos que **todos os procedimentos devem ser realizados primeiro em ambiente de TESTE**, devidamente atualizado e validado, antes da aplicação em produção.

Esta seção foi criada para reunir **informações importantes e soluções rápidas** para eventuais situações que possam ocorrer.  
Explore os tópicos disponíveis no link abaixo para esclarecer suas dúvidas e facilitar sua experiência:

## **Configuração de Chaves para Coleta de Logs**

Antes da reprodução do erro, recomendamos configurar as seguintes chaves na seção [ambiente]: insira

* **TraceStack=1**  
  Documentação: [TDN - TraceStack](https://tdn.totvs.com/x/jopc)
* **FWTRACELOG=1**  
  Documentação: [TDN - FWTRACELOG](https://tdn.totvs.com/x/Yc6qKg)

Na sessão General:

* **LogHttpFuncs=1**  
  Documentação: [TDN - LogHttpFuncs](https://tdn.totvs.com/x/MY5vI)
* **ConsoleMaxSize**=10485760  
  Documentação: [TDN](https://tdn.totvs.com/x/MY5vI) [- ConsoleMaxSize](https://tdn.totvs.com/display/tec/ConsoleMaxSize)
* **Rest\_log\_level**=6

  Documentação: [TDN](https://tdn.totvs.com/x/MY5vI) [- rest\_log\_level](https://tdn.totvs.com/display/tec/rest_log_level)

Essas **chaves devem ser aplicadas no arquivo** ****AppServer.ini**** do ambiente correspondente e permanecerão **ativas durante a execução do serviço**.  
Após a conclusão do processo de coleta, é **necessário desativar as chaves** para retornar à configuração padrão do ambiente.

## **Coleta de Log pelo Smart View**

Adicionalmente, é possível obter informações relevantes diretamente do próprio serviço do SmartView, o que contribui para uma análise complementar dos **logs da aplicação e do serviço**.

**Acesse:**  
[FAQ - Protheus/Smart View](https://tdn.totvs.com/x/WoyLN)  
[TDN - FAQ Smart View](https://tdn.totvs.com/x/WoyLN)

> Consulte a sessão **“Dúvidas Frequentes”**, item **“Quais logs devo analisar/enviar caso tenha um erro/problema”**.
>
> ![Screenshot_1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35487525091351)

## **Procedimento para Captura de Logs**

Após configurar as chaves acima, siga os passos a seguir:

1. **Apague o arquivo**`console.log` da sessão atual do ambiente (presente na pasta `log` do AppServer ou onde definiu para gravar o arquivo log).
2. **Reinicie o serviço do AppServer em modo exclusivo**, se possível, para garantir que a integridade na coleta seja apenas nesse serviço. Caso não possa fazer, certifique-se de que a coleta está sendo realizada no slave devido.
3. **Reproduza o erro novamente**, executando o relatório que apresenta a falha.
4. **Envie o novo**`console.log`**gerado**, juntamente com o **log do SmartView se possível.**
5. **Anexe o Inspetor de Objetos** para uma verificação técnica mais detalhada da data dos fontes
6. **Capture uma imagem da rotina**:  
   **SIGACFG > Ambiente > Cadastros > Configuração TReports/Smart View**  
   Opção: **Token**, no módulo **Configurador**.
7. **Informe se o problema ocorre em todos os relatórios ou apenas em um específico.**
8. **Valide se o seu agent esta, atualizado:**

   **![Screenshot_2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35487525091991)**

A correta coleta e envio dessas informações são essenciais para que a equipe do suporte possa avaliar com precisão o cenário reportado e dar continuidade à tratativa do incidente, seja no módulo de financeiro ou áreas relacionadas.

## **Onde é que ficam os meus LOGS para coleta e envio?**

Os logs estão armazenados nas pastas internas do ambiente. Recomenda-se solicitar ao **time de TI** a extração desses arquivos. Caso não possua acesso, encaminhe este boletim à equipe responsável, pois assim será mais fácil realizar o procedimento conforme as instruções.

## **Mas o meu ambiente fica no T-CLOUD. Como pego os logs no T-CLOUD?**

Caso o seu ambiente esteja **hospedado na Cloud TOTVS**, a **limpeza do console** pode não ser viável de forma imediata. Se você **não possuir acesso direto**, será necessário **abrir uma solicitação** para que a **equipe da Cloud** realize essa ação.

No entanto, é possível **coletar os logs, diretamente pelo Portal** ou via **FTP**.  
Esse procedimento pode ser executado normalmente pelo **time de TI** ou por você, caso tenha acesso ao portal.

🔹 **Atenção:**  
Certifique-se de **coletar os logs do ambiente correto** e **referentes ao período exato do teste**.  
Por exemplo: se o teste foi executado em **28/07/2025 às 10h00**, mas o log disponível apresenta **data e hora anteriores**, o arquivo está incorreto.

Nessa situação, **atualize a página (F5)** algumas vezes para verificar se o log foi atualizado.  
Se o problema persistir, **entre em contato com o time da Cloud** para verificar a atualização ou disponibilização correta do log.

[CLOUD - MP - Download de logs (TCLOUD)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4408646347671-CLOUD-MP-Download-de-logs-TCLOUD)

**Pontual erro:**não foi possível consultar as informações de configuração do DiscoveryEndpoint

Validar se a comunicação dentro do appserver não está apontando para a instância de um serviço integrado, por exemplo, a tag Module=46.

```
[HTTPURI]             
URL=/rest             
PrepareIn=T1         
Instances=2,5,1,1     
CORSEnable=1          
AllowOrigin=*         
Module=46
```

**Observação:**

Essa **TAG** deve ser utilizada **apenas** quando o ambiente **não possuir as licenças FULL e T**. Caso esteja ativa indevidamente, ela entrará em concorrência com o **REST**, ocasionando **erro na tentativa de conexão com o ERP**.

**Não foi possível consultar as informações de configuração do DiscoveryEndpoint**

![resterroaut.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35487525092375)

###### 

Também é necessário **enviar a “Central de Diagnóstico”**, gerada a partir da rotina em que ocorre o problema. Essa ferramenta é **fundamental para que o suporte possa validar** os **fontes, PEs, atualizações** e demais informações técnicas relacionadas.

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como enviar dados pela Central de Diagnóstico?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/33711098138007-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-enviar-dados-pela-Central-de-Diagn%C3%B3stico)

## **Validações pontuais pela sua equipe de infra que possa interessar:**

Em determinadas situações, o problema pode estar relacionado à **compatibilidade do banco de dados**. Nesse caso, recomenda-se **verificar a versão do banco** e, se possível, **nos encaminhar o resultado dessas consultas**. Essas informações são importantes para análise e, se necessário, **para o encaminhamento ao time de Framework**.

Exemplo em **SQL**:

```
SELECT @@VERSION AS 'SQL Server Version
```

![Screenshot_8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35487525092887)

Valide também a configuração de Level de compatibilidade de seu banco de dados.

```
SELECT compatibility_level
FROM sys.databases
WHERE [name] = 'NomeDaBase'
```

![Screenshot_1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35487580263319)

**Importante**

'NomeDaBase' é o nome do banco utilizado na configuração do Smart View.

**Saiba mais**

[Nível de compatibilidade Microsoft](https://learn.microsoft.com/pt-br/sql/t-sql/statements/alter-database-transact-sql-compatibility-level?view=sql-server-ver17)
