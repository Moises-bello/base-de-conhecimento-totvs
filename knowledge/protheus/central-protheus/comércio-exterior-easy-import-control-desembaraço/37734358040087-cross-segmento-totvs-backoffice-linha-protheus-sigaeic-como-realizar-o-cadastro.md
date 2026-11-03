---
article_id: 37734358040087
category: Comércio Exterior - Easy Import Control - Desembaraço
content_hash: b2dc73f1d6067013b84a2c3e8d266b8516715e9903b1e629841b37b4aa8747fe
fetched_at: '2026-06-28T22:39:51.137216+00:00'
product: protheus
section_id: 1500001549442
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAEIC - Como realizar
  o cadastro da Regra de Cálculo do PIS em Documentos Fiscais no Configurador de Tributos
  (FISA170)?
type: support-article
updated_at: '2026-01-19T18:50:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37734358040087-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Como-realizar-o-cadastro-da-Regra-de-C%C3%A1lculo-do-PIS-em-Documentos-Fiscais-no-Configurador-de-Tributos-FISA170
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37734358026519) Tempo aproximado para leitura: **00:04:00 min**  
  
**Dúvida**  
Como realizar o cadastro da Regra de Cálculo do PIS em Documentos Fiscais no Configurador de Tributos (FISA170)?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAEIC - a partir da versão 12.1.2210.  
  
**Solução**

A configuração do Configurador de Tributos para importação tem como objetivo **receber** os valores de impostos já calculados pelo SIGAEIC. O sistema **não** deve recalcular os tributos, mas sim utilizar os **Operandos de Integração** para capturar os valores pronto.

Passos de Configuração Regra de Cálculo do PIS em Documentos Fiscais.

**REGRAS DE CÁLCULO - DOCUMENTOS FISCAIS**

**Acesse:** Regras de Cálculo Documento Fiscal → Regra de Cálculo - Documentos Fiscais

Criar uma regra para cada tributo conforme exemplo abaixo:

**Seção Definição da Regra:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Código Regra** | **Descrição** | **Tributo** | **Data início** | **Data Final** |
| EICPIS | PIS - Importação SIGAEIC | Código do tributo cadastrado para PIS | Data de início da vigência | Deixe em branco |

**Seção Regras de Cálculo:**

|  |  |  |
| --- | --- | --- |
| **Base Cálculo** | **Alíquota** | **Financeira** |
| Código cadastrado para base PIS | PIS - Importação SIGAEIC | Código do tributo cadastrado para PIS |

#### Aba Detalhamento da Fórmula de Cálculo:

1. Clique em **Editar Fórmula**
2. Clique em **Desfazer Tudo** (limpar fórmula padrão)
3. **Tipo da Regra:** 01 - Valores de Origem
4. **Consulta de Regra:** `O:VALOR_INTEGRACAO`
5. Clique em **Adicionar**
6. Clique em **Validar Fórmula**

**Seção Regras de Cálculo:**

|  |  |
| --- | --- |
| **Apuração** | **Escrituração** |
| Informe a apuração | Código cadastrado para regra de escrituração do PIS |

**Seção Definição dos Perfis:**

|  |  |  |  |
| --- | --- | --- | --- |
| **Perf. Ori/Des** | **Perf. Part.** | **Perf. Oper.** | **Perf. Prod.** |
| Selecione origem e destino cadastrado no perfil | Selecione o perfil de participante | **Selecione a operação** | Selecione o perfil de produto |

![2c383b43-4a6e-4e73-beec-b765992d72c6.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/37736789385111)

**Vídeo** ***How to***

|  |
| --- |
|  |

**Saiba mais:**  
[Configurador de Tributos (CFGTRIB) na Importação](https://centraldeatendimento.totvs.com/hc/pt-br/articles/36644911173911-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Configurador-de-Tributos-CFGTRIB-na-Importa%C3%A7%C3%A3o)  
[Guia Prático - Configurador de Tributos na Importação - SIGAEIC](https://tdn.totvs.com/pages/releaseview.action?pageId=1017443678)

**Vídeos:**  
[How To TRADE COMÉRCIO EXTERIOR - Suporte Técnico Protheus](https://tdn.totvs.com/pages/viewpage.action?pageId=766411901)
