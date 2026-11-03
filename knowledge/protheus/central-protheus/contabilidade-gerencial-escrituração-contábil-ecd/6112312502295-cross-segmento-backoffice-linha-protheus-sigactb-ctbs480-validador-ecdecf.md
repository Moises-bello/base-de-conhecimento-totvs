---
article_id: 6112312502295
category: Contabilidade Gerencial - Escrituração-Contábil-ECD
content_hash: 8a4b03e867c6f2200dbfe824a8333da2df74ac3cb96083f2f5d2490db15bba41
fetched_at: '2026-06-28T22:40:52.725346+00:00'
product: protheus
section_id: 1500001537561
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBS480 - Validador
  ECD/ECF
type: support-article
updated_at: '2023-06-01T14:57:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6112312502295-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBS480-Validador-ECD-ECF
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **03:00 min****Dúvida**Como funciona o Validador ECD/ECF ?  
  
**Ambiente**Cross Segmento - Backoffice Linha Protheus - Contabilidade Gerencial – **A partir da versão 12.1.33**

**Solução**

**Procedimento em vídeo:**

Para correto funcionamento da rotina deve-se seguir os passos abaixo:

1. Adicionar a rotina CTBS480 no menu;

#### [COMO INSERIR O CHECKLIST NO MENU](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013342191-RH-Linha-Protheus-GPE-Como-excluir-ou-incluir-rotinas-no-menu)

Essa funcionalidade está disponível a partir da release 12.1.33

2. Necessário ter as [configurações abaixo no server:](https://tdn.totvs.com/pages/releaseview.action?pageId=665275974)

*Habilitar a chave TopMemoMega = 1 na seção [Do Ambiente]*

*Habilitar a chave App\_Environment='environment' na seção [GENERAL];*

*Habilitar a porta de multiprotocolo, adicionando as chaves abaixo na seção [DRIVERS]:             MultiProtocolPort=1*

*multiprotocolportsecure=0*

![general.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6114639882391/general.png)

3. Visão Geral

Tela para validação do ambiente e base de dados para auxiliar na entrega das escriturações contábeis.

![image2022-2-8_9-9-58.png](https://tdn.totvs.com/download/attachments/665275974/image2022-2-8_9-9-58.png?version=2&modificationDate=1651762235457&api=v2)

Dependendo da quantidade de inconsistências encontradas será mostrado o aviso abaixo indicando que para completa visualização das informações é necessário exportar os dados clicando no botão 'Baixar Dados'.

![](https://tdn.totvs.com/download/attachments/665275974/image2022-2-8_9-32-44.png?version=1&modificationDate=1644341784447&api=v2)

4. Validações Gerais  

Nos três primeiros Dash são mostradas algumas informações básicas do ambiente

\* Dados do Servidor e Aplicação, exibe os dados do binário, lib, dbaccess, release do rpo, etc.

![image2022-2-8_9-20-24.png](https://tdn.totvs.com/download/attachments/665275974/image2022-2-8_9-20-24.png?version=1&modificationDate=1644341785330&api=v2)

\*Exibe a data dos principais fontes envolvidos na entrega do ECD / ECF.

![image2022-2-8_9-20-24.png](https://tdn.totvs.com/download/attachments/665275974/image2022-2-8_9-20-24.png?version=1&modificationDate=1644341785330&api=v2)

\*Valida se existem os pontos de entrada ECDCHVCAB, CTBTXCACHE e ECDCHVMOV e se as procedures dinâmicas estão ativas, parâmetro [MV\_CTBSPRC](https://tdn.engpro.totvs.com.br/pages/releaseview.action?pageId=549503023).

![image2022-2-8_9-23-48.png](https://tdn.totvs.com/download/attachments/665275974/image2022-2-8_9-23-48.png?version=1&modificationDate=1644341785137&api=v2)

5 - Validações do ECD

Nesta tela serão mostradas diversas validações de cadastro e base de dados referente a Escrituração Contábil Digital, conforme abaixo:

![](https://tdn.totvs.com/download/attachments/665275974/ecd.gif?version=1&modificationDate=1644341783407&api=v2)

mais detalhes link abaixo

*<https://tdn.totvs.com/pages/releaseview.action?pageId=665275974>*

[*MV\_ULTVECD DT Adesão validador ECD/ECF*](https://tdn.totvs.com/pages/releaseview.action?pageId=695203717)
