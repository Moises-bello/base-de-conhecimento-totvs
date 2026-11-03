---
content_hash: 97c217a0a4750d883999aac4c807f46990f8287722d4bfc5a9006bda13155ea1
fetched_at: '2026-06-29T00:08:31.650568+00:00'
page_id: '273302982'
product: rm
source: tdn-rm
title: DT_Aviso Prévio Trabalhado
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=273302982
version: 140
---

---

# Aviso Prévio Trabalhado

|  |  |  |  |
| --- | --- | --- | --- |
| **Linha de Produto:** | RM | | |
| **Segmento Executor:** | Recursos Humanos | | |
| **Módulo:** | TOTVS Folha de Pagamento | | |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Aviso Prévio Trabalhado | Aviso Prévio Trabalhado | | Rescisão | Rescisão | | | |
| **Requisito (ISSUE):** |  | | |
| **País:** | (X) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |

---

# Interpretação da demanda

Visando atender o eSocial, onde passa a ser necessário registrar a comunicação do **aviso prévio trabalhado** de iniciativa do empregador ou do empregado através do envio do evento S-2250,  o cadastro do aviso prévio trabalhado passará a ser feito fora da tela de rescisão, ou seja,  foi implementado no sistema um menu especifico para tal rotina.

# Analise da demanda

### Criação do Menus

Foi implementado no menu de funcionários (Folha de Pagamento | Administração de Pessoal | Funcionários) um novo ícone para que possa ser feito o cadastro do Aviso Prévio Trabalhado individual.

 

**Observações sobre os campos:**

* Data de demissão prevista

A data prevista de demissão poderá ser igual  ou superior a data do aviso prévio cadastrada.

* Tipo Redução Aviso

Será habilitado apenas se o tipo de demissão for igual a "2 - Inic. Empregador sem justa causa".

Através do processo "Aviso prévio coletivo" disponível no menu **Rescisão**poderá ser feito o lançamento coletivo para os funcionários.

**Observação**: Após o cadastro do aviso prévio trabalhado a situação dos funcionários selecionados serão alteradas para "V - Aviso Prévio".

### Alteração do comportamento da rotina de rescisão

Para que a rotina de rescisão trabalhe em conjunto com o novo menu de cadastro do aviso prévio trabalhado, foi feita algumas alterações de comportamento no processo, sendo elas:

* **Aviso Prévio cadastrado com o tipo 2**

1. O campo “Data de Início do Aviso Trabalho” ficará desabilitado, porém constará a data cadastrada no “Aviso Prévio Trabalhado”.
2. Será desabilitado a opção "Desconta Aviso Prévio";
3. O campo "Aviso Prévio Misto" será habilitado, ficando disponível para marcação.

Observações referente a utilização do parâmetro acima:

1. 1. 1. 1. 1. 1. Quando marcamos o campo "Aviso Prévio Misto" obrigatoriamente será considerado o parâmetro "Tem aviso prévio indenizado"  e os campos  "Data de Início do Aviso Indenizado" e "Dias de Aviso Prévio Indenizado" serão habilitados.
               2. O campo "Data de Início do Aviso Trabalhado" será preenchido automaticamente com a data cadastrada no aviso prévio trabalhado.

* **Aviso Prévio cadastrado com o tipo 4**

1. Os campos “Aviso Prévio Misto” e “Desconta Aviso Prévio” serão habilitados.

Observações:

* Quando os campos “Aviso Prévio Misto” e “Desconta Aviso Prévio estiverem desmarcados  será considerado como aviso prévio trabalhado.
* A utilização do campo "Aviso Prévio Misto" irá afetar o processo em:

1. 1. Obrigatoriamente será considerado o parâmetro "Tem aviso prévio indenizado"  e os campos "Data de Início do Aviso Indenizado" e "Dias de Aviso Prévio Indenizado" serão habilitados.
   2. Será desabilitado a opção "Desconta Aviso Prévio";
   3. O campo "Data de Início do Aviso Trabalhado" será preenchido automaticamente com a data cadastrada no aviso prévio trabalhado.

* **Sem Aviso Prévio cadastrado**

1. Tipo de demissão como 2

* Considerando que não exista aviso prévio cadastrado, obrigatoriamente o sistema irá considerar o aviso prévio indenizado.

2. Tipo de demissão como 4

Deverá ser escolhido entre os parâmetros:

* + Tem Aviso Prévio Indenizado
  + Desconta Aviso Prévio

Obs.: Caso o funcionário não tenha aviso prévio indenizado e nem descontado, deverá selecionar no campo "Indicador de cumprimento de Aviso Prévio" com a opção "Aviso Prévio indenizado ou não exigível" para dar prosseguimento no cálculo da rescisão.

 

Ambos

O parâmetro "Aviso Misto" não ficará disponível  quando não existir um aviso trabalhado previamente cadastrado.

**Observações**:

1. Caso ocorra o cancelamento da rescisão de um funcionário que possua aviso prévio cadastrado, o mesmo terá sua situação retornada para "V - Aviso Prévio", para que a situação volte à "A - Ativo", será necessário executar o processo de cancelamento do aviso prévio presente no menu "Rescisão".
2. Ao cancelar um Aviso Prévio cujo "Motivo de Cancelamento" seja "Exclusão do Aviso", será gerado um gatilho para um registro de evento S-3000 na Fila de Eventos do eSocial.

divs
