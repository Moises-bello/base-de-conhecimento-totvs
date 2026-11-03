---
article_id: 21730388202135
category: ADVPL - Ponto de Entrada
content_hash: 9129c991ecce623cbf69c58e068eceaf1fa7883e9d736b166af71c5c790f6fd2
fetched_at: '2026-06-28T22:40:12.977442+00:00'
product: protheus
section_id: 1500001549122
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL-  Como desabilitar
  customizações no Protheus?
type: support-article
updated_at: '2024-10-24T14:48:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21730388202135-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Como-desabilitar-customiza%C3%A7%C3%B5es-no-Protheus
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21730368293015) Tempo aproximado para leitura: **00:01:30 min****Ocorrência**Como desabilitar customização no Protheus?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - Todas as versões  
  
**Solução**

1° - Pode-se excluir a customização do seu repositório através do VSCode.

![qq.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/21730529721751)

Ou

2º Pode-se desabilitar pela rotina de catálogo de personalização (CFGA030) pelo configurador:

Ambiente -> Cadastros -> Catálogo de personalização.

![CAT.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21730388182551)

Temos uma função de usuário compilada no RPO, para chamar o ponto de entrada AFTERLOG. Devemos selecionar a função que queremos desabilitar e clicar em alterar conforme imagem abaixo.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21730447873687)

Mudamos para opção do campo situação para "desabilitado"

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21730447877399)

Ao executar esse procedimento, na tabela XX7 o campo X7\_STATUS deverá constar igual a 2.

Quando tentar utilizar a rotina, será apresentando mensagem informando que não está compilada no repositório.

![COMP.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21730368294167)

**Saiba Mais**

[Catálogo de personalização](https://tdn.totvs.com/pages/releaseview.action?pageId=382541900)
