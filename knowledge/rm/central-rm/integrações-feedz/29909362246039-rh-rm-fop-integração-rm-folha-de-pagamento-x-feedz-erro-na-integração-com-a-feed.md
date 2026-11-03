---
article_id: 29909362246039
category: Integrações - Feedz
content_hash: 598c80c8e8b9c6a5cc47a238be0e8d1d3a21f8c143b5d5493dd1377b42d7e744
fetched_at: '2026-06-28T22:46:41.462938+00:00'
product: rm
section_id: 28212337440791
source: central-rm
title: RH - RM - FOP - Integração RM Folha de Pagamento x Feedz - Erro na integração
  com a Feedz código XXXX
type: support-article
updated_at: '2025-02-11T20:22:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/29909362246039-RH-RM-FOP-Integra%C3%A7%C3%A3o-RM-Folha-de-Pagamento-x-Feedz-Erro-na-integra%C3%A7%C3%A3o-com-a-Feedz-c%C3%B3digo-XXXX
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29909391835799) Tempo aproximado para leitura: **00:07:24 min****Dúvida**Como identificar a causa do erro na integração RM x Feedz a partir do código de erro retornado no log de execução?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - A partir da versão 12.1.2310  
  
**Solução**

Durante a execução da integração, alguns erros podem surgir. Para facilitar a correção, preparamos uma lista detalhada com os códigos de erro que podem ser retornados:

