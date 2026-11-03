---
article_id: 17330593767703
category: Gestão de Distribuição (SIGAOMS)
content_hash: 4ec9b5ab38c2e03d32d7d295a4a23730af019f2897da810f4e478c15012fd7f0
fetched_at: '2026-06-28T22:45:49.705475+00:00'
product: protheus
section_id: 206957088
source: central-protheus
title: Logística - Linha Protheus - OMS - Como informar o Tipo de Operação e a Classificação
  de Frete no OMSA200 - Montagem de Carga
type: support-article
updated_at: '2025-10-17T19:42:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/17330593767703-Log%C3%ADstica-Linha-Protheus-OMS-Como-informar-o-Tipo-de-Opera%C3%A7%C3%A3o-e-a-Classifica%C3%A7%C3%A3o-de-Frete-no-OMSA200-Montagem-de-Carga
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17330651252887) Tempo aproximado para leitura: **00:02:24 min** **Dúvida**Como informar o Tipo de Operação e Classificação de Frete no **OMSA200 -** **Montagem de Carga**?**Ambiente**TOTVS Logística - TOTVS OMS (Linha Protheus) - Gestão de Distribuição (SIGAOMS) - Todas as versões.  
  
**Solução**No módulo **SIGAOMS**, quando a integração com o **SIGAGFE** está ativada, ou seja, com o parâmetro **MV\_INTGFE** configurado como **.T.**, ao incluir uma carga no **OMSA200**, o botão **Outras Ações** apresentará a opção **Tipo Oper/Class. Frete.**  
As informações de **Tipo Operação** e **Classificação de Frete** podem ser inseridas das seguintes formas:

1. Manualmente, utilizando o botão **Outras Ações > Tipo Oper/Class. Frete**. As informações serão buscadas das tabelas: **GV4 - Tipos de Operação  
   GUB - Classificações de Frete**
2. Se não informar o Tipo Operação e a Classificação de Fretes na **Montagem de Carga**, ao integrar a carga com o **SIGAGFE**, serão consideradas as informações dos parâmetros abaixo:  
   No programa **Parâmetros do Módulo - GFEX000**, configurar os parâmetros **MV\_CDTPOP - Tipo de Operação Padrão**, localizado na aba Integração Protheus e o **MV\_CDCLFR - Classificação de Frete Padrão**, localizado na aba Integração ERP.
3. No **SIGACFG**, por padrão temos o inicializador dos campos abaixo para realizar o preenchimento automático dos campos na **Montagem da Carga**. Os inicializadores deverão estar preenchidos da seguinte forma:  
   **DAK\_CDTPOP** preenchido como: **SuperGetMv("MV\_CDTPOP",.F.,"")**  
   **DAK\_CDCLFR** preenchido como: **SuperGetMv("MV\_CDCLFR",.F.,"")**

**Importante**O envio das informações **Tipo Operação** e **Classificação de Fretes** na integração com **SIGAFE** não são obrigatórias.  
Se desejado alterar o comportamento do Sistema padrão, descrito acima, pode-se utilizar os Pontos de Entradas abaixo:

* **OS200DAK**: após a Montagem da Carga
* **OM200GEC**: antes de executar a Montagem da Carga

As documentações dos Pontos de Entrada citados acima, estão disponíveis na sessão **Saiba Mais**, logo abaixo.  
 **Saiba mais**Mais informações sobre a Integração **Protheus** x **GFE**, verifique no *link* [Integração Protheus x GFE](https://tdn.totvs.com/pages/viewpage.action?pageId=235310789)  
Documentações referente aos **Pontos de Entrada na Montagem de Carga**, verifique o *link* [Logística - Linha Protheus - OMS - Pontos de Entrada disponíveis na rotina Montagem de Carga - OMSA200](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500000900021-Log%C3%ADstica-Linha-Protheus-OMS-Pontos-de-Entrada-dispon%C3%ADveis-na-rotina-Montagem-de-Carga-OMSA200?source=search)  
  
**Glossário****SIGAGFE** - Gestão de Frete Embarcador **SIGAOMS** - Gestão de  Distribuição**SIGACFG** - Configurador ERP Protheus
