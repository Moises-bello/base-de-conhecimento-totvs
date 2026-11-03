---
article_id: 360019748711
category: Encargos
content_hash: 2812fb7f97020850951a35cb51c85e191b236e2baf6ae05213ab447c1f5bb8db
fetched_at: '2026-06-28T22:46:53.370002+00:00'
product: rm
section_id: 1500000834581
source: central-rm
title: RH - RM - FOP - Contabilização
type: support-article
updated_at: '2025-03-12T10:00:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019748711-RH-RM-FOP-Contabiliza%C3%A7%C3%A3o
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)** Tempo aproximado para leitura: **00:07:00 min  
  
Dúvida**Como realizar a parametrização de eventos e/ou encargos para contabilização e sua execução?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**A principal finalidade da Contabilidade é fornecer informações sobre o Patrimônio de ordem econômica e financeira, que facilitam assim as tomadas de decisões, tanto por parte dos administradores ou proprietários, como também por parte daqueles que pretendem investir na empresa. O sistema **TOTVS Gestão Contábil** não tem informações de eventos, seções, encargos ou funcionários. Por isso, para que a contabilização seja gerada corretamente, é preciso fazer um relacionamento dos agrupamentos e integrações da **Folha de Pagamento** com a conta contábil (conta Saldus).  
  
No sistema, a funcionalidade que faz este agrupamento é o **Agrupamento de Contas Contábeis**, disponível em **Encargos | Cadastros | Cadastros Contábeis | Agrupamentos de Contas.**Veja abaixo informações sobre o agrupador e siga os passos sobre como relacioná-los aos eventos e encargos a serem contabilizados:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8865678045335/mceclip0.png)  
  
1. Informe o **Grupo Conta.** Este campo é a referência do agrupamento contábil. Este cadastro é informando no cadastro do evento ou encargo, na aba Dados Contábeis. Tabela dinâmica: **GRPCONT**.  
  
2. Agora deverá ser informado o **Código de Integração**, se houver.Este campo também é informado no cadastro da seção ou centro de custo, aba Dados Contábeis. Tabela dinâmica: **CODINTCONT** / **CODINTGER**.  
  
3. Informe o **Código de Integração Por Funcionário**, se houver.Este campo também é informado no cadastro do funcionário, em **Base de Cálculo | Dados contábeis**. Tabela dinâmica: **INTCONTFUN** / **INTGERFUN**.  
  
4. Informe a **Conta Saldus.** Esta é a conta de integração com o sistema contábil. Os registros são ítens da tabela CCONTA, disponível em **Cadastro | Contabilização | Plano de contas contábeis (RM Saldus)**.  
  
5. Informe o **Código da Filial.** Este cadastro está disponível em **Cadastros | Filiais**. Tabela Dinâmica: **GFILIAL**.  
  
6. Informe o **Código do Departamento.**7. Informe o **Centro de Custo**. Este cadastro está disponível em **Cadastro | Centros de custos (RM Labore)**. Tabela Dinâmica: **PCCUSTO**.  
  
Após realizar a parametrização do **Agrupamento das Contas Contábeis**, será necessário parametrizar os eventos e/ou encargos para geração da contabilização. Para que os eventos e/ou encargos de um colaborador sejam enviados para a contabilização, é necessário seguir os passos abaixo:  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8865679856535/mceclip1.png)

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8865702136727/mceclip2.png)  
  
**Sobre Eventos**  
  
1. Acesse **Administração de Pessoal | Eventos**, edite o evento que deseja parametrizar e vá na aba **Dados Contábeis**;  
  
2. Nos campos **Conta para Crédito** e **Conta para Débito**, será necessário informar um agrupador de contas contábeis;  
  
3. Informe se haverá integração contábil ou por funcionário. Quando o evento e/ou encargo tem o campo **Tem Integração Contábil** marcado, o sistema usará a informação para determinar o **Agrupador de Contas** correto a ser utilizado. O mesmo acontece com o campo **Tem integração por funcionário**. Isso ser dá, pois há casos em que o **Grupo Conta** será ser utilizado em mais de um agrupador, dependendo da parametrização utilizada. Normalmente o **Grupo Conta** é o mesmo, mas as parametrizações do agrupador são divergentes.  
  
4. Informe se a contabilização será parcial no campo **Contabilização Parcial**. Neste tipo de parametrização o evento será responsável apenas por um das contas (crédito ou débito) e outro evento ou encargo será o responsável pela partilha contrária correspondente.  
  
**Sobre Encargos**  
  
1. Acesse **Encargos | Cadastros | Encargos**, edite o encargo que deseja parametrizar e vá na aba **Dados Contábeis**;  
  
2. Nos campos **Conta para Crédito** e **Conta para Débito**, será necessário informar um agrupador de contas contábeis;  
  
3. Informe se haverá integração contábil ou por funcionário. Quando o evento e/ou encargo tem o campo **Tem Integração Contábil** marcado, o sistema usará a informação para determinar o **Agrupador de Contas** correto a ser utilizado. O mesmo acontece com o campo **Tem integração por funcionário**. Isso ser dá, pois há casos em que o **Grupo Conta** será ser utilizado em mais de um agrupador, dependendo da parametrização utilizada. Normalmente o **Grupo Conta** é o mesmo, mas as parametrizações do agrupador são divergentes.  
  
4. Informe se a contabilização será parcial no campo **Contabilização Parcial**. Neste tipo de parametrização o evento será responsável apenas por um das contas (crédito ou débito) e outro evento ou encargo será o responsável pela partilha contrária correspondente.  
  
**Sobre o processo**  
Com todas as parametrizações feitas, o usuário poderá seguir à Geração dos Lançamentos da Contabilização, presente no menu Encargos:  
  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8866710648087/mceclip3.png)  
  
1. Perceba que a rotina fornece a opção de contabilizar Eventos e Encargos separadamente, a depender da marcação das flags correspondentes;  
  
2. O número do lote é preenchido de forma automática e sequencial. É normal o sistema apresentar uma mensagem perguntando se deseja manter ou excluir o lote que já se encontra preenchido, ou mesmo que aquele lote já existe, e se o usuário deseja excluí-lo;  
  
3. Na tela seguinte à demonstrada, caso o usuário não tenha executado as rotinas Geração dos Encargos e Geração do Histórico de Provisão, a Contabilização solicitará a marcação dos flags para executa-las. Sugere-se que antes da contabilização estas rotinas sejam executadas para que o usuário tenha maiores opções de parametrização, se assim for necessário:  
  
**![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8866734498967/mceclip4.png)****Saiba mais**  
[RH - RM - FOP - Contabilização: Não foi encontrado Agrupamento Contábil](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004150272-RH-RM-FOP-Contabiliza%C3%A7%C3%A3o-N%C3%A3o-foi-encontrado-Agrupamento-Cont%C3%A1bil-)  
[Dicas e Soluções - Contabilização .Net](https://tdn.totvs.com/pages/releaseview.action;jsessionid=5B14D95172832808EC3C4DB8B76CB26B?pageId=118883732)  
[Parametrização para Contabilização](https://tdn.totvs.com/pages/releaseview.action?pageId=110428888)
