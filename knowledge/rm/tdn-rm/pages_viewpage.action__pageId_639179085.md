---
content_hash: c420096c1a4e83d8e9181acab9cb7c90f29a74e06e137d0fcec70c97e2203c80
fetched_at: '2026-06-29T00:11:07.079003+00:00'
page_id: '639179085'
product: rm
source: tdn-rm
title: Middleware - Mudanças no Relatório de Conferência - INSS
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=639179085
version: 5
---

## **Relatório de Conferência**

O relatório de conferência de INSS tem como objetivo apoiar na identificação de possíveis divergências entre os valores de INSS existentes no envelope de pagamento com o valores retornados do RET, auxiliando também na conferência dos valores de Segurados, Deduções Salário Família e Maternidade da DCTFWeb.

Os dados apresentados são originados da comparação dos valores de INSS integrados do RH (S-1200, S-2299 e S-2399) contra os valores retornados do Governo pelo evento S-5001.

## **Configurações do Relatório**

Para verificar como configurar e gerar o relatório, acesse: [Middleware - Relatório de Conferência de INSS](https://tdn.totvs.com/pages/viewpage.action?pageId=536721262)

## **Mudanças no Relatório**

A partir das versões abaixo, o relatório de conferência passou por algumas mudanças para melhor usabilidade e, por isso, iremos apresentar nesse documento as principais alterações ocorridas.

**RM:**  12.1.32.154, 12.1.31.218, 12.1.29.300  
**TAF:** A partir do pacote acumulado (expedição contínua) de 01/09/2021

* ### **Cards totalizadores por empresa**

Os cards abaixo, que totalizam os valores encontrados nas fontes de informação (RH e Governo), passam a exibir o somatório do INSS e INSS 13º calculados pela Folha e pela DCTFWeb, respectivamente.

**Importante!** Os detalhamentos dos valores sintéticos dos Cards deixaram de ser apresentados em tela e passaram a serem visualizados através do detalhamento de funcionários e, além disso, com a nova funcionalidade de extração dos dados, o usuário poderá também trabalhar esses valores conforme necessidade.

* ### **Exportação de dados**

Outro item implementado no relatório é a exportação de dados que possibilita, assim, que os resultados obtidos sejam extraídos e avaliados através do Excel.

Para tal, basta clicar no botão  presente nas telas do relatório, conforme exemplo abaixo:

* ### **Funcionários com Múltiplos Vínculos**

Para facilitar a conferência de funcionários com múltiplos vínculos, ao clicar no nome do funcionário, o sistema passou a apresentar o detalhamento dos valores calculados, exibindo nessa tela todos os estabelecimentos que o funcionários possui vínculo:

Assim, basta clicar na seta  ao lado da inscrição do estabelecimento desejado para que os detalhamentos sejam apresentados:

Lembrando que, os valores apresentados são sumarizados por CPF, sendo assim, caso seja realizado algum filtro na geração do relatório, as informações dos múltiplos vínculos podem apresentar divergências. Para alertá-los do fato, será exibida a mensagem abaixo ao realizar qualquer filtro que não englobe toda a empresa:

Clientes TAF Full

Para clientes que utilizam o TAF Full (não utilizam Middleware), o relatório de conferência estará disponível dentro da aplicação TOTVS Automação Fiscal (TAF).

- [Painel de Conferência de INSS](https://tdn.totvs.com/pages/releaseview.action?pageId=528452133)  
- [Como gerar as bases de INSS/FGTS no relatório do eSocial do futuro?](https://tdn.totvs.com/pages/releaseview.action?pageId=546249442)

## **Tabelas utilizadas**

PESOCIALTOTALIZADORES, PESOCIALTOTALIZADORESCPF, PESOCIALTOTAISLOTACAO e PESOCIALTOTALIZADORESAUTONOMOS.
