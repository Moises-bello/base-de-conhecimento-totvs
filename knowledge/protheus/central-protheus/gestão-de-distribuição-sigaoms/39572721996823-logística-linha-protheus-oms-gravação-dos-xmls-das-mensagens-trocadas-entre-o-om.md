---
article_id: 39572721996823
category: Gestão de Distribuição (SIGAOMS)
content_hash: 5939a99cd075bd0687d8fd18e6af302a34bd2c3399d98db9ec8309e506ff485d
fetched_at: '2026-06-28T22:45:49.849623+00:00'
product: protheus
section_id: 206957088
source: central-protheus
title: Logística - Linha Protheus - OMS - Gravação dos XMLs das mensagens trocadas
  entre o OMS com o TOL e o TRE
type: support-article
updated_at: '2026-04-08T18:41:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39572721996823-Log%C3%ADstica-Linha-Protheus-OMS-Grava%C3%A7%C3%A3o-dos-XMLs-das-mensagens-trocadas-entre-o-OMS-com-o-TOL-e-o-TRE
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39572721975319) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
Como funciona a gravação dos arquivos **XMLs** das mensagens trocadas entre o **OMS** com o **TOL** e o **TRE**?  
  
**Ambiente**  
TOTVS Logística - TOTVS OMS (Linha Protheus) - Gestão de Distribuição (SIGAOMS) - Todas as versões  
  
**Solução**  
Para garantir o armazenamento dos arquivos **XML** gerados na integração, é necessário realizar uma configuração pontual no arquivo **appserver.ini** do ambiente.  
  
**Configuração necessária:**  
A gravação dos **XMLs** depende da inclusão do bloco de chaves abaixo:  
  
**[NEOLOG]**  
**Debug=1**  
**DebugPath=Neolog**  
  
Essa configuração habilita o modo de **debug** da integração, permitindo que todas as mensagens trocadas sejam registradas em formato **XML**. Caso esteja com o **valor 1**, será considerado **ativo**, do contrário, será considerado **inativo**.  
  
**Local de gravação dos arquivos:**  
Quando a chave estiver devidamente configurada, os arquivos **XML** serão gerados dentro do diretório **Protheus\_Data**, utilizando a subpasta definida em **DebugPath**.  
  
Caso essa configuração não esteja presente no arquivo **appserver.ini**, o Sistema adotará automaticamente o diretório padrão: **system/neolog**  
  
**Estrutura de diretórios:**  
Tanto o diretório **Protheus\_Data** quanto o caminho **system/neolog** fazem parte da estrutura padrão de instalação do ambiente **Protheus**, não sendo necessária a criação manual dessas pastas.  
  
**Considerações finais:**  
A correta parametrização do bloco **[NEOLOG]** é essencial para viabilizar o rastreamento e a análise das mensagens de integração, facilitando diagnósticos e validações no processo entre os sistemas.  
  
**Importante**  
Para evitar o acúmulo excessivo de arquivos de log gerados pela integração, é recomendável implementar uma rotina de limpeza periódica no servidor.  
  
**Saiba mais**  
Para mais informações acesse boletim técnico e artigo:  
[Integração TOTVS OMS x TOTVS Otimização Logística](https://tdn.totvs.com/pages/releaseview.action?pageId=268801735)  
[Logística - Linha Protheus - OMS - Integração Protheus TOTVS OMS x TOL/TRE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360061123194-Log%C3%ADstica-Linha-Protheus-OMS-Integra%C3%A7%C3%A3o-Protheus-TOTVS-OMS-x-TOL-TRE)  
[Logística - Linha Protheus - OMS - Como habilitar o LOG de integração do TOTVS OMS e TOL/TRE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060684834)  
  
**Glossário**  
**OMS** - Order Management System  
**TOL** - TOTVS Otimização e Logistica  
**TRE** - TOTVS Roteirização e Entregas
