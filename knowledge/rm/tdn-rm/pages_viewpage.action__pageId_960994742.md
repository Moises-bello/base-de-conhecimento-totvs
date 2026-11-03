---
content_hash: d93e9be668d9025131d2a1203bb88a594daedc1d13e71b651177d80119c967e3
fetched_at: '2026-06-29T00:12:13.922811+00:00'
page_id: '960994742'
product: rm
source: tdn-rm
title: DT - Crédito do Trabalhador - Importação de Layout - Fracionamento/Agendamento
  Jobs
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=960994742
version: 2
---

## **01. DADOS GERAIS**

| Produto: | TOTVS - Folha de Pagamento |
| --- | --- |
| Linha deIm Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | Crédito do Trabalhador - Importação de Layout (Excel) |
| País: | Brasil |
| Issue: | [DRHCALCRM-8283](https://jiraproducao.totvs.com.br/browse/DRHCALCRM-8283) |

## **02. LIBERAÇÃO**

Lembrando que, será a partir dos patches:

* 12.1.2410
* 12.1.2502
* 12.1.2506
* 12.1.2510 e posteriores

## **03. SITUAÇÃO/REQUISITO**

O Governo Federal lançou recentemente o "Crédito do Trabalhador", uma nova modalidade de empréstimo consignado destinada a empregados com carteira assinada, incluindo trabalhadores domésticos, rurais e assalariados de Microempreendedores Individuais (MEIs). Essa iniciativa permite que os trabalhadores acessem empréstimos com taxas de juros mais baixas, utilizando o saldo do Fundo de Garantia do Tempo de Serviço (FGTS) como garantia.

Diante dessa novidade, é essencial que o sistema TOTVS Folha de Pagamento seja adequado para atender a **Medida Provisória nº 1.292/2025**. Isso inclui a implementação de funcionalidades que permitam o gerenciamento eficaz desses empréstimos, assegurando conformidade com a legislação vigente e facilitando a administração por parte das empresas. [Fonte](https://www.gov.br/fazenda/pt-br/assuntos/noticias/2025/marco/governo-federal-cria-o-credito-do-trabalhador-linha-com-juros-mais-baixos).

No novo parâmetro “Qtde de Job´s” em “Folha de pagamento | Configurações | Parametrizador | Folha Normal | Crédito do trabalhador” se define a quantidade de jobs para o fracionamento. Quando informando 0 (zero) ou 1 (um) a importação de arquivo ocorre sem fracionamento de jobs. Quando informado valor maior do que 1 (um), o sistema aciona o processo fracionado.

## **04. SOLUÇÃO**

O produto **TOTVS Folha de Pagamento** liberou a **primeira entrega em 26/03/2025**, conforme divulgado na documentação oficial ([TDN - [link](https://tdn.totvs.com/pages/viewpage.action?pageId=925346824)]), a adequação do eSocial.

Neste momento, estamos avançando com a **segunda entrega**, que contempla a adequação e implementação dos processos de cálculos e alterações em cadastros. Veja todas as informações em:

[Crédito do Trabalhador - Linha RM - Medida Provisória Nº 1.292, de 12 de Março de 2025](https://tdn.totvs.com/pages/viewpage.action?pageId=925361639).

## **05.****ASSUNTOS RELACIONADOS**

[DT - Crédito do Trabalhador eSocial](https://tdn.totvs.com/pages/releaseview.action?pageId=925346824)

[Crédito do Trabalhador - Linha RM - Medida Provisória Nº 1.292, de 12 de Março de 2025](https://tdn.totvs.com/pages/viewpage.action?pageId=925361639)

[Leiaute S-1.3 e Nota Técnica 01/2024](https://tdn.totvs.com/pages/viewpage.action?pageId=862114556)

[Governo cria o Crédito do Trabalhador, linha com juros mais baixos](https://www.gov.br/planalto/pt-br/acompanhe-o-planalto/noticias/2025/03/governo-cria-o-credito-do-trabalhador-linha-com-juros-mais-baixos)

[Crédito do Trabalhador - Nova modalidade de consignado](https://www.totvs.com/blog/fiscal-clientes/credito-do-trabalhador-nova-modalidade-de-consignado/)

[Crédito do Trabalhador – Cronograma de Desconto da 1° parcela](https://www.totvs.com/blog/fiscal-clientes/credito-do-trabalhador-cronograma-de-desconto-da-1-parcela/) 

[Crédito do Trabalhador – MTE Publica Novas Regras para Descontos Consignados em Folha de Pagamento](https://www.totvs.com/blog/fiscal-clientes/credito-do-trabalhador-mte-publica-novas-regras-para-descontos-consignados-em-folha-de-pagamento/)  
  
[Crédito Consignado – Requisitos para operacionalização dos sistemas e plataformas digitais](https://www.totvs.com/blog/fiscal-clientes/credito-consignado-requisitos-para-operacionalizacao-dos-sistemas-e-plataformas-digitais/)

[Crédito do Trabalhador – Definição de Regras para Habilitação de Instituições Financeiras](https://www.totvs.com/blog/fiscal-clientes/credito-do-trabalhador-definicao-de-regras-para-habilitacao-de-instituicoes-financeiras/)

[Perguntas Frequentes do Crédito do Trabalhador](https://www.gov.br/trabalho-e-emprego/pt-br/assuntos/credito-do-trabalhador/perguntas-frequentes/perguntas-frequentes/)

[DT - Crédito do Trabalhador - Cálculos](https://tdn.totvs.com/pages/viewpage.action?pageId=939246677)

[DT - Crédito do Trabalhador - Importação de Multi Arquivos](https://tdn.totvs.com/pages/viewpage.action?pageId=960015355)

[DT - Crédito do Trabalhador - Mensagem Importação do Arquivo](https://tdn.totvs.com/pages/viewpage.action?pageId=960025772)

[DT - Crédito do Trabalhador - Importação de Layout (Excel)](https://tdn.totvs.com/pages/viewpage.action?pageId=960026912)
