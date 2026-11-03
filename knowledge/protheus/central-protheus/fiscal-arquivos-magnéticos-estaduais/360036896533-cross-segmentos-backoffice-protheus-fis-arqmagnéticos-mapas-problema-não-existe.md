---
article_id: 360036896533
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: 61e4d8fb215cc095d85cb50a451a37052a3d66b5793cddbc5c0da3b75c11bb3e
fetched_at: '2026-06-28T22:42:11.786433+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - MAPAS - Problema:
  Não existe informações para esta consulta'
type: support-article
updated_at: '2022-08-18T14:01:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036896533-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-MAPAS-Problema-N%C3%A3o-existe-informa%C3%A7%C3%B5es-para-esta-consulta
---

**Ocorrência**Ao acessar a rotina Instruções Normativas (MATA950) para gerar o arquivo magnéticos MAPAS é apresentada a mensagem abaixo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360047570294/mceclip0.png)  
  
  
**Ambiente**  
Protheus – Livros Fiscais – A partir da versão 11.80  
  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
  
1. Realize a criação do **Grupo de Perguntas MAPASV2:**

* No *menu* do módulo **Configurador**, acesse: Base de Dados > Dicionário > Bases de Dados

![](https://tdn.totvs.com/download/attachments/506790632/configinic1.gif?version=1&modificationDate=1565637146460&api=v2)

* À esquerda, clique em *Perguntas*e em seguida clique em *Incluir*

*![](https://tdn.totvs.com/download/attachments/506790632/configinic8.gif?version=1&modificationDate=1565637135007&api=v2)*

* Nomeie o novo Grupo como **MAPASV2**e preencha a tabela de perguntas como se segue:

| Ordem | Pergunta | Tipo | Tamanho | Consulta Padrão |
| --- | --- | --- | --- | --- |
| 1 | Do Grupo ? | Caracter | 4 | SBM - Grupo de Produtos |
| 2 | Até o Grupo ? | Caracter | 4 | SBM - Grupo de Produtos |
| 3 | Do Produto ? | Caracter | 15 | SB1 - Produtos |
| 4 | Até o Produto ? | Caracter | 15 | SB1 - Produtos |

**Observação**: O tamanho das perguntas 1 e 2 devem ser iguais ao tamanho do campo **BM\_GRUPO**da tabela de *Grupos de Produtos* (**SBM**), assim como o tamanho das perguntas 3 e 4 devem ser iguais ao tamanho do campo **B1\_COD** da tabela de *Produtos* (**SB1**).

* Clique em *Confirmar*para salvar as alterações.

Para mais informações consulte o link abaixo:  
<https://tdn.totvs.com/pages/releaseview.action?pageId=506790632>
