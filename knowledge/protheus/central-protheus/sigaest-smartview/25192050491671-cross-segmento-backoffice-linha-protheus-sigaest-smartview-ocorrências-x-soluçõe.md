---
article_id: 25192050491671
category: SIGAEST - SMARTVIEW
content_hash: dcf40a3e546b83334029e0b0af5dc60b04f9ea3538eb317841b339bc18e1a894
fetched_at: '2026-06-28T22:38:47.319538+00:00'
product: protheus
section_id: 16108365627287
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - SMARTVIEW - "Ocorrências"
  X "Soluções" no SmartView do Estoque
type: support-article
updated_at: '2024-10-21T21:08:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/25192050491671-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-SMARTVIEW-Ocorr%C3%AAncias-X-Solu%C3%A7%C3%B5es-no-SmartView-do-Estoque
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25192007173783) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Duvidas frequentes, com ocorrências e soluções mapeadas pelo suporte referente ao Smart View.   
 **Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Release 12.1.2310 ou superior.  
  
**Solução**

**PRINCIPAL:**

Já sabe como a rotina funciona? Suas parametrizações, e como devera ser utilizada? Avalie cada tópico, para entendimento dessas necessidades fundamentais.

* **[Configuração Inicial (Camada de Framework) - Contém vídeos de como configurar o SmartView](https://tdn.totvs.com/pages/releaseview.action?pageId=834823409)**
* **[Exemplos de consultas SmartView do módulo de Estoque/Custos](https://tdn.totvs.com/pages/releaseview.action?pageId=753648179)**

**Ocorrência 01:   
[WARN]Msg…:[O objeto de negócio poderá ser utilizado apenas com o controle de contagens de inventário habilitado (MV\_CONTINV).]**

**Solução**:

- É necessário aplicar atualizações, principalmente da LIB e dos Binários (AppServer e SmartClient) que são amplamente requisitados no conceito de visualização dos resultados do SmartView. Aplicar as seguintes atualizações (release 12.1.2310 ou superior):

- [Acumulado SIGAEST conforme sua versão](https://tdn.totvs.com/x/2hgdHw)  
- [LIB Harpia (importante atualizar)](https://suporte.totvs.com/portal/p/10098/download?e=1050526)  
 - [Appserver (importante atualizar)](https://suporte.totvs.com/portal/p/10098/download#000006/368/TFAPP/)   
- [Smartclient (importante atualizar)](https://suporte.totvs.com/portal/p/10098/download?e=946864#000006/368/TFSC/)

- [DBAccess](https://suporte.totvs.com/portal/p/10098/download#000006/368/TFDBA/)

- Em caso de persistência do problema, para análise de outras possíveis causas, é necessário encaminhar os arquivos [**console.log e console.bak**](https://tdn.totvs.com/display/tec/ConsoleLog) na pasta appserver. Limpar/excluir os arquivos após backup. Acessar a rotina e refazer o processo até gerar o erro, de modo que deve gerar informações no arquivo **console.log**. Envie o arquivo gerado, junto ao inspetor de objetos, para o canal de Suporte Protheus analisar.

**Ocorrência 02:**

**[ERROR]Msg...:[Erro no objeto de negócio 'totvs.estoque.inflowsandoutflows.integratedprovider.inflowsandoutflowstreportsbusinessobject' | : Error : 208 (S0002) (RC=-1) - [Microsoft][ODBC Driver 13 for SQL Server][SQL Server]Invalid object name 'SX10'**

**Solução**:

- Geralmente o incidente está relacionado à configuração do REST utilizado para o acesso do SmartView, o sistema está buscando pela filial/empresa para consulta das tabelas e, se houver erro na configuração da chave "Prepare In" do REST, esse incidente pode ser reproduzido; Em caso de dúvida sobre a configuração das chaves, acesse nossa documentação [Configuração do SmartView](https://tdn.totvs.com/x/8WTCMQ) ou entre em contato com o time de Suporte Framework da TOTVS.

- É essencial a atualização da Lib e dos Binários (AppServer + SmartClient). Recomendamos verificar se as versões mais atuais foram aplicadas ao ambiente que está realizando os testes (release 12.1.2310 ou superior):

- [Acumulado SIGAEST conforme sua versão](https://tdn.totvs.com/x/2hgdHw)  
- [LIB Harpia (importante atualizar)](https://suporte.totvs.com/portal/p/10098/download?e=1050526)  
 - [Appserver (importante atualizar)](https://suporte.totvs.com/portal/p/10098/download#000006/368/TFAPP/)   
- [Smartclient (importante atualizar)](https://suporte.totvs.com/portal/p/10098/download?e=946864#000006/368/TFSC/)

- [DBAccess](https://suporte.totvs.com/portal/p/10098/download#000006/368/TFDBA/)

- Em caso de persistência do problema, para análise de outras possíveis causas, é necessário localizar os arquivos [**console.log e console.bak**](https://tdn.totvs.com/display/tec/ConsoleLog) na pasta appserver. Limpar/excluir os arquivos após backup. Acessar a rotina e refazer o processo até gerar o erro, de modo que deve gerar informações no arquivo **console.log**. Envie o arquivo gerado, junto ao inspetor de objetos, para o canal de Suporte Protheus analisar.

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Consultas Smart View no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/16108365627287-SIGAEST-SMARTVIEW)*
