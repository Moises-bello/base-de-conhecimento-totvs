---
article_id: 13941883133591
category: SIGAACD - Automação e Coleta de Dados
content_hash: f60d5f3874a8afe2600895840485130af6ed084e09bcb720d20a61c97bbbfa20
fetched_at: '2026-06-28T22:39:11.301152+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - ACDV150 - Habilitar
  leitura de Código de Barras de Endereço
type: support-article
updated_at: '2026-01-08T16:10:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/13941883133591-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-ACDV150-Habilitar-leitura-de-C%C3%B3digo-de-Barras-de-Endere%C3%A7o
---

Para habilitar a leitura do código de barras no campo de Endereço na Transferência pelo Meu Coletor de Dados (ACDV150), configure o parâmetro MV\_MCDTPBE para .T.. Se não existir, crie-o como Tipo LÓGICO. A leitura de código de barras é válida na rotina ACDV130, mas não na MATA241, que não é destinada para essa função, embora seja possível avaliar customizações via pontos de entrada.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24130523005335) Tempo aproximado para leitura: **00:02:00 min**  
   
**Dúvida**  
Como **habilitar a leitura do Código de barras** no campo de Endereço na Transferência pelo Meu Coletor de Dados (ACDV150)?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões  
  
**Solução**  
Para esse cenário habilitar o parâmetro [**MV\_MCDTPBE**](https://tdn.totvs.com/x/MZSNJw) para **.T..** Caso não tenha esse parâmetro no ambiente, criar como **Tipo LÓGICO**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37533045269911)

Observação: 

**Na rotina de Movimentação Interna(MATA241) é possível realizar leitura de código de barras?**

R: O codigo de barras está válido para uso no ACD (SIGAACD), por meio da rotina ACDV130 (movimentação interna) feita no coletor/emulador de coletor. Nele você bipa o codigo de barras do produto no coletor e ele já reconhece. Agora no MATA241, realmente não, porque não é uma rotina com objetivo de ler codigo de barras como o ACD é. Mas deixo a listagem de pontos de entrada para avaliar internamente se há algum que a partir dele possa criar uma customização que chegue neste comportamento. Veja detalhes no link: [Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA241 - Pontos de Entrada da rotina Movimentação Múltipla](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004558141-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA241-Pontos-de-Entrada-da-rotina-Movimenta%C3%A7%C3%A3o-M%C3%BAltipla)

***Saiba Mais:***

[*Clique aqui e veja mais artigos sobre SIGAACD - Automação e Coleta de Dados*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550002-SIGAACD-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados)

[*Clique aqui e veja o Guia de referência do APP Meu Coletor de Dados*](https://tdn.totvs.com/pages/viewpage.action?pageId=506994322)

[*Habilitar bipagem do endereço na transferência*](https://tdn.totvs.com/pages/viewpage.action?pageId=663589937)
