---
article_id: 40281090217111
category: Anuais
content_hash: 66bf437cb4cc76d544887fb92a7478f9e0c4dd1491f73fdc371486f8ca7c4077
fetched_at: '2026-06-28T22:46:50.943597+00:00'
product: rm
section_id: 1500000861142
source: central-rm
title: RH - RM - FOP - Campo 4 – Rendimentos Isentos e Não Tributáveis
type: support-article
updated_at: '2026-05-06T20:22:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40281090217111-RH-RM-FOP-Campo-4-Rendimentos-Isentos-e-N%C3%A3o-Tribut%C3%A1veis
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40281051050391) Tempo aproximado para leitura: 00**:10:00 min**  
  
**Dúvida**  
Como preencher e configurar as sub-abas do Campo 4 – Rendimentos Isentos e Não Tributáveis no Informe de Rendimentos?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões

**Solução**

O Campo 4 – Rendimentos Isentos e Não Tributáveis do Informe de Rendimentos tem como finalidade consolidar todos os valores pagos ao beneficiário que, conforme a legislação vigente do Imposto de Renda, não sofrem incidência de tributação. Esses rendimentos devem ser inseridos manualmente e separadamente dos rendimentos tributáveis, garantindo a correta apuração das informações prestadas à Receita Federal.

Este campo é estruturado em sub-abas que permitem a segregação dos diferentes tipos de rendimentos isentos, conforme sua natureza.

**Sub-Aba - Prov.Aposentadoria/Reserva/Reforma/Pensão (+ 65 anos):**

Informe os eventos utilizados no ano referentes a proventos de inatividade pagos a beneficiários com mais de 65 anos.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40281090199447)

**Sub-Aba - 13 Prov.Aposentadoria/Reserva/Reforma/Pensão (+ 65 anos):**

Informe os eventos de 13º salário relacionados a proventos de inatividade pagos a beneficiários com mais de 65 anos.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40281051051543)

**Sub-Aba - Diárias/Ajuda de Custo:**

Informe os eventos de diárias e ajuda de custo, configurados com código de cálculo, utilizados no ano e que não são tributáveis.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40281090200471)

**Sub-Aba - Prov.Aposentadoria p/Moléstia/Acidente em Serviço:**

Informe os eventos de proventos de aposentadoria, pensão ou reforma por moléstia grave ou invalidez permanente (não tributáveis).

Leia mais sobre em: [**FOP\_0004\_DIRF - Código de Receita: 3533 (Proventos de Aposentadoria)**](https://tdn.totvs.com/pages/viewpage.action?pageId=209453637)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40281051052951)

***Sub-Aba - Prov.Aposentadoria p/Moléstia/Acidente em Serviço Sobre o 13º salário:***

Informe os eventos de 13º salário relacionados a proventos de aposentadoria, pensão ou reforma por moléstia grave ou invalidez permanente (não tributáveis).

Leia mais em: [**FOP\_0004\_DIRF - Código de Receita: 3533 (Proventos de Aposentadoria)**](https://tdn.totvs.com/pages/viewpage.action?pageId=209453637)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40283400272791)

**Sub-Aba - Lucro/Dividendos pagos por PJ a partir de 1996:**

Informe os eventos referentes à distribuição de lucros ou dividendos pagos a sócios ou acionistas, apurados a partir de 1996.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40281051053335)

**Sub-Aba - Valores pagos ao Titular ou Sócio Microempresa:**

Informe os eventos de valores pagos a titular ou sócio de microempresa ou empresa de pequeno porte, exceto pró-labore e aluguéis.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40281090204567)

**Sub-Aba - Indenização Rescisão Contrato Trabalho / PDV / Ac. Trab.**

Informe os eventos de indenizações rescisórias, PDV ou acidente de trabalho. Considerar eventos com código de cálculo 62 e código de cálculo 99 sem incidência de IRRF.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40281090205207)

**Sub-Aba Outros (especificar)**

Campo 5 / Linha 8 / Outros (especificar): refere-se ao item 8 da Tabela Dinâmica INT41;

O sistema sempre irá gerar, na primeira linha, o evento com **código de cálculo “39 – Abono Pecuniário”,**desde que o funcionário possua esse evento na Ficha Financeira do respectivo ano-base do Informe de Rendimentos. E a partir da da 2a. linha o sistema irá imprimir a descrição do item 8 da Tabela Dinâmica e os eventos relacionados na aba.

Campo 5 / Linha 9 / Outros (especificar): refere-se ao código 9 da Tabela Dinâmica INT41;

Campo 5 / Linha 10 / Outros (especificar): refere-se ao código 10 da Tabela Dinâmica INT41.

Essas descrições devem ser ajustadas conforme a necessidade de cada cliente.

Para realizar a alteração, acesse o menu Administração de Pessoal | Tabelas Dinâmicas, e em seguida, localize a tabela de código**INT41** e ajuste a descrição conforme deseja que a informação seja apresentada no Informe de Rendimentos.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40283400275223)

**Sub-Aba - Bolsa Estudo Médico-Residente**

Informe o evento referente à bolsa paga a médico-residente durante o ano.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40281051057303)

**Saiba Mais**  
[**Campo 4 - Parametrização do menu de emissão da rotina DIRF / Informe de Rendimentos**](https://tdn.totvs.com/pages/releaseview.action?pageId=208347682#Mapeamento-2-4)
