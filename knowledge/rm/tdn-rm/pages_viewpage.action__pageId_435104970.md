---
content_hash: 4f776ab630081808fd40904c0d94d75e7d9245ee9ec879dc395a2127e8c02d85
fetched_at: '2026-06-29T00:09:47.171978+00:00'
page_id: '435104970'
product: rm
source: tdn-rm
title: Encerrar / Rescindir - Processo - Rescindir
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435104970
version: 24
---

## ❌ Rescindir Contrato de Locação

A rescisão é o encerramento de um contrato antes do período previsto de vigência final e pode ocorrer por iniciativa do locador ou do locatário.

---

## **🛠️** Pré-condições

1. Ter  [efetivado](https://tdn.totvs.com/pages/viewpage.action?pageId=435105001) um Contrato de Locação.
2. Ter preenchido a [Lista de Verificação para Encerramento.](https://tdn.totvs.com/pages/viewpage.action?pageId=435105011)

---

## **📝** Rescindindo um Contrato de Locação

**Passo 1**  
Selecione o Contrato de Locação e acesse: **Anexo / Encerrar / Rescindir**.

**Passo 2**  
Clique em **Incluir**.

**Passo 3**  
Preencha os campos abaixo.  
  
🟨 Aba Identificação

* **Contrato de Locação**: Campo de preenchimento automático.
* **Código de Encerramento**: Campo de preenchimento automático.
* **Situação do Encerramento**: Campo de preenchimento automático.
* **Data de Encerramento**: Campo obrigatório.

📌 **Observação**  
A data informada na rescisão é considerada como dia locado, ou seja, o sistema entende que o imóvel ainda está em uso nessa data.

## ✅ Exemplo prático

*Se o cliente realizar a rescisão no dia 30/09, todas as parcelas com vencimento até o dia 30/09 (inclusive) serão mantidas.*  
*O sistema cancelará apenas os lançamentos a partir do dia 01/10, inclusive essa data.*

* **Data de Efetivação do Encerramento**: Campo de preenchimento automático.
* **Tipo de Rescisão**:

  + Unilateral solicitada pelo locatário
  + Unilateral solicitada pelo locador
  + Acordo bilateral
  + Outros

* **Rescisão**: Para que o encerramento do contrato seja realizado, este campo deve estar marcado.
* **% Taxa de Administração**:  
  Esse percentual terá prioridade sobre a taxa de administração definida no contrato de administração.  
  Para manter a taxa definida no contrato de administração, não informe o percentual no momento da rescisão ou informe o valor **0 (zero)**.  [Veja mais sobre esse procedimento (Clique Aqui).](https://tdn.totvs.com/pages/viewpage.action?pageId=1032880106)
* **Parâmetro de integração financeira:** O usuário pode definir um parâmetro específico para a geração dos lançamentos financeiros de rescisão. Caso este campo permaneça em branco, então o sistema irá utilizar os parâmetros definidos no contrato de locação;
* **Multa Contratual:** Associa uma multa à rescisão do contrato. O valor do Evento Financeiro de Rescisão será a soma do valor da Rescisão com o valor da Multa. **¹**
* **Observação:** Texto livre.

**Passo 4 -** Salvar  
**Passo 5 -** Acesse a Aba Cálculos de Rescisão:  
  
🔢Aba Cálculos da Rescisão

* **Fórmula Rescisória**: Campo de preenchimento automático.
* **Valor da Rescisão**: Campo de preenchimento automático.
* **Valor de Desconto**.
* **Valor Final da Rescisão**: Valor da Rescisão menos o Valor de Desconto.
* **Grid de Evento Financeiro**.

false

## 🧮 Cálculo da Rescisão – Locatário

Ao gerar os valores para o locatário, o sistema passa a marcar automaticamente, no evento, os parâmetros de incidência de taxa administrativa e DIMOB, além de definir a ação do locador como **pagar**.

Esses ajustes se aplicam exclusivamente aos contratos de aluguel que possuem contrato de administração vinculado ao imóvel.

Antes da efetivação da rescisão, é possível ajustar essas configurações diretamente no evento gerado.

Com essas alterações, ao efetivar a rescisão, o sistema passa a gerar os lançamentos considerando o valor de repasse definido no contrato de administração, utilizado para a geração do lançamento do locador.

**Passo 4**  
Salvar.

**Passo 5**  
Efetivar a rescisão.

false

## ⚙️Rescisão – Parâmetro Rescisão Marcado

Quando o evento de cobrança referente à rescisão ou à multa rescisória estiver configurado para calcular a taxa administrativa, e a ação do locador estiver definida como pagar, o percentual informado na rescisão — se houver — será utilizado no cálculo.  
Nesse caso, esse percentual terá prioridade sobre a taxa de administração definida no contrato de administração.

**✅ Finalização do Processo**

**Passo 6**  
Verifique que o status da rescisão foi alterado para **Efetivado**.

**Passo 7**  
Selecione o registro da rescisão e clique em **Editar**.

**Passo 8**  
O sistema exibirá a tela de rescisão com a memória de cálculo do encerramento no campo de observação, além das abas de cálculos de rescisão e histórico de eventos financeiros pendentes.

false

## 🔄Exceção para Regra de Vencimento da Multa Contratual

Quando a multa for utilizada em um processo de rescisão de contrato, ela será gerada agregada ao valor do encerramento. Nesse cenário, a regra de vencimento informada na multa é ignorada, e a data de vencimento será definida, por padrão, como a data do evento financeiro.

Essa data pode ser alterada ao editar o evento gerado, antes de sua integração ao efetivar a rescisão.

Quando o evento financeiro é gerado pelo cálculo da rescisão, o sistema utilizará a data do encerramento como padrão para a data do evento financeiro. Essa data também pode ser alterada antes da integração.

A data de emissão será sempre igual à data do evento financeiro, caso o usuário não configure comportamento diferente nos [parâmetros do Aluguel.](https://tdn.totvs.com/pages/viewpage.action?pageId=435105240#TotvsIncorpora%C3%A7%C3%A3o-Par%C3%A2metros-Aluguel-EventoFinanceiro)

false

## 🟨 Status “Em Aprovação”

Em um workflow do Fluig, a situação do cadastro da rescisão pode estar como **Em Aprovação**. Essa situação impede a edição do cadastro, porém permite que a rescisão seja efetivada.

false

## 🟧 Exclusão da Contabilidade

Quando o parâmetro de contabilização automática estiver marcado, o sistema excluirá automaticamente os lançamentos contábeis gerados e relacionados às competências posteriores à data da rescisão.

false

## 🟩 Outras Ações Possíveis em Contratos Rescindidos

🔹 **Confissão de Dívida:** Permite renegociar valores pendentes com base no histórico do contrato.

🔹 **Geração de Eventos Financeiros:** Aplicável para cobranças específicas, como honorários advocatícios ou taxas relacionadas a processos jurídicos.  Esses eventos permitem inserir novas cobranças, mesmo que o contrato esteja rescindido.

false

## 📑Uso de Contratos Rescindidos em Confissão de Dívida

**Motivo para permitir o uso**

Em muitos casos, o cliente em dívida já teve o contrato rescindido ou encerrado, pois não mantém mais uma relação ativa, como uma loja, mas ainda possui débitos pendentes.

Para negociar a dívida, é necessário que contratos rescindidos estejam acessíveis no sistema, mesmo que não possuam lançamentos ativos.

Apesar de rescindidos, os contratos de locação continuam sendo instrumentos válidos para determinados tipos de ações administrativas e financeiras.

Como Fazer

---

Efetivar Encerramento/Rescisão

Desfazer Encerramento/Rescisão
