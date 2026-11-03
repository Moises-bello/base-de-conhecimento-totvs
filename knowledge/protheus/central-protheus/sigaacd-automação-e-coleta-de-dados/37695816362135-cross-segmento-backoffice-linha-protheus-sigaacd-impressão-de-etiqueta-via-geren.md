---
article_id: 37695816362135
category: SIGAACD - Automação e Coleta de Dados
content_hash: 07c83beea1590376a248e89f54b6b622d5bd460740436b875a8516874264eec4
fetched_at: '2026-06-28T22:39:12.749910+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - Impressão de Etiqueta
  via Gerenciador de Impressão.
type: support-article
updated_at: '2026-01-27T19:43:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37695816362135-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Impress%C3%A3o-de-Etiqueta-via-Gerenciador-de-Impress%C3%A3o
---

O artigo explica como configurar impressoras térmicas Zebra no TOTVS Protheus para impressão de etiquetas, destacando o uso da classe FWMSPrinter que elimina a necessidade de mapeamento de portas. A configuração é feita no Local de Impressão (ACDA060), podendo optar por impressão direta ou via MSCBSPOOL. É essencial que o nome da impressora seja igual em todas as estações para funcionamento automático.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37695831782679) Tempo aproximado para leitura: **00:2:00 min**  
  
**Dúvida**  
Como configurar uma impressora térmica?    
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Automação e Coleta de Dados - Todas as versões.  
  
**Solução**

## **01.****VISÃO GERAL**

