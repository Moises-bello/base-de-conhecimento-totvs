---
article_id: 360016547552
category: Materiais - Compras (SIGACOM)
content_hash: f22a195471bbe24b7d014b5afa42637aaca5c9f1d0b236d6e72c97eb18c02162
fetched_at: '2026-06-28T22:41:25.371779+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Transferências de Aprovação
  de Alçadas para o Superior
type: support-article
updated_at: '2022-03-28T17:55:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016547552-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Transfer%C3%AAncias-de-Aprova%C3%A7%C3%A3o-de-Al%C3%A7adas-para-o-Superior
---

**Dúvida**Como Realizar a transferência de aprovação de Alçadas para Superior?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão de Compras - Todas as versões.  
  
**Solução**Para solucionar essa dúvida, realize os seguintes passos:  
  
1. Acesse o Módulo de Compras - Atualizações - Administração de Compras - Aprovadores (MATA095);  
  
2. Cadastre um novo aprovador que será utilizado como Superior de um outro aprovador;  
  
3. Localize e altere o cadastro do aprovador que necessitará ter suas alçadas aprovadas pelo superior;  
  
4. Preencha o campo Superior (AK\_APROVSUP) com o código do aprovador que cadastrou;  
  
![Capturar.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360012746392/Capturar.PNG)  
  
5. Acesse a rotina Liberação de Dctos (MATA094) disponível em Atualizações - Liberação;  
  
6. Posicione no documento desejado e selecione a opção Outras Ações - Aprovar pelo Superior - Transferir para Superior;  
  
![Capturar.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360012804671/Capturar.PNG)  
  
7. Será exibida uma tela com os dados da alçada;  
  
8. Ao confirmar o documento será transferido para o superior e não ficará mais visível para o aprovador anterior.

![20220328_110631.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/5069951531799/20220328_110631.gif)

**Observação:**

Processo utilizado quando o aprovador já não possuí mais saldo de aprovação e precisa que o documento seja liberado.

***Saiba Mais :***

[MP - SIGACOM - Como Realizar a Aprovação de Alçadas pelo Superior ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016734791)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
