---
content_hash: 7e658e4a482cd033e67f85f9164c489fb9acae6808f17b76b5ee8f44e7d5c3c8
fetched_at: '2026-06-29T00:10:05.421555+00:00'
page_id: '452719290'
product: rm
source: tdn-rm
title: Movimento Rescisório de Ponto
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719290
version: 1
---

**Movimento Rescisório de Ponto**

---

Por meio do TOTVS Automação de Ponto é possível realizar o cálculo rescisório do funcionário, de forma a gerar o movimento de ponto incluindo as horas do banco de horas e movimento de integração da folha com opção de redução da jornada, devido ao cumprimento do aviso prévio.   
   
**Atenção!** Para cálculo do movimento de ponto para rescisão, o sistema precisa ter a referência da data de demissão do funcionário, portanto, deve constar o cadastro da rescisão para o funcionário em questão, bastando para isso, apenas salvar os dados do cadastro, ou seja, não precisa executar o cálculo.  
   
  
As próximas telas do assistente vão depender das opções de parametrização marcadas, basta que o usuário faça o proposto pela etapa do assistente, até finalizar o processo para que o sistema calcule o movimento rescisório referente às horas apuradas por meio das batidas de ponto:  
   
**Etapa 1 -** **Visualizar funcionários**  
   
Abre a visão de funcionários para que o usuário faça a gestão de ponto conforme opções disponíveis nos anexos.  
   
**Etapa 2 -**  **Executar recálculo**  
   
Realiza o recálculo do movimento do funcionário para o período atual e/ou futuro:  
**Exemplo:**   
Período atual: 01/09/2011 a 30/09/2011  
CHAPA 00001 – Data de demissão: 15/10/2011  
CHAPA 00002 – Data de demissão: 25/09/2011  
   
Para a chapa 00001, será realizado o recálculo para o período atual e futuro, pois  a sua demissão está com data no período futuro, já para a chapa 00002, será realizado o recálculo apenas para o período atual, pois a data de sua demissão consta no período atual.  
**Etapa 3 - Executar Compensação e/ou Lançamento do banco de horas**   
   
Gestão do banco de horas dos funcionários, de forma a realizar compensações e lançamento das horas restantes para o movimento de ponto do funcionário.   
   
**Etapa 4 - Executar o lançamento de Eventos para o TOTVS Folha de Pagamento**  
   
Definição dos eventos a lançar para o movimento de integração da folha, tanto para o período atual como futuro.   
   
**Atenção!** Caso o usuário, selecione um funcionário cuja rescisão tenha sido cadastrada com data posterior ao período atual do ponto e, não houver período futuro cadastrado na Automação de Ponto, o sistema abre a tela de cadastro de período para que o usuário cadastre esse período e, em seguida, continue o processo de rescisão.   
 

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Compensação e Lançamento do Banco de Horas  
Lançamento para a Folha de Pagamento  
Aviso Prévio Trabalhado
