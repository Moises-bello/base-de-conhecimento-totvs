---
article_id: 4403082499735
category: RH - Contabilização
content_hash: 87bfbe230b22fa54773e48dbcdf3d1e218ec719be2a785374c6471f4e48ea9b2
fetched_at: '2026-06-28T22:43:46.111495+00:00'
product: protheus
section_id: 360003109092
source: central-protheus
title: RH - Linha Protheus - GPE - Diferenças entre débito e crédito ao Contabilizar
  por matrícula
type: support-article
updated_at: '2025-07-30T02:31:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4403082499735-RH-Linha-Protheus-GPE-Diferen%C3%A7as-entre-d%C3%A9bito-e-cr%C3%A9dito-ao-Contabilizar-por-matr%C3%ADcula
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33811020749847) Tempo aproximado para leitura: **00:01:00 min**

**Ocorrência**Diferenças entre débito e crédito ao Contabilizar por matrícula

**Ambiente:**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as Versões  
  
**Causa:**Esta situação ocorre pois a rotina atingiu o limite máximo de linhas nos lançamentos contábeis de integração vindo de outros módulos. Essa mesma solução pode ser aplicada quando existem diferenças entre os valores de crédito e débito contabilizados por Matricula e Centro de Custo, estando o segundo com um valor maior.  
  
**Solução:**

Para que seja contabilizada todos os lançamentos é necessário ajustar  o conteúdo do parâmetro **MV\_NUMLIN** para a quantidade necessária, por default o conteúdo do mesmo é 999, permitindo inserir 999 linhas na integração com o módulo **Contabilidade Gerencial** - **SIGACTB**.   
  
Acesse a rotina de Parâmetros no **Configurador** - **SIGACFG** -> **Ambiente** -> **Cadastro** -> **Parâmetros > MV\_NUMLIN** e inserir uma nova quantidade. **O limite máximo para o parâmetro é de 35657 linhas.  
  
Saiba Mais**Para adquirir mais conhecimento acesso o(s) *link*(s) abaixo:[MP - SIGACTB - MV\_NUMLIN MV\_NUMMAN](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006753632-MP-SIGACTB-MV-NUMLIN-MV-NUMMAN)
