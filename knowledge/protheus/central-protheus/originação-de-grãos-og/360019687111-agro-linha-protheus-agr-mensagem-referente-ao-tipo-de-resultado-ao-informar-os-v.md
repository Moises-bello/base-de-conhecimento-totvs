---
article_id: 360019687111
category: Originação de Grãos (OG)
content_hash: 29ec89803efa2548a83985cc97cb3cae295022ea64dbd75e604f966119bc569e
fetched_at: '2026-06-28T22:45:41.007499+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Mensagem referente ao tipo de resultado ao informar
  os valores inicial e final
type: support-article
updated_at: '2025-04-10T13:51:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019687111-Agro-Linha-Protheus-AGR-Mensagem-referente-ao-tipo-de-resultado-ao-informar-os-valores-inicial-e-final
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20416112871063)*** Tempo aproximado para leitura:**00:00:40 min****Ocorrência**Na rotina **AGRA035 - Tabela Classificação**, opção **Descontos**, das **Ações Relacionadas,** ao informar o valor **Inicial** nos **Dados** dos **Sub-Itens da Tabela** é exibida a mensagem: **O tipo de resultado é percentual. Por favor, informe um valor até 99,99.**

![VALF.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/7491941880215)

**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Causa**Essa mensagem é exibida porque o campo **Tipo Result** está preenchido com o conteúdo **P -** **Percentual.**   
  
**Solução**Para que seja possível inserir um valor maior e que não seja percentual nos campos **Inicial e** **Final**, é necessário que o campo **Tipo Result** esteja com o conteúdo **F - Faixa.**Para solucionar essa ocorrência, realize os seguintes passos:  
  
**1.** Altere o campo **Tipo Result** e insira o conteúdo **F - Faixa**;  
  
**2.** Preencha os campos **Inicial e Final** com o valor necessário.
