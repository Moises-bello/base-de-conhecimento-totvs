---
article_id: 360044751214
category: MDT - Atendimento Médico
content_hash: 25b37be356d251560ee789e2ba17bc80ba5ac923bcff24ea2c183711f0d778a3
fetched_at: '2026-06-28T22:44:20.541514+00:00'
product: protheus
section_id: 360010945694
source: central-protheus
title: RH - Linha Protheus - MDT - Como  relacionar exames em um Atestado de Saúde
  Ocupacional (ASO)
type: support-article
updated_at: '2025-09-03T12:42:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044751214-RH-Linha-Protheus-MDT-Como-relacionar-exames-em-um-Atestado-de-Sa%C3%BAde-Ocupacional-ASO
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30372382456983)** Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Ao incluir um  Atestado de Saúde Ocupacional **(****ASO)** para uma ficha médica através do **Prontuário Médico** rotina **(MDTA410)**, como realizar o relacionamento de exames?  
É possível relacionar os exames programação de exames no ASO?   
Exames complementares no atestado de saúde ocupacional ASO.  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho – Todas as versões  
  
**Solução**Antes de realizar o processo de relacionamento do exame no ASO, é necessário fazer a configuração do parâmetro **MV\_NGEXREL**.Esse parâmetro identifica se na tela de seleção de exames serão apresentados os exames que já possuem um resultado ou se serão apresentados os exames que estão apenas previstos para o funcionário realizar.  
MV\_NGEXREL = Indica quais exames devem estar habilitados na inclusão de **Atestado(ASO)**. Conteúdo deve ser **1-Apenas exames já realizados** ou **2-Todos os exames previstos**.    
  
Para apresentar todos os exames do funcionário, incluindo os exames que o mesmo ainda não realizou, configure no módulo do Configurador o parâmetro **MV\_NGEXREL** com o conteúdo igual a **2**.

Processo para vincular exames no ASO:

1. Entrar no modulo de **Medicina e Segurança do Trabalho (SIGAMDT).**
2. Em **Atualizações>Atendimento Medico>Prontuário Medico ( rotina MDTA410)**, selecionar a ficha médica desejada  
     
   ![](https://tdn.totvs.com/download/attachments/423932433/image2018-10-17_14-37-26.png?version=1&modificationDate=1539800201140&api=v2)
3. Na aba **ASO's**incluir um Atestado de Saúde Ocupacional.  
     
   ![](https://tdn.totvs.com/download/attachments/423932433/image2018-10-17_14-47-26.png?version=1&modificationDate=1539800201107&api=v2)  
     
   4. No menu lateral desta mesma tela, selecionar a última opção referente a **Relacionamentos**, em seguida escolher a opção **Exames**.  
     
   ![](https://tdn.totvs.com/download/attachments/423932433/image2018-10-17_15-12-49.png?version=1&modificationDate=1539800201037&api=v2)  
     
   5. Na tela de relacionamento de exames, selecionar o tipo de exame a ser associado ao atestado e clicar na opção + **Relac. Exames**.  
     
   ![](https://tdn.totvs.com/download/attachments/423932433/image2018-10-17_15-11-55.png?version=1&modificationDate=1539800201077&api=v2)  
     
   6. Com isso, será apresentada uma tela para selecionar em específico os exames que serão relacionados ao ASO. Em seguida basta salvar a seleção.  
     
   ![](https://tdn.totvs.com/download/attachments/423932433/image2018-10-17_15-13-39.png?version=1&modificationDate=1539800200943&api=v2)  
    **Saiba Mais**  
   [Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)[Artigos Atendimento Médico](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360010945694-MDT-Atendimento-M%C3%A9dico) **[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6961760300311-EC-Assistente-Carolina-Segmentos-Funcionalidades-da-Carolina)**
