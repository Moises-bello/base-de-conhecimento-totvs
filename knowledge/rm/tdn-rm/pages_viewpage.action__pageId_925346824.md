---
content_hash: 8c8c4bae43a30e163423d9a06ccad5f0ef22744852c552cc6c7f64692f3fa3d7
fetched_at: '2026-06-29T00:12:07.411831+00:00'
page_id: '925346824'
product: rm
source: tdn-rm
title: DT - Crédito do Trabalhador - eSocial
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=925346824
version: 93
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS - Folha de Pagamento |
| Linha deIm Produto: | Linha RM |
| Segmeto: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | Crédito do Trabalhador - eSocial |
| País: | Brasil |
| Issue: | [DRHROTRM-13406](https://jiraproducao.totvs.com.br/browse/DRHROTRM-13406 "View this issue") |

## **02. LIBERAÇÃO**

Lembrando que, será a partir dos patches:

* 12.1.2406.254
* 12.1.2410.197
* 12.1.2502.117 e superiores

## **03. SITUAÇÃO/REQUISITO**

O Governo Federal lançou recentemente o "Crédito do Trabalhador", uma nova modalidade de empréstimo consignado destinada a empregados com carteira assinada, incluindo trabalhadores domésticos, rurais e assalariados de Microempreendedores Individuais (MEIs). Essa iniciativa permite que os trabalhadores acessem empréstimos com taxas de juros mais baixas, utilizando o saldo do Fundo de Garantia do Tempo de Serviço (FGTS) como garantia.

Diante dessa novidade, é essencial que o sistema TOTVS Folha de Pagamento seja adequado para atender a **Medida Provisória nº 1.292/2025**. Isso inclui a implementação de funcionalidades que permitam o gerenciamento eficaz desses empréstimos, assegurando conformidade com a legislação vigente e facilitando a administração por parte das empresas. [Fonte](https://www.gov.br/fazenda/pt-br/assuntos/noticias/2025/marco/governo-federal-cria-o-credito-do-trabalhador-linha-com-juros-mais-baixos).

## **04. SOLUÇÃO**

O produto TOTVS Folha de Pagamento está sendo  adequado para atender à Medida Provisória que institui o "Crédito do Trabalhador".

No entanto, até o momento, o Governo Federal não disponibilizou o leiaute oficial para que as empresas de software possam importar automaticamente os valores mensais do empréstimo a ser descontado dos funcionários.

Dessa forma, a empresa poderá consultar as informações de empréstimo de seus colaboradores no site **Emprega Brasil**. Mensalmente, a organização deverá baixar o arquivo de empréstimo e realizar o lançamento manual na folha de pagamento para posterior envio ao eSocial diretamente na folha de pagamento.

Abaixo, apresentamos a adequação realizada na geração do eSocial, assegurando que os valores sejam corretamente transmitidos conforme o leiaute do eSocial.

Será disponibilizada uma **segunda entrega,** com previsão para **30/04/2025,** contemplando as alterações nos demais processos necessários para a correta geração da folha de pagamento.

Na geração do XML dos eventos **S-1200, S-2299 ou S-2399**, o sistema validará a existência da Modalidade de Empréstimo "**Crédito do Trabalhador eSocial**" para a correta geração da tag **`<descFolha>`**.

### 

Caso exista um evento com a natureza de rubrica **"9253 - Empréstimos eConsignado - Desconto"** no envelope do funcionário para a competência em que está sendo gerado o evento **S-1200, S-2299 ou S-2399**, e não exista um empréstimo cadastrado para esse evento, o sistema apresentará a seguinte mensagem de erro:

falseATENÇÃO:

Em relação às naturezas de rubrica do Crédito do Trabalhador, sugerimos consultar o **Manual de Orientações do Empregador - Programa Crédito do Trabalhador disponibilizado no site do governo.**  
A**partir da página 27** são demonstrados exemplos contendo, inclusive, a natureza de rubrica nos eventos relacionados ao empréstimo (desconto do empréstimo, provisão, provento da provisão, etc.).

Link do manual: [Manual de Orientação Crédito do Trabalhador](https://www.gov.br/trabalho-e-emprego/pt-br/servicos/empregador/fgtsdigital/manual-e-documentacao-tecnica/manual-operacional-do-empregador-programa-credito-do-trabalhador-v2-16-05-25.pdf)

## **05.** **ASSUNTOS RELACIONADOS**

[Leiaute S-1.3 e Nota Técnica 01/2024](https://tdn.totvs.com/pages/viewpage.action?pageId=862114556)

[Crédito do Trabalhador - Linha RM - Medida Provisória Nº 1.292, de 12 de Março de 2025](https://tdn.totvs.com/pages/viewpage.action?pageId=925361639)

[Governo cria o Crédito do Trabalhador, linha com juros mais baixos](https://www.gov.br/planalto/pt-br/acompanhe-o-planalto/noticias/2025/03/governo-cria-o-credito-do-trabalhador-linha-com-juros-mais-baixos)

[Crédito do Trabalhador - Nova modalidade de consignado](https://www.totvs.com/blog/fiscal-clientes/credito-do-trabalhador-nova-modalidade-de-consignado/)

[Crédito do Trabalhador – Cronograma de Desconto da 1° parcela](https://www.totvs.com/blog/fiscal-clientes/credito-do-trabalhador-cronograma-de-desconto-da-1-parcela/) 

[Crédito do Trabalhador – MTE Publica Novas Regras para Descontos Consignados em Folha de Pagamento](https://www.totvs.com/blog/fiscal-clientes/credito-do-trabalhador-mte-publica-novas-regras-para-descontos-consignados-em-folha-de-pagamento/)  
  
[Crédito Consignado – Requisitos para operacionalização dos sistemas e plataformas digitais](https://www.totvs.com/blog/fiscal-clientes/credito-consignado-requisitos-para-operacionalizacao-dos-sistemas-e-plataformas-digitais/)

[Crédito do Trabalhador – Definição de Regras para Habilitação de Instituições Financeiras](https://www.totvs.com/blog/fiscal-clientes/credito-do-trabalhador-definicao-de-regras-para-habilitacao-de-instituicoes-financeiras/)

[Perguntas Frequentes do Crédito do Trabalhador](https://www.gov.br/trabalho-e-emprego/pt-br/assuntos/credito-do-trabalhador/perguntas-frequentes/perguntas-frequentes/)
