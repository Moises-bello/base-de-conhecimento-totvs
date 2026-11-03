---
content_hash: db3ec6978430c674e262a1c711bb291751414815b01dcdcf67d5bc0dcd122ade
fetched_at: '2026-06-29T00:12:08.445314+00:00'
page_id: '934632073'
product: rm
source: tdn-rm
title: Contrato de Locação - Aditivos - Alteração de Parâmetros do Aluguel Complementar
  (v12.1.2506+)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=934632073
version: 1
---

Importante: Dada a liberação da modificação de alteração das faixas de aluguel complementar pelo usuário, removemos a opção de alteração de faixas via aditivo.

Este aditivo permite alterar os parâmetros de aluguel complementar, já cadastrado previamente em um determinado contrato efetivado.

**Pré-condições**

* Ter habilitado a permissão [02.03.01.36 e 37] para Efetivar / Desfazer aditivo de Alteração de Parâmetros do Aluguel Complementar, do perfil do TOTVS Gestão de Imóveis, localizada em *Serviços Globais / Segurança / Perfis.*
* Ter efetivado o Contrato de Locação
* Ter incluído um Motivo do Aditivo

#FF9000Campos da tela Identificação:

* **Código do aditivo:** Código do aditivo realizado, campo preenchido automaticamente  pelo sistema;
* **Data do aditivo:** Data da criação do aditivo. A partir dessa data será aplicado no Contrato de Locação as alterações do aditivo;
* **Tipo de aditivo:** Exibe o Tipo de Aditivo no qual está sendo cadastrado. Esse campo é preenchido automaticamente pelo sistema, onde o é preenchido pelo Tipo de Aditivo selecionado no Anexo do Contrato de Locação >> Aditivo;
* **Situação do aditivo:** Exibe a situação do aditivo, que pode ser:
  + **Preparação:** O aditivo tem essa situação quando está sendo cadastrado e ainda não foi executado o processo "Efetivar Aditivo" ou quando é executado o processo "Desfazer Aditivo" em um aditivo com a situação "Efetivado". Nessa situação é permitido alterar o aditivo e as modificações cadastradas não são aplicadas ao Contrato de Locação associado;
  + **Efetivado:**O aditivo tem essa situação quando é executado o processo "Efetivar Aditivo". Nessa situação não é possível alterar o aditivo. As modificações cadastradas já foram aplicadas ao Contrato de Locação, quando foi executado o processo "Efetivar Aditivo";
* **Motivo do aditivo:** Motivo do aditivo a ser executado. Novos motivos de aditivos podem ser criados através do Cadastro de Motivo do aditivo, que se encontra no seguinte caminho Aluguel >> Cadastros >> Motivo de aditivo.
* **Número do Aditivo no Cliente:** Campo onde o cliente informa o número do Aditivo no Contrato físico. Podendo assim realizar o agrupamento de vários aditivos do sistema a um aditivo físico.

#FF9000Aba de Parâmetros

* **Parâmetro antigo - Aluguel Complementar:** Todas as informações nesta região são apenas informativas e mostram a fórmula de cálculo e a taxa de participação já cadastradas para o Aluguel Complementar.
* **Parâmetro novo - Aluguel Complementar:** Nesta região será possível informar uma nova fórmula, bem como uma nova taxa de participação para o Aluguel Complementar, como vemos abaixo:
  + **Tipo de Evento Financeiro:** O evento que será usado na geração de lançamentos.
  + **Buscar Vencimento:** Se irá informar ou buscar do contrato.
  + **Regra de Vencimento:** Caso seja informar será aberto para seleção.
  + **Buscar Parâmetro:**Se irá informar ou buscar do contrato.
  + **Parâmetro de Integração Financeira:**Caso seja informar será aberto para seleção.
  + **% Taxa de Participação no faturamento:** Neste campo será definido o novo percentual para a taxa de participação. Caso queira informar apenas uma nova fórmula, o usuário poderá manter a Taxa de Participação antiga, e alterar somente a fórmula.
  + **Mínimo (Opções relativas ao aluguel mínimo)**
    - **Valor Período:** O mínimo que deve ser faturado em determinado período
    - **Meses:** Período para geração do aluguel complementar

**Incluindo um Aditivo de Alteração de Parâmetros do Aluguel Complementar**

* Selecione o Contrato de Locação e acesse: Anexo / Aditivo / Alteração de Parâmetros do Aluguel Complementar.
* Clique em Incluir Aditivo de Alteração de Parâmetros do Aluguel Complementar. Preencha os campos:

* + **Data do Aditivo:** A data do aditivo deve estar dentro do período de vigência do Contrato de Locação. Esta data será utilizada como data inicial dos novos registros de aluguel em dobro criados pelo aditivo.
  + **Motivo do Aditivo**: Informar um Motivo do Aditivo.
  + Clique no campo de fórmula de cálculo do aluguel complementar para alterar a fórmula de cálculo, bem como defina a nova taxa de participação no faturamento.

* Salvar e [Efetivar Aditivo](https://tdn.totvs.com/display/LRM/Aditivo+-+Processo+-+Efetivar+Aditivo)
* Verifique que o status do Aditivo foi alterado para Efetivado.

**Efetivação do Aditivo de Alteração de Parâmetros do Aluguel Complementar**

Ao efetivar o aditivo, o processo permitirá ao usuário informar se as medições existentes serão regeradas com os novos parâmetros. 

*Tela da efetivação do aditivo, com a opção de regerar os lançamentos das medições marcada.*

Importante!

* Para as medições que possuem o status "Pendente" ou seja, que ainda não estão integradas e sem lançamento financeiro, estas continuarão com este status, mesmo com o usuário optando pela regeração;
* O sistema sempre obterá as medições da próxima competência após a data do aditivo. Por exemplo, se o aditivo tem a data 15/01/2019, a medição de competência 01/2019 não irá obter os valores atualizados do aditivo. Apenas a medição de competência 02/2019 e por diante.
* O processo de aditivo de alteração do parâmetro financeiro complementar entra em vigor a partir da data do aditivo. Caso a geração do lançamento complementar ocorra antes dessa data, será considerado o parâmetro anterior, ou seja, o parâmetro que foi utilizado no momento da geração do lançamento.
* Ao acessar o menu Evento financeiro  correspondente a este contrato será observado que o campo "Parâmetros de integração financeira" sempre exibirá o parâmetro  
  financeiro complementar utilizado na criação do evento.

Como Fazer

---

* [Efetivar Aditivo](https://tdn.totvs.com/display/LRM/Aditivo+-+Processo+-+Efetivar+Aditivo)
* [Desfazer Aditivo](https://tdn.totvs.com/display/LRM/Aditivo+-+Processo+-+Desfazer+Aditivo)
