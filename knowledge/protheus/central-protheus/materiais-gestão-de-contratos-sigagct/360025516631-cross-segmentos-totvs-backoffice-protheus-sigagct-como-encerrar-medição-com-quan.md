---
article_id: 360025516631
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: dfc69a383cce83648e9a6d6850de203cb01283653cda937f9cc7ec25dfc32307
fetched_at: '2026-06-28T22:37:19.970468+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Como encerrar medição
  com quantidade zerada sem gerar pedidos ? Parâmetro MV_CNNOPED
type: support-article
updated_at: '2026-02-10T12:46:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025516631-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Como-encerrar-medi%C3%A7%C3%A3o-com-quantidade-zerada-sem-gerar-pedidos-Par%C3%A2metro-MV-CNNOPED
---

**Dúvida**

Como encerrar medição com quantidade zerada sem gerar pedidos ? Parâmetro MV\_CNNOPED  
  
**Ambiente**

Microsiga Protheus – Gestão de contratos  – A partir da versão 12  
  
**Solução**

Esta situação pode acontecer, por exemplo, também quando o valor da multa ou bonificação zere o valor total da medição.

Neste caso, para solucionar essa dúvida, podem ser realizados os seguintes passos:

1. Acesse o módulo Configurador (SIGACFG)  
2. Habilitar o parâmetro MV\_CNNOPED   
3. A medição sendo realizada pela rotina CNTA121 o campo CXN\_ZERO da linha Planilha deverá estar marcado com conteúdo igual a Sim.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8364369943447)

***Obs1:***

***O saldo do cronograma financeiro não é consumido, pois, o valor total da medição ficará zerado,  sendo assim atualizará somente no cronograma o campo "Dt. Realizado".***

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4419858264215)

***Obs2:***

Na utilização da Medição Zerada, o saldo de quantidade do Item da Planilha do Contrato e saldo da Competência do Cronograma Financeiro não são baixados/consumidos e a competência ainda fica disponível para ser utilizada na medição.

Caso se deseje não mais medir a competência em questão pode-se realizar uma Revisão do Contrato para redistribuir e/ou zerar o saldo da Competência alterando o Valor Previsto da competência (lembrando que nos ajustes de valores do Cronograma na Revisão deve-se manter o "Valor Total da Planilha" igual ao valor "Montante do Cronograma" conforme o conceito do módulo).

***Obs3:***

A funcionalidade de "Medição com quantidade Zerada" não é ativa ou tem possibilidade de se utilizada para contratos do Tipo "Flexivel" do artigo abaixo:

[Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Como realizar a inclusão de um Contrato Flexível ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037640253-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Como-realizar-a-inclus%C3%A3o-de-um-Contrato-Flex%C3%ADvel#:~:text=Para%20incluir%20um%20Contrato%20do,seja%2C%20ser%C3%A1%20um%20contrato%20flex%C3%ADvel) ,

nos quais não é possivel por padrão do sistema esta utilização com a alteração do campo "CXN\_ZERO" para "Sim".

***Obs4:***

A funcionalidade de "Medição com quantidade Zerada" no padrão do módulo é contemplada apenas para uso pela rotina de Medição no processo manual (CNTA121).

No uso da rotina de medição automática medição, a rotia não contempla o preenchimento deste campo, e caso se deseje, pode-se avaliar a possibilidade através de uma customização conforme a necessidade.

[Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Quais os Pontos de Entrada da Rotina de Medição Automática - CNTA260 ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008103842-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Quais-os-Pontos-de-Entrada-da-Rotina-de-Medi%C3%A7%C3%A3o-Autom%C3%A1tica-CNTA260)

[Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Pontos de entrada para rotina de Medição](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022685112-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Pontos-de-entrada-para-rotina-de-Medi%C3%A7%C3%A3o)

***Saiba Mais:***

* [DSERSGC-2853 - Não é possível encerrar medição zerada](https://tdn.totvs.com/x/pIkPEw)
* [Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001539581)