|  |  |  |
| --- | --- | --- |
| Código | Mensagem | Detalhes |
| 500 | Ocorreu um problema ao tentar conectar a plataforma da Feedz. | Caso possua restrição em seu firewall, verifique se os endereços abaixo possuem liberação para as conexões externas.   * Produção: [https://integrations.feedz.com.br](https://integrations.feedz.com.br/) * SandBox: [https://integrations.feedz.dev](https://integrations.feedz.dev/) |
| 0100 | Ocorreu um erro inesperado! > Não foi possível salvar o colaborador. | Ocorre quando o e-mail enviado no colaborador ou líder já existe na base da Feedz. Por se tratar de um campo pessoal, este e-mail não será listado na mensagem. |
| 4998 | Id do processo não encontrado | Significa que o processId informado na requisição de consulta de lotes está incorreto. |
| 4999 | Ocorreu um erro inesperado! | Representa erros genéricos ou inesperados que podem acontecer no servidor ou que podem ser gerados por algum aspecto incorreto não previsto do lote enviado. |
| 5000 | Token inválido ou expirado! / Bearer token não informado. | Isso indica que o token não foi informado na requisição ou informado não é válido. É necessário conferir se o token informado é igual à chave API na plataforma Feedz. Em caso afirmativo, é necessário gerar outra chave. |
| 5000 | Body vazio | Significa que foi enviada uma requisição para gravar um lote, mas sem nenhum dado. |
| 5001 | O total de itens enviados no corpo da requisição excede o limite de 100 registros. Todos os registros foram ignorados no processamento. | Ocorre ao enviar um lote com mais de 100 registros. |
| 5003 | A pessoa NPE (IntegrationId = IDN) está referenciando um gestor que não existe. Essa pessoa não será importada. | Esse erro ocorre ao tentar cadastrar um colaborador, vinculando a um gestor que ainda não foi cadastrado. |
| 5004 | A pessoa NPE (IntegrationId = IDN) está referenciando ela mesmo como chefe. Essa pessoa não será importada. | Esse erro ocorre ao tentar cadastrar um colaborador, vinculando ela mesma como gestora (integrationId = managerIntegrationId). |
| 5005 | A pessoa NPE (IntegrationId = IDN) está referenciando um departamento que não existe. Essa pessoa não será importada. | Esse erro ocorre ao tentar cadastrar um colaborador, vinculando a um departamento que ainda não foi cadastrado. |
| 5006 | A pessoa NPE (IntegrationId = IDN) está referenciando uma unidade que não existe. Essa pessoa não será importada. | Esse erro ocorre ao tentar cadastrar um colaborador, vinculando a uma unidade que ainda não foi cadastrada. |
| 5008 | A pessoa NPE (IntegrationId = IDN) está referenciando um cargo que não existe. Essa pessoa não será importada. | Esse erro ocorre ao tentar cadastrar um colaborador, vinculando a um cargo que ainda não foi cadastrado. |
| 5009 | O ID de integração (IntegrationId) é obrigatório e não foi informado para a Pessoa NPE. Essa pessoa não será importada. | Ocorre ao enviar uma pessoa e não informar se id de integração. |
| 5011 | O nome (Name) é obrigatório e não foi informado para a Pessoa (IntegrationId = IDN). Essa pessoa não será importada. | Ocorre ao enviar uma pessoa e não informar seu nome. |
| 512 | O e-mail (Email) é obrigatório e não foi informado para a Pessoa 'NPE' (IntegrationId = IDN). Essa pessoa não será importada. | Ocorre ao enviar uma pessoa e não informar seu e-mail. |
| 5013 | A pessoa 'NPE' (IntegrationId = IDN) possui o mesmo e-mail de outra pessoa da lista de pessoas enviadas ou da base. Essa pessoa não será importada. | Essa validação existe para evitar cadastrar pessoas duplicadas na base. Assim não é possível cadastrar dois e-mails iguais para integrationIds diferentes e vice versa. |
| 5014 | A pessoa 'NPE' (IntegrationId = IDN) deve ter o nome digitado somente com caracteres com nome, sobrenome e apenas 1(um) espaço entre eles. | Esse erro ocorre ao informar um nome inválido. |
| 5015 | A pessoa 'NPE' (IntegrationId = IDN) não pode ter o apelido igual ao nome. | Ocorre quando o name é igual ao socialName. |
| 5016 | O email fornecido 'EML' para a pessoa 'NPE' (IntegrationId = IDN) não está em um formato válido. | Ocorre ao enviar uma pessoa com o e-mail em formato inválido. |
| 5017 | O registro com o nome 'NRA' não foi salvo durante o processamento porque o campo 'IntegrationId' não foi informado." | Ocorre ao enviar qualquer registro auxiliar e não informar o integrationId. |
| 5018 | O registro com o código 'IDN' não foi salvo durante o processamento porque o campo 'Name' não foi informado. | Ocorre ao enviar qualquer registro auxiliar e não informar o nome. |
| 5030 | Quando informado a data de demissão deve ser também informado o motivo (dismissalType). | Ocorre ao enviar data de demissão e não informar o motivo. |
| 5031 | Deve ser informado o motivo da demissão (dismissalType) apenas quando for informado a data de demissão. | Ocorre ao enviar motivo da demissão e não informar a data de demissão. |
| 5032 | A data de admissão não pode ser maior que a data de demissão. | Ocorre ao enviar uma data de admissão posterior à data de demissão. |
| 5048 | O ID de integração do líder (managerIntegrationId = MII) informado para a pessoa (personIntegrationId = IDN) não existe. | Ocorre ao tentar vincular pessoa e líder pela rota persons-bind e não ter esse líder cadastrado previamente na plataforma. |
| 5049 | O ID de integração da pessoa (personIntegrationId = IDN) informada não existe. | Ocorre ao tentar vincular pessoa e líder pela rota persons-bind e não ter esse colaborador cadastrado previamente na plataforma. |
| 5050 | Uma pessoa (personIntegrationId = IDN) não pode ser líder de sí próprio | Ocorre ao tentar vincular uma pessoa a ela mesma como líder (personIntegrationId = managerIntegrationId) através da rota persons-bind. |

**Exemplo:**

Ao tentar integrar um funcionário, foi retornado o erro código 5016. Este erro ocorre quando o e-mail do colaborador está em formato inválido, conforme descrito no mapeamento.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29910015333399)

Ao verificar o cadastro do funcionário, veja que o formato do e-mail está incorreto: "**teste.com.br**".  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/29910015335575)

Atualizamos o e-mail para um formato válido, como por exemplo: "**marcelo@totvs.com.br**".  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/29910015337751)

Após alteração cadastral, foi possível integrar o funcionário com sucesso:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/29910038791575)

**Saiba Mais:**

**[TDN - Integração RM x FEEDZ](https://tdn.totvs.com.br/pages/releaseview.action?pageId=785614408)**

**[Integração RM Labore x Feedz - Nenhum funcionário atende a seleção](https://centraldeatendimento.totvs.com/hc/pt-br/articles/28206773411095-RH-RM-FOP-Integra%C3%A7%C3%A3o-RM-Labore-x-Feedz-Nenhum-funcion%C3%A1rio-atende-a-sele%C3%A7%C3%A3o)**
