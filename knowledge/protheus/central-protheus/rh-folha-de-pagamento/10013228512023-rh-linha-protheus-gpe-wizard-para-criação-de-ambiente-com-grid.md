---
article_id: 10013228512023
category: RH - Folha de Pagamento
content_hash: 807477c6ebbc2df16a1e7295b54c4f87a69ebd07178e25df18c17757776c3b91
fetched_at: '2026-06-28T22:44:16.443595+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Wizard para criação de ambiente com GRID
type: support-article
updated_at: '2024-09-12T11:24:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10013228512023-RH-Linha-Protheus-GPE-Wizard-para-cria%C3%A7%C3%A3o-de-ambiente-com-GRID
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26319539923351) Tempo aproximado para leitura: **00:02:00 min****Ocorrência***Wizard* para criação de ambiente com GRID.  
**Ambiente**TOTVS RH - TOTVS RH ( Linha Protheus ) GPE Gestão de Pessoal - A partir da versão 12.1.27.  
  
**Causa**Devido a complexidade para criação de ambientes com processamento em GRID, solicita-se um *wizard* facilitador para criação de um ambiente padrão.  
  
**Solução**Desenvolvida a rotina **GPEGRIDWZ**, que deverá ser executada diretamente pelo smartclient e que permitirá a criação de um ambiente com GRID baseado no ambiente onde foi executado.  
A rotina possibilitará a definição do IP e porta do *coordinator* e dos *agents*, bem como a quantidade de *agents* e limite de conexão de cada *agent*.  
  
A rotina deve ser iniciada a partir do smartclient, exemplo:  
![](https://tdn.totvs.com/download/attachments/707369936/image2022-9-1_14-12-12.png?version=1&modificationDate=1662054775883&api=v2)

**Importante**O appserver do ambiente utilizado será duplicado e utilizado como base para a configuração do novo ambiente.  
  
Ao iniciar a rotina, um breve resumo será exibido:  
![](https://tdn.totvs.com/download/attachments/707369936/image2022-9-1_14-14-19.png?version=1&modificationDate=1662054775723&api=v2)  
  
Após avançar, deverá ser definida as parametrizações do *coordinator*. O nome do ambiente não poderá ser alterado, pois é o mesmo do ambiente utilizado na execução da rotina. As demais informações poderão ser alteradas. O IP e porta exibidos são os mesmos do ambiente que esta sendo executado, caso exista a necessidade de executar o novo ambiente em paralelo com o atual, na mesma máquina, a porta deverá ser alterada.  
Nesta tela também deverá ser definido a quantidade de *gridagents* que serão criados, bem como o limite de conexões por *agent*. Essas informações devem ser analisadas de acordo com a infraestrutura disponível, o documento [*GridServer* - Como configurar](https://tdn.totvs.com/display/public/framework/GridServer+-+Como+configurar) trás algumas orientações a respeito.  
  
![](https://tdn.totvs.com/download/attachments/707369936/image2022-9-1_14-17-41.png?version=1&modificationDate=1662054775563&api=v2)  
  
Na próxima tela será solicitado o IP e porta de cada *GridAgent* que será criado, de acordo com a quantidade definida na tela anterior. O IP inicial é o mesmo do c*oordinator*, mas recomenda-se que os *agents* estejam em máquina separadas. A porta inicial e a próxima, após a porta do *coordinator*. Deve ser verificado se todas estão disponíveis para que a conexão do *agent* não seja bloqueada na hora de subir o ambiente.  
  
![](https://tdn.totvs.com/download/attachments/707369936/image2022-9-1_14-26-59.png?version=1&modificationDate=1662054775417&api=v2)  
  
Ao avançar o processo de criação das informações para o novo ambiente será iniciado:  
  
![](https://tdn.totvs.com/download/attachments/707369936/image2022-9-1_14-28-30.png?version=1&modificationDate=1662054775100&api=v2)  
  
Nessa etapa poderá ser feito dois processos diferentes, que dependem explicitamente da necessidade do usuário.  
  
**Primeira opção:** Criação apenas do appserver.ini do *Coordinator* e dos *GridAgents*, ficando a cargo do usuário a duplicação das pastas do servidor e copia dos INI's para dentro de cada uma após a geração.  
Para esta opção nenhum processo deve ser feito antes da geração do ambiente, ao término do processo será exibido o local onde os arquivos foram gerados, junto aos arquivos um TXT é criado com orientação sobre os próximos passos:  
  
![](https://tdn.totvs.com/download/attachments/707369936/image2022-9-1_14-34-30.png?version=1&modificationDate=1662054774957&api=v2)  
  
Os arquivos foram criados dentro da pasta informada:  
  
![](https://tdn.totvs.com/download/attachments/707369936/image2022-9-1_14-35-39.png?version=1&modificationDate=1662054774813&api=v2)  
  
Trecho do TXT com orientação sobre os próximos passos:  
  
![](https://tdn.totvs.com/download/attachments/707369936/image2022-9-1_14-36-22.png?version=1&modificationDate=1662054774677&api=v2) **Segunda opção:** A outra opção é a de gerar a pasta do appserver inteira, com os INI's dentro, uma para o *coordinator* e uma para cada *GridAgent*. Para que o processo seja executado desta forma, é necessário antes criar a pasta *GridServer*, dentro da pasta appserver do ambiente que será executado. Dentro da pasta GridServer deverá ser colocado uma cópia da pasta appserver, para que a rotina possa duplicar os arquivos para o *coordinator* e para os *gridagents*, a pasta deverá ficar dessa forma:  
  
![](https://tdn.totvs.com/download/attachments/707369936/image2022-9-1_14-39-29.png?version=1&modificationDate=1662054774537&api=v2)  
  
Estando o ambiente montado dessa forma, ao processar a rotina, a pasta será duplicada de acordo com as configurações. O processo desta forma será mais moroso que o anterior, uma vez que será necessário efetuar a cópia dos arquivos. Quanto maior a quantidade de GridAgents, maior será o tempo para criar os arquivos, ao final do processamento a pasta deverá estar da seguinte forma:  
  
![](https://tdn.totvs.com/download/attachments/707369936/image2022-9-1_14-43-0.png?version=1&modificationDate=1662054774393&api=v2)  
  
Neste modelo bastará mover as pastas para suas devidas máquinas e iniciar os serviços, conforme orientação no TXT:  
  
![](https://tdn.totvs.com/download/attachments/707369936/image2022-9-1_14-44-13.png?version=1&modificationDate=1662054774237&api=v2)  
  
**Importante**Os IP's e portas do *coordinator* e GridAgents são exibidos no TXT de ambas as opções para facilitar a cópia dos arquivos para a máquina correta. Uma vez que cada GridAgent pode ter um IP diferente, se ele for copiado para a máquina errada, não conseguiram se comunicar com o *coordinator*.

**Saiba mais**  
[DT Wizard para criação de ambiente com GRID](https://tdn.totvs.com/pages/viewpage.action?pageId=707369936)  
[Cálculo com multiprocessamento](https://tdn.totvs.com/pages/releaseview.action?pageId=624622730)

[RH - Protheus - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)

[RH - Linha Protheus - GPE - Como fazer o download (baixar) do pacote de expedição contínua (acumulado) do RH Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)

[ChatBot Carol Assistant](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022200991)
