---
article_id: 17710383461399
category: Assinatura Eletrônica
content_hash: d6d31053814d9c73a6d62a1290aaa8b9e82aceba35c7a1b906163768da801dd1
fetched_at: '2026-06-28T22:46:44.115091+00:00'
product: rm
section_id: 4403549405207
source: central-rm
title: 'RH - RM - FOP - TOTVS Assinatura Eletrônica: Como integrar relatórios de Recibo
  de Férias?'
type: support-article
updated_at: '2024-06-12T21:03:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/17710383461399-RH-RM-FOP-TOTVS-Assinatura-Eletr%C3%B4nica-Como-integrar-relat%C3%B3rios-de-Recibo-de-F%C3%A9rias
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17710380037143) Tempo aproximado para leitura: **00:04:14 min****Dúvida** Como gerar e integrar relatórios de Recibo de Férias para assinatura no TOTVS Assinatura Eletrônica?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**

**1. Parametrização do Grupo de Relatórios:**

Para a geração/integração dos relatórios do tipo **Recibo de Férias**, deverá cadastrar um Grupo de Relatórios utilizando o tipo de relatório **Recibo de Férias**, cadastre conforme o passo a passo descrito na documentação: [RH - RM - FOP - Assinatura Eletrônica: Tipos de relatório](https://centraldeatendimento.totvs.com/hc/pt-br/articles/9686996012183).

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17709764521623)

Durante a parametrização do Grupo de Relatórios, atente-se para a seção **Opções de envio do aviso de férias**:

* **Enviar no dia do aviso de férias (antecipa para primeiro dia útil se não for dia útil):** Ao marcar essa opção o sistema somente integrará os avisos de férias com data de aviso na data da execução do processo ou a data de pagamento no dia da execução do processo.
* **Enviar com X dias de antecedência:**Essa opção permite o envio do documento a X dias do seu início (data do aviso ou data de pagamento).
* **Não validar essa regra:**Não serão validadas datas utilizando umas das regras anteriores, para a geração **será necessário incluir a data conforme o tipo do relatório**, na primeira tela do processo de integração de relatórios, dentre as regras, essa será a mais flexível e dentre todas **recomendamos**a sua utilização.

Os relatórios utilizados neste tipo de relatórios obrigatoriamente devem tem os campos chaves que o tipo de relatório busca para a geração, no caso dos relatórios de recibo de férias, são os campos: **CODCOLIGADA  | CHAPA | FIMPERAQUIS | DATAPAGTO**.

A TOTVS disponibiliza relatórios padrão para utilização no RM, são disponibilizados a partir do TOTVS Compartilhamento: [RH - RM - FOP- Como importar relatórios através do totvs compartilhamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/7781155867543-RH-RM-FOP-Como-importar-relat%C3%B3rios-atrav%C3%A9s-do-totvs-compartilhamento).

Para o tipo **Recibo de Férias**, recomendamos a utilização do relatório do book padrão **FOPREL00112 - Recibo de Férias**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17709860962327)

**2. Processo de Integração de Relatórios:**

Para integrar o relatório do tipo recibo de férias, é necessário que o funcionário tenha suas férias calculadas, onde o recibo será localizado de acordo com a Data do Pagamento, portanto, habilite a opção **Enviar sob demanda (disparo manual)**e insira um intervalo de datas que contenha a Data do Pagamento.

Veja um exemplo onde o funcionário possui a data de pagamento do recibo de férias em 30/10/2023:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17710028394519)

Ao preencher o intervalo em que o Processo de integração de relatórios buscará, insira um intervalo onde a data do pagamento do recibo esteja presente:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17710190391959)

Ao executar, serão apresentados os funcionários que atendem à seleção:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17710169850391)

Execute o processo para de integração, onde será solicitado o login do usuário com permissão para publicar documento na plataforma do TOTVS Assinatura Eletrônica.

**Saiba mais**

**[TOTVS Assinatura Eletrônica - Definições e Parametrizações](https://tdn.totvs.com/pages/releaseview.action?pageId=607590749)**
