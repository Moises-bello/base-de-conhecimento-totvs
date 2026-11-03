---
article_id: 23673296229783
category: eSocial - Gerar XML/ Integração Evento
content_hash: bb9aa39bc1bea754fdd7aab75cf5e2e317de7b06c626708fff3041a521614214
fetched_at: '2026-06-28T22:47:12.043720+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: RH - RM - FOP - eSocial - Como informar ao governo que o contrato passou de
  prazo determinado para prazo indeterminado para contratos definidos em dias
type: support-article
updated_at: '2025-08-29T12:39:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23673296229783-RH-RM-FOP-eSocial-Como-informar-ao-governo-que-o-contrato-passou-de-prazo-determinado-para-prazo-indeterminado-para-contratos-definidos-em-dias
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23673296195351) Tempo aproximado para leitura: **00:03:10 min** **Dúvida**Como informar ao governo que o contrato passou de prazo determinado para prazo indeterminado para contratos definidos em dias?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as versões  
  
**Solução**A alteração do prazo do contrato, quando é alterado de prazo determinado para prazo indeterminado é enviado no evento S-2206.   
De acordo com o MOS, Item 6.6 do evento S-2206 - Contrato por prazo determinado, não é obrigatório o envio do S-2206, informando a indeterminação do contrato por prazo definido em dias, uma vez que o governo já entenderá a indeterminação automática do contrato, após ter ultrapassado o prazo definido no evento inicial (S-2190, S-2200 ou S-2300).

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23673296198167)

No item 6.7, informa as duas exceções às quais, deverão ser enviados os eventos S-2206, que são para as categorias 103 e 102. Nestes casos, quando exceder o prazo determinado, deverá ser convertido em vínculo empregatício comum, sendo necessário o envio do S-2206 alterando o tipo de contrato, categoria do trabalhador e outras alterações decorrentes da conversão.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23673573618327)

Tais informações também constam nas [Perguntas Frequentes do Governo](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes-producao-empresas-e-ambiente-de-testes).

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25803197127575)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25803219911703)

Caso a empresa queira enviar o S-2206 para os funcionário que já alteraram o Tipo de contrato de trabalho para indeterminado, será necessário seguir o passo a passo abaixo:

[S-2206 - Geração do gatilho de alteração do término de contrato (tag <tpContr>)](https://tdn.totvs.com/pages/releaseview.action?pageId=857922038)

**Importante**

-  Ao marcar o parâmetro "Gerar gatilho para Final do Contrato", serão gerados apenas gatilhos para o evento S-2206. Caso selecione outro evento será apresentada a mensagem abaixo:

![](https://tdn.totvs.com/download/attachments/857922038/image-2024-8-6_9-31-37.png?version=1&modificationDate=1722947497463&api=v2)

- Apenas os términos de contrato que ocorram dentro da competência serão considerados na geração;  
- Com o recurso de Agendamento de tarefas, você pode programar para gerar os gatilhos automaticamente, sem a necessidade de interação do usuário, tornando o processo mais dinâmico e produtivo. Isso funciona com o JobServer configurado para execução em modo 3 Camadas. Para mais informações sobre a configuração, clique [aqui](https://tdn.totvs.com/pages/releaseview.action?pageId=857922038).

**Saiba mais**  
Para mais informações acesse:  
- [Documentação Técnica](https://www.gov.br/esocial/pt-br/documentacao-tecnica) ;  
- [RH - RM - FOP - eSocial - Como gerar o evento S-2206](https://centraldeatendimento.totvs.com/hc/pt-br/articles/11334863362839-RH-RM-FOP-eSocial-Como-gerar-o-evento-S-2206)   
- [Contrato de Experiência](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360001092267-RH-RM-FOP-eSocial-Contrato-de-Experi%C3%AAncia)
