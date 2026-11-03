---
content_hash: 1fb72df6842ddc61626b72146537b68107568f8d6226d7340222dba8e8456807
fetched_at: '2026-06-29T00:09:47.763785+00:00'
page_id: '435105065'
product: rm
source: tdn-rm
title: Relatórios - Notas Promissórias
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435105065
version: 13
---

Nota promissória é um título cambiário em que seu criador assume a obrigação direta e principal de pagar o valor correspondente no título. A nota promissória nada mais é do que uma promessa de pagamento, e para seu nascimento são necessárias duas partes: o emitente ou subscritor (devedor), criador da promissória no mundo jurídico, e o beneficiário ou tomador que é o credor do título. A nota promissória é prevista no decreto 2044 de 31 de dezembro de 1908 e na Lei Uniforme de Genebra, seus requisitos são os seguintes:

* A denominação "nota promissória" lançada no texto do título.
* A promessa de pagar uma quantia determinada.
* A época do pagamento, caso não seja determinada, o vencimento será considerado à vista.
* A indicação do lugar do pagamento, em sua falta será considerado o domicílio do subscritor (emitente).
* O nome da pessoa a quem, ou a ordem de quem deve ser paga a promissória.
* A indicação da data em que, e do lugar onde a promissória é passada, em caso de omissão do lugar será considerado o designado ao lado do nome do subscritor.
* A assinatura de quem passa a nota promissória (subscritor).
* Assinatura de duas testemunhas identidade e (ou) cpf e endereço das mesmas.
* Sem rasuras, pois perde o valor a nota promissória.

**Pré-Condições**

**1-** O usuário deve ter permissão para executar os relatórios de Empreendimentos. As permissões podem ser acessadas em: TOTVS RM / Serviços Globais/ Segurança/ Perfis/ Sistema - Incorporação.

**2-** O usuário deve ter importado a estrutura dos relatórios abaixo, acessando: TOTVS RM / Serviços Globais/Gestão/ RM Reports/ Processo/ Importar Estrutura de Relatório.

* NP001 Notas Promissórias

**Executando o relatório de Notas Promissórias**

**Passo 1-** Acesse: TOTVS RM/ Projetos/ Incorporação/ Relatórios/ Nota Promissória.

**Passo 2-** Será exibido o formulário responsável por gerar o relatório desejado. Os  campos de preenchimento obrigatório são exibidos na tela destacados em negrito. Os campos do formulário são:

* **Relatório**: Campo responsável por definir qual relatório será executado, de acordo com as estruturas de relatório que foram importadas na pré-condição 2.
* **Cliente:** Campo qual deve ser informado  um código do Cliente.
* **Venda:**Campo qual deve ser informado  o Número da Venda para retornar uma nota promissória. Habilitado para preenchimento após informar o número da venda
* **Grupo:** Campo qual deve ser selecionado um grupo de componentes de um plano de financiamento
* **Tipo Parcela:** Campo qual o usuário selecionará  o tipo de parcela  de um grupo de componentes em um plano de financiamento.
* **Filtro Por:** Permite que seja efetuado um filtro por [Numeração] ou por Data de [Vencimento].
* **Numeração Inicial e Final:** Habilitado para preenchimento se for selecionado o filtro por [Numeração]. Este campo faz referencia ao número do componente de acordo com o grupo e tipo de parcela selecionados.
* **Vencimento Inicial e Final:** Habilitado para preenchimento se for selecionado o filtro por [Vencimento].Este campo faz referencia ao vencimento da parcela de um plano de financiamento

**Passo 3-** Preencha os campos e clique em [Executar].
