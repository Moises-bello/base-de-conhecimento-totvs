---
content_hash: 9be1459a3dd45bf95af157d0acfe57cdccd0c260caa84fd72fcc6d30b05f009e
fetched_at: '2026-06-29T00:05:53.384935+00:00'
page_id: '1070066693'
product: rm
source: tdn-rm
title: DT - Processo para atualizar Dedução por Dependente
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1070066693
version: 8
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS Folha de Pagamento |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | Atualizar Dedução por Dependente |
| País: | Brasil |
| Issue: | [DRHCALCRM-12156](https://jiraproducao.totvs.com.br/browse/DRHCALCRM-12156) |

## **02. VERSÕES**

**A partir das Versões:**

* 12.1.2506.323
* 12.1.2510.253
* 12.1.2602.167 e Superiores

## **03.****SITUAÇÃO/REQUISITO**

Possibilitar a atualização do campo “Valor de Dedução do Rendimento Tributável”, existente no anexo de Dependentes do Funcionário, para que a dedução do dependente seja considerada sempre que aplicável, mesmo quando não houver desconto de IRRF ou quando for utilizado o desconto simplificado mensal.

 "Ainda que as deduções legais não sejam utilizadas no cálculo do IRRF em razão da aplicação do desconto simplificado mensal, tais informações permanecem existentes no contexto fiscal do trabalhador e devem ser devidamente declaradas. A própria orientação oficial do eSocial, constante no FAQ 10.39 (atualizado em 17/12/2025), estabelece expressamente que, mesmo quando aplicado o desconto simplificado mensal, é obrigatório o envio dos dados de deduções legais aplicáveis ao trabalhador no evento de pagamento. Assim, a não utilização das deduções no cálculo não afasta a obrigatoriedade de sua informação no evento S-1210."

Veja mais detalhes da consultoria no link: [eSocial - Envio de dedução de dependentes no S-1210](https://tdn.totvs.com/pages/releaseview.action?pageId=1056129814)

## **04.****SOLUÇÃO**

Foi criado o processo “Atualizar Dedução por Dependente”, disponível em: Administração de Pessoal | Funcionário | Anexos | Folha de Pagamento | Dependentes | Processos

Com essa melhoria, o histórico dos dependentes passa a ser preenchido sempre que existir direito à dedução, e não apenas nos casos em que houver desconto de IRRF.

Veja mais detalhes em [Atualizar Dedução por Dependente](https://tdn.totvs.com/pages/viewpage.action?pageId=1070067509)

## **05. ASSUNTOS RELACIONADOS**

* [Processo Atualizar Dedução por Dependente](https://tdn.totvs.com/pages/viewpage.action?pageId=1070067509)
* [Valor Dedução do Rendimento Tributável](https://tdn.totvs.com/pages/releaseview.action?pageId=784779468)
* [Valor Dedução do Rendimento Tributável no Cadastro de Dependentes - Alterações no cálculo para atender ao leiaute S-1.2 que irá substituir a DIRF](https://tdn.totvs.com/pages/releaseview.action?pageId=786553670#tabs-passo3)
* [Passo a Passo para atualizar o "Valor Dedução do Rendimento Tributável" do Dependente](https://tdn.totvs.com/pages/viewpage.action?pageId=1070064028)
