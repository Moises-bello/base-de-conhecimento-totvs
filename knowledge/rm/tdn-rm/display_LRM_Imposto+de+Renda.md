---
content_hash: 04deafb3891525ad9c591766eb632a880c001d62edd92e36a42130c1fe509f2c
fetched_at: '2026-06-29T00:10:07.802429+00:00'
page_id: '452719441'
product: rm
source: tdn-rm
title: Imposto de Renda
type: documentation
url: https://tdn.totvs.com/display/LRM/Imposto+de+Renda
version: 3
---

Informação para selecionar o período de apuração para o lançamento financeiro do IRRF.   
Lembrando que somente ficará disponível se o usuário selecionar um tipo de lançamento ativo de IRRF (5-IRRF a pagar, 8-IRRF de Férias, 9-IRRF de Rescisão, 12-IRRF 13º a pagar ou 20 – Total de IRRF).  
   
**Data inicial e Data final**  
Informe o período no qual o sistema buscará os eventos de IRRF observando a data de pagamento do evento.  
   
**Observação:**  
1.    O sistema não considerará as informações dos campos: Ano, Mês e Período de competência. Será verificada a data de pagamento dos eventos com a data de apuração informada na pasta Imposto de Renda.  
2.    Para os lançamentos de IRRF de férias, o sistema verificará a data de pagamento das férias. Quando houver rateio por centro de custo e as férias não tiverem sido lançadas, os valores dos rateios dos lançamentos de IRRF Férias serão calculados com base no rateio fixo do funcionário. Para os demais casos, será considerada a movimentação por centro de custo.  
3.    No histórico dos lançamentos de IRRF será exibido o período de apuração informado na pasta Imposto de Renda.  
4.    Quando o funcionário tiver movimentação de férias informada no envelope, mas não tiver o envelope de férias cadastrado, no lançamento financeiro do IRRF de Férias o sistema irá buscar do envelope do funcionário, caso contrário, buscará do envelope de férias.  
5.    Para a base parametrizada por centro de custo, ao gerar o lançamento financeiro do IRRF de Férias, o sistema irá verificar se o evento de IRRF de Férias tem o campo "Centro de Custo no Evento" preenchido. Caso não esteja preenchido, o sistema buscará do rateio fixo do cadastro do funcionário.  
   
**Código da Receita**  
Informe o código da receita para ser considerado pelo RM Liber na geração da DARF, caso não necessite desta informação deixar em branco.  
   
Para geração do lançamento financeiro de IRRF (DARF) separando os valores de acordo com o tipo de funcionário (autônomos ou celetistas), o usuário deverá selecionar o tipo de funcionário na grade de Seleção de Funcionários e informar o código da receita no momento da geração dos lançamentos.   
   
**Observações:**  
1.    Caso haja necessidade de gerar mais de uma DARF na empresa, o usuário deverá realizar o processo quantas vezes forem necessárias separando por Seleção de Funcionários.  
2.    Neste campo estão listados os valores da tabela "Códigos da Receita" cadastrados no RM Fluxus e que são aplicáveis à pessoa física.

---

[Voltar a pagina inicial](http://tdn.totvs.com/pages/viewpage.action?pageId=452719571)
