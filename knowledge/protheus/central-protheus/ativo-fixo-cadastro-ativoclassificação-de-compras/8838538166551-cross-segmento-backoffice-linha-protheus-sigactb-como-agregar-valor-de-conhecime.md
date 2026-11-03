---
article_id: 8838538166551
category: Ativo Fixo - Cadastro Ativo/Classificação de Compras
content_hash: 82301b94144b5e5316a0ca026cb9af12a96786fa2d91e0b98a593b6d43213591
fetched_at: '2026-06-28T22:41:48.468441+00:00'
product: protheus
section_id: 1500001547662
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - Como Agregar valor de
  conhecimento de frete e NF de garantia estendida em bens do ativo fixo
type: support-article
updated_at: '2023-01-12T12:02:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8838538166551-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-Como-Agregar-valor-de-conhecimento-de-frete-e-NF-de-garantia-estendida-em-bens-do-ativo-fixo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:07:00 min****Dúvida**  
Como Agregar valor de conhecimento de frete e NF de garantia estendida em bens do ativo fixo?

**Ambiente**

Cross Segmento - Backoffice Linha Protheus - Contabilidade Gerencial – **A partir da versão 12.1.33**

**Solução**  
Para solucionar essa dúvida, realize os seguintes passos:

* + Criação do parâmetro **MV\_AGVLATF**para controlar este novo funcionamento.  
    Caso **MV\_AGVLATF = .T.**(default), funcionará o novo comportamento descrito acima.  
    Caso **MV\_AGVLATF = .F.**, funcionará o comportamento do legado, gerando um novo bem ao incluir uma CTE com TES que controla ativo.
  + Para ambos os cenários, a TES deverá estar configurada para controlar ativo (F4\_ATUATF = S).

O parâmetro estará disponível automaticamente a partir do **release 12.1.2310,**porém poderá ser criado manualmente ou através da aplicação da expedição contínua de compras.  
[Pacote de atualização - Compras](https://tdn.totvs.com/pages/viewpage.action?pageId=522011099)

**Criação do Parâmetro:**

**Acessar o Configurador / Dicionário / Base de Dados.**

1. Clicar em **Parâmetros**;
2. Clicar em **Incluir**;  
     
   ![](https://tdn.totvs.com/download/attachments/705454296/image2021-7-30_16-38-52.png?version=1&modificationDate=1661276257860&api=v2)
3. Preencher os campos conforme abaixo:  
     
   ![](https://tdn.totvs.com/download/attachments/705454296/image2022-8-23_14-36-40.png?version=1&modificationDate=1661276257707&api=v2)![](https://tdn.totvs.com/download/attachments/705454296/image2022-8-23_14-36-56.png?version=1&modificationDate=1661276257557&api=v2)  
     

   **Tabela 2:**

   | Campo: | Aba: | Valor: |
   | --- | --- | --- |

   | **Filial:** | Informações | Preencher este campo, caso o controle dos parâmetros seja por Filial |
   | **Nome var:** | Informações | MV\_AGVLATF |
   | **Tipo:** | Informações | 3 - Lógico |
   | **Conteúdo:** | Informações | .T. |
   |  | | |
   | **Descrição: Cont. Descriç Cont. Descriç** | Descrição | Indica se deve ou não agregar valor ao incluir uma CTE vinculada a uma NF de ativo fixo. |

   [Issue origem da melhoria DMANMAT02-38932 ( desenvolvimento Compras)](https://tdn.totvs.com/display/public/PROT/DT+Agrega+valor+de+conhecimento+de+frete+e+NF+de+garantia+estendida+em+bens+do+ativo+fixo)
