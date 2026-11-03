---
article_id: 360022631252
category: Materiais - Compras (SIGACOM)
content_hash: f81e3b2e993d7e02b0fe53d2855e6dd2f336bd45e45984cad42f3cc0a0cf6954
fetched_at: '2026-06-28T22:41:21.937652+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: 'Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Notas fiscais com
  valores zerados  '
type: support-article
updated_at: '2022-05-18T21:06:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022631252-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Notas-fiscais-com-valores-zerados
---

**Dúvida**

Como gerar um documento com valor total zerado

**Ambiente**Microsiga Protheus, Compras- à partir da 11.8  
  
   
**Solução**

Para emitir Notas Fiscais com valores zerados e que estejam somente com a descrição, configure o campo **F4\_VLRZERO** com a opção **SIM**.

A emissão das Notas Fiscais requerem a configuração que descrevemos a seguir:

**Cadastro de TES:**

|  |  |
| --- | --- |
| Credita ICMS (**F4\_CREDICM**) | Não |
| Calcula ICMS (**F4\_ICM**) | Não |
| Cod. Fiscal (**F4\_CF**) | Informe o CFOP |
| L.Fisc. ICMS (**F4\_LFICM**) | ICMS Zerado/Outros/Isento.  A escrituração da Nota Fiscal deve ser analisada pelo Departamento Fiscal de sua empresa. |
| Agrega Valor (**F4\_AGREG**) | Não |
| Vlr. Zerado(**F4\_VLRZERO**) | Sim |
| Fórmula (**F4\_FORMULA**) | No menu  **Atualizações/ Cadastros / Fórmulas**, crie uma fórmula com o conteúdo **Texto desejado conforme art. XXXX do RICMS** para ser vinculada ao TES. |

**Parâmetro**:

O parâmetro **MV\_LFAGREG = .T. (*True/* Verdadeiro)** indica se deve ser feita a escrituração, mesmo não agregando valor ao total da nota. Ao habilitá-lo como =**.T. (*True/* Verdadeiro)** as informações são geradas na tabela SF3 (Livros Fiscais).9
