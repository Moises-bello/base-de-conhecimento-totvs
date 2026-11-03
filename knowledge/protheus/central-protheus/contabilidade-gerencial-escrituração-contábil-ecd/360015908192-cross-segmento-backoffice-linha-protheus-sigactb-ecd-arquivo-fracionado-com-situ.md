---
article_id: 360015908192
category: Contabilidade Gerencial - Escrituração-Contábil-ECD
content_hash: e76d963c1093a01c16dabd3e2ebbafd6f7702299b5c575b612574bb8eafef561
fetched_at: '2026-06-28T22:40:44.753472+00:00'
product: protheus
section_id: 1500001548702
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - ECD – Arquivo Fracionado
  COM Situação Especial (Extinção,Fusão,Incorporação,Transformação ...)
type: support-article
updated_at: '2022-04-22T13:44:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015908192-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-ECD-Arquivo-Fracionado-COM-Situa%C3%A7%C3%A3o-Especial-Extin%C3%A7%C3%A3o-Fus%C3%A3o-Incorpora%C3%A7%C3%A3o-Transforma%C3%A7%C3%A3o
---

**Ocorrência**

* Como realizar a exportação do ECD para Situação Especial (Extinção,Fusão,Incorporação,Transformação...)
* Como gerar  [Arquivo Fracionado que NÃO seja Situação Especial (Clique Aqui)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047508094-MP-SIGACTB-ECD-Arquivo-Fracionado-que-N%C3%83O-seja-Situa%C3%A7%C3%A3o-Especial-?source=search)

**Ambiente**Cross Segmento - Backoffice Linha Protheus - Contabilidade Gerencial- A partir da versão 12

**Solução**

* Realizar a apuração de resultado (CTBA211) no período da situação especial
* Possuir o Calendário Contábil com o período da situação especial
* Ao gerar a revisão da rotina de escrituração contábil deve ser informada a data da situação especial

**Passos**

**Exemplo : Situação especial 01/01/2017 a 16/09/2017**

**Apuração anual**

* Apuração deve ser executada de 01/01/2017 a 16/09/2017 (período da situação especial)
* Através da rotina de dados contábeis auxiliares (CTBA007) o sistema gera a data da apuração (Tabela CW0)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360007734812/mceclip2.png)

**Apuração Trimestral**

Obs.:caso a apuração for trimestral será  necessário realizar apuração do período da situação especial :  
Ex.:

* 01/01 a 31/03
* 01/04 a 30/06
* 01/07 a 16/09

* Através da rotina de dados contábeis auxiliares (CTBA007) o sistema gera a data da apuração (Tabela CW0)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360008373412/mceclip0.png)

* Cadastro do calendário  deve ser criado com o período da situação especial
* Foi realizado o cadastro  de 01/01 a 16/09 , conforme o período apresentado neste exemplo

**Calendário quando for apuração Anual**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360007735392/mceclip7.png)

**Calendário quando for apuração Trimestral**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360008410311/mceclip0.png)

* Preencher os parâmetros abaixo conforme descreve o manual da receita

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360011617211/mceclip0.png)

* **Apuração Anual** será gerado um único arquivo
* Informar na Data Inicial e Final  o período da Situação especial
* Não Informar "Apuração de Exercício(L/P)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360011617511/mceclip1.png)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360011618252/mceclip2.png)

* **Apuração Trimestral -**  **Layout 1 ao 6** será gerado **4** arquivos separados, apartir do **Layout 7**será gerado 1 Unico arquivo

**Layout 1 ao 6 :**

* Informar na Data Inicial e Final  o período da Situação especial
* Não Informar "Apuração de Exercício(L/P)

**1º Arquivo gerado**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360014288412/mceclip0.png)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360014288492/mceclip1.png)

**2º Arquivo Gerado**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/360014288612/mceclip4.png)**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/360014290871/mceclip2.png)**

**3º arquivo gerado**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/360014288712/mceclip5.png)**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/360014288752/mceclip6.png)**

**A partir do Layout 7**

* Informar na Data Inicial e Final  o período da Situação especial
* Informar "Apuração de Exercício(L/P) 16/09/2017 (última apuração do período)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360028212891/mceclip1.png)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360028213011/mceclip2.png)

Saiba Mais :

[MP - SIGACTB - ECD– Como gerar o arquivo da ECD com Apuração trimestral](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016231592-MP-SIGACTB-ECD-Como-gerar-o-arquivo-da-ECD-com-Apura%C3%A7%C3%A3o-trimestral?source=search)

[MP-SIGACTB: ECD LAYOUT 7 TRIMESTRAL UNIFICADA](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025347591-MP-SIGACTB-ECD-LAYOUT-7-TRIMESTRAL-UNIFICADA-?source=search)

[MP - SIGACTB - ECD 2020 : SITUAÇÃO ESPECIAL OCORRIDA DE MAIO A DEZEMBRO DE 2019](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041914373-MP-SIGACTB-ECD-2020-SITUA%C3%87%C3%83O-ESPECIAL-OCORRIDA-DE-MAIO-A-DEZEMBRO-DE-2019?source=search)

[MP - SIGACTB - ECD 2020 : SITUAÇÃO ESPECIAL OCORRIDA DE JANEIRO A ABRIL 2020](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041440154-MP-SIGACTB-ECD-2020-SITUA%C3%87%C3%83O-ESPECIAL-OCORRIDA-DE-JANEIRO-A-ABRIL-2020?source=search)

[MP - SIGACTB - ECD 2020 : ANTECIPAR A ENTREGA DO ARQUIVO NÃO SE TRATANDO DE UMA SITUAÇÃO ESPECIAL 2019](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041440454-MP-SIGACTB-ECD-2020-ANTECIPAR-A-ENTREGA-DO-ARQUIVO-N%C3%83O-SE-TRATANDO-DE-UMA-SITUA%C3%87%C3%83O-ESPECIAL-2019?source=search)

[MP - SIGACTB : ECD PRÉ-REQUISITOS PARA GERAR](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028834291-MP-SIGACTB-ECD-PR%C3%89-REQUISITOS-PARA-GERAR-?source=search)
