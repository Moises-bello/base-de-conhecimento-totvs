---
content_hash: 2ee43e3a57b80e937cb955a912bbeb946c43ac74281b0e0b51fb4f395eb39cbb
fetched_at: '2026-06-29T00:09:25.887053+00:00'
page_id: '423938194'
product: rm
source: tdn-rm
title: Cupom Fiscal
type: documentation
url: https://tdn.totvs.com/display/LRM/Cupom+Fiscal
version: 28
---

**Informamos que possui dados pessoais contidos nesta entidade.**

**Para mais informações sobre a LGPD e as soluções oferecidas pela TOTVS consulte nossa página neste link ([https://tdn.totvs.com/pages/releaseview.action?pageId=514427789](https://tdn.totvs.com/pages/releaseview.action?pageId=514427789 "Follow link")).**

O cadastro de Cupom Fiscal é utilizado para incluir/editar cupons fiscais que não foram incluídos através do processo de importação/integração com os softwares de frente de loja, permitindo o cadastro manual de todas as informações do cupom (valores financeiros, itens e pagamentos), bem como, processos de cálculo, rateios e associação de Redução Z.

Além disso, as rotinas permitem o cálculo e a validação das informações inseridas no cupom para posterior vinculação a movimentos já inseridos no sistema.

O cadastro do Cupom Fiscal pode ser acessado através do menu Cadastros | Fiscais | Mais\[...\] | Cupom Fiscal.

**Importação de Cupom Fiscal / Movimento via TXT**

* Para inclusão do Movimento/Cupom Fiscal via importação de arquivo TXT, deve-se utilizar o conceito de Movimento V4(disponível em C:\TOTVS\CorporeRM\ObjetosGerenciais\Conceitos) de acordo com o layout de importação de movimento V4 disponível em C:\TOTVS\CorporeRM\ObjetosGerenciais\Layout;
* A inclusão do movimento através da importação gera de forma automática o cupom fiscal e sua associação ao movimento;
* Na importação, quando todos os itens do cupom estão cancelados, na linha do movimento, o campo referente a status deve conter o valor  C (cancelado) e a(s) linha(s) do(s) item(s) esteja com campo cancelado como N (não). O arquivo estando desta forma, tanto o Cupom Fiscal quanto o movimento serão criados como Cancelado, contendo o(s) respectivo(s) item(s).
* Na importação, para item cancelado em cupom com 2 itens ou mais, a posição referente ao status do item(Linha I, posição 815) deve conter o valor  S (cancelado) e N (não Cancelado). O arquivo estando desta forma, tanto o Cupom Fiscal quanto o movimento serão criados. O movimento será criado sem o item cancelado no arquivo importado e o cupom será criado com o item tendo sua flag marcada como Item de Cupom Cancelado.

**Inclusão de **Cupom Fiscal**via TotvsMessage ou Web Service**

No processo de inclusão do Cupom Fiscal, via TotvsMessage ou Web Service, é seguida a seguinte regra:

1. Quando o CPF do Adquirente vem preenchido e o Nome do Adquirente está em branco no arquivo XML de inclusão de Cupom Fiscal, é realizada uma consulta no cadastro de Cliente / Fornecedores para buscar o nome do mesmo.
2. Caso seja encontrado mais de um cadastro com o mesmo CPF/CNPJ, não é preenchido o Nome do Adquirente.

***Observação*:** Essa regra se aplica a Cupom Fiscal do tipo "SAT", "NFC-e"ou "Normal".
