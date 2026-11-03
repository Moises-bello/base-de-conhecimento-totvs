---
content_hash: 250840cadb163be2151caa72db532bf687cf70e5d7da21a563f6e92b63034022
fetched_at: '2026-06-29T00:10:39.218198+00:00'
page_id: '546248415'
product: rm
source: tdn-rm
title: TOTVS Construção Gestão de Imóveis - Aluguel - Agendamento de Reajuste
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=546248415
version: 2
---

**Agendamento de Reajuste**  
Neste Processo iremos agendar os reajustes monetários para serem executados automaticamente de acordo com as configurações estipuladas.  
   
**Tipo Data Reajuste:** Informe se o reajuste será no mês corrente, próximo mês ou irá estipular uma data.  
**Geração de Boleto:** Informe se o reajuste será somente no Fluxus para gerar o Boleto ou não. Obs: serão reajustadas apenas as parcelas com vencimento na data do reajuste.  
   
**Atenção:**  
Para utilizar o agendamento de reajuste, é necessário configurar o ambiente para 3 camadas com no mínimo 30 Threads.  
O Serviço "RM.Host.Service.exe" deverá estar executando no servidor de aplicação para que o processo seja disparado automaticamente.  
   
   
Configuração do Arquivo "Alias.dat" no Servidor de Aplicação  
   
Habilitar o processamento de Job e configurar com no mínimo 30 Threads no arquivo Alias.dat  
Arquivo "Alias.dat":  
<?xml version="1.0" standalone="yes"?> <RMSAliasData xmlns="[{+}](http://tempuri.org/RMSAliasData.xsd)<http://tempuri.org/RMSAliasData.xsd+>">   <DbConfig>     <Alias>localhost</Alias>     <DbType>SqlServer</DbType>     <DbProvider>SqlClient</DbProvider>     <DbServer>rm0005422</DbServer>     <DbName>MASB1100</DbName>     <UserName>sysdba</UserName>     <Password>masterkey</Password>     <RunService>false</RunService>     <JobServerEnabled>true</JobServerEnabled>     <JobServerMaxThreads>30</JobServerMaxThreads>     <JobServerLocalOnly>true</JobServerLocalOnly>     <JobServerPollingInterval>10</JobServerPollingInterval>     <ChartAlertEnabled>false</ChartAlertEnabled>     <ChartAlertPollingInterval>20</ChartAlertPollingInterval>     <ChartHistoryEnabled>false</ChartHistoryEnabled>     <ChartHistoryPollingInterval>20</ChartHistoryPollingInterval>     <RSSReaderMailEnabled>false</RSSReaderMailEnabled>     <RSSReaderMailPollingInterval>20</RSSReaderMailPollingInterval>   </DbConfig> </RMSAliasData>  
Configuração do arquivo "RM.Host.Service.exe.config" no Servidor de Aplicação: <?xml version="1.0" encoding="utf-8" ?> <configuration>   <appSettings>     <add key="SelfHosted" value="false" />     <add key="ActionsPath" value="c:\[rm.net](http://rm.net)\bin;c:\[corpore.net](http://corpore.net)\bin" />     <add key="JobServer3Camadas" value="true"/>   </appSettings> </configuration>  
   
Configuração do arquivo "RMSGI.exe.config" na máquina Cliente: Habilitar no arquivo "RMSGI.exe.config" a arquitetura 3 camadas:  
<?xml version="1.0"?> <configuration> <appSettings>   <add key="Port" value="8050"/>   <add key="UseExternalHost" value="true"/>   <add key="SelfHosted" value="false"/>   <add key="JobServer3Camadas" value="true"/> </appSettings> </configuration>  
 

* Deverá ser realizado o ajuste para permitir a inclusão e alteração de escalonamentos com valor igual a 0 (zero).
* Deverão ser removidas todas as validações que verificam e obrigam o preenchimento deste campo com valor maior que 0 (zero).
* A geração de lançamentos financeiros irá considerar o escalonamento com valor 0 e seu comportamento será:
  + Será criado, no Evento Financeiro de locação, as parcelas correspondentes aos meses do escalonamento com valor 0.
  + As parcelas com valor liquido 0 não serão integradas ao sistema financeiro.
  + As parcelas com valor original igual a 0 (zero), mas que possuam eventos agregados e tenham valor liquido maior que 0, serão criadas normalmente.
    - Deverá ser configurado no Fluxus para que seja permitido criar lançamentos com valor original igual a 0 (zero).
  + Será mantida a validação na geração de lançamentos para que não seja possível criar lançamentos com valor liquido menor ou igual a 0 (zero), considerando para isto o valor original (igual a zero) e os valores de integração a somar e subtrair.
    - Para os casos em que o valor liquido seja menor ou igual a 0, será exibida a mensagem orientando os ajustes manuais dos eventos agregados, alterando o vencimento ou redistribuindo o valor de forma a não tentar criar um lançamento com valor liquido menor ou igual a 0 (zero).
    - Caso seja necessário realizar alguma cobrança ou pagamento no período que gere lançamento com valor liquido menor ou igual a 0, estes deverão ser realizados a partir de Eventos avulsos.
* O Valor do escalonamento zerado deverá ser considerado normalmente na contabilização do aluguel, respeitando as regras contábeis onde não é gerado lançamento zerado.
  + Os cálculos de valores lineares serão realizados e o escalonamento zerado impactará diminuindo o valor da média linearizada.
* Esta implementação não irá causar impactos no processamento da DIMOB de Aluguel, pois considera os lançamentos financeiros e suas baixas.
* Será criado um cadastro de "Tipo de escalonamento", onde o usuário poderá informar uma descrição e esta poderá ser associada ao escalonamento em seu cadastro / edição.
