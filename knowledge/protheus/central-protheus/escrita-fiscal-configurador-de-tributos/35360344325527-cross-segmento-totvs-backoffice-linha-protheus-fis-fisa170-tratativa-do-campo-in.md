---
article_id: 35360344325527
category: Escrita Fiscal - Configurador de Tributos
content_hash: fd4ce370034589acd548b7b5a2e98bc0c5f471203a02122868baca7282fa8782
fetched_at: '2026-06-28T22:39:17.542586+00:00'
product: protheus
section_id: 26791332087191
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - FISA170 - Tratativa
  do Campo Incidência da Regra de Escrituração sobre operação de redução
type: support-article
updated_at: '2025-10-03T13:36:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35360344325527-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-FIS-FISA170-Tratativa-do-Campo-Incid%C3%AAncia-da-Regra-de-Escritura%C3%A7%C3%A3o-sobre-opera%C3%A7%C3%A3o-de-redu%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35360349270039) Tempo aproximado para leitura: **00:M03:00 min**  
  
**Dúvida**  
Tratativa do Campo Incidência da Regra de Escrituração sobre operação de redução  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**  
O campo **Incidência** possui a mesma tratativa aplicada ao campo Livro Fiscal do TES.

A Regra de Escrituração é responsável por alimentar corretamente as informações nas tabelas SFT e SF3. Uma vez preenchidas, essas tabelas garantem que os dados sejam levados para a apuração de forma correta.

O campo **Incidência Parcela Reduzida (CJ2\_IREDBS)** define a incidência da parcela reduzida da base de cálculo e possui as seguintes opções:

* **1 = Isento**
* **2 = Outros**

**Atenção:** caso este campo não esteja preenchido em uma operação com redução de base de cálculo, o sistema adotará como padrão gravar a parcela reduzida na coluna **Outros**.

**Exemplo de configuração e gravação em operação com cálculo de ICMS com redução:**

* **Regra de Escrituração**

Incidência: Tributado   
Incidência Parcela Reduzida: em branco/outros (gravará na coluna outros)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35360344283927)

* **Gravação dos Livros Fiscais**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35360349272855)

* **Regra de Escrituração**

Incidência: Tributado   
Incidência Parcela Reduzida: Isento

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35360344285975)

* **Gravação dos Livros Fiscais**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35360349276055)

* **Regra de Escrituração**

Incidência: Tributado e Outros  
Incidência Parcela Reduzida: Isento

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35360349277847)

* **Gravação dos Livros Fiscais**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35360349279639)

* **Regra de Escrituração**

Incidência: Tributado, Isento e Outros  
Incidência Parcela Reduzida: Isento

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35360349280279)

* **Gravação dos Livros Fiscais**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35360344295831)

**Atenção:** veja que na coluna "ICMS ISENTO" quando configurado conforme acima o sistema soma na base o valor da base + valor da parcela reduzida, ou seja, 350,00 + 350,00 = 1000,00
