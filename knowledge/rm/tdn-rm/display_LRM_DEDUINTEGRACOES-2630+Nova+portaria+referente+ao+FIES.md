---
content_hash: 477c62cbd0025818655b36682eea7cc3a9dc7558182d120e272f89374222bc37
fetched_at: '2026-06-29T00:10:37.804161+00:00'
page_id: '540890709'
product: rm
source: tdn-rm
title: DEDUINTEGRACOES-2630 Nova portaria referente ao FIES
type: documentation
url: https://tdn.totvs.com/display/LRM/DEDUINTEGRACOES-2630+Nova+portaria+referente+ao+FIES
version: 1
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Educacional |
| Módulo: | TOTVS Educacional |
| Função: | Cadastro de bolsas / Extrato financeiro |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DEDUINTEGRACOES-2630](https://jiraproducao.totvs.com.br/browse/DEDUINTEGRACOES-6619) |

## **02. SITUAÇÃO/REQUISITO**

De acordo com a mudança na Legislação do FIES, é necessário que os alunos que possuem o benefício do Novo FIES gerem os boletos pelo site da instituição financeira e não mais pelo sistema da instituição.

## **03. SOLUÇÃO**

Alteração no cadastro de bolsa para contemplar o código do novo FIES. A partir deste código, foram feitas as alterações nos portais (antigo e novo portal), educaMobile e novo extrato financeiro do aluno (payments) para que os botões de impressão do boleto e botão de pagamento com cartão de crédito/débito não fiquem disponíveis para alunos que possuem o benefício do novo FIES.

No exemplo abaixo temos a bolsa identificada com o novo FIES e suas parcelas geradas, bem como parcelas geradas sem a bolsa.

* **RM Educacional:**

Parcelas geradas para o novo serviço criado para efeito de testes, SERVIÇO NOVO FIES e parcelas geradas com serviço Mensalidade de Nutrição sem a bolsa.

Assim, ao acessar a página de extrato financeiro, o aluno que contém boletos gerados a partir de lançamentos dos serviços que contenham o benefício do novo FIES, não será possível a emissão do boleto, nem acesso ao IPTE (código de barras), conforme imagens abaixo:

* **Corpore Net:**

* **Novo portal do aluno:**

* **Extrato financeiro (Payments):**

* **eduConnect:**

* **Central de Comunicações - Agendamento/envio de mensagens :**

No serviço de agendamento e envio de mensagens do RM Educacional, ao selecionar a mensagem de aviso de boleto com vencimento próximo, o sistema irá selecionar apenas os registros que não tenham a bolsa do novo FIES para envio das mensagens.
