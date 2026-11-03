---
content_hash: c9b43717b804d760f58100f35b087d9ef8a95f5a9c72e40ec4fcd51beaf1b3aa
fetched_at: '2026-06-29T00:12:03.642665+00:00'
page_id: '912370568'
product: rm
source: tdn-rm
title: PI - Proposta - Validar VPL
type: documentation
url: https://tdn.totvs.com/display/LRM/PI+-+Proposta+-+Validar+VPL
version: 11
---

### Introdução

---

Será processado diversas validações configuradas na modalidade da proposta***,*** entre eles, o percentual mínimo e máximo de número de parcelas, valor de entrada, número de prestação antes e depois da entrega e TMA.

### Utilização

---

O parâmetro **'Usar Alçada de Aprovação como Desconto ao Invés de VPL'**, localizado em *Ambiente > Parâmetros > Portal de Imóveis > Proposta de Venda (3/3)*, altera o critério de validação da alçada. Quando ativo, o sistema passa a validar a alçada com base no **Desconto** aplicado, substituindo a validação por **VPL**. Desta forma, a hierarquia de prioridade para o desconto torna-se: 1º Alçada de Desconto e 2º Por Modalidade.

Nessa configuração, o sistema **não usa** o cálculo padrão de VPL, que considera ganho financeiro no tempo (*juros, correção, prazo, financiamento etc*.).  
Em vez disso, ele trabalha apenas com:

* Valor de tabela do imóvel;

* Valor proposto ao cliente;

* Percentual máximo permitido pela alçada;

* Percentual máximo permitido pela modalidade.

O objetivo é garantir que o desconto aplicado **não ultrapasse o limite permitido**, sempre escolhendo o valor **mais restritivo**.

#### **Como o sistema define o limite válido**

Sempre que esse parâmetro estiver ativado:

1. O sistema verifica qual é o **percentual máximo de desconto** permitido pela **Alçada de Aprovação;**

1. Verifica também o percentual máximo permitido pela **Modalidade de Venda;**

1. O sistema compara os dois valores e determina o limite válido como sendo **o menor deles** (o mais restritivo);

1. Se a proposta ultrapassar esse limite, ela é marcada como **reprovada** e o usuário recebe um aviso claro informando o motivo.

Exemplo**Situação do Imóvel**

* Valor de tabela (preço cheio): R$ 200.000,00

**Regras configuradas**

* Alçada de Aprovação: permite até 2% de desconto
* Modalidade de Venda: permite até 3% de desconto

**Determinação automática do limite**

* O sistema compara os percentuais:

* + 2% (alçada)
  + 3% (modalidade)

* Limite válido = 2%, porque é o mais restritivo.

---

**Cálculo do valor mínimo permitido**

* 2% de desconto sobre R$ 200.000,00 = **R$ 4.000,00**
* Valor mínimo permitido para proposta: R$ 200.000,00 – R$ 4.000,00 = **R$ 196.000,00**

---

**Exemplo de proposta feita pelo corretor**

* Valor proposto: **R$ 185.000,00**
* Diferença para o valor de tabela: R$ 200.000,00 – R$ 185.000,00 = **R$ 15.000,00**
* Percentual de desconto real aplicado: 15.000 / 200.000 = **7,5%**

---

**Resultado**

* Proposta reprovada automaticamente.
* Motivo exibido ao usuário: "O desconto aplicado ultrapassa o limite permitido pela alçada de aprovação (máx. 2%)."

Caso este parâmetro permaneça desmarcado, a validação será realizada com base no VPL (Valor Presente Líquido). A hierarquia de prioridade para o cálculo seguirá a ordem: 1º Alçada, 2º Modalidade e 3º Empreendimento.

VPL da Alçada: 

VPL da Modalidade e outros parâmetros de validação:

VPL do Empreendimento:

Já nos componentes da modalidade existem parâmetros que impedem a alteração do registro se não atender a configuração, aqui não existe a possibilidade de aprovação do gestor.  
Para ver mais, consulte:
