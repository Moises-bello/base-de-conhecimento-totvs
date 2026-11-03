---
article_id: 29072459169431
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: f32804129396ff1ebe0eb6a794258ad8a627fbeb969cdba787b6b38e8e8df6d6
fetched_at: '2026-06-28T22:37:22.963779+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Help NORATEIO ao clicar
  em "Vis Rateio" de Títulos Gerados pela Medição do Módulo SIGAGCT
type: support-article
updated_at: '2026-01-14T16:51:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/29072459169431-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Help-NORATEIO-ao-clicar-em-Vis-Rateio-de-T%C3%ADtulos-Gerados-pela-Medi%C3%A7%C3%A3o-do-M%C3%B3dulo-SIGAGCT
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29072459135511) Tempo aproximado para leitura: **00:05:00 min**  
  
**Ocorrência**  
Help "NORATEIO" ao clicar na opção "Vis Rateio" na Rotina FINA050 de Títulos Gerados pelo Módulo Gestão de Contratos.

**Ambiente**  
Cross Segmentos - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão de Contratos - Todas as versões

**Causa**  
O rateio informado no Contrato/Medição é levado somente o para o Pedido de Compras gerado na medição, não é levado para o título quando este é gerado por essa medição.

**Solução**

**P:** O que precisa ser configurado no contrato para que no título do contas a pagar o campo rateio E2\_RATEIO seja preenchido com "Sim" ?  
**R:** Caso queira configurar o rateio para o título, para que possa Visualizar em outras "Ações->Vis Rateio" do Contas a Pagar, siga as orientações da Documentação:

[Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINA050 - Como incluir contas a pagar com rateio externo e visualizá-lo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016073632-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA050-Como-incluir-contas-a-pagar-com-rateio-externo-e-visualiz%C3%A1-lo)

***Obs:***

O Rateio dos títulos gerado pelo GCT segue da mesma forma que o processo de Inclusão manual de Títulos, dessa forma, ao incluir um Título pelo módulo Gestão de contratos o campo **E2\_RATEIO** vai preenchido igual **Não**, será necessário alterar o título gerado ajustar o campo **E2\_RATEIO = Sim** para que possa incluir o Rateio no título.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29072446853143)

É necessário também ter o **Lançamento padrão 511** configurado no Módulo Contabilidade gerencial , para que possa ser gerado a tabela CV4 ,segue exemplo abaixo, configure conforme sua necessidade.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29072446855447)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29072446859543)

Após seguir as orientações acima e incluir o Rateio no título , será gerado a tabela CV4 , dessa forma será possível visualizar o rateio informado no título conforme as orientações do artigo

[Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINA050 - Como incluir contas a pagar com rateio externo e visualizá-lo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016073632-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA050-Como-incluir-contas-a-pagar-com-rateio-externo-e-visualiz%C3%A1-lo)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29072459145751)

***Saiba Mais:***

[Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Centro de Custo e outras Entidades Contábeis não são levadas para o Título gerado pela Medição - CNTA121](https://centraldeatendimento.totvs.com/hc/pt-br/articles/7753942435991-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Centro-de-Custo-e-outras-Entidades-Cont%C3%A1beis-n%C3%A3o-s%C3%A3o-levadas-para-o-T%C3%ADtulo-gerado-pela-Medi%C3%A7%C3%A3o-CNTA121)

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001539581)
