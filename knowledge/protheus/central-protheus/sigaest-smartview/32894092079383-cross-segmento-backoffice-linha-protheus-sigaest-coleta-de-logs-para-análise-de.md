---
article_id: 32894092079383
category: SIGAEST - SMARTVIEW
content_hash: dd27ec5d2dff12380faf6241be8a2759478d4b227adbe0127a269f01020629ad
fetched_at: '2026-06-28T22:38:47.161446+00:00'
product: protheus
section_id: 16108365627287
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Coleta de Logs para
  Análise de erros nos relatorios SmartView
type: support-article
updated_at: '2026-03-11T17:16:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/32894092079383-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Coleta-de-Logs-para-An%C3%A1lise-de-erros-nos-relatorios-SmartView
---

O artigo orienta sobre a coleta e análise de logs para resolver erros em relatórios Smart View no TOTVS Protheus (Estoque/Custos). Recomenda atualizar o ambiente, configurar chaves no AppServer.ini, reiniciar serviços, reproduzir erros e enviar logs para suporte. Também aborda procedimentos para ambientes Cloud e validações de banco de dados para diagnóstico.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32894092069655) Tempo aproximado para leitura: **00:03:00 min**  
  
**Dúvida**  
Durante a geração de relatorios smartview no estoque custos e areas correlacionadas, é apresentado erros em tela, como avaliar os logs gerados, e coleta-los para validação?

**Erros comuns**

*- O ERP TOTVS teve um comportamento inesperado*  
*- connectors.native.internal-server-error*  
*- connectors.native.failed-to-deserialize*  
*- 400 BadRequest*  
*- 500 InternalServerError*  
*- Http failure response for*  
*- Relatório não existe ou não cadastrado corretamente na tabela de/para*  
*- O conteúdo retornado pelo ERP TOTVS não condiz com o padrão esperado*  
*- Não foi possível consultar as informações de configuração do DiscoveryEndpoint*  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Protheus Release 12.1.2310.  
  
**Solução**

Caso algum relatório do Smart View apresente erro em tela ou qualquer tipo de inconsistência durante a execução, é fundamental realizar a coleta dos logs do ambiente, a fim de possibilitar uma análise precisa e a identificação da causa do problema, considerando o uso de chaves importantes para corroborar com a analise.

**IMPORTANTE:** As validações dos relatorios smartview funcionam com linguagens avançadas, e com isso é extremamente importante, certificar das atualizações mais recentes em seu ambiente como um todo:

