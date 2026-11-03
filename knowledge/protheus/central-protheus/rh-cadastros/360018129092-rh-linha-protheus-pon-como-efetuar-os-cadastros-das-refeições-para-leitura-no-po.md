---
article_id: 360018129092
category: RH - Cadastros
content_hash: 9856771498f8d49791b21dfb48b2e873a766acb95f09473629b211658866d1e2
fetched_at: '2026-06-28T22:44:52.859687+00:00'
product: protheus
section_id: 32419135703319
source: central-protheus
title: RH - Linha Protheus - PON - Como efetuar os cadastros das refeições para Leitura
  no Ponto Eletrônico
type: support-article
updated_at: '2026-05-19T14:26:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018129092-RH-Linha-Protheus-PON-Como-efetuar-os-cadastros-das-refei%C3%A7%C3%B5es-para-Leitura-no-Ponto-Eletr%C3%B4nico
---

****![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36384292582551) Tempo aproximado para leitura: 00:01:30 min**  
Dúvida**Como realizar o cadastro dos tipos de refeições e das refeições para utilização na Leitura de Refeições no Ponto Eletrônico?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**O cadastro de refeições, geralmente é usado para empresas que utilizam do controle de refeição para seus funcionários onde o registro do consumo das refeições é feita por meio da marcação numa catraca especifica para o refeitório.  
  
Para o cadastro de refeição é necessário seguir com os procedimentos abaixo:  
  
**- Cadastros de Eventos:**Acesse o **módulo 16-SIGAPON, em Atualizações > Cadastro do ponto > Eventos**:  
Criar/alterar **Eventos** vinculados aos **IDs de Ponto** abaixo:

**015A** (% empresa). Esse evento deve ser vinculado com uma verba do tipo Base Provento para que os valores sejam levados para folha.  
**016A** (% do funcionário). Esse evento deve ser vinculado com uma verba do tipo Desconto, para que os valores sejam levados para folha.

**Exemplos:**Evento **015A > REFEICAO PARTE EMPRESA**:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19224117357335)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19224117373335)  
  
Evento **016A > REFEICAO PARTE FUNCIONARIO:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19224094251927)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19224122850199)**

**- Tipos de Refeição:**Acesse o módulo **16-SIGAPON**, em **Atualizações > Cadastro do ponto> Tipos de Refeição:**  
Cadastre os tipos de refeição, onde deve ser informado o valor da refeição, o % da empresa e do Funcionário.  
  
**Importante:**O percentual de desconto e valor de refeição é definido por cada regra de negócio de sua empresa e essa definição é de responsabilidade do responsável da empresa. Os exemplos a seguir é somente para utilizar como base cadastral.  
  
Exemplo de cadastros:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19224107437335)  
Veja um tipo de refeição de exemplo do cadastro:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19224107448343)  
  
**Obs:** Quando fizer o cadastro pela primeira vez, automaticamente será criado um registro com nome **OUTROS**, ele é usado para refeições que são feitas fora dos horários pré-fixados (**veja passo 2**), para refeições classificadas como Outros, também pode ser fixado valor da mesma forma que fixa o valor para os Tipos de Refeição cadastrados pelo usuário (**conforme** **passo 1**).

**- Refeição:**Acesse o módulo **16-SIGAPON**, em **Atualizações > Cadastro do ponto > Refeições:**  
Cadastre as Refeições. Neste cadastro será informado a faixa de horário em que o funcionário poderá fazer este tipo de refeição.   
Exemplo: 01 - Desjejum das 04:01 às 10:00 ou Almoço – 10:01 às 14:30 e para cada tipo de Refeição informe as faixas de acordo com a necessidade da empresa.   
Exemplo de cadastros:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19224107453719)  
  
**- Regra de Apontamento:**Acesse o módulo **16-SIGAPON**, em **Atualizações > Cadastro do ponto > Regra de Apontamento > Apontamentos:**  
Informe na Regra de Apontamento no campo **Desc. Refeiç** à opção **S-Sim** em todas as Regras que quiser que seja implantado o controle da refeição e que suba nos resultados após o cálculo mensal para integração dos eventos na folha;  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19224094278807)  
  
