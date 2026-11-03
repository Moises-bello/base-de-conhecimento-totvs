---
content_hash: 50fe976aafd33e9c6aaf031c81522c315aa35ea5bd10abfe46b96b860ec1a34b
fetched_at: '2026-06-29T00:08:05.891826+00:00'
page_id: '236421277'
product: rm
source: tdn-rm
title: BD0010_Inclusão_tags_Melhores_Práticas_BR
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=236421277
version: 3
---

|  |  |
| --- | --- |
| **Produto:** | Tag para otimização |
| **Versões:** | Todas |
| **Ocorrência:** | Inclusão de configurações nos arquivos .config |
| **Ambiente:** | RM (LOCAL ou 3 CAMADAS) |
| **Passo a passo:** | Atualmente existem configurações que resultam no ganho de performance que se refere a inclusão das tags abaixo em todos os arquivos de configuração de acordo com as condições abaixo:  Recomendamos que seja utilizado o aplicativo **RM.UpdateConfig.exe**disponível em**C:\totvs\CorporeRM\RM.Net,**pois quando é realizado a copia ou digitação diretamente nos arquivos pode ser que aconteça algum erro de digitação ou similar durante o processo, causando outros problemas ao bom funcionamento do produto.    Basta selecionar o arquivo desejado nos campos superiores, localizar a TAG que deseja ser altera e posteriormente clicar em **Salvar:**    **Após salvar, abrir o arquivo diretamente no diretório e verificar se a tag foi incluída corretamente.**   ---   Quando obtemos clientes utilizando banco de dados **Oracle**, obtemos as TAGS **UseDbSchemaCache** e **DBShemaCacheMaxSize** que altera o modo em que os dados salvos, criando um arquivo de cache salvando as principais informações no mesmo, deste modo as buscas dos resultados irão realizar a leitura primeira do cache em paralelo ao banco.           *ATENÇÃO: Valores muitos elevados podem ocasionar perda de desempenho e (ou) erros como '**Server did not respond within the specified timeout interval**'.* É aconselhável informar o **DBShemaCacheMaxSize** com no máximo 3000, o ideal é informar um valor menor e considerar o aumento conforme necessidade.  Este é um número baseado em nosso feeling de atendimento, este número é a quantidade de consultas (apenas o schema) que a aplicação irá armazenar no cache do host. Ou seja, a forma de você acompanhar o número é verificar quantas consultas diferentes são realizadas no banco de dados a cada reinicialização do **RM.Host.Services.exe**, pois quando reinicializado o cache é limpo.   * **UseDbSchemaCache** (TAG inclusa nos configs cliente e servidores) - Indica se o sistema guardará em cache os esquemas obtidos pelas consultas. * **DbSchemaCacheMaxSize** (TAG inclusa nos configs servidores - **RM.Host.Service.exe.config, RM.Host.JobRunner.exe.config e RM.Host.exe.config**) - Define a quantidade de schemas que serão guardados em cache.   Exemplo: |
| **Observações:** | Para mais informações:  **COMUNIDADE** [R@Tecnologia](http://fluig.totvs.com/portal/p/10097/post/rtecnologia-community/1639774)   **Canais de Atendimento:**  **Abertura de Chamados** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)  **Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 8 – (Tecnologia), 2 – (Banco de Dados) |
