---
content_hash: 3d6063077d67e8abb94d331315468edd7ace64d30f2a21cb38c4cb5f166e1c79
fetched_at: '2026-06-29T00:10:31.045211+00:00'
page_id: '520659378'
product: rm
source: tdn-rm
title: Contrato de Locação - Gestão - Multas contratuais
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=520659378
version: 11
---

Para acessar a funcionalidade seguir o seguinte menu: Aluguel > Contratos de Locação > Contrato de Locação > Anexos > Multa.  
Esta funcionalidade está associada aos contratos de locação. A multa cadastrada poderá ser cobrada quando da rescisão antecipada do contrato de locação, ou mesmo quando da retirada de algum imóvel ou área do contrato de locação antes de um dado prazo.

**Pré-condições**

* Ter cadastrado um

**Campos do cadastro de Multa**

* **Código da Multa:**Código da multa cadastrada. O valor é gerado automaticamente pelo sistema assim que o cadastro é salvo
* **Data de Expiração:** A multa só será passível de cobrança caso a rescisão do contrato ocorra até desta data, ou a retirada de algum imóvel ou área de imóvel ocorra até esta data
* **Descrição:** Descrição para a multa
* **Valor:** Valor informando para a multa. Caso seja informado, não será possível informa fórmula para o valor da multa.
* **Fórmula:** Fórmula para cálculo do valor da multa. Pode buscar informações do contrato, dos imóveis e/ou áreas dos imóveis, despesas e com isso calcular o valor desejado para a multa. Uma vez informada, não é possível informar um valor fixo para a multa. É possível usar o botão  para calcular o valor da multa e a memória de cálculo que resultou neste valor.
* **Parâmetro de integração financeira:**  usado para gerar o lançamento que será usado para cobrar a multa.
* **Código regra de vencimento:**  usada para gerar o lançamento que será usado para cobrar a multa. **¹**
* **Tipo de evento financeiro:**  usado para gerar o lançamento que será usado para cobrar a multa.
* **Despesas:**  a serem consideradas ao cobrar a multa. Caso a multa tenha valor informado, este valor é sempre atualizado para o somatório dos valores das despesas, sempre que se altera as despesas vinculadas.

falseExceções para regra de emissão / vencimento

* Quando a multa for utilizada em um processo de rescisão de contrato, a mesma é gerada agregada ao valor do encerramento. Neste cenário a regra de vencimento informada na multa é ignorada e a data de vencimento é definida como default a data do evento financeiro. Esta data pode ser alterada ao editar o evento gerado, antes do mesmo ser integrado ao efetivar a rescisão.
* Quando o evento financeiro é gerado pelo cálculo da rescisão, o sistema utilizará a data do encerramento como default para a data do evento financeiro gerado. Esta data pode ser alterada ao editar o evento gerado, antes do mesmo ser integrado ao efetivar a rescisão.
* A data de emissão será sempre igual a data do evento financeiro, caso o usuário não configure o comportamento nos [parâmetros do Aluguel](https://tdn.totvs.com/pages/viewpage.action?pageId=435105240#TotvsIncorpora%C3%A7%C3%A3o-Par%C3%A2metros-Aluguel-EventoFinanceiro).
