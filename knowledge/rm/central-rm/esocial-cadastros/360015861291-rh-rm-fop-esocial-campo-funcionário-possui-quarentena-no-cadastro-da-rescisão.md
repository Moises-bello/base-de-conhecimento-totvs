---
article_id: 360015861291
category: eSocial - Cadastros
content_hash: 48dbd9f2c23bf939adfba349455a9e20ba075becee81b2b5db1bad82f58816f5
fetched_at: '2026-06-28T22:47:14.447898+00:00'
product: rm
section_id: 1500000834341
source: central-rm
title: RH - RM - FOP - eSocial - Campo Funcionário possui Quarentena no cadastro da
  rescisão
type: support-article
updated_at: '2024-12-26T15:47:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015861291-RH-RM-FOP-eSocial-Campo-Funcion%C3%A1rio-possui-Quarentena-no-cadastro-da-rescis%C3%A3o
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24348994585879) Tempo aproximado para leitura: 00:03:00 min**

**Dúvida**Para que serve o campo **Funcionário possui Quarentena** no cadastro da rescisão?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as versões  
  
**Solução**Este campo foi criado com o intuito de declarar ao eSocial determinado pagamento realizado à funcionário de confiança  durante o período informado. Tal pagamento é uma forma de contraprestação pela não concorrência, estabelecendo restrição por período acordado para que o empregado não trabalhe para empresa concorrente, em caso de rescisão contratual.

Para parametrização e lançamento dessa rotina, deverão executar os seguintes passos:  
1. Ao realizar o cadastro da rescisão do funcionário, selecione a flag **Funcionário possui Quarentena** e informe a data final da quarentena.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360041293094)

2. O pagamento da importância, deverá ser realizado mensalmente até o fim do período informado no campo supracitado através da rescisão complementar. Para isso, acesse o menu **eSocial | Acordo Coletivo / Reajuste por Lei** e crie um novo registro com o tipo de acordo **F - Outras verbas de natureza salarial  ou não salarial devidas após desligamento**. A **Data do efeito** deverá ser anterior ao desligamento do funcionário;

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360042127933)

3. Após realizar a parametrização acima, no mês subsequente ao da rescisão deverá ser executado o processo de rescisão complementar. Acesse o menu **Rescisão | Complementar**, preencha os dados do período da rescisão e no campo**Data último movimento**informe uma data da competência atual. No campo **Dissídio/Convenção/Acordo Coletivo**marque a opção **Não.** Selecione as flags **Calcular somente Eventos informados** e **Pagamento de verbas de natureza salarial  ou não salarial devidas após desligamento** para que o sistema habilite o campo ***Dados do* Dissídio/Convenção/Acordo Coletivo**, onde deverá ser informado o registro criado no passo 2. Após avançar a tela, no campo **Eventos a serem somados em todas as rescisões complementares** deverá ser incluído o evento criado para pagamento da verba ao funcionário. Salve e execute a rescisão complementar.

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360042128073)

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360041295054)

**Importante**Os **passos 2 e 3** deverão ser **repetidos todos os meses** até a competência final informada no campo **Data Fim Quarentena** presente no cadastro da rescisão. Os eventos S-1200 e S-1210 serão gerados para todos os meses em que se realizar a rescisão complementar e devem, então, ser transmitidos para o governo.
