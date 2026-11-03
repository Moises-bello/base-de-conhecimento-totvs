---
article_id: 10893760874263
category: GESTOR
content_hash: 0c7e7a8d9b39fab317e2518e97f3f42c66261ddb1fb0d78a45de211d56cac1ad
fetched_at: '2026-06-28T22:44:35.523296+00:00'
product: protheus
section_id: 10299702833303
source: central-protheus
title: RH - Linha Protheus - MEU RH - Como fazer para solicitação feita por um Gestor
  em nome de um subordinado ir direto para aprovação do RH.
type: support-article
updated_at: '2026-06-16T19:00:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10893760874263-RH-Linha-Protheus-MEU-RH-Como-fazer-para-solicita%C3%A7%C3%A3o-feita-por-um-Gestor-em-nome-de-um-subordinado-ir-direto-para-aprova%C3%A7%C3%A3o-do-RH
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30646215945623) Tempo aproximado para leitura: **00:03:00 min**  
  
**Ocorrência**  
Como fazer a solicitação feita de um Gestor para um subordinado ir direto para aprovação do RH?  
  
**Ambiente**  
TOTVS RH (Linha Protheus) - Meu RH – todas as versões  
  
**Causa**  
Solicitação feita por um gestor esta indo para aprovação do nível superior  
  
**Solução**  
Para evitar divergências entre o fluxo de aprovação de solicitações que são feitas de um gestor, foi implementada uma melhoria que permite que as solicitações de Férias, Abono e Ponto, sejam enviadas diretamente para aprovação do RH, desde que elas tenham sido incluídas por meio de um gestor para um subordinado.  
  
Essa melhoria está sendo disponibilizada por meio do novo parâmetro **MV\_SUPTORH**. Quando este parâmetro estiver definido com valor verdadeiro (.T.), as solicitações de Férias, Abono e Ponto feitas de um gestor para um subordinado serão enviadas diretamente para aprovação do RH.  
  
Abaixo os dados do novo parâmetro:

| Campo | Conteúdo |
| --- | --- |
| Nome da variável (X6\_VAR): | MV\_SUPTORH |
| Tipo (X6\_TIPO): | L - (Lógico) |
| Descrição (X6\_DESCRIC): | Indica que as solicitações de Férias, Ponto e |
| Descrição 1 (X6\_DESC1): | Abono, quando incluídas no Meu RH de um gestor |
| Descrição 2 (X6\_DESC2): | para um subordinado, irão direto para o RH. |
| Valor Padrão (X6\_CONTEUD): | .F. |

O novo parâmetro estará disponível à partir da versão **12.1.2210**, contudo, pode-se criá-lo manualmente, conforme a necessidade.  
  
Após a criação deste parâmetro é necessário reiniciar os serviços do **MEU RH**.  
[**Documento Oficial Produto, sobre a melhoria.**](https://tdn.totvs.com/pages/viewpage.action?pageId=702820807)  
  
**Saiba Mais**  
[**RH - Linha Protheus - MEU RH - Aprenda sobre o MEU RH e como fazer a implantação**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036164214)  
[**CLIQUE AQUI para acessar mais artigos e FAQs sobre o MEU RH**](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)  
[**CLIQUE AQUI para acessar a documentação de referência sobre o MEU RH**](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)
