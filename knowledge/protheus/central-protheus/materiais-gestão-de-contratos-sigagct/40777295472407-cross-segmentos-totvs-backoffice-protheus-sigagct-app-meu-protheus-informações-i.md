---
article_id: 40777295472407
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: e4d99abab7e1ce6f3a0b08b139767f8807d25d3bf5dfbc562d218267e1e66b0c
fetched_at: '2026-06-28T22:37:21.391138+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - App Meu Protheus -
  Informações incorretas de Clientes/fornecedores nos detalhes da medição App Meu
  Protheus
type: support-article
updated_at: '2026-05-27T18:52:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40777295472407-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-App-Meu-Protheus-Informa%C3%A7%C3%B5es-incorretas-de-Clientes-fornecedores-nos-detalhes-da-medi%C3%A7%C3%A3o-App-Meu-Protheus
---

A correção no app Meu Protheus para documentos de aprovação do tipo Medição permite exibir informações corretas de clientes e fornecedores vinculados, facilitando a análise na aprovação. A atualização está disponível, com o pacote de correção na Central de Downloads, e contido no final deste artigo.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40777256201367) Tempo aproximado para leitura: **00:05:00 min**

**Ocorrência**

Informações incorretas de Clientes/fornecedores nos detalhes da medição app meu protheus

**Ambiente**

Cross Segmentos - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão de Contratos - Todas as versões

**Causa**

Na tela de Listagem e detalhes de um documento de aprovação do tipo Medição (MD e IM), no app Meu Protheus, é exibido somente o primeiro cliente/fornecedor vinculado ao documento, não mostrando as informações corretamente quando as medições possuem mais de um cliente/fornecedor.

**Solução**  
Foi desenvolvida uma nova consulta que, ao abrir um documento de aprovação do tipo Medição no app, busca automaticamente todos os fornecedores e clientes vinculados às planilhas daquele documento e os exibe diretamente na tela de listagem e detalhes. Com isso, o aprovador passa a ter todas as informações necessárias em um único lugar, agilizando a análise e a tomada de decisão.

Para solucionar essa ocorrência, realize os seguintes passos:  
1. Aplique o pacote de correção conforme sua versão para validação em ambiente de teste.

A Release Oficial foi expedida e publicada na Central de Downloads.  
O pacote pode ser acessado no endereço: 12.1.2310:<https://r.totvs.io/p/1247160> ; 12.1.2410:<https://r.totvs.io/p/1247161> ; 12.1.2510:<https://r.totvs.io/p/1247162> ;

Para acessar a documentação da solicitação acesse o link: <https://tdn.totvs.com/pages/viewpage.action?pageId=1060239302>

***Saiba Mais:***

* [Guia de uso - Meu Protheus](https://tdn.totvs.com/x/uTxZEg)
* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [Mais Artigos Materiais - Compras (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001539581-Materiais-Gest%C3%A3o-de-Contratos-SIGAGCT)
