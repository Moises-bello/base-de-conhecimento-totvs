---
content_hash: 3cf5e853dc439e77811755c311d271d6791d98b1d375be0d77611d776d0cd4e2
fetched_at: '2026-06-29T00:05:58.507809+00:00'
page_id: '187534436'
product: rm
source: tdn-rm
title: Perfomance - Isolamento de processos
type: documentation
url: https://tdn.totvs.com/display/LRM/Perfomance+-+Isolamento+de+processos
version: 6
---

O Isolamento de processos possibilita que para cada JOB solicitado, seja aberta um thread no sistema operacional realizando o processamento de forma independente. Neste cenário a carga total que antes era aplicada no serviço RM.Host.Service.exe do servidor é dimensionada em vários processos, evitando sobrecarga e travamento em todos os Jobs caso apresente inconsistência em um processo específico durante sua execução.

                Para utilizar o recurso, é necessário realizar a inclusão das tags “**ISOLATEPROCESS**” e “**ENABLEPROCESSISOLATION**” no bloco “</appSettings>”  do arquivo de configuração dos arquivos RM.Host.Service.exe.CONFIG no servidor.

                Recomendamos que seja utilizado o aplicativo **RM.UpdateConfig.exe**disponível em**C:\totvs\CorporeRM\RM.Net,**pois quando é realizado a copia ou digitação diretamente nos arquivos pode ser que aconteça algum erro de digitação ou similar durante o processo, causando outros problemas ao bom funcionamento do produto.

Basta selecionar o arquivo desejado nos campos superiores, localizar a TAG que deseja ser altera e posteriormente clicar em **Salvar:**

**TAGS:**

<add key="ISOLATEPROCESS" value="true" />  
<add key="ENABLEPROCESSISOLATION" value="true" />

**EXEMPLO:**

**Importante:**

                Caso o arquivo de configuração **RM.Host.JobRunner.exe.config** não exista no diretório **C:\TOTVS\CorporeRM\RM.Net**, crie uma cópia do arquivo de configuração do serviço **RM.Host.Service.exe.config**, posteriormente renomeie para **RM.Host.JobRunner.exe.config**.

                Para efetivar a ativação do isolamento, reinicie o serviço RM.Host.Service.exe do servidor.
