---
article_id: 360023351171
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 7bec5b9e881f1290670bf1d9daf3712556821c118e333de498246ad052b5236c
fetched_at: '2026-06-28T22:38:31.186754+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: MP-FAT-Configuração para Faturamento e a Desoneração da Folha de Pagamento
  - Tabela S033
type: support-article
updated_at: '2021-04-28T15:54:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360023351171-MP-FAT-Configura%C3%A7%C3%A3o-para-Faturamento-e-a-Desonera%C3%A7%C3%A3o-da-Folha-de-Pagamento-Tabela-S033
---

**Dúvida**

Como gerar o registro da S033 para tratamento de desoneração?

**Ambiente**

Microsiga Protheus -  a partir da versão 11.80.  
  
**Solução**

Para Faturamento:

1- Valide os campos **B5\_CODATIV** e **B5\_INSPAT**:  
Somente Produtos que possuem Complemento de Produtos (Tabela **SB5**) com os dois campos preenchidos vão ser considerados na Desoneração da Folha de Pagamento.   
O primeiro campo refere-se ao código de atividade do produto (uma tabela) e o segundo define se o produto recolhe INSS Patronal.

2- Parâmetros **MV\_CFAREC** e **MV\_CFEREC**:  
Quais os CFOPS que devem compor, e quais NÃO devem compor o INSS Patronal.

3- Somente serão consideradas Movimentações sobre com Pedidos gerados como Tipo N com CFOPs iniciados em 5 ou 6 (dentro do Estado e fora do Estado).  
Não são considerados movimentos de Complemento ou Devolução no Faturamento, porém, são consideradas as Devoluções das Nfs emitidas no Faturamento (Devoluções que são registradas como tipo D no Compras - MATA103).

4- Para configurar a vigência, verifique o link abaixo

**[MP - FAT - Desoneração da Folha - Parâmetro MV\_FOLMES V12](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017658492-MP-FAT-Desonera%C3%A7%C3%A3o-da-Folha-Par%C3%A2metro-MV-FOLMES-V12?source=search)**

\* A data que a desoneração considera é a de DIGITAÇÃO da Nf de Entrada em caso de devolução. Não a de Emissão.

Valide também a  documentação técnica de recursos humanos:

- Boletim Técnico da rotina Desoneração da Folha de Pagamento para versão 11 – GPEM013: **<http://tdn.totvs.com/pages/viewpageattachments.action?pageId=6078932&highlight=Desonera%C3%A7%C3%A3o+da+Folha+de+Pagamento.+pdf#Brasil+--+114944-attachment-Desonera%C3%A7%C3%A3o+da+Folha+de+Pagamento.+pdf>**

**SAIBA MAIS:**

**[FAT0116\_Faturamento\_e\_a\_Desoneração\_da\_Folha\_de\_Pagamento\_Tabela\_S033](http://tdn.totvs.com/pages/releaseview.action?pageId=244936287)**

**Obs:****A TOTVS orienta incisivamente que solicite um Consultor TOTVS a fim de implementar e homologar a funcionalidade no ambiente.****O Suporte Help Desk não orienta em implementação da ferramenta.**

**Para os clientes que estão deixando de utilizar a desoneração em folha, antes de alterar o parâmetro MV\_CFAREC, avalie a apuração de PIS/COFINS, pois estes CFOPs deixarão de ser considerados como receita, dispensando a apresentação desses documentos da Apuração de PIS/COFINS.**
