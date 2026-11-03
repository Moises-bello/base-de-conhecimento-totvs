---
article_id: 360044450133
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 6efbb71d2c5d157e6cc41cd495ee7258a31393c00557988b48d8dfb442a82902
fetched_at: '2026-06-28T22:42:47.184195+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: MP - SIGAPCP - Configurar no MATA108 a aglutinação de OPIs/SCs para documentos
  gerados pelo MRP
type: support-article
updated_at: '2020-03-11T20:15:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044450133-MP-SIGAPCP-Configurar-no-MATA108-a-aglutina%C3%A7%C3%A3o-de-OPIs-SCs-para-documentos-gerados-pelo-MRP
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:03:30 min**  
 **Dúvida**Como configurar a aglutinação de **OPIs - Ordens de produção intermediárias** e **SCs - Solicitações de Compra** no **MATA108 - Complemento de Produto** na geração de documentos do **MRP - Material Requiriments Planning**?  
   
 **Ambiente**Microsiga Protheus - Planejamento e Controle da Produção - Versão 12  
  
**Solução**  
Os campos **B5\_FORMMRP - Form. MRP** e **B5\_AGLUMRP - Aglu. MRP**no **MATA108** são inicializados com o valor padrão igual a **1-Pelo Programa**, de forma que o produto assuma as parametrizações do **MRP**.  
O campo **B5\_FORMMRP**, quando parametrizado com os valores **2-Por OP** ou **3-Por Necessidade**, sobrepõe o que foi parametrizado no **MRP** nas perguntas **Geracao de SCs?** e **Geracao de OPs Prod. Interme?** para o produto.  
O campo **B5\_AGLUMRP**, quando parametrizado com valor maior que 1, e sendo essa periodicidade maior que a informada nos parâmetros do **MRP** no campo **Periodicidade do MRP**, sobrepõe a aglutinação de **OPIs**/**SCs** para o produto.  
O campo **B5\_FORMMRP** deve ser parametrizado no produto pai, para que ao gerar as ordens para atender sua necessidade, saiba como gerar as **OPIs**/**SCs** de seus componentes.  
O campo **B5\_AGLUMRP** deve ser parametrizado no produto filho, para que ao gerar as **OPI**/**SCs** para atender sua necessidade, verifique como devem ser aglutinados os documentos.  
As **OPIs**/**SCs** somente serão aglutinadas se todos os produtos pais no cálculo estiverem com o parâmetro **B5\_FORMMRP** igual a **3-Por Necessidade**, ou, com valor igual a **1-Pelo Programa** e a geração de **OPIs**/**SCs** estiver parametrizada no **MRP** para gerar por necessidade.

* Quando a faixa de datas considerada para aglutinar os documentos não tem início a partir da data da primeira necessidade do componente, e sim, conforme a periodicidade escolhida.  
    
  + Exemplo 1:  
    Data base da execução do **MRP** é 03/05 - Quinta-feira.  
    Componente aglutina os documentos por semana.  
    Necessidades para 03/05- Quinta-feira e 09/05 - Quarta-feira.  
    O primeiro período considerado será 29/04 - Domingo a 05/05 - Sábado.  
    O segundo período considerado será 06/05 - Domingo a 12/05 -Sábado.  
    Sendo assim, essas necessidades não serão aglutinadas, pois estão em semanas diferentes
  + Exemplo 2:  
    Data base da execução do **MRP** é 03/05 - Quinta-feira.  
    Componente aglutina os documentos por quinzena.  
    Necessidades para 08/05 - Terça-feira e 17/05 - Quinta-feira.  
    O primeiro período considerado será até o dia 15/05.  
    O segundo período considerado será do dia 16/05 em diante.  
    Sendo assim, essas necessidades não serão aglutinadas, pois estão em quinzenas diferentes.
* Quando a forma de geração dos documentos e a aglutinação estão parametrizadas em um produto, é importante que os seus componentes também estejam parametrizados corretamente.

  + Exemplo 1:  
    **MATA010 - Produtos:** PA, PI e MP  
    **MATA200 - Estrutura**:  
     PA->PI  
     PI->MP  
    **MATA108:**  
    PA - **B5\_FORMMRP = 3**, **B5\_AGLUMRP = 1**.  
    **Previsões de Venda** para o PA nas datas = 10/05 quantidade 10 e 22/05 quantidade 15.  
    PI  - **B5\_FORMMRP = 3**, **B5\_AGLUMRP = 5**.  
    MP - **B5\_FORMMRP = 1**, **B5\_AGLUMRP = 5**.  
      
    Resultado esperado ao gerar os documentos a partir do **MRP** diário, parametrizado para gerar **OPIs/SCs** **Por OP**:  
    **OP** do produto PA para o dia 10/05 com quantidade 10.  
    **OP** do produto PA para o dia 22/05 com quantidade 15.  
    **OP** do produto PI para o dia 10/05 com quantidade 25.  
    **SC** do produto MP para o dia 10/05 com quantidade 25.

**Importante**  
Valores disponíveis para o campo **B5\_FORMMRP: 1-Pelo Programa**, **2-Por OP**, **3-Por Necessidade**.  
Valores disponíveis para o campo **B5\_AGLUMRP: 1-Pelo Programa**, **2-Diário**, **3-Semanal**, **4-Quinzenal**, **5-Mensal**, **6-Trimestral** e **7-Semestral**.