Antes, para realizar impressão em impressora de linguagem ZPL de conexão USB ou Rede era necessário realizar o mapeamento via [NET USE](https://tdn.totvs.com/pages/viewpage.action?pageId=235596006) para alguma porta, como por exemplo a LPT. Devido a necessidade de facilitar a configuração e impressão das etiquetas, o mecanismo de impressão passa a utilizar a classe [FWMSPrinter](https://tdn.totvs.com/display/public/framework/FWMsPrinter). Agora é possível realizar impressão sem a necessidade de realizar mapeamento de porta. Somente selecionar a impressora instalada no gerenciador de impressão do sistema operacional da **máquina local** no cadastro de Local de Impressão (ACDA060).

Aviso

**Esta funcionalidade foi homologada somente para impressoras ZEBRA.**

## 

## **02.****CADASTRO LOCAL DE IMPRESSÃO**

Para selecionar a impressora no Local de Impressão (ACDA060), deve acessar o menu *Atualizações > ACD > Locais P/Impressão*.

Nesse novo mecanismo de impressão, existem duas possibilidades de impressão: Envio de impressão diretamente para impressora sem a configuração do MSCBSPOOL ou utilizando a configuração de impressão via MSCBSPOOL.

**CONFIGURAÇÃO IMPRESSÃO DIRETA**

**Porta LPT:**0 - Nenhum  
**Tipo:**0 - Local  
**Drv Windows:**1 - Sim  
**Impressora:** Selecione a impressora

**![](https://tdn.totvs.com/download/attachments/731890309/image2023-2-24_11-37-40.png?version=1&modificationDate=1677249461170&api=v2)**

O campo *Impressora*(CB5\_PRINTR) foi criado para realizar a seleção da impressora instalada no gerenciador de impressão da **máquina local**do usuário, sendo ela instalada fisicamente na máquina ou compartilhada, mas para ativar o campo *Impressora*é necessário que o campo *Drv Windows* (CB5\_DRVWIN) esteja igual a 1 - Sim.

Com o campo ativado, para selecionar a impressora, basta clicar no campo e apertar a tecla de atalho do teclado F3 ou clicar na lupa no final do campo. Selecione a impressora e clique em OK após selecionado.

![Lista de Impressoras](https://tdn.totvs.com/download/attachments/731890309/image2023-1-10_8-35-42.png?version=1&modificationDate=1673350542947&api=v2 "Lista de Impressoras")

**CONFIGURAÇÃO IMPRESSÃO VIA MSCBSPOOL**

**Porta LPT:**0 - Nenhum  
**Tipo:**3 - Spool  
**Fila:**Selecione a fila de impressão  
**Drv Windows:**0 - Não

**![](https://tdn.totvs.com/download/attachments/731890309/image2023-2-24_11-40-43.png?version=1&modificationDate=1677249643803&api=v2)**

Após realizado configurações, clicar em Salvar.

## **03.****IMPRESSÃO ETIQUETAS**

**IMPRESSÃO VIA SMARTCLIENT**

A impressão será realizada conforme impressora selecionada no Local de Impressão (ACDA060), o mesmo nome de impressora deverá estar em cada estação/máquina do usuário que queira realizar impressão das etiquetas. Porém, caso o nome da impressora instalada na estação/máquina local esteja divergente ou não esteja instalada, apresentará mensagem abaixo para o usuário.

![](https://tdn.totvs.com/download/attachments/731890309/image2023-1-5_16-10-59.png?version=1&modificationDate=1672945860420&api=v2)

Após clicar em Sim, irá apresentar a impressora ou lista de impressoras instaladas no gerenciador de impressão da **estação/máquina local** para selecionar. Depois de selecionado, clicar em Ok para realizar a impressão.

 **IMPRESSÃO VIA VTDEBUG / TELNET**

Conforme tópico anterior (a.), caso o nome da impressora instalada na estação/máquina local esteja divergente ou não esteja instalada, apresentará mensagem abaixo para o usuário.

![](https://tdn.totvs.com/download/attachments/731890309/image2023-1-5_16-31-24.png?version=1&modificationDate=1672947085403&api=v2)

Após pressionar a tecla S, irá apresentar a impressora ou a lista de impressoras instaladas no gerenciador de impressoras do **servidor do Appserver** para selecionar. Depois de selecionado, apertar a tecla ENTER e a impressão será realizada.

Aviso

A consulta de impressoras utilizando VTDEBUG/TELNET é realizada no gerenciador de impressão do **servidor**onde o **Appserver**está configurado. Utilizando sistemas operacionais **Linux**, para que consiga visualizar as impressoras, realizar configuração conforme documentação: [Seção ServerPrinters -- 29447](https://tdn.totvs.com/pages/viewpage.action?pageId=6064903)

**IMPRESSÃO VIA MSCBSPOOL**

As parametrizações no MSCBSPOOL permanecem as mesmas, porém, na opção PORTA, deverá selecionar a impressora que deseja realizar a impressão e ativar o Drv Windows.

A rotina passa utilizar a mesma classe de impressão **FWMSPrinter**, se estiver utilizando as configurações citadas conforme item 02 tópico B desta documentação.

## 

## **04.****INFORMAÇÕES ADICIONAIS**

Para correto funcionamento dessa funcionalidade de forma automática, o nome da impressora selecionada no Local de Impressão (ACDA060) deverá ser o mesmo em todas estações/máquinas que realizam impressão de etiquetas.

Importante

O pacote que contém alterações de dicionário de dados só estarão disponíveis na próxima Expedição Contínua do Estoque e Custos que está prevista para ser publicada a partir do dia 24/03/2023. Porém, caso queira realizar a criação do campo manualmente, seguir orientações conforme Documento Técnico: [DT Local de impressão](https://tdn.totvs.com/pages/viewpage.action?pageId=731884505)

## **05.****TABELAS UTILIZADAS**

* CB0 - ID de Etiquetas
* CB5 - Tipos de Impressão

**Saiba Mais:**

[*Clique aqui e veja mais artigos sobre SIGAACD - Automação e Coleta de Dados*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550002-SIGAACD-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados)

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Protheus funciona com WebAgent em dispositivo mobile?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/37472298352151-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Protheus-funciona-com-WebAgent-em-dispositivo-mobile)
