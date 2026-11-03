---
content_hash: 653a40092ea56dd7d5d5ff17434629667fdb4830af9a584a8b2b4fbbfd316741
fetched_at: '2026-06-29T00:09:58.960445+00:00'
page_id: '452718264'
product: rm
source: tdn-rm
title: Geração de Encargos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452718264
version: 3
---

Encargos da folha de pagamento: são despesas recolhidas ao encerrar a folha de pagamento e são gerados para posterior contabilização selecionando o ano e mês de competência e período.   
   
O sistema traz como default (padrão) o mês e ano de competência atual e período igual ao atual.  
   
O campo Período é flexível no caso de contabilizar um ou mais de um período a ser selecionado, sendo que será apresentado um campo onde os períodos deverão ser separados por vírgula. **Exemplo:** 1, 2,3  
   
O parâmetro "Permite valores negativos para fórmulas" permite que o sistema faça a geração de encargos com valores negativos gerados por fórmula, ou seja, somente para os encargos cujo tipo é A (Valor calculado através de fórmula).  
   
O parâmetro "Calcula somente rateio de encargos" é utilizado para o caso de alteração no rateio de encargos e seja necessário apenas o cálculo do rateio de encargos.  
   
O parâmetro "Considera duas casas decimais p/fórmulas" Com este parâmetro marcado os encargos calculados por fórmula serão gerados considerando apenas duas casas decimais, caso o parâmetro esteja desmarcado será gerado considerando quatro casas decimais. Na visualização dos históricos de encargos serão exibidos quatro casas decimais, caso os encargos tenham sido gerados com o parâmetro marcado as duas últimas casas decimais irão aparecer zeradas.  
   
A "Seleção de Encargos Ativos para Contabilização" serve para indicar quais os grupos de encargos (código de encargos ativos) devem ser processados.  
   
**Atenção:** O sistema de folha de pagamento somente gera os rateios por cento de custo no histórico de encargos na rotina de contabilização quando parâmetro "Usa histórico de rateio de encargos na contabilização retroativa" estiver marcado nos parâmetros do sistema.

Dica

Veja também: [Exemplos para regra de cálculo dos encargos 5 - Provisão de FGTS de férias e 6 - Provisão de encargos de férias](https://tdn.totvs.com.br/pages/viewpage.action?pageId=790646098#1-1)
