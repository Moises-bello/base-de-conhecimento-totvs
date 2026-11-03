---
content_hash: 2d2a64bd6a1ef76c5b2275f2709673b28e804da0b30eaa9e143b52aa814782d5
fetched_at: '2026-06-29T00:11:05.022288+00:00'
page_id: '627997947'
product: rm
source: tdn-rm
title: 10272032 FISCAL01-14383 - NFS-E Geração da tag ISSRETIDO com o valor 3 – Substituição
  Tributária.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=627997947
version: 4
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS Backoffice |
| Linha de Produto: | DistribuiçãoConstrução ProjetosLinha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | SPED Fiscal |
| Ticket: | 10272032 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-14383 |

## **02. SITUAÇÃO/REQUISITO**

No layout da Prefeitura de Criciúma/SC existe a tag IssRetido atualmente o ERP só gera os valores 1- Sim ou 2- Não, porém a Prefeitura implementou a opção 3 – Substituição Tributária. Veja abaixo:

tsSimNao - Essa tag é a demonstração dos valores que podem ser gerados na tag ISSRETIDO  
  
Identificação de Sim/Não/Substituição Tributária  
  
1 – Sim  
2 – Não  
3 – Substituição Tributária

Obs: O cliente deseja gerar a tag ISSRETIDO com o valor 3 – Substituição Tributária.

## **03. SOLUÇÃO**

Na emissão da NFS-e, atualmente a Tag ISSRETIDO verifica o Tipo de Recolhimento do ISS, se Retido e ou Retido Deduzido então gerar “1 Sim (Retido)”, se o Tipo de Recolhimento for outros (Devido, Isento...) em tão gerar “2 Não (Normal)”.

A opção de “3 Substituição Tributária” não tem relação como o Tipo de Recolhimento da linha do ISS no item/movimento, mas com o Responsável pelo pagamento do Imposto, que no caso do cliente, é a Empresa Prestadora do serviço.

Criado mais uma Opção “Substituição Tributária” no Cadastro do Cliente\Fornecedor, aba Tributos, campo Retenção De ISS.

Foi alterado o processo de envio de NFS-e para que seja verificado a opção "Substituição Tributária” no cadastro do Cliente\Fornecedor | Aba Tributos | Retenção De ISS na geração da tag IssRetido. Caso esteja marcado como substituição tributária no campo citado acima, a tag será sempre gerada com valor 3.

Tratamento feito de forma pontual para o município de Criciúma - SC
