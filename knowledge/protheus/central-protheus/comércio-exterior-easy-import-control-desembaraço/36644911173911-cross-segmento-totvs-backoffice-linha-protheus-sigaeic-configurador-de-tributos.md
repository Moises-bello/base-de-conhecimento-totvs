---
article_id: 36644911173911
category: Comércio Exterior - Easy Import Control - Desembaraço
content_hash: 2d56ce2242f68e888846b7eeed641ef3f8b8da0433add4a90ea9d756b1244f85
fetched_at: '2026-06-28T22:39:51.266804+00:00'
product: protheus
section_id: 1500001549442
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAEIC - Configurador
  de Tributos (CFGTRIB) na Importação
type: support-article
updated_at: '2026-01-09T18:29:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36644911173911-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Configurador-de-Tributos-CFGTRIB-na-Importa%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36644943412631) Tempo aproximado para leitura: **00:04:00 min**  
  
**Dúvida**

Como configurar o Configurador de Tributos (CFGTRIB) para processar os valores de impostos (II, IPI, ICMS, PIS, COFINS, CBS e IBS) já calculados pelo módulo SIGAEIC em operações de importação?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAEIC - a partir da versão 12.1.2210

**Solução**

A configuração do Configurador de Tributos para importação tem como objetivo **receber** os valores de impostos já calculados pelo SIGAEIC. O sistema **não** deve recalcular os tributos, mas sim utilizar os **Operandos de Integração** para capturar os valores prontos.

A configuração contempla os tributos II, IPI, ICMS, PIS, COFINS, CBS e IBS.

Passos de Configuração

**ETAPA 1: Cadastro dos Tributos**

Acesse: Regras Fiscais → Cadastros → Tributo.

Cadastre os tributos de importação com o ID TOTVS apropriado:

| **Campo** | **IPI** | **ICMS** | **PIS** | **COFINS** | **CBS** | **IBS ESTADUAL** | **IBS MUNICIPAL** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Tributo** | EICIPI | EICICM | EICPIS | EICCOF | CBSFED | IBSEST | IBSMUN |
| **Esfera** | 1-Federal | 2-Estadual | 1-Federal | 1-Federal | 1-Federal | 2-Estadual | 1-Municipal |
| **ID Tributo (ID TOTVS)** | 000022 | 000021 | 000015 | 000016 | 000062 | 000060 | 000061 |

> **Nota:** Todas as informações de "CÓDIGO" têm caráter sugestivo. O usuário deve avaliar e definir a codificação mais adequada.

**ETAPA 2: Cadastro de Perfis**

1. **Perfil de Produto:**

   * Acesse: Perfis → Perfil de Produto.
   * Na aba **Origens dos Produtos**, inclua a origem `1 - ESTR. (IMPORTAÇÃO DIRETA)`.
2. **Perfil de Operação:**

   * Acesse: Perfis → Perfil de Operação.
   * Verifique qual tipo de operação será utilizado em seu processo.
3. **Perfil de Participante:**

   * Acesse: Perfis → Perfil Participante.
   * Na aba **Participantes**, utilize o **Tipo** `1 - Fornecedor / Cliente` e inclua os fornecedores de importação.
4. **Perfil de Origem/Destino:**

   * Acesse: Cadastros → Perfil Tributário de Origem e Destino.
   * Na aba **UF's Origem/Destino**, defina a **UF Origem** como `EX (Exterior)`  e especifique as **UFs Destino**.

**ETAPA 3: Regras de Base de Cálculo**

Acesse: Regras de Cálculo Documento Fiscal → Regra de Base de Cálculo.

Na **Aba Detalhamento da Fórmula de Cálculo**:

* Defina o **Valor Origem** como `11 - Fórmula Manual`.
* Clique em **Editar Fórmula**.
* **Tipo da Regra**: `01 - Valores de Origem`.
* **Consulta de Regra**: Utilize o Operando de Integração `O:BASE_INTEGRACAO`.
* Repita para todos os tributos.

