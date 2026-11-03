---
article_id: 11912715269911
category: 'RH - Verbas '
content_hash: c9a213cd7aceb3d71103752121331313cdf15b69dfb264c81f97cb4b46c8de8e
fetched_at: '2026-06-28T22:43:19.920736+00:00'
product: protheus
section_id: 360010838314
source: central-protheus
title: RH - Linha Protheus - GPE - Como cadastrar os Id's de cálculo relacionados
  aos adicionais de Licença Maternidade por adoção
type: support-article
updated_at: '2025-09-12T17:22:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11912715269911-RH-Linha-Protheus-GPE-Como-cadastrar-os-Id-s-de-c%C3%A1lculo-relacionados-aos-adicionais-de-Licen%C3%A7a-Maternidade-por-ado%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26938292847639) Tempo aproximado para leitura: **00:02:05 min** **Dúvida**Quais os id's de cálculo relacionados aos adicionais de Licença Maternidade por adoção  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12  
  
**Solução**

Para geração de verbas de Base para os Adicionais de Aux. Maternidade de Adoção, devem ser criadas novas verbas com os ID´s abaixo, na rotina Verbas em **Atualizações > Definições de Cálculos > Verbas (GPEA040)**:

| ID | Descrição |
| --- | --- |

| 1906 | ATS Maternidade Adoção |
| 1907 | Insalubridade Maternidade Adoção |
| 1908 | Periculosidade Maternidade Adoção |
| 1909 | Adic. Cargo Confiança Maternidade Adoção |
| 1910 | Adic. Transferência Maternidade Adoção |

**Exemplo para criação de Verbas:**

| Código da Verba | ID p/ Calculo | Tipo do Cód | Tipo Verba |
| --- | --- | --- | --- |

| B01 | 1906 | 3-Base(Provento) | V-Valor |
| B02 | 1907 | 3-Base(Provento) | V-Valor |
| B03 | 1908 | 3-Base(Provento) | V-Valor |
| B04 | 1909 | 3-Base(Provento) | V-Valor |
| B05 | 1910 | 3-Base(Provento) | V-Valor |

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26938314221079)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26938314222487)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26938314224791)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26938314225431)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26938314252311)

**Importante**

-Após cadastro de verbas dos IDs 1906 a 1910, o valor gerado na verba de **ID 0238-Base Aux. Maternidade Adoção** deixará de utilizar o salário/dia incorporado, passando a considerar o **salário/dia base**, para evitar duplicar os valores dos adicionais, caso estes estejam configurados para incorporar ao salário.  
  
-Com relação às **incidências**, não apontamos como os campos da aba de **incidência** e **eSocial** devem ser preenchidos, pois entendemos que este são informações que devem ser informadas mediante interpretação do cliente junto ao seu jurídico/contador.   
  
  
**Saiba Mais**[RH - Verbas](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360010838314-RH-Verbas)  
[RH - Linha Protheus - GPE - Como configurar Licença Maternidade por Adoção](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051079813-RH-Linha-Protheus-GPE-Como-configurar-Licen%C3%A7a-Maternidade-por-Ado%C3%A7%C3%A3o?source=search)  
[DT Separação de adicionais do salário no cálculo da folha quando existe licença maternidade por adoção](https://tdn.totvs.com/pages/viewpage.action?pageId=731898654)
