---
content_hash: 279c2582f011b2b79c8c07cc1d615ed7790f077707a1b2a01ac4648ff5048caf
fetched_at: '2026-06-29T00:12:09.088018+00:00'
page_id: '939246677'
product: rm
source: tdn-rm
title: DT - Crédito do Trabalhador - Cálculos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=939246677
version: 54
---

## **01. DADOS GERAIS**

| Produto: | TOTVS - Folha de Pagamento |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | Crédito do Trabalhador - Cálculos |
| País: | Brasil |
| Issue: | [DRHCALCRM-8100](https://jiraproducao.totvs.com.br/browse/DRHCALCRM-8100) |

## **02. LIBERAÇÃO**

Lembrando que, será a partir dos patches:

* 12.1.2406.296
* 12.1.2410.271
* 12.1.2502.174
* 12.1.2506.118
* e superiores

## **03. SITUAÇÃO/REQUISITO**

O Governo Federal lançou recentemente o "**Crédito do Trabalhador**", uma nova modalidade de empréstimo consignado destinada a empregados com carteira assinada, incluindo trabalhadores domésticos, rurais e assalariados de Microempreendedores Individuais (MEIs). Essa iniciativa permite que os trabalhadores acessem empréstimos com taxas de juros mais baixas, utilizando o saldo do Fundo de Garantia do Tempo de Serviço (FGTS) como garantia.

Diante dessa novidade, é essencial que o sistema TOTVS Folha de Pagamento seja adequado para atender a **Medida Provisória nº 1.292/2025**. Isso inclui a implementação de funcionalidades que permitam o gerenciamento eficaz desses empréstimos, assegurando conformidade com a legislação vigente e facilitando a administração por parte das empresas. [Fonte](https://www.gov.br/fazenda/pt-br/assuntos/noticias/2025/marco/governo-federal-cria-o-credito-do-trabalhador-linha-com-juros-mais-baixos).

## **04. SOLUÇÃO**

O produto **TOTVS Folha de Pagamento** liberou a **primeira entrega em 26/03/2025**, conforme divulgado na documentação oficial ([TDN - [link](https://tdn.totvs.com/pages/viewpage.action?pageId=925346824)]), a adequação do eSocial.

Já avançamos em várias entregas e sugerimos que, para melhor utilização do sistema e processo, seja utilizada a versão atualizada conforme item 01 deste documento.   
Veja todas as parametrizações e demais detalhamentos em:

* [Crédito do Trabalhador - Linha RM - Medida Provisória Nº 1.292, de 12 de Março de 2025](https://tdn.totvs.com/pages/viewpage.action?pageId=925361639).

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

## **06. PATCHES CONFORME FASEAMENTO**

As alterações realizadas ocorreram de forma faseada, conforme detalhamento abaixo:

* **1ª Fase: 26/03/2025:**  eSocial - [DT - Crédito do Trabalhador eSocial](https://tdn.totvs.com/pages/releaseview.action?pageId=925346824)  
  12.1.2406.254; 12.1.2410.197; 12.1.2502.117; 12.1.2506 e superiores
* **2ª Fase: 30/04/2025:** Cadastro do Empréstimo, Importação de Empréstimos Crédito do Trabalhador, Cálculos de Folha e Rescisão e Importação/Exportação  
  12.1.2406.270; 12.1.2410.223; 12.1.2502.138; 12.1.2506 e superiores
* **3ª Fase: 09/05/2025:**Cancelamento de Movimento e rescisão  
  12.1.2406.275; 12.1.2410.226; 12.1.2502.142; 12.1.2506 e superiores
* **4ª Fase: 16/05/2025:** Provisionamento de Férias - ***Necessário executar RM.Atualizador.exe***12.1.2406.277; 12.1.2410.229; 12.1.2502.145; 12.1.2506 e superiores
* **5ª Fase: 06/06/2025:** Recálculo automático  
  12.1.2406.284; 12.1.2410.247; 12.1.2502.154; 12.1.2506 e superiores
* **6ª Fase: 18/06/2025:**Provisionamento de férias proporcionalizando por dias de férias e Não zerar valor do empréstimo no cadastro para provisionamento preventivo nas férias  
  12.1.2406.287; 12.1.2410.257; 12.1.2502.160; 12.1.2506.104 e superiores
* **7ª Fase: 27/06/2025:**Margem Consignável considerando eventos com o somatório de todas as rubricas de vencimento e descontos com incidência previdenciária subtraindo o desconto de INSS e IRRF  
  12.1.2406.290; 12.1.2410.261; 12.1.2502.164; 12.1.2506.108 e superiores
* **8ª Fase: 04/07/2025:** Margem Consignável considerando os demais períodos do envelope de pagamento  
  12.1.2406.292; 12.1.2410.265; 12.1.2502.167; 12.1.2506.112 e superiores
* **9º Fase: 09/07/2025:**PORTARIA MTE Nº 933, DE 5 DE JUNHO DE 2025 - Possibilitar realizar mais de um crédito para o mesmo funcionário  
  12.1.2406.296; 12.1.2410.271; 12.1.2502.174; 12.1.2506.118 e superiores
