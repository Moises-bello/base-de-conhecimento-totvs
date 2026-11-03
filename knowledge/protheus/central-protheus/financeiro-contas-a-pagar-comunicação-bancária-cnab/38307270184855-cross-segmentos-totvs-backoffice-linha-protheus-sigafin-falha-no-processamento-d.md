---
article_id: 38307270184855
category: Financeiro - Contas a Pagar - Comunicação Bancária CNAB
content_hash: cdbb170dc59f99792e4773e44e363757b34c4bda4b66291d79fa1d95c8e4c29d
fetched_at: '2026-06-28T22:37:56.530977+00:00'
product: protheus
section_id: 1500001550622
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFIN - Falha no processamento
  de Retorno CNAB via Schedule com arquivo em diretório local (C:) raiíz
type: support-article
updated_at: '2026-02-10T19:29:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38307270184855-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFIN-Falha-no-processamento-de-Retorno-CNAB-via-Schedule-com-arquivo-em-diret%C3%B3rio-local-C-rai%C3%ADz
---

**[Remover as instruções entre colchetes e altere o tempo aproximado para leitura]**  
  
![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38307245773463) Tempo aproximado para leitura: **HH:MM:SS min**  
  
**Dúvida**  
Ao efetuar um retorno CNAB via Schedule (utilizando rotinas como FINA205, FINA435, ou Automáticas), os títulos não são baixados mesmo com os parâmetros de diretório (EE\_DIRPAG / EE\_DIRREC e EE\_BKPPAG / EE\_BKPREC) apontando para o caminho do arquivo (exemplo: C:\CNAB\).

Por que o processamento não ocorre?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFIN - Todas as versões

**Solução**  
O incidente ocorre porque o processamento via Schedule (Job) é executado diretamente pelo serviço do servidor (AppServer), e não pelo cliente local (SmartClient).

Quando uma rotina é agendada via Schedule, o serviço do Protheus busca os arquivos baseando-se na estrutura de diretórios do servidor onde o serviço está rodando (RootPath), e não no disco local (C:\) da estação de trabalho do usuário que criou o agendamento

Para corrigir o processamento, siga as diretrizes abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38307270160279)

Localização do Arquivo: O arquivo de retorno CNAB deve ser salvo obrigatoriamente dentro da estrutura de pastas do servidor (dentro do RootPath configurado no appserver.ini ou diretório mapeado acessível pelo serviço do Protheus).

**Configuração do Caminho:**

Nos parâmetros do CNAB (Tabela SEE - Campos EE\_DIRPAG / EE\_DIRREC) ou na configuração da rotina, informe o caminho relativo ou absoluto considerando a visão do Servidor, e não a unidade de disco local.

**Incorreto para Schedule: C:\cnab\retorno\**

**Correto para Schedule: \cnab\retorno\ (Considerando que a pasta cnab está na raiz do Protheus Data).**

**Importante:**

A utilização de caminhos locais (como C:\) funciona apenas quando a rotina é executada manualmente via menu (interface), pois neste cenário o sistema utiliza o acesso do Client.

**Exceções:**

A única exceção a esta regra aplica-se caso exista uma documentação oficial no TDN (Totvs Developer Network) afirmando explicitamente que uma rotina específica (X) possui tratamento diferenciado para buscar arquivos locais c:\ mesmo quando executada via Schedule.

Caso não haja essa documentação explícita para a rotina em questão, deve-se seguir o padrão de alocar o arquivo no servidor.

**Saiba Mais**  
Para mais detalhes sobre a configuração de jobs e diretórios no Protheus, consulte:

[TDN - CNAB (Modelo 2)](https://tdn.totvs.com/display/public/PROT/CNAB)

[TDN - Schedule Protheus](https://tdn.totvs.com/pages/releaseview.action?pageId=471926159)

[KCS - Ao rodar o retorno do CNAB via Job Schedule não executa as baixas dos títulos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/9531944838295-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA205-FINA435-Ao-rodar-o-retorno-do-CNAB-via-Job-Schedule-n%C3%A3o-executa-as-baixas-dos-t%C3%ADtulos)
