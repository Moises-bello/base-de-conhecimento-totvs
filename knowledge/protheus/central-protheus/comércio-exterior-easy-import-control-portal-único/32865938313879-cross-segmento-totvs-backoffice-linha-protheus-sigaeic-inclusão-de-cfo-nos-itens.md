---
article_id: 32865938313879
category: Comércio Exterior - Easy Import Control - Portal Único
content_hash: 40b4a9fae670f8877ae879651143944f17f369ebd66a8a3fc5edac9847a8acc1
fetched_at: '2026-06-28T22:39:40.268750+00:00'
product: protheus
section_id: 27387892471703
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Inclusão de CFO
  nos Itens da DUIMP
type: support-article
updated_at: '2025-06-26T12:46:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/32865938313879-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Inclus%C3%A3o-de-CFO-nos-Itens-da-DUIMP
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32865954095255) Tempo aproximado para leitura: **00:05:00 min**  
**Dúvida**  
Como faço para incluir o CFO nos itens da DUIMP e qual procedimento quando o processo possui muitos itens?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus)  – Easy Import Control – A partir da versão 12.1.2310.  
  
**Solução**  
Nos processos do tipo DUIMP, a rotina de Apropriação de CFO não poderá mais ser utilizada. No entanto, ainda é possível empregar a operação cadastrada na rotina de CFO, desde que se enquadre em um dos dois cenários previstos para sua aplicação:

1) Para cenário que envolva um item ou mais.

Solicitamos que acesse a rotina de Desembaraço e siga o caminho: Menu → Outras Ações → Itens DUIMP. Em seguida, vá até a aba 'Tributação' (parte superior) e depois até a aba 'ICMS' (parte inferior). Informe o número da operação e salve. Este procedimento é aplicável a situações em que somente alguns produtos requerem a operação especificada.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32865954095639)

2) Para um cenário que envolva vários itens.

Caso seja necessário informar para vários produtos, recomendamos criar um registro na rotina de **Regime de Tributação DUIMP (EICTRB100)**. Esse regime define a forma de recolhimento de impostos e contribuições nos âmbitos federal, estadual e municipal.  
Para regulamentar as leis e normas aplicáveis, foi desenvolvido o cadastro de Regime de Tributação DUIMP, que pode ser utilizado nas fases de **Purchase Orde, Embarque/Desembaraço** (para cálculo das previsões de tributação) e **Recebimento de Importação** (para cálculo dos impostos e geração da Nota Fiscal).

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32865954098199)

Se forem muitos itens e para não ter que cadastrar um por um temos um facilitador. É só clicar no menu outras ações e selecionar a opção associar produtos.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32865938298903)

Uma janela de parâmetros será exibida, permitindo o uso de filtros para especificar se o produto é importado, além de definir os intervalos de NCM e Ex-NCM. Após configurar os filtros desejados, clique em 'OK'.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32865954099351)

Os produtos cadastrados serão exibidos. Selecione aqueles desejados para prosseguir com a inclusão da operação:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32865938300311)

Serão exibidos os produtos associados a esta operação.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32865938300439)

Depois acesse a aba ICMS no topo e informe a operação desejada.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32865938300695)

Após concluir este procedimento, salve o cadastro. Se o desembaraço já estiver criado, acesse os itens da DUIMP e informe o código do regime cadastrado. Para isso, vá até a aba **'Tributação'**, localize o campo '**Cód. Regime** (**WV\_CODREG**)' no lado direito da tela e insira o código correspondente. Ao confirmar, a operação será aplicada automaticamente a todos os produtos do NCM em questão.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32865954101015)

Ao acessar a rotina de recebimento de importação nos itens será exibida o cfo para os produtos do ncm em questão.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32865954101527)

**Saiba mais**  
[Regime de Tributação DUIMP](https://tdn.totvs.com/pages/releaseview.action?pageId=723312139)  
[Itens DUIMP](https://tdn.totvs.com/display/public/PROT/Itens+DUIMP)  
[C.F.O](https://tdn.totvs.com/pages/releaseview.action?pageId=306858507)
