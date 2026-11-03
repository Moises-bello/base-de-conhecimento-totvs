---
article_id: 9057928367127
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: 2924a44ee421a09c7d1f97b86398150f9e330bbe8ae5b4f04feb1f5eb906e802
fetched_at: '2026-06-28T22:38:45.353462+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Ponto de Entrada CHGX5FIL
type: support-article
updated_at: '2026-03-24T12:03:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9057928367127-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Ponto-de-Entrada-CHGX5FIL
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33852394537879)Tempo aproximado para leitura: **00:03:00 min**  
  
**Dúvida**  
Exemplo de utilização do Ponto de Entrada **CHGX5FIL - SX5 Compartilhada com Numerações de NF (Tabela 01) Exclusivas**.  
  
**Ambiente**  
Cross Segmentos - Backoffice Protheus - SIGAFAT - A partir da release 12  
  
**Solução**

A finalidade do ponto de entrada **CHGX5FIL** é permitir ao usuário controlar o acesso das numerações da Tabela 01 da SX5 (**SX5 compartilhada com Tabela 01 exclusiva**), ou seja, através do PE é possível filtrar as numerações/séries de notas que serão apresentadas no momento do faturamento conforme a filial, mesmo com a **SX5** compartilhada.  
  
**Exemplo**

```
User Function CHGX5FIL() 

      Local cFilSx5 := cFilAnt  //Filial que será utilizada na filtragem de numerações/séries
      Alert("Passando pelo PE CHGX5FIL") 

Return cFilSx5
```

**Saiba Mais**

[**PE CHGX5FIL SX5 Compartilhada com Numerações de NF (Tabela 01) Exclusivas**](https://tdn.totvs.com/x/79ZGJg)

[**Controle de Numeração do Documento de Saída no Protheus**](https://tdn.totvs.com/pages/viewpage.action?pageId=329024579)  
[**Help A460FLOCK**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/115001427588-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-Faturamento-SIGAFAT-Help-A460FLOCK-ao-selecionar-a-numera%C3%A7%C3%A3o-da-Nota-de-Sa%C3%ADda)