**ETAPA 4: Regras de Alíquota**

Acesse: Regras de Cálculo Documento Fiscal → Regra de Alíquota.

Na **Aba Detalhamento da Fórmula de Cálculo**:

* Defina o **Valor Origem** como `06 - Fórmula Manual`.
* Clique em **Editar Fórmula**.
* **Tipo da Regra**: `01 - Valores de Origem`.
* **Consulta de Regra**: Utilize o Operando de Integração `O:ALIQUOTA_INTEGRACAO`.
* Repita para todos os tributos.

**ETAPA 5: Regras de Escrituração**

Acesse: Regras de Cálculo Documento Fiscal → Regra de Escrituração.

Na **Seção Incidência**:

* **Incidência**: Defina como `8 - Integração`. **Este campo é essencial para a integração**.
* **Total da Nota**: Sem ação.
* **Tabela CST**: Selecione o CST apropriado para o tributo.

| **Tributo** | **CST Sugerido** | **Observação** |
| --- | --- | --- |
| **IPI** | 00, 49, 50 | Conforme operação |
| **ICMS** | 00, 10, 20 | Conforme operação |
| **PIS/COFINS** | 01, 02 | Conforme operação |
| **CBS / IBS** | A definir | Aguardar legislação |

**ETAPA 6: Regras de Cálculo - Documentos Fiscais**

Acesse: Regras de Cálculo Documento Fiscal → Regra de Cálculo - Documentos Fiscais.

**Seção Regras de Cálculo:**

* **Base Cálculo**: Código cadastrado na ETAPA 3.
* **Alíquota**: Código cadastrado na ETAPA 4.
* **Financeira**: Deixe em branco (não gera título).

**Aba Detalhamento da Fórmula de Cálculo:**

1. Clique em **Editar Fórmula**.
2. Clique em **Desfazer Tudo** (para limpar a fórmula padrão).
3. **Tipo da Regra**: `01 - Valores de Origem`.
4. **Consulta de Regra**: Utilize o Operando de Integração `O:VALOR_INTEGRACAO`.

**Seção Definição dos Perfis:**

* Preencha os campos Perf. Ori/Des, Perf. Part., Perf. Oper.  e Perf. Prod.  com os perfis criados na ETAPA 2.

**Teste da Configuração**

1. No SIGAEIC, gere uma pré-nota de importação.
2. Acesse **Documento de Entrada (MATA103)** e classifique a pré-nota, informando a TES.
3. Os tributos configurados devem aparecer automaticamente com os valores já calculados.

**Verificações:**

* Os valores devem ser idênticos aos calculados pelo SIGAEIC.
* **Não** deve haver recálculo dos tributos.
* Para conferência de II, IPI, ICMS, PIS e COFINS, verifique na aba **Impostos**.
* Para conferência de CBS e IBS, verifique na aba **Tributos Genéricos**.

**Saiba Mais**  
[CFGTRIB - Configurador de Tributos - Linha Microsiga Protheus - TDN](https://www.google.com/search?q=https://tdn.totvs.com.br/display/public/PROT/CFGTRIB%2B-%2BConfigurador%2Bde%2BTributos)

[CFGTRIB - Operandos de Integração - Linha Microsiga Protheus - TDN](https://www.google.com/search?q=https://tdn.totvs.com/pages/releaseview.action%3FpageId%3D932351237)

[CFGTRIB - Regras Escrituração - Linha Microsiga Protheus - TDN](https://www.google.com/search?q=https://tdn.totvs.com/display/public/PROT/CFGTRIB%2B-%2BConfigurador%2Bde%2BTributos%23CFGTRIBConfiguradordeTributos-CadastrodeRegradeEscritura%25C3%25A7%25C3%25A3o)

[FAQ - Reforma Tributária - Comércio Exterior - Linha Microsiga Protheus - TDN](https://www.google.com/search?q=https://tdn.totvs.com/pages/releaseview.action%3FpageId%3D941240555%23FAQ-4)
