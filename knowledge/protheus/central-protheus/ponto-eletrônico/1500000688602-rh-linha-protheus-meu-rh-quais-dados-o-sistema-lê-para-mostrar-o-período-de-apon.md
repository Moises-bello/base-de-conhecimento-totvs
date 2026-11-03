---
article_id: 1500000688602
category: PONTO ELETRÔNICO
content_hash: d477bcd571493dd8dc8195d9263753b84364bcee71ca09ebe154de2aad53e5c0
fetched_at: '2026-06-28T22:44:36.724892+00:00'
product: protheus
section_id: 10299685322391
source: central-protheus
title: RH - Linha Protheus - MEU RH - Quais dados o sistema lê para mostrar o período
  de apontamento no espelho de ponto
type: support-article
updated_at: '2026-06-26T21:29:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500000688602-RH-Linha-Protheus-MEU-RH-Quais-dados-o-sistema-l%C3%AA-para-mostrar-o-per%C3%ADodo-de-apontamento-no-espelho-de-ponto
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19225791444247) Tempo aproximado para leitura: 00:03:00 min**  
  
**Dúvida**  
Quais dados o sistema lê para mostrar o período de apontamento no Meu RH no espelho de ponto?  
  
**Ambiente**  
TOTVS RH (Linha Protheus) - MEU RH - todas as versões  
  
**Solução**  
O sistema sempre irá referenciar o conteúdo de dois parâmetros:  
- **MV\_PAPONTA** (dia inicial/dia final do período de apontamento)   
- **MV\_PONMES** (período de apontamento em aberto)   
  
Os parâmetros poderão ser cadastrados na rotina Períodos de Apontamento (SPO), localizada no modulo SIGAPON no caminho **Atualizações > Cadastro de Ponto > Períodos de apontamentos (PONA290)**, ou então via Configurador SIGACFG, na rotina **Ambiente > Cadastros > Parâmetros**.  
  
Em caso de duvidas na sobre alteração de Períodos de Apontamento consulte:  
[**Como alterar dia inicial e final do período de apontamento da forma correta**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013375112)  
  
Exemplo de conteúdo dos parâmetros:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19225253278615)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19225236871831)  
  
Neste cenário, o período de Ponto aberto é **01/10/2023 a 31/10/2023.**  
  
No App Meu RH, demonstrará da seguinte maneira o períodos:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19225253290647)  
  
**Saiba Mais**  
[**CLIQUE AQUI** para acessar mais artigos e FAQs sobre o MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)  
[**CLIQUE AQUI** para acessar a documentação de referências sobre o MEU RH](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)
