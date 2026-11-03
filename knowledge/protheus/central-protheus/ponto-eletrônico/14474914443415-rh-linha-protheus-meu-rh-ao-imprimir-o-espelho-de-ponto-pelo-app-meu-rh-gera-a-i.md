---
article_id: 14474914443415
category: PONTO ELETRÔNICO
content_hash: 4a49d67e2b5318c7d029ba56a0cb9ac7467fc28921b6e394d39baf68bd1d0d34
fetched_at: '2026-06-28T22:44:36.612762+00:00'
product: protheus
section_id: 10299685322391
source: central-protheus
title: RH - Linha Protheus - Meu RH - Ao imprimir o espelho de ponto pelo App Meu
  RH gera a impressão em duplicidade
type: support-article
updated_at: '2026-06-22T18:20:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/14474914443415-RH-Linha-Protheus-Meu-RH-Ao-imprimir-o-espelho-de-ponto-pelo-App-Meu-RH-gera-a-impress%C3%A3o-em-duplicidade
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19283954888343) Tempo aproximado para leitura: **03:00 min** **Dúvida**Ao imprimir o espelho de ponto pelo App Meu RH a impressão gera em duplicidade  
  
**Ambiente**TOTVS RH (Linha Protheus) - Meu RH – todas as versões  
  
**Solução**São três os motivos que esta duplicidade ocorre no espelho de ponto, **tanto via App Meu RH** quanto via **PONR010 no módulo SIGAPON**, conforme enumerado abaixo:  
  
1) O **período de apontamento aberto**, dado pelos parâmetros **MV\_PAPONTA e MV\_PONMES**, está gravado como fechado **na tabela SPO - rotina PONA290**.   
Este processo é incorreto, pois na SPO **só ficarão os períodos já fechados pela rotina de Fechamento**, portanto se o mesmo período aberto pelos parâmetros estiverem na SPO, acesse a rotina de Período de Apontamento, no módulo SIGAPON (PONA290) e, delete o período ainda em aberto que está gravado como fechado;  
  
Para verificação acesse o módulo **16 - SIGAPON**, na rotina **Atualizações > Cadastro de Ponto > Períodos de Apontamento**.  
Nesta primeira tela estão os período efetivamente fechados:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19283954894615)  
  
O período de apontamento aberto, ficará em **Outras Ações > Modificar Período > Apenas Visualizar**  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/19283954898839)**Ou seja, se este período de **01/10/2023 a 31/10/2023 que está aberto**, também estivesse incluído erroneamente na primeira tela, **precisaria ser excluído de lá.**  
  
2) Nos parâmetros deste ambiente, existem **MV\_PAPONTA e MV\_PONMES com filial em branco e filial preenchida**.  
Esse processo é errado, pois somente pode haver preenchimento dos parâmetros **com um conceito de filial**, dependendo do compartilhamento da SPO, ou seja, **se sua SPO for Exclusiva**, SOMENTE poderá haver, **parâmetros MV\_PAPONTA e MV\_PONMES com filial preenchida**. Da mesma forma, se a **SPO for Compartilhada**, somente poderá haver **MV\_PAPONTA e MV\_PONMES com filial em branco**;  
Sobre este ponto, segue uma documentação específica sobre o assunto:  
[RH - Linha Protheus - PON - Orientação sobre como utilizar os parâmetros de Leitura e a tabela SPO, responsável pelo fechamento mensal](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045460153-RH-Linha-Protheus-PON-Orienta%C3%A7%C3%A3o-sobre-como-utilizar-os-par%C3%A2metros-de-Leitura-e-a-tabela-SPO-respons%C3%A1vel-pelo-fechamento-mensal?source=search)  
  
3) Se utilizar o fonte *RDMake* **IMPESP customizado**, por lá haverá uma pergunta que o conteúdo precisará estar com 0, que é a **MV\_PAR15 - Número de Cópias - variável nCopias  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19283954903959)**  
**Saiba Mais**

[**CLIQUE AQUI** para acessar mais artigos e FAQs sobre o MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)  
[**CLIQUE AQUI** para acessar a documentação de referências sobre o MEU RH](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)
