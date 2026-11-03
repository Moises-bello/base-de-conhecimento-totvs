---
article_id: 23675325083287
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: d07440e27d72a9f98e4448d14e1da944218c213f8bb51d90e7ea40489d011b8a
fetched_at: '2026-06-28T22:42:00.985087+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - Por que o registro
  G125 do Sped Fiscal apresenta o ICMS Complementar nos campos 05 e 08, quando não
  há ICMS Próprio na operação?
type: support-article
updated_at: '2024-05-23T12:30:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23675325083287-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Por-que-o-registro-G125-do-Sped-Fiscal-apresenta-o-ICMS-Complementar-nos-campos-05-e-08-quando-n%C3%A3o-h%C3%A1-ICMS-Pr%C3%B3prio-na-opera%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23675325032087) Tempo aproximado para leitura: **00:03:00 min****Ocorrência**Por que os campos **05** e **08** do registro **G125** do **Sped Fiscal**, está apresentando o valor de **ICMS Complementar** quando não há **ICMS Próprio** destacado?

**Ambiente**Cross Segmentos - TOTVS Backoffice (Linha Protheus) -Livros Fiscais – Todas as versões  
  
**Causa**  
Esse incidente ocorre, pois a parametrização do sistema está incorreta para o participante utilizado nesta operação.  
  
**Solução**

Para solucionar esta dúvida, é necessário frisar que somente poderá obter a apropriação do **CIAP** somente do **ICMS Complementar** quando se tratar de um **Fornecedor** optante pelo **Simples Nacional**, sendo assim, configure o campo **F9\_SIMPNAC = 1**.  
  
Caso o campo mencionado esteja diferente disso, o sistema compreenderá que o **ICMS próprio** deve ser acatado e alimentará o campo **05** do **G125** com o conteúdo do **F9\_VALICMS** (este campo soma o **F9\_VALIMP** + **F9\_VALFRET**), acarretando de duplicar o valor de **ICMS Complementar** no **G125**, apresentando tanto no campo **05** (devido estar aglutinado no campo **F9\_VALICMS**) e também no campo **08** do mesmo registro (pois este campo busca do **F9\_VALICCO**).

Ao obter o conteúdo do **F9\_SIMPNAC** = **1** o sistema alimentará apenas o campo **08** deste **G125**, não causando duplicidade de valor para o **Fisco**.

*Print* **SF9**:

![](https://totvssuporte.zendesk.com/attachments/token/opvxzFa9E5L7UF7MuTuQ8Ed0T/?name=image.png)

**Sped Fiscal** quando o campo **F9\_SIMPNAC = 2**:

*Print*:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23675340756119)

**Sped Fiscal** quando o campo **F9\_SIMPNAC = 1**:

*Print:*

![](https://totvssuporte.zendesk.com/attachments/token/ZqcaDzqvgxylaOvVSAweXMK3O/?name=image.png)
