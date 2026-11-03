---
content_hash: 5c2fc920b1bad4dbd5fae6dba041162821eeefcdedb90e13fa6d4a0e22aa803f
fetched_at: '2026-06-29T00:06:28.657655+00:00'
page_id: '233756573'
product: rm
source: tdn-rm
title: BD0006_Isolamento_Processos_BR
type: documentation
url: https://tdn.totvs.com/display/LRM/BD0006_Isolamento_Processos_BR
version: 3
---

|  |  |
| --- | --- |
| **Produto:** | Performance |
| **Versões:** | 11.82.39 ou superior |
| **Ocorrência:** | Balanceamento de Conexões x Servidor de Aplicação |
| **Ambiente:** | RM |
| **Passo a passo:** | O Isolamento de processos possibilita que para cada JOB solicitado, seja aberta um thread no sistema operacional realizando o processamento de forma independente. Neste cenário a carga total que antes era aplicada no serviço RM.Host.Service.exe do servidor é dimensionada em vários processos, evitando sobrecarga e travamento em todos os Jobs caso apresente inconsistência em um processo específico durante sua execução.    **Obs.: A partir da versão 12.1.4 esse recurso é nativo do CorporeRM e dispensa a parametrização abaixo. Exceto quando as tags correspondentes foram imputadas manualmente com o valor *false*.**  Para utilizar o recurso, é necessário realizar a inclusão das tags “**ISOLATEPROCESS**” e “**ENABLEPROCESSISOLATION**” no bloco “</appSettings>”  do arquivo de configuração dos arquivos RM.Host.Service.exe.CONFIG no servidor.  Recomendamos que seja utilizado o aplicativo **RM.UpdateConfig.exe**disponível em**C:\totvs\CorporeRM\RM.Net,**pois quando é realizado a copia ou digitação diretamente nos arquivos pode ser que aconteça algum erro de digitação ou similar durante o processo, causando outros problemas ao bom funcionamento do produto.    Basta selecionar o arquivo desejado nos campos superiores, localizar a TAG que deseja ser altera e posteriormente clicar em **Salvar:**  **TAGS:**  <add key="ISOLATEPROCESS" value="true" /> <add key="ENABLEPROCESSISOLATION" value="true" />  **EXEMPLO:**    **Importante:**                  Caso o arquivo de configuração **RM.Host.JobRunner.exe.config** não exista no diretório **C:\TOTVS\CorporeRM\RM.Net**, crie uma cópia do arquivo de configuração do serviço **RM.Host.Service.exe.config**, posteriormente renomeie para **RM.Host.JobRunner.exe.config**.                  Para efetivar a ativação do isolamento, reinicie o serviço RM.Host.Service.exe do servidor. |
| **Observações:** | Para mais informações:  **COMUNIDADE** [R@Tecnologia](http://fluig.totvs.com/portal/p/10097/post/rtecnologia-community/1639774)   **Canais de Atendimento:**  **Abertura de Chamados** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)  **Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 8 – (Tecnologia), 2 – (Banco de Dados) |
