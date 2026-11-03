---
article_id: 38860356664215
category: Financeiro - Aplicação / Emprestimos
content_hash: 2b2a6baba064925d411db8e19ebb7334369e38d52d3e00b29397e23af20f81ce
fetched_at: '2026-06-28T22:37:59.366741+00:00'
product: protheus
section_id: 1500001550542
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA716 - Como cadastrar
  uma Aplicação tipo template (TEM) com IR tabela progressiva e IOF taxa zero
type: support-article
updated_at: '2026-03-09T19:19:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38860356664215-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA716-Como-cadastrar-uma-Aplica%C3%A7%C3%A3o-tipo-template-TEM-com-IR-tabela-progressiva-e-IOF-taxa-zero
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38860387332759) Tempo aproximado para leitura:  **00:05:00 min**  
  
**Dúvida**  
Como cadastrar uma Aplicação tipo template **(TEM)** com IR tabela progressiva e **IOF** taxa zero?

**Ambiente:**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - A partir da versão 12.1.2210   
  
**Solução**  
Para aplicar o IR tabela progressiva e o IOF taxa zero em uma aplicação do tipo TEM (Template), é necessário primeiro criar um Template com uma fórmula para de cada imposto e vincular esse template à uma Aplicação dentro da rotina Aplicações e Empréstimo, conforme a seguir:

**1.**Acesse a rotina de Aplicações e Empréstimos **(FINA716),**clique em **Templates**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38903167978391)

**2**. Selecione a opção**Incluir.**

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/38860356648727)](https://centraldeatendimento.totvs.com/hc/article_attachments/38860356648727)

**3.**Digite um**código**para o Template, uma**descrição**e em seguida clique em**Adicionar Fórmula.**

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/38860356649111)](https://centraldeatendimento.totvs.com/hc/article_attachments/38860356649111)

**4.** Em fórmulas, coloque uma descrição: exemplo **IR,**selecione o **tipo IR**e coloque a função **Tabela de IR** em seguida clique em**Confirmar.**

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/38860356649495)](https://centraldeatendimento.totvs.com/hc/article_attachments/38860356649495)

**5.** Repita o mesmo processo da etapa 4, selecione o tipo **IOF,** a função **IOF com taxa** e a **Taxa de IOF = 0,00** em seguida clique em**Confirmar.**

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/38860387335191)](https://centraldeatendimento.totvs.com/hc/article_attachments/38860387335191)

**6.** Após template criado, incluir um **Contrato** selecionando a operação **Template** com o código que foi criado, será apresentado uma tela com as configurações do **IR** e **IOF** para serem selecionadas, selecione em seguidaa clique em**Confirmar.**

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/38860387335703)](https://centraldeatendimento.totvs.com/hc/article_attachments/38860387335703)[![](https://centraldeatendimento.totvs.com/hc/article_attachments/38860387337111)](https://centraldeatendimento.totvs.com/hc/article_attachments/38860387337111)

**Saiba mais**

[Cadastro de Templates](https://tdn.totvs.com/display/public/PROT/Cadastro+de+templates+-+FINA716)

[Financeiro - Aplicações e empréstimos - FINA716](https://tdn.totvs.com/pages/releaseview.action?pageId=680254799)
