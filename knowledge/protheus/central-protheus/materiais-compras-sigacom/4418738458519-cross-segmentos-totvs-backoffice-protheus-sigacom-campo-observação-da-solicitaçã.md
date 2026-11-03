---
article_id: 4418738458519
category: Materiais - Compras (SIGACOM)
content_hash: 7de366c3f3e94087614eea3afce4831d547f458420b53d943eb927a183170058
fetched_at: '2026-06-28T22:41:14.314936+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Campo Observação da
  Solicitação de Compras ( C1_OBS ) e C7_OBS do Pedido
type: support-article
updated_at: '2025-11-03T19:39:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4418738458519-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Campo-Observa%C3%A7%C3%A3o-da-Solicita%C3%A7%C3%A3o-de-Compras-C1-OBS-e-C7-OBS-do-Pedido
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36074925486487) Tempo aproximado para leitura: **00:03 min** **Dúvida**

Ao incluir uma **Solicitação de Compras** informando o campo "Observação" esta observação não esta disponível no campo **C7\_OBS**  
  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGACOM - Versão 12  
  
**Solução**

Na versão 12 foi criado o campo **C7\_OBSM** que por ser do tipo "memo" permite um maior número de caracteres digitados. Este é o campo de observação nativo na versão 12 e não é permitido a desmarcação do campo Usado via configurador.  
Porém, por questão de legado o campo **C7\_OBS** permanece ativo e caso não seja necessário a utilização poderá desmarcar a opção Usado no configurador e utilizar o novo campo C7\_OBSM.

![20220111_150010.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4418744874263)

**Obs.**Na tabela de Solicitação de Compras SC1, não temos como alterar o campo C1\_OBS para memo. Se trata de um comportamento padrão do produto.

***Saiba Mais:***

* [Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Relação dos campos Observação ( C7\_OBS e C7\_OBSM ) no relatório MATR110](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028825071)
* [Cross Segmentos Totvs Backoffice Protheus - SIGACOM - Consulta F6 ( Itens de Pedido de Compras ) no Documento de Entrada não apresenta as informações de Observações (C7\_OBS ou C7\_OBSM) do Pedido](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500002146602)
* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
