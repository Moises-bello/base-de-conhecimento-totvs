---
content_hash: 9f63a2c46abefcb6179fdda6c7ead8595e03d15d9b5990636772275c19f9b22b
fetched_at: '2026-06-29T00:11:26.314563+00:00'
page_id: '716346681'
product: rm
source: tdn-rm
title: DT - Parecer SEI 16120/20
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=716346681
version: 10
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | **RM** |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS Folha de Pagamento |
| Função: | Funcionários - Afastamentos Tipo P,T e O - cálculo do atestado médico (15 primeiros dias pagos pela empresa) |
| País: | Brasil |
| Ticket: | S/N |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DRHCALCRM-3026](https://jiraproducao.totvs.com.br/browse/DRHCALCRM-3026)  [DRHCALCRM-3027](https://jiraproducao.totvs.com.br/browse/DRHCALCRM-3027)  [DRHCALCRM-3028](https://jiraproducao.totvs.com.br/browse/DRHCALCRM-3028)  [DRHCALCRM-3034](https://jiraproducao.totvs.com.br/browse/DRHCALCRM-3034)  [DRHCALCRM-3035](https://jiraproducao.totvs.com.br/browse/DRHCALCRM-3035) |

## **02. Versões**

**12.1.2205.229**

**12.1.2209.175**

**12.1.2302.1**

## **03. SITUAÇÃO/REQUISITO**

Para adequar o produto a legislação [Parecer SEI Nº 16120/2020/ME](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes-producao-empresas-e-ambiente-de-testes/#7-23----29-12-2020----parecer-sei-n--16120-2020-me--como-deve-ser-tratada-a-incid-ncia-tribut-ria-nos-15-primeiros-dias-de-afastamento-que-antecedem-o-benef-cio-de-aux-lio-doen-a-) foram realizadas modificações no sistema para adequar aos novos procedimentos.

## **04. SOLUÇÃO**

1. Alterado o tratamento do código de cálculo CC 445 - ATESTADO MÉDICO COM INCIDÊNCIA SOMENTE SEGURADO:
2. Criado o código de cálculo CC465 - DIFERENÇA ATESTADO MÉDICO SEM INCIDÊNCIA EM INSS para cálculo da diferença salarial do evento CC 445 - ATESTADO MÉDICO COM INCIDÊNCIA SOMENTE SEGURADO:
3. Criada a flag 'Afastamento pela previdência social' no anexo 'Histórico de Afastamentos' do cadastro de funcionários, para que o usuário possa calcular o evento, conforme o [Parecer SEI Nº 16120/2020/ME](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes-producao-empresas-e-ambiente-de-testes/#7-23----29-12-2020----parecer-sei-n--16120-2020-me--como-deve-ser-tratada-a-incid-ncia-tribut-ria-nos-15-primeiros-dias-de-afastamento-que-antecedem-o-benef-cio-de-aux-lio-doen-a-);
4. Efetuado tratamento para ser lançado através do grupo de eventos ou manualmente os códigos de cálculo criados;
5. Tratada a flag 'Afastamento pela previdência social' no anexo 'Histórico de Afastamentos' do cadastro de funcionários, no módulo de Importação de Dados da Folha de Pagamento e no arquivo de Exportação de Históricos de Afastamento.

## **05. DEMAIS INFORMAÇÕES**

      

[Código de Cálculo 465 - Diferença Atestado Médico Sem incidência em INSS](https://tdn.totvs.com/pages/viewpage.action?pageId=717693258)

[Importação de Dados da Folha de Pagamento - Histórico de Afastamentos](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452719293)

[Funcionários - Anexos - Histórico de Afastamentos](https://tdn.totvs.com/pages/viewpage.action?pageId=452719319)

[Pasta Folha Normal - Afastamentos 1/2](https://tdn.totvs.com.br/pages/releaseview.action?pageId=452719376)

[Folha de Pagamento - Atestado médico com incidência somente segurado (CC445)](https://tdn.totvs.com/pages/viewpage.action?pageId=590618716)
