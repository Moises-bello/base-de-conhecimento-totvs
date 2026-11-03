---
content_hash: 8824db265a457cba29d21109bf533a761a8ec7406d68d4033abaebecdc2279bb
fetched_at: '2026-06-29T00:11:32.239989+00:00'
page_id: '745748808'
product: rm
source: tdn-rm
title: cópiaTOTVS Educacional x EAD (WebEnsinoAMS) -  Boletos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=745748808
version: 1
---

**Boletos**

---

A entidade Boletos pode ser sincronizada do TOTVS Educacional para o WebEnsino.

A integração da entidade Contratos de um determinado Aluno do TOTVS Educacional será sincronizada com a entidade Boleto do WebEnsino. Essa integração permite apenas um tipo de operação, veja abaixo:

|  |  |
| --- | --- |
| **TOTVS EDUCACIONAL** | **WEBENSINO** |
| Inclui no TOTVS Educacional | Inclui no WebEnsino |

**Pré-Requisitos**

Para que a integração do Contrato de um determinado aluno seja feita do TOTVS Educacional para o WebEnsino, são necessários uma série de cadastros:

**Incluir:**

- Curso

- Habilitação

- Matriz Curricular

- Matriz Aplicada

- Parametrização por Curso

- Aluno

- Curso/Habilitações

- Contratos

- Plano de Pagamento

- Criação de Parcelas

Quando todos os pré-requisitos estiverem cadastrados, no cadastro de aluno (Anexos | Contratos), deve ser informado o Plano de Pagamento e Habilitação para a criação das parcelas. Editando as parcelas criadas e acessando o menu Processos | Gerar Lançamento, o sistema irá gerar os lançamentos no financeiro referente as mesmas. Feito isso quando o sistema WebEnsino solicita as listagens dos boletos, ele se conecta ao TOTVS Educacional (através de um Web Service) e busca todas as parcelas (boletos) que estão lançadas e em aberto no Financeiro. O aluno que tiver essas parcelas, dentro do WebEnsino conseguirá ter acesso para que possa imprimir os boletos de todos os meses disponíveis. Caso identifique a o boleto já foi pago pode-se acessar o Financeiro e dar baixa na parcela. (Essa parcela baixada não será mais apresentada para o aluno quando acessar o WebEnsino)

**Observações**

Para que essa integração seja concluída com sucesso, dentro do Financeiro (TOTVS Gestão Financeira) deverá estar criado um relatório (Gerador) para impressão das informações do boleto. Esse mesmo relatório deverá estar informado dentro dos parâmetros 'RM Portal - Gerais' do Totvs Educacional. Lembrando que a Biblioteca deverá estar instalada no servidor onde se encontra o TOTVS Business Conector.
