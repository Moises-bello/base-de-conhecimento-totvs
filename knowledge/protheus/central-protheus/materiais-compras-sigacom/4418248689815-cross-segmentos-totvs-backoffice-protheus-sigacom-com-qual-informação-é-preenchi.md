---
article_id: 4418248689815
category: Materiais - Compras (SIGACOM)
content_hash: 65344f81269da735b96533556851dc87f72d40d29262039f55d6c58b7ef63ae3
fetched_at: '2026-06-28T22:41:14.409472+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Com qual informação
  é preenchida a Data de Limite de Compra relatório MATR100?
type: support-article
updated_at: '2026-05-28T13:15:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4418248689815-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Com-qual-informa%C3%A7%C3%A3o-%C3%A9-preenchida-a-Data-de-Limite-de-Compra-relat%C3%B3rio-MATR100
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40794335452055) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**  
  
Com qual informação é preenchida a Data de Limite de Compra relatório MATR100?  
  
**Ambiente**  
  
Cross Segmento - TOTVS Backoffice (Linha Protheus) -  Todas as versões  
  
**Solução**  
No padrão vem preenchido com o Conteúdo do campo Data da Necessidade (C1\_DATPRF) da Solicitação de Compras.

Ou caso no relatório apresente uma informação diferente do conteúdo do campo C1\_DATPRF no campo Limite de Compra do relatório. O sistema verifica se no  Cadastro de Produto estiver preenchido os campos Campo Entrega (B1\_PE) e Tipo Prazo (B1\_TIPE) o sistema faz um Calculo com o conteúdo do  conteúdo do campo Data de Necessidade da Solicitação de compras (C1\_DATPRF) e retorna a quantidade de dias do Campo Entrega (B1\_PE) de acordo com o Tipo de Prazo (B1\_TIPE)  do Cadastro de Produto para preencher no campo Limite de Compra do Relatório.

**Segue um Exemplo Abaixo:**

Aba MRP/Suprimentos de Produto

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4418236372887)

Data da Necessidade Solicitação de Compras

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4418236671639)

Data Limite de Compra no Relatório **Matr100**

**![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4418236769047)**

O prazo de entrega no Cadastro do Produto (B1\_PE) nesse exemplo foi definido com 30 e o Tipo Prazo (B1\_TIPE) = Dias.

A Data da Necessidade da Solicitação de compras 06/01/2022 observe que o sistema retornou 30 dias preenchendo no campo Data de Limite de Compras no relatório MATR100 com 07/12/2021.

***Obs:***

O relatório MATR110, assim como os demais relatórios TReport, se encontram descontinuados:

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Quais relatórios do módulo compras foram descontinuados em 31/10/2024 ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/22742567772183-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Quais-relat%C3%B3rios-do-m%C3%B3dulo-compras-foram-descontinuados-em-31-10-2024)

Assim, caso se necessite verificações em seu funcionamento ou customizações, abaixo segue link para download dos fontes de relatórios TReport padrões de Materiais para essas verificações/customizações:

<https://suporte.totvs.com/portal/p/10098/customer-portal-dashboard/services/downloads?e=1152070>

***Saiba Mais:***

* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
