---
article_id: 4414061138711
category: MDT - PPRA
content_hash: 9f566caf2363b81104e5ce29e5f6c53bf21828fb0477920a49279b621a700198
fetched_at: '2026-06-28T22:44:27.354505+00:00'
product: protheus
section_id: 360010945454
source: central-protheus
title: 'RH - Linha Protheus - MDT - No processo de exclusão de um Risco, retorna a
  mensagem: HELP: NGINTMOD.'
type: support-article
updated_at: '2025-09-05T16:44:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4414061138711-RH-Linha-Protheus-MDT-No-processo-de-exclus%C3%A3o-de-um-Risco-retorna-a-mensagem-HELP-NGINTMOD
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30372541853335) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**No processo de exclusão de um Risco, após entrar na rotina MTDA180 e clicar em **Outras Ações - Excluir**, retorna a mensagem: HELP: NGINTMOD. Problema: Exclusão não permitida. Existe registro em outro arquivo que utiliza esta informação. Solução: Verificar integridade da informação no arquivo citado acima.  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho – Todas as versões  
  
**Causa**Ocorre esta mensagem quando o risco possui relacionamentos com algumas tabelas, como:  Epc x Riscos (TO9); Epi x Riscos (TNX); Exames por Risco (TN2). Então quando tenta realizar a exclusão o sistema informa que aquela informação é utilizada por alguma tabela e não permite continuar o processo.   
  
**Solução**

Para que a exclusão seja efetuada com sucesso, é necessário que o risco não possua relacionamentos com as seguintes tabelas:

* Acidentes de Trabalho (TNC)
* Epc x Riscos (TO9)
* Epi x Riscos (TNX)
* Exames por Risco (TN2)
* Histórico de Avaliações (TGD)
* Laudos x Riscos (TO1)
* Nível Organizacional (TAF)
* Plano de Ação por Risco (TNJ)
* Requisito x Necessidades (TOA)
* Resultado Avaliação (TG6)
* Risco x Medida de Controle (TJF)
* Riscos ASO (TMX)
* Riscos x Produtos Químicos (TJD)
* Riscos da Permissão (TI2)
* Treinamento por Necessidade (TY4)

Para verificar se o risco está relacionado com algumas das tabelas acima poderá entrar na rotina de **Risco** em  **Outras Ações - Relacionamentos** ou no menu **Atualizações - PPRA - Relacionamentos**, após acessar um desses caminhos, verifique na parte inferior em todas as abas se existe alguma informação relacionada, clica no registro e aperte delete.  
  
Conforme GIF abaixo:

![3cBSFZOiud.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4414060410135)

**Saiba Mais**[Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[MDT - PPRA](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360010945454-MDT-PPRA)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6961760300311-EC-Assistente-Carolina-Segmentos-Funcionalidades-da-Carolina)
