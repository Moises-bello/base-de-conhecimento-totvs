---
content_hash: 4cf7c44dc680b063fc2ddbf76d84769b232038445a0b64bfd9d95109c76d7b1b
fetched_at: '2026-06-29T00:11:49.403761+00:00'
page_id: '832643986'
product: rm
source: tdn-rm
title: Nova forma de Manipulação de Arquivos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=832643986
version: 17
---

Avisos!

1. É importante que as rotinhas sejam validadas em ambientes de homologação para as áreas impactadas sejam informadas sobre as mudanças.
2. Caso essas rotinas tenham customizações específicas, cabe ao cliente realizar os ajustes e adequações necessárias,

## **01. VISÃO GERAL**

Informções

Essas mudanças se aplicam tanto a instalações em ambientes **OnPremise** quanto na **TCloud**.

Nossas rotinas de manipulação de arquivos estão sendo atualizadas para lidar com arquivos relativos, uma abordagem mais adequada para a manipulação de arquivos.

Essas melhorias estão em conformidade com as regras da **LGPD** e de **evolução tecnológica da linha RM**.

## **02. MANIPULAÇÃO DE ARQUIVOS**

Anteriormente, a manipulação de arquivos era realizada através da configuração de parâmetros da respectiva rotina, nos quais os caminhos absolutos eram configurados conforme cada ambiente.

Os arquivos passam a ser gerados através de caminhos relativos controlados pela configuração da tag **FileServerPath**:

2.1 **Se a tag não estiver configurada**, os arquivos serão gerados dentro da pasta "**Arquivos**" no local de instalação do RM. Exemplo: C:\TOTVS\CorporeRM\RM.Net\Arquivos\Saúde\Coligada\_1\Filial\_3\TISS\Elegibilidade

2.2 **Se a tag estiver configurada**, os arquivos serão salvos conforme local indicado. Exemplo: Se configurado o caminho \\SERVIDOR\_ARQUIVOS\COMPARTILHAMENTO, o arquivo da Elegibilidade do exemplo acima, seria gravado em \\SERVIDOR\_ARQUIVOS\COMPARTILHAMENTO\Saúde\Coligada\_1\Filial\_3\TISS\Elegibilidade

Dica

Para saber como realizar a configuração global de compartilhamento de arquivos, consulte a documentação disponível

## **03. ROTINAS IMPACTADAS**

Os parâmetros que antes indicavam os diretórios de armazenamento dos arquivos foram descontinuados de acordo com a sua versão do quadro abaixo.

| Parâmetros | Rotinas | Versão |
| --- | --- | --- |
| Empresa > TISS > Mensagens Recebidas | Elegibilidade Solicitação de Autorização Status da Autorização Solicitar Cancelamento Autorização | 12.1.2406 |
| Empresa > TISS > Mensagens Transmitidas | Elegibilidade Solicitação de Autorização Status da Autorização Solicitar Cancelamento Autorização Faturamento para Convênios | 12.1.2406 |
| Empresa > TISS > Controle de Log | Utilizados somente em rotinas TISS versão 2 e foram descontinuados com o termino do suporte Delphi na 2406 | 12.1.2406 |
| Empresa > TISS > Repositório | Utilizados somente em rotinas TISS versão 2 e foram descontinuados com o termino do suporte Delphi na 2406 | 12.1.2406 |
| Unidade Diagnóstico > Integrações | Integração Pixeon; Integração Carestream; Integração Tuxxon | 12.1.2406 |
