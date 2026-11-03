---
article_id: 360004571372
category: eSocial - Gerar XML/ Integração Evento
content_hash: ffb6090475c6b5711a7c10b166e3936f19590f8753b38571cd00b0d1496de693
fetched_at: '2026-06-28T22:47:11.858556+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: 'RH - RM - FOP - eSocial  - Erro 803 na integração com TAF: O valor do campo
  sourceBranch (TAFFIL) não está cadastrado no complemento de empresas'
type: support-article
updated_at: '2025-01-20T17:55:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004571372-RH-RM-FOP-eSocial-Erro-803-na-integra%C3%A7%C3%A3o-com-TAF-O-valor-do-campo-sourceBranch-TAFFIL-n%C3%A3o-est%C3%A1-cadastrado-no-complemento-de-empresas
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24970903135639) Tempo aproximado para leitura: 00:02:00 min****Ocorrência**Ao realizar a integração dos eventos do TOTVS Folha de Pagamento com o TAF é apresentado a mensagem de erro **Código erro TAF: 803.****Descrição erro TAF: o valor do campo sourceBranch (TAFFIL) não está cadastrado no complemento de empresas**.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360042987514)

**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - eSocial - Todas as versões  
  
**Causa**Este erro geralmente é causado quando o código da filial informado em **Configurações | Parametrizador | eSocial | Integração com o TAF** no TOTVS Folha de Pagamento está diferente do campo **Cod Filial** do complemento cadastral no TAF, ou quando a configuração do serviço de integração não foi realizada para as empresas do TAF cujos dados estão sendo enviados.  
  
**Solução**Para correção da ocorrência favor executar as duas validações abaixo:  
• Configuração da **Integração no RM**  
1. No TAF acesse **Atualização | Empresa | Complemento Cadastral**, edite o registro e verifique o valor informado no campo **Cod Filial;**2.  No TOTVS Folha de Pagamento acesse **Configurações | Parametrizador | eSocial | Integração com TAF** e informe no campo **Código da Filial TAF** o mesmo valor do campo **Cod Filial** validado acima. O valor precisa ser idêntico, incluindo espaços existentes.

• Configuração do **serviço de integração**  
1. No servidor onde o TAF encontra-se instalado acesse o diretório **[...]TAF\bin\app** e edite o arquivo **appserver.ini**. Para facilitar a edição, o arquivo deverá ser aberto no bloco de notas;  
2. Localize a seção **[TAF\_CFGJOB]** presente no final do arquivo conforme abaixo;

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360042988354)

3. A chave **PrepareIn** deve conter o código do **Grupo de Empresas do TAF.** Abaixo exemplos de possíveis configurações para a chave;  
      - Utilizando o código do grupo de empresas: **PrepareIn**=01  
      - Utilizando diversos códigos de grupos de empresas: **PrepareIn**=01,02,99  
      - Utilizando a palavra **ALL** para que o server considere todos os grupos de empresas (opção recomendada): **PrepareIn=***ALL*  
**Importante**  
Caso seja ajustado algum atributo no arquivo appserver.ini será necessário reiniciar o serviço TAF-WS.  
Caso persista o erro de integração mesmo após estes ajustes, gentileza realizar a abertura de um Ticket para a equipe do atendimento técnico do TOTVS Folha de Pagamento incluindo as evidências do erro e das configurações.
