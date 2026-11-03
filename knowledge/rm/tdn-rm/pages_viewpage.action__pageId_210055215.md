---
content_hash: 6b142291d79dedf02777592be0bbd6fb94d561e535908660ef644bbb674852c2
fetched_at: '2026-06-29T00:06:15.407497+00:00'
page_id: '210055215'
product: rm
source: tdn-rm
title: TST0001 - Configuração WebService TOTVS Avaliação e Pesquisa Versão 12
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=210055215
version: 122
---

# Configuração do WebService TOTVS Avaliação e Pesquisa para versões 12

|  |  |
| --- | --- |
| **Produto:** | TOTVS Avaliação e Pesquisa |
| **Versões:** | 12.1.1 |
| **Ocorrência:** |  |
| **Ambiente:** | Oracle | SQL |
| **Passo a passo:** | Após realizar a instalação do RM, acessar o diretório **CorporeRM\WebService**:      Editar o arquivo Web.config:      Na linha 56, alterar o valor da chave para o nome da conexão presente no arquivo C:\totvs\CorporeRM\RM.Net\Alias.dat        Na linha 59, alterar o valor da chave para o valor presente na propriedade Port do arquivo RM.Host.Service.exe        Abaixo da propriedade TcpPort, incluir a chave (caso não exista): **<add key="Host" value="localhost" />** |
| **Observações:** |  |

divs
