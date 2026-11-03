---
article_id: 4407778030743
category: eSocial - Middleware
content_hash: 2e07981fe1397427fe17ae4e82df63fa4c899ebd08da71e7e80ae4d5b5040d8b
fetched_at: '2026-06-28T22:47:05.602924+00:00'
product: rm
section_id: 1500000834541
source: central-rm
title: 'RH - RM - FOP - eSocial - Middleware: Relatório de Conferência de FGTS'
type: support-article
updated_at: '2024-10-30T19:46:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4407778030743-RH-RM-FOP-eSocial-Middleware-Relat%C3%B3rio-de-Confer%C3%AAncia-de-FGTS
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24341557313943)** Tempo aproximado para leitura:**00:02:00 min****Dúvida**Como configurar e gerar o relatório de conferência de FGTS para identificação de divergências entre Folha de Pagamento e Governo?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial  - A partir da 12.1.28.106   
  
**Solução**Através do relatório de conferência FGTS será possível consultar as **Bases** e **Valores de Depósito de FGTS** presentes em seu sistema de **Folha de Pagamento** e na *tag* **dpsFGTS** do evento **S-5003 - Totalizador FGTS por Trabalhador** retornado pelo governo. Para configuração e geração do relatório, siga os passos abaixo:

**Configuração do Relatório**

1. Realize a configuração do **DefaultDB** nos arquivos **.config** do *Host*. Informações em: [Configurando DefaultDB](https://tdn.totvs.com/display/public/LRM/Configurando+DefaultDB);  
2. Acesse o menu **Configurações | Parametrizador | eSocial | Integração com Middleware**, aba**Outros parâmetros**para [configuração do API e APP](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044519633);  
2.1. **Servidor/Porta API** são o servidor e porta onde o serviço de API's RM está sendo executado (**ApiPort** do Host RM). No caso onde a ApiPort não foi discriminada nas configurações do Host, utilizar a **HttpPort**;  
2.2. **Servidor/Porta APP** são o servidor e porta onde o aplicativo **THF** está sendo executado (**HttpPort** do Host RM);

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24341546492183)

**Geração do Relatório**

1. Para gerar o Relatório, acesse o menu **eSocial | Conferência INSS/FGT**S;  
2. No menu lateral, selecione a opção **Relatório de Conferência (INSS)** e preencha as opções de geração;

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4407945786903)

3. O sistema irá exibir o **Valor Depósito FGTS** calculado pela Folha de Pagamento e pela DCTFWeb. Além disso, também exibirá uma lista com os valores detalhados por funcionário;

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4407940274327)

**Observação**  
Para visualizar os valores de Valor de Depósito de FGTS 13º Salário, Valor de Depósito de FGTS Rescisório, Base de FGTS, Base de FGTS 13º Salário e Base de FGTS Rescisório para cada fonte de informação deverá acessar o detalhamento de mais valores sintéticos:

![Capturar.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/4529579954071)

Acesse a página abaixo para visualizar os detalhes sobre cada campo do relatório e como acessar o detalhamento dos valores por funcionários:  
     - [Middleware - Relatório de Conferência de FGTS](https://tdn.totvs.com/pages/releaseview.action?pageId=536720973)  
  
**Importante**Ressaltamos a importância de manter o RM, TAF e TSS sempre atualizados para que inconsistências já corrigidas e novas implementações relacionadas ao Middleware sejam aplicadas no ambiente.  
  
**Saiba mais**  
Para informações sobre a ativação do Middleware e mais detalhes sobre a configuração do relatório, acesse:  
     - [- Passos para ativação do Middleware e configuração dos relatórios de conferência](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360056069833)
