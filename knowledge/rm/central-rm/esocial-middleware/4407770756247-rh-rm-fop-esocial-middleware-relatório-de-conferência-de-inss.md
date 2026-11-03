---
article_id: 4407770756247
category: eSocial - Middleware
content_hash: 6f3cb4828597919123776d18c3d386bc007b7de20c76cdc7cf42f5eeda0f5850
fetched_at: '2026-06-28T22:47:05.608522+00:00'
product: rm
section_id: 1500000834541
source: central-rm
title: 'RH - RM - FOP - eSocial - Middleware: Relatório de Conferência de INSS'
type: support-article
updated_at: '2025-11-05T11:28:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4407770756247-RH-RM-FOP-eSocial-Middleware-Relat%C3%B3rio-de-Confer%C3%AAncia-de-INSS
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24315636276247)** Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Como configurar e gerar o relatório de conferência de INSS para identificação de divergências entre Folha de Pagamento e Governo  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - A partir dos Patches 12.1.29.299, 12.1.31.218 e 12.1.32.154  
  
**Solução**O relatório de conferência de INSS sofreu alterações ao longo do período para adaptações ao eSocial, passando a buscar, a partir dos patches supracitados, o valor retornado pelo governo na *tag* **vrCpSeg** do evento **S-5001**. Para configuração e geração do relatório, siga os passos abaixo:

**Configuração do Relatório**

1. Realize a configuração do **DefaultDB** nos arquivos **.config** do *Host*. Informações em: [Configurando DefaultDB](https://tdn.totvs.com/display/public/LRM/Configurando+DefaultDB);  
2. Acesse o menu **Configurações | Parametrizador | eSocial | Integração com Middleware**, aba **Outros parâmetros** para [configuração do API e APP](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044519633);  
2.1. **Servidor/Porta API** são o servidor e porta onde o serviço de API's RM está sendo executado (**ApiPort** do Host RM). No caso onde a ApiPort não foi discriminada nas configurações do Host, utilizar a **HttpPort**;  
2.2. **Servidor/Porta APP** são o servidor e porta onde o aplicativo **THF** está sendo executado (**HttpPort** do Host RM);

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4407919197207)

**Geração do Relatório**

1. Para gerar o Relatório, acesse o menu **eSocial | Conferência INSS/FGT**S;  
2. No menu lateral, selecione a opção **Relatório de Conferência (INSS)** e preencha as opções de geração;

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4407922735127)

3. O sistema irá exibir o **Valor INSS e INSS 13º** calculado pela Folha de Pagamento e pela DCTFWeb. Além disso, também exibirá uma lista com os valores detalhados por funcionário;

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4407922751895)

Acesse a página abaixo para visualizar os detalhes sobre cada campo do relatório, como exportar os dados e como acessar o detalhamento dos valores por funcionários:  
     - [Middleware - Relatório de Conferência de INSS](https://tdn.totvs.com/pages/releaseview.action?pageId=536721262)  
  
**Importante**  
Ressaltamos a importância de manter o RM, TAF e TSS sempre atualizados para que inconsistências já corrigidas e novas implementações relacionadas ao Middleware sejam aplicadas no ambiente.  
  
**Saiba mais**  
Para informações sobre a ativação do Middleware e mais detalhes sobre a configuração do relatório, acesse:  
     - [Passos para ativação do Middleware e configuração dos relatórios de conferência](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360056069833)  
     - [Middleware - Mudanças no Relatório de Conferência - INSS](https://tdn.totvs.com/pages/releaseview.action?pageId=639179085)
