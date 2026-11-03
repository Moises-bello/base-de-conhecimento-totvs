---
article_id: 4942587681047
category: Faturamento - Integrações
content_hash: 8169bfe207f401bed14b52c8c9c47a1a52d34a7158fde0a91ceb1c99fba452c9
fetched_at: '2026-06-28T22:38:26.557010+00:00'
product: protheus
section_id: 1500001539261
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT -Tratamento de
  Integrações EAI após a descontinuação do Mata030
type: support-article
updated_at: '2023-06-16T20:04:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4942587681047-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Tratamento-de-Integra%C3%A7%C3%B5es-EAI-ap%C3%B3s-a-descontinua%C3%A7%C3%A3o-do-Mata030
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15370084846615) Tempo aproximado para leitura: **00:01:30 min** **Dúvida**Com a descontinuidade da rotina mata030, como serão tratadas as integrações por EAI para o cadastro de cliente?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - a partir da 12.1.27.  
  
**Solução**

Mesmo com a descontinuidade do **MATA030** a partir de **04/04/22**, as integrações por EAI ao cadastro de cliente não sofrerão mudanças, inclusive para os pontos de entrada que a integração utiliza.

Hoje, a rotina **CRMA980** que substituirá a **MATA030**, já possui em sua codificação alguns desvios que identificam se é **XML**, usar o **MATI030**, se for **Json**, usar o  **MATI030O**.

Se estiver com o parâmetro **mv\_mvcsa1** habilitado para usar o **CRMA980** , o adapter precisará estar cadastrado para a rotina crma980 e não MATA030.

Se não estiver com o parâmetro habilitado, o sistema fará a transação via **MATA030**, porém, a partir de **04/04/2022**, este fonte ficará obsoleto e não receberá qualquer manutenção ou melhoria.

O sistema somente deixará de usar o parâmetro **mv\_mvcsa1** e já terá a mudança no menu com chamada direta do **CRMA980** a partir do release **12.1.2210**, observando a nova nomenclatura de releases Protheus.  
  
**Saiba Mais**

* **[How To | MP - SIGAFAT - Rotina MATA030 Descontinuada](https://youtu.be/aEY_Xk_wnCg)**
* **[Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Rotina cadastro de cliente (MATA030) descontinuada](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4403853592471-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Rotina-Cadastro-de-Cliente-MATA030-Descontinuada)**
* **[Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Ajuste de ordem de agrupamento de campos customizados após descontinuidade no MATA030](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4834772340759-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Ajuste-de-ordem-de-agrupamento-de-campos-customizados-ap%C3%B3s-descontinuidade-no-MATA030)**
