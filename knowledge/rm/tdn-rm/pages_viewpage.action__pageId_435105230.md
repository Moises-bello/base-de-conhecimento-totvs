---
content_hash: d722a53956b87f1fa64cbd0fa25a072403520bba645b52daf29af31674e4d232
fetched_at: '2026-06-29T00:09:49.090582+00:00'
page_id: '435105230'
product: rm
source: tdn-rm
title: Condomínio - Manutenção de Empreendimentos - Síndico
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435105230
version: 6
---

Este cadastro é utilizado no módulo de Condomínio, para realizar o cadastro de Síndicos.

Ao cadastrar um síndico o sistema pode ou não realizar a isenção de cobranças no condomínio para o mesmo. É importante ressaltar que, para que a cobrança seja isenta devemos além de cadastrar o síndico, associar também os itens de cobrança onde irão ocorrer a isenção.

Os campos são nesta tela são:

* **Código:** Código do síndico cadastrado.
* **Empreendimento:** Empreendimento vinculado ao síndico.
* **Unidade:** Unidade vinculada ao síndico. Importante: Quando o campo "Aplica Isenção da Taxa de Condomínio" estiver desmarcado, o cadastro de unidade não é obrigatório.
* **Subunidade**: Subunidade vinculada ao síndico. Obrigatório e necessário para identificar qual subunidade será isenta de cálculo no Fechamento Individual. Quando o campo "Aplica Isenção da Taxa de Condomínio" estiver desmarcado, o cadastro de subunidade não é obrigatório.
* **Cliente/Fornecedor:** Informações do Síndico.
* **Data de Início do Mandato:** Início do Mandato para o síndico.
* **Data Final do Mandato:** Fim do Mandato para o síndico.
* **Aplica Isenção da Taxa de Condomínio:** Marcando esta opção, o Síndico estará isento de cobrança para todos os itens associados neste cadastro.

Este cadastro está disponível também como anexo para os cadastros de Empreendimento e Unidade/Subunidade no módulo de Condomínio.

### **Realizando o cadastro do síndico e seus efeitos na cobrança**

---

Veja o cadastro abaixo:  
Na imagem, estamos dizendo que o Síndico associado a Subunidade 000001 terá isenção nos cálculos de todos os itens de cobrança associados ao **Empreendimento 2046**

Entendemos então que no período do ano de 2025, o sindico estará isento de cobranças nas competências dentro de seu mandado.

### Efeito no condomínio individual

---

No exemplo, realizamos um fechamento individual para a subunidade 000001. Na competência 02/2025

Ao verificar os cálculos temos para a subunidade 000001, um cálculo de cobrança direta.

Verifique que, ao acessar a apuração desta subunidade que temos R$ 2500,00 calculados. Porém, como temos essa cobrança direcionada ao síndico, a mesma é isenta de cobrança. Veja o campo "Cálculo isento  = Sim".

Ao gerar o financeiro não serão gerados lançamentos para essa subunidade.
