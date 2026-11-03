---
article_id: 8188934752535
category: ADVPL - Classe e Função
content_hash: 77eccfb444f7cd24e87df60e6c167e53f0a1b1b739176a84ed2fa29bed0309bc
fetched_at: '2026-06-28T22:40:17.120408+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Qual função permite
  acessar e editar um grupo de perguntas SX1 Pergunte
type: support-article
updated_at: '2024-03-17T14:36:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8188934752535-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Qual-fun%C3%A7%C3%A3o-permite-acessar-e-editar-um-grupo-de-perguntas-SX1-Pergunte
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**Qual função permite acessar e editar um grupo de perguntas de programa baseando-se no arquivo **SX1**  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – Todas as versões  
  
**Solução**Função **Pergunte()**Esta função permite acessar e editar um grupo de perguntas de programa baseando-se no arquivo **SX1**. Mostra uma tela contendo um lote de parâmetros a serem respondidos ou confirmados pelo usuário.  
  
Inicializa as variáveis de pergunta (**mv\_par??**).  
**Sintaxe:****Pergunte**( **c*****Pergunta** ,* [ ***lPerg*** ] *,* [ ***cTitulo*** ] ) -> lógico  
  
**Parâmetros:**

|  |  |  |  |
| --- | --- | --- | --- |
| **Argumento** | **Obrigat**. | **Tipo** | **Descrição** |
| cPergunta | Sim | C | Pergunta cadastrada no dicionário de dados ( SX1) a ser utilizada. |
| lPerg | Não | L | Indica se exibirá a tela para edição. |
| *cTitulo* | Não | C | Título do diálogo. |

**Descrição:**Esta função inicializa as variáveis de pergunta (**mv\_par01**,...) baseado na pergunta cadastrado no Dicionário de Dados (**SX1**).   
Se o parâmetro **lPerg** não for especificado ou for verdadeiro será exibida a tela para edição da pergunta e se o usuário confirmar as variáveis serão atualizadas e a pergunta no **SX1** também será atualizada.  
  
**Exemplo:**

```
Pergunte("CON010")
```

**Saiba mais**  
**[SX1 - Perguntas do usuário](https://tdn.totvs.com/pages/releaseview.action?pageId=22479548)**  
**[Funções Relacionadas - SX1](https://tdn.totvs.com/pages/releaseview.action?pageId=22479552)  
[Funções auxiliares de Dicionários](https://tdn.totvs.com/pages/releaseview.action?pageId=353290193)**
