---
article_id: 33641519524503
category: Gestão de Transportes (TMS)
content_hash: db412c980331e710a09ac01f1a0e6121db0b8a5185b1d80730b8deb00b1866c2
fetched_at: '2026-06-28T22:45:29.436891+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Modais de transportes na emissão do CTe
type: support-article
updated_at: '2025-07-23T19:37:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/33641519524503-Log%C3%ADstica-Linha-Protheus-TMS-Modais-de-transportes-na-emiss%C3%A3o-do-CTe
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33641519510807) Tempo aproximado para leitura: **00:03:00 min**  
  
**Dúvida**  
Quais são os modais de transportes utilizados pelo **TMS** na geração do CTe?  
  
**Ambiente**  
TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**  
A emissão do **CTe** no **Protheus TMS** é homologada apenas para os modais de transportes **01 - Rodoviário** e **06 - Multimodal**.  
  
Os modais **02 - Aéreo, 03 - Aquaviario, 04 - Ferroviário** e **05 - Dutoviário** não foram homologados e não são atendidos no processo padrão de geração do **XML** do **CTe** e na impressão do **DACTE**.  
  
Os clientes que necessitarem utilizar o **TMS** para emitir e imprimir **CTe** nos modais que não foram homologados, devem customizar os **RDMAKES CTESEFAZ3** e **RTMSR35**.  
  
Segue exemplo de caso sobre o uso dos modais de transporte no **Protheus TMS** para exemplificar este posicionamento:  
  
Os grupos de Menus que indicam os modais Aéreo e Fluvial no **TMS**, são utilizados para situações onde há uma transição do modal rodoviário para outro modal. Para conseguir efetuar estes processos operacionais, o **TMS** utiliza os campos com o título de **Tipo de transporte.** Com este campo, é possível classificar em qual fluxo operacional um documento será utilizado para cobrir o transbordo do modal rodoviário até o aeroporto ou porto. Desta forma, ao criarmos viagens, através destes menus mencionados, o Sistema filtrará os documentos corretos.   
  
A seguir temos dois exemplos básicos:  
  
**Exemplo Aéreo** - A Transportadora Transportes MODAIS efetuará um transporte de mercadoria de Arujá - SP até Camaçari - BA. Neste processo ocorrerá um redespacho através do modal aéreo. O processo será iniciado por sua filial de São Paulo - SP que coletará a mercadoria em Arujá - SP para descarregar no aeroporto de Cumbica, Guarulhos - SP. A empresa aérea despachará a mercadoria até o aeroporto de Salvador -BA. A filial de Salvador - BA da Transportes MODAIS vai retirar a mercadoria no aeroporto para entregar no destino final em Camaçari - BA.  
  
**Exemplo Fluvial** - A Transportadora Transportes MODAIS efetuará um transporte de mercadoria de Palmas - TO até Manaus - AM. Neste processo ocorrerá um redespacho através do modal fluvial. O processo será iniciado por sua filial de Palmas - TO que coletará a mercadoria, o reboque será embarcado em uma balsa da empresa NAVIOS em Belém - PA. A NAVIOS despachará a mercadoria até Manaus - AM. A filial de Manaus - AM da Transportes MODAIS vai retirar o reboque na NAVIOS e entregar no destino final.  
  
Como podemos notar nos exemplos apresentados, o **Tipo de transporte** é apenas um controle interno do **TMS** para situações operacionais.  
  
Para baixar os **RDMAKES** citados, clique aqui [**Logística - Linha Protheus - TMS - RDMAKES para o CTe e MDFe**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/24339487959703-Log%C3%ADstica-Linha-Protheus-TMS-RDMAKES-para-o-CTe-e-MDFe)  
  
**Glossário**  
**CTe** - Conhecimento de Transporte Eletrônico;  
**DACTE** - Documento Auxiliar de Conhecimento de Transporte Eletrônico;  
**RDMAKES** - Fontes que podem ser customizados pelo cliente;  
**XML** - Extensible Markup Language.
