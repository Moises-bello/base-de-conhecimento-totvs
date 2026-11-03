---
article_id: 9247590555927
category: SIGAEST - LEGAIS
content_hash: c531b83e67076c0b8b7df26796a24c4113e96f9286495fae098851735f89029a
fetched_at: '2026-06-28T22:38:51.823897+00:00'
product: protheus
section_id: 1500001538941
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Sessão UC (Consumo)
  do Mapa SIPROQUIM 2 não gera todos os códigos de utilização ?
type: support-article
updated_at: '2022-09-30T18:31:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9247590555927-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Sess%C3%A3o-UC-Consumo-do-Mapa-SIPROQUIM-2-n%C3%A3o-gera-todos-os-c%C3%B3digos-de-utiliza%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:30 min** **Dúvida**Sessão UC (Consumo) do Mapa SIPROQUIM 2 (MATA950 - MATA913) não gera todos os códigos de utilização ?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.   
  
**Solução**

O manual do SIPROQUIM 2, na sessão UC (referente a Consumo) aborda que no layout existem 5 opções de código de utilização:

![](https://totvssuporte.zendesk.com/attachments/token/KUiIrAieMNnd54mEv3LAHsqLr/?name=image.png)

O Protheus atualmente trata apenas o código de utilização 4 - Consumo para Processo Produtivo, conforme print abaixo:![](https://totvssuporte.zendesk.com/attachments/token/zU8gL14BIRG0WhOeRATUu0cNo/?name=image.png)

[Clique aqui para maiores detalhes da sessão UC](https://tdn.totvs.com/pages/releaseview.action?pageId=506993288)

Isso ocorre pois a tabela SD3 é composta por movimentos de todos os tipos e não temos forma de classifica-los em uma das 4 opções restantes acima, e a possibilidade de realizar um movimento em um dia e um contra movimento em outro já nos impossibilita de compor o saldo correto do consumo, uma vez que esses consumos devem ser discriminados por dia no arquivo texto.

O módulo de Estoque/Custos foi desenvolvido para atender diversas regras de negócio. Porém, as regras de negócio envolvidas na seção UC são muito específicas e hoje, cada empresa tem seu próprio método de controlar esses tipos de movimento dentro do ERP, não sendo possível a implementação de um programa que atenda à todas elas.

Caso tenha a necessidade de geração desses códigos de utilização, temos o Ponto de Entrada **[MAPPFTP](https://tdn.totvs.com/display/public/PROT/Mapas+-+Ponto+de+Entrada+MAPPFTP)** que permite a manipulação das informações conforme necessidade do cliente antes da composição do arquivo. 

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Legais no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538941-SIGAEST-LEGAIS)*
