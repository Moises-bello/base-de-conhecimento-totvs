---
article_id: 20885696694551
category: eSocial - Gerar XML/ Integração Evento
content_hash: 8530d235555e05876d761c1eb73657368f1635f94462c73fec7836ce38f32b81
fetched_at: '2026-06-28T22:47:12.065748+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: RH - RM - FOP - eSocial - Como preencher a tabela obrigatória de Dedução do
  Rendimento Tributável no Cadastro de Dependentes (S-1.2)
type: support-article
updated_at: '2026-06-01T17:39:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20885696694551-RH-RM-FOP-eSocial-Como-preencher-a-tabela-obrigat%C3%B3ria-de-Dedu%C3%A7%C3%A3o-do-Rendimento-Tribut%C3%A1vel-no-Cadastro-de-Dependentes-S-1-2
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20885665017239) Tempo aproximado para leitura: **00:04:00 min**  
  
**Dúvida**  
Como preencher a tabela obrigatória de Dedução do Rendimento Tributável no Cadastro de Dependentes?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as Versões  
  
**Solução**  
A partir do leiaute S-1.2, será informado no XML S-1210, a **Dedução do rendimento tributável relativa a dependentes**, através do grupo **dedDepend.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20885665032727)

Para que o sistema puxe essas informações no XML S-1210 01/2024, é necessário o preenchimento da tabela PFDEPIRRFDED. O preenchimento da tabela é realizado com o preenchimento dos campos no cadastro do**Dependente | Anexos | Valor Dedução do Rendimento Tributável**.

Essa tabela será preenchida quando o usuário já estiver utilizando uma das versões supracitas e que já tenha rodado o Rm.Atualizador, antes do lançamento da folha de 12/2023 (caso trabalhe com mês caixa), ou 01/2024 (caso trabalhe com mês competência). No momento do cálculo de folha, férias e 13º salário quando o dependente incidir em IRRF, dentro das condições legais, os valores serão inseridos neste anexo.

Caso o usuário já tenha lançado a folha (conforme cenário acima), será necessário:

**1. Quando ainda estiver na mesma competência na Folha**, o usuário poderá recalcular a folha, assim a tabela será preenchida automaticamente.;

**2. Quando o usuário já estiver em uma competência na Folha diferente,** haverá duas opções:

* **Manualmente**, acessando o cadastro do funcionário que possui dependente, em **Dependente | Anexos | Valor Dedução do Rendimento Tributáve**l e preenchendo os campos;

![](https://totvssuporte.zendesk.com/attachments/token/pQkP6F0BEkDUeTpdFrtlDS6qI/?name=image.png)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20885696677143)

* **Importação**, acessando **Configurações | Importações | Importação de Dados da Folha de Pagamento**.

![](https://totvssuporte.zendesk.com/attachments/token/HY4IwRBfn5bwtdJj1otEy3iaZ/?name=image.png)  
   
![](https://totvssuporte.zendesk.com/attachments/token/UAGtvHETI0cAQy9Yv9jjP3oKn/?name=image.png)

**Principais Campos e Parâmetros para a importação**

|  |  |
| --- | --- |
| ``` Campo ``` | ``` Descrição ``` |
| ``` Ano de Competência ``` | ``` Ano competência a que o registro se refere ``` |
| ``` Mês de Competência ``` | ``` Mês competência a que o registro se refere ``` |
| ``` Período ``` | ``` Período a que o registro se refere ``` |
| ``` Ano Caixa ``` | ``` Ano Caixa a que o registro se refere ``` |
| ``` Mês Caixa ``` | ``` Mês Caixa a que o registro se refere ``` |
| ``` Tipo de Movimento ``` | ``` Tipo de movimento deste registro, indica se é um registro referente a Folha de pagamento, 13° Salário, Férias ou Férias Rescisão ``` |
| ``` Valor ``` | ``` Valor do rendimento tributável ``` |
| ``` Dt. Vencto Férias ``` | ``` Caso o registro seja do tipo 3 - Férias, esse campo deve ser preenchido com a data de vencimento das férias do funcionário ``` |
| ``` Data Pagto. Férias ``` | ``` Caso o registro seja do tipo 3 - Férias, esse campo deve ser preenchido com a data de pagamento das férias do funcionário ``` |

 

**Importante**

Caso o usuário precise de saber o cálculo para o valor a ser informado, será necessário a solicitação para a Equipe Folha Cálculo;

Só serão permitidos a inclusão de registros no mês competência atual, anterior ao atual ou posterior;

Não será possível a inclusão de registros em anos e meses competências onde não existem registros de Ficha Financeira;

Quando for selecionado a inclusão de um registro utilizando o Tipo 3 - Férias , será necessário a inclusão da Dt. Vencto Férias e Dt. Pagto. Férias;

Para o calculo das férias, o vínculo dos valores dedutíveis dos dependentes com o recibo de férias são as datas de vencimento e data de pagamento das férias. Então, caso esse o recibo seja calculado e após o calculo tenha a sua data de pagamento alterada, os valores dedutíveis ficarão duplicados na tabela. Neste caso, a exclusão deverá ocorrer manualmente;

Para o IRRF de participação nos lucros não serão inseridos dados no anexo. Para usuários do parâmetro “Deduz valor por dependente na base de IRRF PL” marcado será emitido mensagem conforme TDN - Parâmetros de Cálculo 2/2;

Para acessar essa nova funcionalidade, deve-se permitir o acesso ao menu [01.01.01.01] Valor Dedução do Rendimento Tributável no perfil do sistema folha de pagamento, na aba segurança em serviços globais.

**Saiba mais**

Para mais informações acesse:

- [Valor Dedução do Rendimento Tributável](https://tdn.totvs.com/pages/releaseview.action?pageId=784779468)  
[- Valor Dedução do Rendimento Tributável no Cadastro de Dependentes - Alterações no cálculo para atender ao leiaute S-1.2 que irá substituir a DIRF](https://tdn.totvs.com/pages/releaseview.action?pageId=786553670)  
- [Parâmetros de Cálculo 2/2](https://tdn.totvs.com/pages/releaseview.action?pageId=561848185)
