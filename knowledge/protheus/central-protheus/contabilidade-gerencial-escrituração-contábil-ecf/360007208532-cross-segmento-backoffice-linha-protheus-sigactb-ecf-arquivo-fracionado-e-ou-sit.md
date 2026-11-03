---
article_id: 360007208532
category: Contabilidade Gerencial - Escrituração Contábil - ECF
content_hash: 0ccb47c7bbba8ce771b9ff2cf7c09cd27b4fb600589b485406b123c8411df0ef
fetched_at: '2026-06-28T22:40:47.313962+00:00'
product: protheus
section_id: 1500001537721
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - ECF - Arquivo Fracionado
  e ou  Situação Especial (Extinção,Fusão,Incorporação,Transformação ...)
type: support-article
updated_at: '2024-07-31T14:57:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007208532-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-ECF-Arquivo-Fracionado-e-ou-Situa%C3%A7%C3%A3o-Especial-Extin%C3%A7%C3%A3o-Fus%C3%A3o-Incorpora%C3%A7%C3%A3o-Transforma%C3%A7%C3%A3o
---

**Ocorrência**

* Como realizar a exportação do ECF para Situação Especial (Extinção,Fusão,Incorporação,Transformação...)
* Como gerar arquivo fracionado para situações onde a empresa possui DATA DE INICIO em período diferente de 01/01

**Ambiente**  
Cross Segmento - Backoffice Linha Protheus - Contabilidade Gerencial – A partir da versão 12.

**Solução**

* Realizar a apuração de resultado (CTBA211) no período da situação especial
* Possuir o Calendário Contábil com o período da situação especial
* Ao gerar a revisão da rotina de escrituração contábil deve ser informada a data da situação especial

**Passos**

**Exemplo : Situação especial **01/01/2017 a 16/09/2017****

**Apuração anual**

* Apuração deve ser executada de 01/01/2017 a 16/09/2017
* Através da rotina de dados contábeis auxiliares (CTBA007) o sistema gera a data da apuração (Tabela CW0)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360007734812)

**Apuração Trimestral**

Obs.:caso a apuração for trimestral será  necessário realizar apuração do período da situação especial :  
Ex.:

* 01/01 a 31/03
* 01/04 a 30/06
* 01/07 a 16/09

* Através da rotina de dados contábeis auxiliares (CTBA007) o sistema gera a data da apuração (Tabela CW0)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360008373412)

* [Cadastro do calendário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024569414-MP-SIGACTB-ECF-CADASTRO-DE-CALEND%C3%81RIO-CONTABIL?source=search) deve ser criado com o período da situação especial
* Foi realizado o cadastro  de 01/01 a 16/09

**Calendário quando for apuração Anual**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360007735392)

**Calendário quando for apuração Trimestral**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360008410311)

* Preencher o parâmetro abaixo

![001.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360007782051)

* Informar na Data Inicial e Final  o período da Situação especial
* Não Informar "Apuração de Exercício(L/P)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360007734852)

* Verificar manual da receita o preenchimento dos parâmetros abaixo
* **Campo 5- [11) Período de apuração do IPRJ e CSLL (FORMA\_APUR)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4403566448279-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBS001-ECF-Registro-0010-Per%C3%ADodo-de-apura%C3%A7%C3%A3o-do-IRPJ-e-CSLL-?source=search) ?**  
  T- Trimestral  
  A- Anual

  **Campo 6- [12) Qualificação da Pessoa Jurídica (COD\_QUALIF\_PJ) ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4415478314519-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBS001-ECF-Registro-0010-Qualifica%C3%A7%C3%A3o-da-Pessoa-Jur%C3%ADdica-?source=search)**  
  01- PJ em Geral  
  01- PJ componente do Sistema FInar  
  03- Sociedades Seguradoras, de Ca

  **Campo 7- [13) Forma de trib. no Período (FORMA\_TRIB\_PER)?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4415486620695-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBS001-ECF-Registro-0010-Forma-de-trib-no-Per%C3%ADodo-?source=search)**

  **Campo 8- [14) Forma de apura. da Estimativa (MES\_BAL\_RED)?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4415471717655-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBS001-ECF-Registro-0010-Forma-de-apura-da-Estimativa-?source=search)**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360007735992)

Deve se basear no manual da receita para preenchimento dos parâmetros

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4409792533911)
