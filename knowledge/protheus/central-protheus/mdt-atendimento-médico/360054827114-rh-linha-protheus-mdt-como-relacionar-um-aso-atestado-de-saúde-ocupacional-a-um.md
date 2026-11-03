---
article_id: 360054827114
category: MDT - Atendimento Médico
content_hash: f9e9b42e9b1d120dbdd0be4fabf4dd6b940b73e7bb208159e40a373e48a2a2e1
fetched_at: '2026-06-28T22:44:20.391745+00:00'
product: protheus
section_id: 360010945694
source: central-protheus
title: RH - Linha Protheus - MDT - Como relacionar um ASO (atestado de saúde ocupacional)
  a um exame que não possui resultado
type: support-article
updated_at: '2025-07-12T00:43:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360054827114-RH-Linha-Protheus-MDT-Como-relacionar-um-ASO-atestado-de-sa%C3%BAde-ocupacional-a-um-exame-que-n%C3%A3o-possui-resultado
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25844433683095)**Tempo aproximado para leitura: **00:02:00 min****Dúvida**  
Como relacionar um ASO (atestado de saúde ocupacional) a um exame que não possui resultado?  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as versões  
  
**Solução**Existe no protheus o parâmetro **MV\_NGEXREL**, ele indica quais exames devem estar habilitados na inclusão de Atestado(**ASO**), se o parâmetro for definido com **1** (Apenas exames na realizados), e se for **2** (todos os exames previstos). Então para relacionar o **ASO** a um exame sem resultado o parâmetro deve ser definido com 2.

Via de regra ao clicar em Exames será exibido uma tela para relacionar ao **ASO** os exames ocupacionais realizados pelo funcionário. Se o parâmetro **MV\_NGEXREL** for definido como **1**, serão listados **apenas os exames realizados**, ou seja, que possuam o campo **Data Resul.** (TM5\_DTRESU) preenchido, o que libera também a opção de **Visualizar e Resultado.**   
  
Somente aparecerão listados os registros de exame que seguirem as seguintes regras:

1. O exame não pode estar relacionado e nenhum outro registro de ASO;
2. A origem do exame deve ser ocupacional;
3. A natureza do exame deve ser a mesma do ASO;
4. Se o parâmetro MV\_NGEXREL estiver definido como 1, o registro deve ter data de resultado;
5. Se o parâmetro MV\_NGEXREL for 1, também é liberado a visualização do registro de exame e do seu respectivo resultado.

Para alterar o parâmetro acesso o modulo **SIGACFG** no caminho: ambiente > cadastros > parâmetros.  
  
**Saiba Mais**[Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6961760300311-EC-Assistente-Carolina-Segmentos-Funcionalidades-da-Carolina)
