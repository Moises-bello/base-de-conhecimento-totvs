---
article_id: 27106970697623
category: SIGAEST - SMARTVIEW
content_hash: fde906ed1fa7836273f95082dd13d082e34e0f45e33652a1e9b45fd08fcb9a70
fetched_at: '2026-06-28T22:38:47.231917+00:00'
product: protheus
section_id: 16108365627287
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Validacao de performance
  para geracao de relatorios Smartview
type: support-article
updated_at: '2025-03-12T12:23:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/27106970697623-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Validacao-de-performance-para-geracao-de-relatorios-Smartview
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27106997839511) Tempo aproximado para leitura: **00:03:00 min****Dúvida**Durante a geração de um relatorio SmartView, esta apresentando lentidão, ou queda de serviços durante a geração.

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - A partir da versão 12.1.2310  
  
**Solução**

Para garantir a melhor performance na geração de relatórios no Smartview, é fundamental verificar se o ambiente está utilizando as versões mais recentes disponíveis. As atualizações do Smartview frequentemente trazem melhorias de desempenho, correções de bugs e novas funcionalidades que otimizam o processamento e a exibição dos dados com as chamadas de requisições que passam pelo serviço REST. Caso o ambiente não esteja atualizado, recomendamos fortemente que seja realizada a atualização, assegurando assim o aproveitamento das melhorias e garantindo maior eficiência na geração dos relatórios.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27107489308695)

Também é importante, certificar das atualizações do modulo ao qual esta validando os relatorios, onde aqui no caso seria o ESTOQUE, bem como a validação das libs e artefatos.

[- Acumulado SIGAEST conforme sua versão](https://tdn.totvs.com/x/2hgdHw)

- [LIB Atual](https://suporte.totvs.com/portal/p/10098/download#000006/368/TFLIB/) - | [Harpia](https://suporte.totvs.com/portal/p/10098/download?e=1050526)

- [Appserver](https://suporte.totvs.com/portal/p/10098/download#000006/368/TFAPP/)

- [DBAccess](https://suporte.totvs.com/portal/p/10098/download#000006/368/TFDBA/)

- [Procedures](https://centraldeatendimento.totvs.com/hc/pt-br/articles/15131065568791-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Procedure-Desatualizada-e-Incompat%C3%ADvel-quais-as-diferen%C3%A7as-%C3%89-poss%C3%ADvel-utilizar-as-rotinas)

**Caso não esta atualizado, sugerimos que atualize.**

**Mas porque certificar de todas essas atualizações fora o SmartView?**

**Acumulado do modulo:** Quanto mais recente for o Acumulado, maior é a probabilidade de que melhorias e correções estejam aplicadas, trazendo benefícios como otimização de performance.

**LIB:** Ela inclui melhorias de performance, correção de bugs e adequações de segurança, além de possibilitar a integração com novos módulos e recursos.

**Appserver:** Ele centraliza a comunicação entre os usuários e o banco de dados, processando requisições e garantindo que as transações sejam executadas de forma eficiente e segura. Além disso, o AppServer possibilita a escalabilidade do ambiente, suportando o aumento de usuários e operações sem comprometer o desempenho. Manter o AppServer atualizado é crucial para melhorar a performance.

**Dbaccess:** É essencial para garantir a compatibilidade do sistema Protheus com as versões mais recentes de banco de dados e obter melhorias de performance e segurança no acesso aos dados. As atualizações do Dbaccess incluem correções de bugs, otimizações de conexão e ajustes que evitam possíveis falhas de comunicação entre o sistema e o banco de dados. Isso garante um ambiente mais estável e eficiente, reduzindo riscos de indisponibilidade e problemas de integridade nas transações realizadas.

**Procedures**: Manter as procedures atualizadas é crucial, pois as versões mais recentes costumam incluir otimizações nas querys com a utilização dos relatorios Smart e até mesmo os antigos MATR, resultando em maior performance e precisão na geração dos dados.

**Meu ambiente esta atualizado, mas a geração do relatorio é lenta:**

Apesar do ambiente estar atualizado, a geração do relatório vier apresentar lentidão. Para que possamos mitigar o ocorrido, solicitamos que siga os procedimentos abaixo para coleta de informações necessárias:

**1. Limpeza do arquivo console.log**: Limpe o arquivo `console.log` da sessão do **AppServer** onde o serviço **REST** está sendo executado.

**2. Ativação do LogProfiler:** Configure a chave `[**LogProfiler**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019902592-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-habilitar-e-gerar-o-LogProfiler)` no mesmo **AppServer** que está executando o serviço **REST**.

**3. Acesso ao Relatório desejado:** E configure os parâmetros desejados, mas não gere a consulta ainda.

**4. Ativação do Rastreamento via DBMonitor:** Antes de gerar a consulta, ative o rastreio no **DBMonitor** para coleta e geração do arquivo `**[DBTRACE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019902592-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-habilitar-e-gerar-o-LogProfiler)**`.

**5. Geração do Relatório:** Após configurar o **rastreio**, gere o relatório normalmente até ser finalizado.

Com isso, basta anexar em uma solicitação aberta ao suporte os seguintes dados para validação.

- Arquivo gerado pelo `LogProfiler`  
- Arquivo `DBTRACE`  
- Inspetor de Objetos

Essas informações são essenciais para nossa análise detalhada para avaliação de performance.

**Saiba mais:**

[*Como configurar o SmartView*](https://tdn.totvs.com/x/8WTCMQ)

*[Clique aqui e veja mais artigos sobre Relatórios SmartView do Estoque Custos](https://tdn.totvs.com/x/pwKQLg)*
