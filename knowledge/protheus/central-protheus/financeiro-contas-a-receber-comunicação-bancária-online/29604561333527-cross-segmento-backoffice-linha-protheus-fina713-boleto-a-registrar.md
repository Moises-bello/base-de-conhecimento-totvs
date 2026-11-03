---
article_id: 29604561333527
category: Financeiro - Contas a Receber - Comunicação Bancária Online
content_hash: 0db4eb4999edbfa8a55f0b7a30dc8f111a1934f6d704f6a008921998d0773e77
fetched_at: '2026-06-28T22:37:49.143816+00:00'
product: protheus
section_id: 26656227629847
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - FINA713 - Boleto a registrar
type: support-article
updated_at: '2026-01-09T20:43:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/29604561333527-Cross-Segmento-Backoffice-Linha-Protheus-FINA713-Boleto-a-registrar
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29604561297431) Tempo aproximado para leitura: **00:10 min**  
  
**Dúvida**  
O que validar quando o boleto fica a registrar?   
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - A partir da release 12.1.33  
  
**Solução**  
O envio das informações ao banco depende da ativação do schedule e da execução do Job **FINA713**.

**Para iniciarmos as validações:**

**1º Schedule e Agent Habilitados e ativos**

O Schedule deve ser iniciado, seja o novo (Smart Schedule) ou o antigo (Schedule), conforme ilustrado na imagem abaixo. Caso se trate do antigo, o agente também deve ser iniciado, uma vez que, no novo Smart Schedule, o agente é iniciado automaticamente.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29604548462487)

**2º Validar configuração do JOB**

Para cada empresa, deve ser configurado um JOB, assim como uma filial, que, por sua vez, irá abranger as demais filiais.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29604561303191)

**Importante**

Caso se trate da cloud da Totvs ou de um ambiente separado para os JOBs, a configuração do JOB da rotina será realizada por meio desse ambiente.

Outro ponto importante, em alguns caso quando é cloud da Totvs, o campo "Comunicação no Cliente" deve ser configurado com "wf"

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29604561307031)

O JOB deve ser cadastrado em apenas um ambiente. Se estiver cadastrado em mais de um ambiente para a mesma empresa, isso poderá travar o processo. A validação pode ser feita por meio de um SELECT na tabela XX1.

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/29604561308183)**

**3º Cadastro de Bancos**

Preencher o campo obrigatório **Banco oficial (A6\_BCOOFI)**

**4º Cadastro de Parâmetros de Banco**

Cada banco possui **particularidades específicas**, sendo essencial validar a documentação oficial de cada instituição. Um preenchimento incorreto de qualquer campo impedirá o envio das informações ao banco.

**Para mais informações:**

[Contas a receber (Comunicação bancária online)](https://tdn.totvs.com/pages/releaseview.action?pageId=612548392)

5º **Configurações de Contas**

Caso haja alterações nas informações dos cadastros de banco ou no cadastro de parâmetros banco, será necessário excluir o cadastro atual e incluí-lo novamente em configurações de contas do novo painel gestor.

Após a realização das validações mencionadas, **execute o job da FINA713** e verifique se ocorre alguma falha. Caso ocorra falha, consulte o campo **EA\_APIMSG na SEA.** Caso não haja nenhuma informação gerada, isso indica que alguma das validações acima esta divergente. Se, por outro lado, houver dados gerados e não gerou o boleto, encaminhe o conteúdo do JSON para a equipe de suporte, juntamente com o console log, para que possam validar e identificar o problema.

**Importante**

Para o console log gerar o conteúdo do erro deve-se ativar as tags abaixo

Na seção **[ENVIRONMENT/AMBIENTE]** adicionar ou ativar  **FWFRAME\_TRACELOG=1**

Na seção **[GENERAL]**  adicionar ou ativar **Consolelog=1, LogHttpFuncs=1 e tlpp\_rest\_log=1 ConsoleMaxSize=125829120**
