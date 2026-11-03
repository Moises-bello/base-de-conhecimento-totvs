---
content_hash: 12babf3e72cb12ffe1878834808fc2dc4fec667a61c877aca8745184a210df62
fetched_at: '2026-06-29T00:12:10.870809+00:00'
page_id: '954073260'
product: rm
source: tdn-rm
title: Passo a Passo para atualizar o Saldo de FGTS do funcionário
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=954073260
version: 16
---

#### **Objetivo:**

Orientar, de forma clara e detalhada, como realizar a atualização do saldo de FGTS do funcionário no sistema TOTVS Folha de Pagamento, utilizando as cotações mensais e a data do último saldo informado, garantindo que os campos relacionados ao FGTS sejam atualizados corretamente tanto para fins rescisórios quanto para o Saldo conforme CEF.

**1. Obtenha o extrato da Caixa**

Pegue o extrato do FGTS do funcionário referente ao mês que deseja atualizar.

**Exemplo:** se for atualizar a partir do mês 03/2025, utilize o extrato correspondente a esse mês.

#### **2. Cadastre o saldo inicial**

No menu Funcionário | Anexos | Folha de Pagamento | Manutenção do FGTS, inclua o valor deSaldo Inicial conforme consta no extrato da Caixa.

* Selecione o "Tipo Lançamento" igual a "Saldo Inicial".
* Informe no campo "Data Lançamento" a última data existente no campo "Data" do extrato da Caixa. Conforme print no item 1.

#### **3. Atualize os dados no cadastro do funcionário**

No menu Funcionário | Pasta FGTS/SEFIP, deverá preencher os campos abaixo, conforme informações existentes no extrato da Caixa:

* **Saldo FGTS na CEF:** corresponde ao valor apresentando no campo "**SALDO**" do extrato da Caixa;
* **Saldo FGTS Fins Rescisórios:** corresponde ao valor apresentando no campo "**Valor Base para Fins Rescisórios**" do extrato da Caixa;
* **Data Última FGTS**: a data deve ser composta sempre com o dia 10 e mês e ano do campo "**Atualizado em**" do extrato da Caixa.

**Exemplo:** Conforme extrato da Caixa demonstrado no item 1.

falseATENÇÃO:

Ao utilizar o extrato da Caixa, é imprescindível informarexatamente os valores que constam no documento. Esses valores devem ser usados para preencher os campos "Saldo FGTS na CEF", "Saldo FGTS para Fins Rescisórios", "Valor Base para Fins Rescisórios" e "Data da Última Movimentação do FGTS". **Não é permitido realizar cálculos manuais** ou subtrair valores de lançamentos para preencher essas informações.

#### **4. Verifique as cotações**

No menu Administração de Pessoal | Cadastros Globais | Cotações, confira se as cotações do FGTS estão cadastradas corretamente.

⚠️ **Importante:** As cotações devem ser cadastradas **com base no mês anterior** ao da atualização.

**Exemplo:** Para atualização de Maio, utilize a cotação de Abril.

#### **5. Execute a atualização**

No menu Administração Pessoal | Alterações Cadastrais | Atualização do Saldo de FGTS realize o processamento para que os dados sejam atualizados conforme descrito abaixo:

Verifique que o valor ficou igual ao do novo extrato da Caixa:

Conforme o novo extrato da Caixa (vide print acima), o funcionário realizou dois saques no mês de 06/2025. Para que o sistema considere esses valores como abatimentos no campo "Saldo FGTS na CEF", acesse o menu Funcionário | Anexos | Folha de Pagamento | Manutenção do FGTS e inclua o valor do saque, utilizando o Tipo de Lançamento igual a "Débito / Resgate / Saque".

**Atenção:** Caso existam dois saques na mesma data, como no exemplo apresentado, some os valores, pois o campo **"**Data de Lançamento" é uma chave primária e não permite múltiplos registros com a mesma data.

No cenário do exemplo, o valor total a ser lançado é **R$5.068,13** (R$1.911,64 + R$3.156,49). Ao salvar o registro com o tipo "Débito / Resgate / Saque", o sistema aplicará automaticamente o sinal de negativo (–) ao valor, considerando-o como abatimento no saldo.

Lembrando que, após salvar os valores do SALDO, o sistema recalculará automaticamente o campo "Saldo FGTS na CEF".

Sempre que desejar que o campo "**Saldo FGTS Fins Rescisórios"** seja recalculado deverá executar o processo Recálculo Saldo de FGTS, existente no menu Administração Pessoal | Alterações Cadastrais. Veja detalhes no link [Recálculo do Saldo de FGTS](https://tdn.totvs.com/pages/viewpage.action?pageId=452718752)