[- Acumulado BackOffice conforme sua versão](https://tdn.totvs.com/x/2hgdHw)  
- [LIB Atual](https://suporte.totvs.com/portal/p/10098/download#000006/368/TFLIB/) - [Logo Guará](https://suporte.totvs.com/portal/p/10098/download?e=989259) | [Harpia](https://suporte.totvs.com/portal/p/10098/download?e=1050526)  
- [Appserver](https://suporte.totvs.com/portal/p/10098/download#000006/368/TFAPP/)  
- [Smartclient](https://suporte.totvs.com/portal/p/10098/download#000006/368/TFSC/search/searchAll) - [Lobo Guará](https://suporte.totvs.com/portal/p/10098/download#detail/947510) | [Harpia](https://suporte.totvs.com/portal/p/10098/download#detail/1112221)  
- [DBAccess](https://suporte.totvs.com/portal/p/10098/download#000006/368/TFDBA/)  
- [Central de Atualizações](https://suporte.totvs.com/portal/p/10098/download?e=946864#000006/368/TFSC/)  
É importante atualizar seu produto constantemente, mantendo-o sempre na última versão disponível no Portal de Clientes ([Central de Download](https://suporte.totvs.com/portal/p/10098/download#000006/all/)), a fim de contemplar todas as melhorias e correções disponibilizadas.  
Efetuar o Backup antes da atualização.  
Todos os procedimentos devem ser realizados primeiro em ambiente TESTE atualizado.

Esta seção foi criada para ajudar você a encontrar informações importantes e soluções rápidas para eventuais problemas que possam surgir. Explore os tópicos do link abaixo para esclarecer suas dúvidas e facilitar sua experiência!  
[FAQ - Protheus/Smart View](https://tdn.totvs.com/x/WoyLN)

## **Casos com solução possivel**

*- O ERP TOTVS teve um comportamento inesperado*  
*- connectors.native.internal-server-error*

Caso voce tenha efetuado atualizações recentemente, e esses dois erros apresentem apenas em algum relatorio especifico de estoque custos, uma sugestão é a reinstalação das procedures de 14 ate 22, e após tentar novamente gerar o relatorio.

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Procedure Desatualizada ou Incompatível](https://centraldeatendimento.totvs.com/hc/pt-br/articles/15131065568791-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Procedure-Desatualizada-ou-Incompat%C3%ADvel)

## **Configuração de Chaves para Coleta de Logs**

Antes da reprodução do erro, recomendamos configurar as seguintes chaves no ambiente:

* **LogHttpFuncs=1**  
  Documentação: [TDN - LogHttpFuncs](https://tdn.totvs.com/x/MY5vI)
* **TraceStack=1**  
  Documentação: [TDN - TraceStack](https://tdn.totvs.com/x/jopc)
* **FWTRACELOG=1**  
  Documentação: [TDN - FWTRACELOG](https://tdn.totvs.com/x/Yc6qKg)

Essas chaves devem ser aplicadas no **AppServer.ini** do ambiente correspondente e estarão ativas durante a execução do serviço, **após o processo de coleta, desative as chaves**.

## **Coleta de Log pelo Smart View**

Adicionalmente, é possível obter informações relevantes diretamente do próprio serviço do SmartView, o que contribui para uma análise complementar dos **logs da aplicação e do serviço**.

**Acesse:**  
**FAQ – Protheus/Smart View**  
[TDN - FAQ Smart View](https://tdn.totvs.com/x/WoyLN)

> Consulte a sessão **“Dúvidas Frequentes”**, item **“Quais logs devo analisar/enviar caso tenha um erro/problema”**.
>
> ![Screenshot_1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32895804428311)

## **Procedimento para Captura de Logs**

Após configurar as chaves acima, siga os passos a seguir:

1. **Apague o arquivo** `console.log` da sessão atual do ambiente (presente na pasta `log` do AppServer ou onde voce definiu para gravar o arquivo log).
2. **Reinicie o serviço do AppServer em modo exclusivo**, se possível, para garantir integridade na coleta seja apenas nesse serviço, caso não puder fazer, certifique-se que a coleta esta sendo realizada no slave devido.
3. **Reproduza o erro novamente**, executando o relatório que apresenta a falha.
4. **Envie o novo** `console.log` **gerado**, juntamente com o **log do SmartView se possivel.**
5. **Anexe o Inspetor de Objetos** para uma verificação técnica mais detalhada da data dos fontes
6. **Capture uma imagem da rotina**:  
   **SIGACFG > Ambiente > Cadastros > Configuração TReports/Smart View**  
   Opção: **Token**, no módulo **Configurador**.
7. **Informe se o problema ocorre em todos os relatórios ou apenas em um específico.**
8. **Valide o seu agent esta atualizado:![Screenshot_2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32896108826263)**

A correta coleta e envio dessas informações é essencial para que a equipe do suporte possa avaliar com precisão o cenário reportado e dar continuidade à tratativa do incidente, seja no modulo de Estoque ou areas relacionadas.

## **Onde é que fica os meus LOGS para coleta e envio?**

Os logs ficam nas pastas internas do seu ambiente, voce deve solicitar ao seu TIME de TI, que pegue os logs caso voce não tenha acesso, envie esse boletim a eles que sera mais facil efetuarem o processo conforme instruções.

## **Mas o meu ambiente fica no T-CLOUD, como Pego os logs no T-CLOUD?**

Se o seu ambiente é em Cloud TOTVS, a limpeza do console acaba não sendo muito viavel de inicio, **pois voce precisa abrir uma solicitação para o CLOUD realizar essa ação caso você não tenha acesso**. Mas você pode efetuar a coleta dos logs no portal normalmente, ou via FTP, isso também é um processo que pode ser efetuado normalmente pelo seu time de T.I, ou caso voce tenha acesso ao portal.

Atenção: Basta se atentar, se esta realizando a coleta do ambiente correto, bem como o log correto, veja o horario gravado antes de coletar, por exemplo: se voce fez um teste em 28/07/2025 as 10:00am, mas voce visualizou que o log do serviço que voce fez o procedimento é de uma data e horario antes disso, então não é esse log que voce deve coletar, de alguns refresh F5 na pagina, para verificar se o log é atualizado, e caso não seja, devera acionar o time CLOUD.

[CLOUD - MP - Download de logs (TCLOUD)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4408646347671-CLOUD-MP-Download-de-logs-TCLOUD)

**Pontual erro:** Não foi possível consultar as informações de configuração do DiscoveryEndpoint

Validar se a comunicação dentro do appsever, não esteja apontando para instancia de um serviço integrado, por exemplo a tag Module=46.

```
[HTTPURI]             
URL=/rest             
PrepareIn=T1         
Instances=2,5,1,1     
CORSEnable=1          
AllowOrigin=*         
Module=46
```

**Observação:**Essa TAG deve ser informada somente se não tiver as licenças FULL e T em seu ambiente, ela ativa ira concorrer com o REST, gerando o erro na tentativa de conexão com o ERP

**Não foi possível consultar as informações de configuração do DiscoveryEndpoint**

![resterroaut.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33540964579863)

Também efetue o envio da **"Central de Diagnostico"**, gerada apartir da rotina que ocorre o problema, essa ferramente é extremamente importante para o suporte validar os fontes/PEs/Atualizações **etc**.

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como enviar dados pela Central de Diagnóstico?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/33711098138007-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-enviar-dados-pela-Central-de-Diagn%C3%B3stico)

## **Validações pontuais pela sua equipe de infra que possa interessar:**

Em algumas situações, o problema pode estar relacionado a compatibilidade de seu banco de dados, então a sugestão é avaliar a versão do banco, podera nos retornar os dados dessas consultas também, em casos de necessidade de redirecionamento ao time de Framework, exemplo em SQL:

```
SELECT @@VERSION AS 'SQL Server Version
```

![Screenshot_8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33533041451415)

Valide também a configuração de level de compatibilidade de seu banco de dados

```
SELECT compatibility_level
FROM sys.databases
WHERE [name] = 'NomeDaBase'
```

![Screenshot_1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33533041453463)  
**Obs.:** 'NomeDaBase' é o nome do banco utilizado na configuração do Smart View.

Saiba mais sobre a compatibilidade do seu banco em: [Nível de compatibilidade Microsoft](https://learn.microsoft.com/pt-br/sql/t-sql/statements/alter-database-transact-sql-compatibility-level?view=sql-server-ver17)

**Saiba mais**:

[*Clique aqui e veja mais artigos sobre Estoque Custos*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001533821-Estoque-e-Custos-SIGAEST)
