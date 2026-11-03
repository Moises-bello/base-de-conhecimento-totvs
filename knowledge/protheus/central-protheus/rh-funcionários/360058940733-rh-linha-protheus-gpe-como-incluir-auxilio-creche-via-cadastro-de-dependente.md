---
article_id: 360058940733
category: RH - Funcionários
content_hash: de09f58aa88d579ab992c6eb6ab8cfdd95be70bd362051a60ce10b5b6b9e7094
fetched_at: '2026-06-28T22:43:27.598053+00:00'
product: protheus
section_id: 360011909593
source: central-protheus
title: RH - Linha Protheus - GPE - Como incluir auxilio creche via cadastro de dependente
type: support-article
updated_at: '2025-07-17T14:43:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058940733-RH-Linha-Protheus-GPE-Como-incluir-auxilio-creche-via-cadastro-de-dependente
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26441261333655) Tempo aproximado para leitura: **00:02:00 min**  
**Dúvida**Como incluir auxilio creche via cadastro de dependente?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução** **1.** O primeiro passo é cadastro na tabela S015, através do caminho **Atualizações > Definição Cálculos > Manutenção Tabelas (GPEA320) > S015:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360096879814)  
  
Campos:**

* **Filial =** Campo padrão, Código da filial que será calculado o auxílio-creche.
* **Mês/Ano** = Campo padrão, Mes/Ano que as informações serão válidas, caso fique em branco será válido para todos os meses e anos.
* **Sequência** = Campo auto numerado para controle interno da tabela.
* **Sindicato** = Código do sindicato que estes valores terão efeito.
* **Limite de Meses** = Quantidade máxima de meses que o dependente pode ter para receber o auxílio.
* **Valor do Pagamento** = Valor a ser pago do auxílio-creche.
* **Meses a Partir De**= Quantidade mínima de meses que o dependente pode ter para receber o auxílio, ou seja acima desta quantidade de meses o dependente estará enquadrado nesta faixa.
* **Isento de IR (S/N)**= Indicará se esta faixa terá ou não a isenção de Imposto de Renda, o campo deverá ser preenchido com "S" ou "N" (Sim para isenção e Não para retenção de IR)  
  **Obs**. Caso o conteúdo deste campo esteja vazio ou **preenchido com S - COM RETENÇÃO PARA IRRF** o Auxílio será pago na verba de **ID 721 COM INCIDÊNCIA PARA IR**  
  Caso o conteúdo deste campo esteja **preenchido com N - SEM RETENÇÃO PARA IRRF**o auxilio será pago na verba de **ID 1414 SEM INCIDÊNICIA PARA IR**  
  **Obs**. O novo campo Meses a Partir De, foi criado para atuar junto com o campo Limite de Meses, desta forma é possível fazer um De/Até e criar faixas de idade que terão ou não retenção de Imposto de Renda

**Exemplo de preenchimento da tabela S015 - AUXILIO CRECHE:  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360099194593)**

* Neste exemplo de preenchimento, a empresa só paga o auxílio-creche para os funcionários do sindicato 01.
* Para os dependentes que recebem o auxílio-creche e tem de 0 até 60 meses (5 anos) o valor do auxílio será de R$ 300,00 e será isento de imposto de renda
* Para os dependentes que recebem o auxílio-creche e tem acima de  60 meses o valor do auxílio será de R$ 400,00, mas com retenção de imposto de renda.

**2.** Após cadastro da S015, acesse **Atualizações > Funcionários > Dependentes (GPEA020)**. Selecione o funcionário e **clique em Manutenção**  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360099195073)  
  
**3.** Preencha os campos para inclusão do dependente, selecione **SIM** no campo Aux. Creche e clique em confirmar:  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360096880834)

**Saiba mais:**[RH - Linha Protheus - GPE - Cadastro Auxílio Creche gera mensagem: Quando o campo "Aux. Creche" for preenchido com sim, deverá existir valor no campo "Valor Creche" ou então registro válido na tabela S015](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052504013-RH-Linha-Protheus-GPE-Cadastro-Aux%C3%ADlio-Creche-gera-mensagem-Quando-o-campo-Aux-Creche-for-preenchido-com-sim-dever%C3%A1-existir-valor-no-campo-Valor-Creche-ou-ent%C3%A3o-registro-v%C3%A1lido-na-tabela-S015)  
[RH - Linha Protheus - GPE - Como o sistema valida o termino de direito do auxilio creche](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058450393-RH-Linha-Protheus-GPE-Como-o-sistema-valida-o-termino-de-direito-do-auxilio-creche)  
[RH - Linha Protheus - GPE - Quais as documentações relacionadas ao cadastro de funcionários?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/11311670958615-RH-Linha-Protheus-GPE-Quais-as-documenta%C3%A7%C3%B5es-relacionadas-ao-cadastro-de-funcion%C3%A1rios)
