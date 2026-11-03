---
article_id: 38741160434199
category: Escrita Fiscal - Configurador de Tributos
content_hash: f646e70c25386a5651d8fe67cd7c3512f08054e4ddedf32626adbe72996dd170
fetched_at: '2026-06-28T22:39:17.684449+00:00'
product: protheus
section_id: 26791332087191
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Relacionamento entre
  tabelas SD1/SD2, SFT, CJ3 e F2D no Configurador de Tributos
type: support-article
updated_at: '2026-03-02T15:30:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38741160434199-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Relacionamento-entre-tabelas-SD1-SD2-SFT-CJ3-e-F2D-no-Configurador-de-Tributos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38741160421271) Tempo aproximado para leitura: **10:00 min**  
  
**Dúvida**  
Relacionamento entre tabelas **SD1/SD2, SFT, CJ3 e F2D** na utilização do Configurador de Tributos.  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - Todas as versões  
  
**Solução**  
Ao utilizar o **Configurador de Tributos** para cálculo de impostos em documentos de entrada (SD1) ou saída (SD2), é necessário compreender como ocorre a gravação e o relacionamento das informações entre as tabelas:

* SD1 / SD2
* SFT
* CJ3
* F2D

Quando um imposto é calculado pelo **Configurador de Tributos**, o sistema gera um **ID de tributo (IDTRIB)** para identificar a regra aplicada.

### 1. Tabelas SD1 e SD2

Nos itens do documento:

* **SD1 (Itens de NF de Entrada)**

  + Campo: D1\_IDTRIB
* **SD2 (Itens de NF de Saída)**

  + Campo: D2\_IDTRIB

Esses campos armazenam o **ID do tributo gerado no momento do cálculo**.

---

### 2. Tabela SFT (Livro Fiscal)

Na tabela **SFT**, o campo:

* FT\_IDTRIB

Também recebe o mesmo ID do tributo calculado, garantindo rastreabilidade entre item do documento e escrituração fiscal.

---

### 3. Tabela CJ3

A tabela **CJ3** armazena informações detalhadas da geração do tributo.

* Campo: CJ3\_IDTGEN

Este campo grava o mesmo ID gerado no cálculo do tributo (IDTRIB), permitindo o vínculo entre:

* Documento (SD1/SD2)
* Livro Fiscal (SFT)
* Geração do tributo (CJ3)

---

### 4. Tabela F2D

A tabela **F2D** complementa o relacionamento fiscal.

* Campo: F2D\_IDREL

Este campo também recebe o ID do tributo, permitindo relacionar o cálculo com os detalhamentos fiscais vinculados ao documento.

**Documentações relacionadas:**

[CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS – Campos que armazenam as informações dos impostos IBS e CBS.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/35065194117911-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Campos-que-armazenam-as-informa%C3%A7%C3%B5es-dos-impostos-IBS-e-CBS)

[CFGTRIB - Configurador de Tributos - P12](https://tdn.totvs.com/display/public/PROT/CFGTRIB+-+Configurador+de+Tributos+-+P12)
