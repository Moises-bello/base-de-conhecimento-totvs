---
article_id: 32315939784215
category: Relatórios
content_hash: 848f4bd6e15941400329b0c65758686cfb7d30f309f1c852c489a18ab8a2a4e7
fetched_at: '2026-06-28T22:46:39.202997+00:00'
product: rm
section_id: 1500000861642
source: central-rm
title: RH - RM - PTO - Relatório do Espelho de Ponto Digital via Smart View
type: support-article
updated_at: '2025-05-26T17:09:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/32315939784215-RH-RM-PTO-Relat%C3%B3rio-do-Espelho-de-Ponto-Digital-via-Smart-View
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32315939767063) Tempo aproximado para leitura: 00:02:30 min  
  
Dúvida**Como emitir o relatório Espelho de Ponto Digital via Smart View?

**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Automação de Ponto - A partir da versão 12.1.2406.100 e superiores.

**Solução**

Para gerar o Espelho de Ponto Digital através do Smart View, é necessário seguir os seguintes passos:

**1. Instalação e Configuração**  
Realize a instalação e configuração do Smart View e parametrize a integração com RM, conforme orientações no artigos abaixo:  
[Cross Segmentos - Backoffice RM - BI - Instalação Smart View](https://centraldeatendimento.totvs.com/hc/pt-br/articles/13311540250007)  
  
**2. Importação dos Recursos smart view (relatório)**  
Após concluir a instalação e configuração, será necessário importar o relatório correspondente à sua versão do RM:

* PTOTRP0002 – Para versões a partir da 12.1.2406.100
* PTOTRP0003 – Para versões a partir da 12.1.2410

A importação dos relatórios deve ser realizada através do TOTVS Compartilhamento. Consulte o artigo abaixo para seguir os passos:

[Framework - Linha RM - Frame - TOTVS Compartilhamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/8876331402775)

**3. Geração do Relatório**  
Após a importação, o relatório poderá ser gerado de duas formas:

* Via Smart View Agent
* Pelo menu do RM: **Gestão | Smart View**

Siga os guias específicos abaixo, de acordo com a versão do sistema:

* [Smart View - Espelho de Ponto Digital (12.1.2406.100 e superiores)](https://tdn.totvs.com/display/public/LRM/DT+-+Smart+View+-+Espelho+de+Ponto+Digital#1-1)
* [Smart View - Espelho de Ponto Digital (12.1.2410 e superiores)](https://tdn.totvs.com/pages/releaseview.action?pageId=859589836)

O relatório será gerado no formato padrão conforme as configurações aplicadas. Abaixo segue uma imagem de exemplo:  
  
![negativos_hor.pdf.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/32315939768855)

**Importante**  
O Espelho de Ponto Digital foi atualizado e agora conta com novos campos. Consulte a documentação completa sobre os novos parâmetros disponíveis:

Imprimir Eventos do Movimento do Período

Imprimir Campos Complementares

Imprimir Horas Extra  
  
Acesse:  
[Smart View - Adição dos parâmetros](https://tdn.totvs.com/pages/releaseview.action?pageId=856935871)

**Saiba Mais:**[Relatórios Smart View PTO - Automação de Ponto](https://tdn.totvs.com/pages/releaseview.action?pageId=795914964)  
[TReports agora é Smart View](https://tdn.totvs.com.br/pages/releaseview.action?pageId=774621419)  
[Documentos de Referência Smart View](https://tdn.totvs.com.br/pages/releaseview.action?pageId=632492810)
