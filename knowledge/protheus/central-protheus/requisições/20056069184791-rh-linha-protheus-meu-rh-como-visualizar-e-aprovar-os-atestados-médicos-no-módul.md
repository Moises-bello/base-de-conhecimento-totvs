---
article_id: 20056069184791
category: REQUISIÇÕES
content_hash: 454c3156af5b0be73f87bb0ad8549afc2c6b5862d3c0b44b4e1128698a918e69
fetched_at: '2026-06-28T22:44:37.572399+00:00'
product: protheus
section_id: 10299632459799
source: central-protheus
title: RH - Linha Protheus - Meu RH - Como visualizar e aprovar os Atestados Médicos,
  no módulo 35 - SIGAMDT
type: support-article
updated_at: '2025-11-04T20:54:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20056069184791-RH-Linha-Protheus-Meu-RH-Como-visualizar-e-aprovar-os-Atestados-M%C3%A9dicos-no-m%C3%B3dulo-35-SIGAMDT
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20056082353047) Tempo aproximado para leitura: **00:04:00 min** **Dúvida**Como visualizar e aprovar os Atestados Médicos, no módulo 35 - SIGAMDT  
  
**Ambiente**TOTVS RH (Linha Protheus) - MEU RH - Todas as versões  
  
**Solução**Foi implementada uma Melhoria para que, quando **o funcionário incluir via Meu RH**, uma requisição de **Atestado Médico**, a essa solicitação seja possível aprovar estando logado no **Módulo 35 do Protheus - SIGAMDT.**  
  
Inicialmente, será necessário a criação do parâmetro **MV\_MDTMRH**, conforme documentado [aqui.](https://tdn.totvs.com/pages/viewpage.action?pageId=791841928)  
  
Também é possível a criação manual do parâmetro, para isso, acesse o **Configurador do Protheus** e realize a inclusão do parâmetro **MV\_MDTMRH** conforme os *print* abaixo:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/20056069145879)  
  
Após criação, também via **Configurador**, mas na rotina de **Cadastro > Menus**, é necessário adicionar a **rotina TCFA040 no menu do SIGAMDT.**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/20056069147415)  
  
Ao clicar no menu Medicina, transportar para o quadro do lado direito.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/20056082360471)  
  
Orientação é que seja adicionar como **Novo Item, em Miscelânea > Sistema.**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/20056069154711)  
  
Por fim, salve e gere o menu com o nome **SIGAMDT**.  
  
Ao *logar* novamente no Protheus, **módulo 35, a rotina terá sido inserida no menu.**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/20056082362391)  
  
Agora, bastará acessar essa rotina, e quando houver **Atestados Médicos a serem aprovados pelo RH**, os mesmos serão demonstrados para efetivação.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/20056069157271)  
  
Neste momento, ao aprovar a solicitação, o módulo de MDT irá referenciar dois parâmetros, que obrigatoriamente, precisarão estar ativados.   
  
São eles, **MV\_NGMDTAF e MV\_MDTGPE**.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/20140687990679)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/20140661806871)  
  
Lembrando que, para que essa funcionalidade tenha efeito, **o Protheus precisará estar atualizado** com a **Expedição Contínua do GPE e do MDT**, juntamente com a execução do **UPDDISTR do dicionário diferencial de dados de cada pacote.**   
  
Para ter acesso ao pacote de atualização do GPE, [clique aqui.](https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/RH_EXPEDICAO_CONTINUA)  
Para ter acesso ao pacote de atualização do MDT, [clique aqui.](https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/MDT_EXPEDICAO_CONTINUA)  
  
**Saiba Mais:**  
[**CLIQUE AQUI** para acessar mais artigos e FAQs sobre o MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)  
[**CLIQUE AQUI** para acessar a documentação de referências sobre o MEU RH](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)
