---
article_id: 28441116541847
category: eSocial - Parametrizador
content_hash: 7263d670fbcfa6524add5a0497ea23cd7e5fbbe0dbeaea200769ea61a72dd606
fetched_at: '2026-06-28T22:47:06.229657+00:00'
product: rm
section_id: 1500000834501
source: central-rm
title: RH - RM - FOP - eSocial - Consultar número de eventos transmitidos pelo eSocial
type: support-article
updated_at: '2024-12-11T11:23:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28441116541847-RH-RM-FOP-eSocial-Consultar-n%C3%BAmero-de-eventos-transmitidos-pelo-eSocial
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28441077706007)**Tempo aproximado para leitura: **00:01:30 min**

**Dúvida**Como consultar os eventos enviados no eSocial em determinado intervalo de tempo?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as versões  
  
**Solução**

Para  que seja possível identificar a quantidade de registros enviados através do RM em determinado período de tempo, é necessário realizar uma consulta SQL na tabela PESOCIALEVENTOS considerando a data de envio destes registros.

A consulta pode ser executada por dentro do próprio RM, através da Visão de Dados, seguindo os passos abaixo:

1. Acesse o menu **Gestão | Visão de Dados** e clique em **+** para incluir uma nova consulta;   
   [BI - Consultas SQL menu Visões de Dados](https://centraldeatendimento.totvs.com/hc/pt-br/articles/13055235652759)
2. Preencha os campos **Código** e **Título** conforme desejado. No campo **Aplicação** informe **RM LABORE**;
3. Na caixa de texto logo abaixo, preencha a seguinte consulta SQL:  
   *SELECT COUNT(ID) FROM PESOCIALEVENTOS NOLOCK*  
   *WHERE DATAENVIO >= 'AAAA-MM-DD' AND DATAENVIO < 'AAAA-MM-DD'*  
   *-- Substitua "AAAA" pelo ano, "MM" pelo mês e "DD" pelo dia, conforme o período que quer validar*  
     
   ![](https://totvssuporte.zendesk.com/attachments/token/EYJxRzC6PsFPWw3A9XJOnhTU7/?name=image.png)
4. Após, clique em Salvar para que o cadastro seja salvo no sistema;
5. Pra executar a consulta, clique em Executar na parte superior direita da tela. O sistema irá exibir o número de registros transmitidos pelo RM conforme o período informado na consulta;

Na base de dados TOTVS utilizada para o cadastro acima temos, por exemplo, 10.616 registros cuja integração ocorreu no mês 07/2024.

![](https://totvssuporte.zendesk.com/attachments/token/z31OcTTfG7aiM4MCKXOnfAOj0/?name=image.png)

**Importante**Para que o número exibido esteja correto, é importante **restaurar os eventos da Fila Complementar** para a Fila de Eventos oficial antes de executar a consulta: [eSocial - Restaurar fila de eventos complementar](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036243133-RH-RM-FOP-eSocial-Restaurar-fila-de-eventos-complementar)

Para clientes que possuem **Franquia do TSS (Cloud)**, o número de registros do RM pode não ser exatamente igual ao do TSS visto alguns cenários como:  
     - Eventos integrados mais de uma vez devido à rejeição: Mantém um único registro no RM, mas geram mais de um registro no TSS;  
     - Possível exclusão de registros no RM, sem que tenha ocorrido a mesma exclusão no TSS;  
     - Entre outros.
