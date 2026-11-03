---
article_id: 360052716514
category: RH - Funcionários
content_hash: 1fd43a9958a68fb80972eec1809b4ee4f2e3fb73d8108e709abc44e50020d5fe
fetched_at: '2026-06-28T22:43:27.680803+00:00'
product: protheus
section_id: 360011909593
source: central-protheus
title: RH - Linha Protheus - GPE - Como restringir o acesso de usuários quanto a alteração
  de campos específicos no cadastro dos Funcionários
type: support-article
updated_at: '2025-09-02T13:26:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052716514-RH-Linha-Protheus-GPE-Como-restringir-o-acesso-de-usu%C3%A1rios-quanto-a-altera%C3%A7%C3%A3o-de-campos-espec%C3%ADficos-no-cadastro-dos-Funcion%C3%A1rios
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24459112950423) Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**Como **restringir o acesso** do usuário para alterar informação de um campo específico?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Este procedimento poderá ser efetuado para **qualquer campo do sistema**, para que somente um ou mais usuários possam alterar a informação.  
  
O exemplo abaixo se refere a rotina de **Cadastro de Funcionários - campo Salário da aba Funcionais.  
  
1 -** No campo **Salário,** clique com **F1** para identificar qual o nome deste campo. Neste caso, é **RA\_SALARIO:**  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360087312893)

**2 -** Acesse o módulo de **Configurador > Usuários > Senha > Usuários,** anote o **ID do usuário** que terá acesso para alterar o campo RA\_SALARIO. Neste caso, apenas o usuário de ID 000003 terá essa permissão:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31971946289047)

**3 -** Acesse **Base de Dados > Dicionários > Arquivos,** pesquise o nome da tabela do campo em questão. Neste caso, é a tabela **SRA:**![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360086136574)

**4 -** Selecione a opção **Editar > Funcionário > Campos**:  
  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360086144854)

**5 -** Pesquise o campo **RA\_SALARIO**:  
  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360086146414)

**6 -** Selecione **Editar** > aba **Opções >** campo **Modo Edição** informe a variável ‘**\_\_cUserId**’ que é carregada automaticamente quando o usuário acessa o sistema, validando qual usuário terá acesso.   
Neste caso, o campo deve ficar desta forma:**\_\_cUserId $ "000003"**Caso queira liberar o acesso para outros usuários, basta separar os demais IDs por vírgulas.  
  
![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360087337373)

**7 -** Por fim, atualize o Banco de Dados em acesso exclusivo, selecionando o botão **Atualizar Base de Dados.**

**Saiba Mais:**  
[RH - Linha Protheus - GPE - Restringir acesso de usuário a determinada rotina](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059006033-RH-Linha-Protheus-GPE-Restringir-acesso-de-usu%C3%A1rio-a-determinada-rotina?source=search)  
[RH - Linha Protheus - GPE - Configuração para que determinados usuários possam visualizar ou não um campo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059356113-RH-Linha-Protheus-GPE-Configura%C3%A7%C3%A3o-para-que-determinados-usu%C3%A1rios-possam-visualizar-ou-n%C3%A3o-um-campo?source=search)
