---
article_id: 11337325374871
category: Quírons
content_hash: fe461f75050043b3501607f07fd413caa2abe6f1433b0b4f9c841b27f96d71d3
fetched_at: '2026-06-28T22:42:52.177026+00:00'
product: protheus
section_id: 9033517492119
source: central-protheus
title: RH - Linha Protheus - GPE - Quírons - Como realizar a Carga Inicial para o
  Quírons
type: support-article
updated_at: '2025-04-16T19:47:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11337325374871-RH-Linha-Protheus-GPE-Qu%C3%ADrons-Como-realizar-a-Carga-Inicial-para-o-Qu%C3%ADrons
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31467576636439)Tempo aproximado para leitura: **00:03:00 min**

**Dúvida**Como realizar a **Carga Inicial** de dados do **Protheus para o Quírons?**

**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões

**Solução**  
Para realizar a **Carga Inicial** de dados do **Protheus para o Quírons,** siga os passos abaixo:  
  
**1 -** [Incluir no menu do SIGAGPE a rotina **GPEM925**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/18048749947287-RH-Linha-Protheus-GPE-Qu%C3%ADrons-Como-incluir-no-menu-SIGAGPE-a-rotina-de-Carga-Inicial-para-integra%C3%A7%C3%A3o-com-o-Qu%C3%ADrons)  
**2 -** Acessar a rotina **GPEM925** e preencher os parâmetros conforme necessidade  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31467576637847)  
  
  
**3 -** De acordo com os filtros, ao final do processamento da rotina será gerado um *log* em tela, para que o usuário consiga verificar quais dados geraram registros na tabela **RJP**, para **posterior integração** com o Quirons via [***schedule*** da rotina **GPEM923:**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/18329527763095-RH-Linha-Protheus-GPE-Qu%C3%ADrons-Como-configurar-o-Schedule-para-integra%C3%A7%C3%A3o-Protheus-x-Qu%C3%ADrons)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31467576639127)  
  
  
**4 -** Por fim, ao fechar o *log* em tela, será mostrada uma mensagem ao usuário detalhando a quantidade de registros que foram encontrados:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31467583119383)  
  
  
**5 -** É possível consultar o ***status*** dos registros pela rotina [**Monitor de Integração (GPEM924):**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/11464498386455-RH-Linha-Protheus-GPE-Qu%C3%ADrons-Como-consultar-o-Status-das-integra%C3%A7%C3%B5es-no-Monitor-dentro-do-Protheus)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31467576640791)

**Saiba Mais**  
[Artigos Sobre Quírons](https://tdn.totvs.com/pages/releaseview.action?pageId=529308420)