**- Tabela de Horário Padrão:**Acesse o módulo **16-SIGAPON**, em **Atualizações > Cadastro do ponto > Tabela de Horário Padrão:**  
Informe o código da refeição na tabela de horário padrão no campo **Cod. Refeição** em todos os Turnos que quiser que seja implantado o controle da refeição.  
  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4405663492375)  
  
**- Relógios:**Para leitura de arquivos TXT siga o procedimento:  
Cadastre um Relógio com tipo **R** (Refeição). O leiaute deve ser configurado pelo usuário, de acordo com o leiaute personalizado da empresa fornecedora do controle de refeições.   
Veja exemplo de cadastro de relógio na documentação a seguir: [RH - Linha Protheus - PON - Como cadastrar um relógio para leitura e gravação das refeições contidas no arquivo TXT de Ponto](https://centraldeatendimento.totvs.com/hc/pt-br/articles/19222215435927-RH-Linha-Protheus-PON-Como-cadastrar-um-rel%C3%B3gio-para-leitura-e-grava%C3%A7%C3%A3o-das-refei%C3%A7%C3%B5es-contidas-no-arquivo-TXT-de-Ponto?source=search)  
  
Já em casos de leituras de refeições integradas pelo SURICATO, valide o cadastro de relógio, conforme documentação:  
[RH - Linha Protheus - PON x Suricato - Integração de Marcações de Refeição do Suricato](https://centraldeatendimento.totvs.com/hc/pt-br/articles/34216293178007-RH-Linha-Protheus-PON-x-Suricato-Integra%C3%A7%C3%A3o-de-Marca%C3%A7%C3%B5es-de-Refei%C3%A7%C3%A3o-do-Suricato)  
  
**- Leitura e Apontamento:**Acesse o módulo **16-SIGAPON**, em **Miscelânea > Cálculos > Leitura/Apontamento Marcações:**  
Faça a **Leitura/Apontamento**, utilizando as perguntas conforme dois exemplos abaixo:  
1° exemplo:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19224104427543)  
2° Exemplo:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19224104429975)  
  
**- Visualização das marcações de refeições;**  
Após a leitura e apontamento das marcações referente a **Refeição** ficarão disponíveis em **Atualizações > Lançamentos > Refeições.  
  
- Cálculo Mensal:**Acesse o módulo **16-SIGAPON,** em **Miscelânea > Cálculos  > Cálculo Mensal:**Faça o **Cálculo Mensal,** onde ao realizar o cálculo o sistema subirá nos **Resultados** as verbas vinculadas aos eventos atribuídos aos **IDS 015A e 016A.****- Resultados:**Acesse o módulo**16-SIGAPON,** em **Atualizações > Lançamentos  > Resultados:**  
Filtrar o funcionário e visualizar, apresentará as verbas calculadas e disponíveis para serem integradas com a folha.  
 **- Integração Folha;**Faça a **Integração Folha,** onde ao realizar a Integração o sistema subirá as verbas geradas nos **Resultados** para a **Folha de Pagamento;  
  
- Relatório de Refeições:**Acesse o módulo **16-SIGAPON,**em **Relatórios > Diversos > Refeições**É possível emitir o relatório de refeições para análise e conferência, veja mais sobre o relatório na documentação abaixo:  
[RH - Linha Protheus - PON - Relatório de Refeições - PONR070](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050364213-RH-Linha-Protheus-PON-Relat%C3%B3rio-de-Refei%C3%A7%C3%B5es-PONR070?source=search) ****Saiba mais:**[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)  
[RH - Linha Protheus - PON - Integração com a Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050379453-RH-Linha-Protheus-PON-Integra%C3%A7%C3%A3o-com-a-Folha-de-Pagamento-?source=search)**[RH - Linha Protheus - PON - Como fazer e qual a finalidade do Cálculo Mensal](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051550453-RH-Linha-Protheus-PON-Como-fazer-e-qual-a-finalidade-do-C%C3%A1lculo-Mensal?source=search)
