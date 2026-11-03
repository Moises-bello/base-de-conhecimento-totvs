---
content_hash: 219a00ad82c6dee571b6f5024c5923447e17c96995a563d12b174f051cc93b43
fetched_at: '2026-06-28T21:35:27.927862+00:00'
page_id: '6066537'
product: fluig
source: tdn-fluig
title: Log4j
type: documentation
url: https://tdn.totvs.com/display/fluig/Log4j
version: 14
---

Fique atento!

O TOTVS ESB não é mais ofertado por se tratar de uma solução legada. A nova solução para realizar integrações é o TOTVS iPaaS. Saiba mais detalhes **[aqui](https://www.totvs.com/totvs-ipaas/)**. 

Na opção Log4j podem ser configurados os logs do Fluig ESB. A seguir tem-se os campos disponíveis para essa configuração.

| Campo | Descrição |
| --- | --- |
| Level of Log | Nível do log do Fluig ESB. Neste campo existem quatro níveis:   1. WARN 2. INFO 3. DEBUG 4. ERROR |
| Number of Log Files | Número de arquivos de log que podem existir no diretório indicado. |
| Size File of Log | Tamanho em megabytes do arquivo de log. |

A visualização do *log* pode ser realizada acessando o arquivo 'esb.log' localizado em [instalação ESB]\data. Caso a inicialização do ESB Server tenha sido realizada através do arquivo startup-esb.bat' localizado em [instalação ESB]\bin, a visualização do *log* pode ser feita através do Console ou Prompt de Comandos da aplicação.
