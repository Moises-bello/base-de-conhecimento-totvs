---
content_hash: 3ae4833e0a4b85a7811176718cfd4c7b107e18225e6bc9f8b041e2e7bfd7e796
fetched_at: '2026-06-29T00:09:21.999767+00:00'
page_id: '422545943'
product: rm
source: tdn-rm
title: Bloco A (EFD Contribuições)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422545943
version: 19
---

## Documentos Fiscais — Serviços (Sujeitos ao ISS)

1leftA001Registro A001**Registro A001 — Abertura do bloco A**  
Este registro informa se houve movimentação no bloco A.a010Registro A010**Registro A010 — Identificação do Estabelecimento**  
Gerado para cada filial que possuiu movimentação no período da escrituração.a100Registro A100

**Registro A100 — Documento — Nota Fiscal de Serviço**  
Este registro é gerado para lançamentos de serviço cujo CFOP é do tipo não fiscal  e que possuam os tributos PIS, COFINS, PIS Importação ou COFINS Importação.

Para lançamentos cancelados, o status segue a seguinte consistência:

* Se a data de cancelamento da nota for dentro do mês de geração da Rotina, o status dos lançamentos gerado no Registro A100 é igual a "Cancelado".
* Se a data de cancelamento da nota diferente do mês de geração da Rotina, o status dos lançamentos gerado no Registro A100 é igual a "Normal".

**Campo(14 VL\_DESC):**

Se o campo "Valor Total Recebido" estiver marcado (Anexo [Tributo do Produto do Município](https://tdn.totvs.com/pages/viewpage.action?pageId=423938770#TributosdoProdutoporMunic%C3%ADpio-NFS-e) na aba NFSe),

será gerado com o valor da diferença entre o valor total do documento e a base de cálculo do tributo ISS.

Senão,

será gerado com o valor dos Descontos do Lançamento Fiscal.

Este registro será gerado para lançamentos Fiscais cujo código modelo de documento for 55 (NF-e) e possuírem na natureza de operação a informação CFPS preenchida.a110Registro A110**Registro A110 — Complemento do Documento — Informação Complementar da NF**  
Este registro só será gerado se o lançamento declarado no registro A100 possuir o campo [INFCOMPLDOCFISCAL](http://tdn.totvs.com.br/pages/viewpage.action?pageId=190518894) e este estiver preenchido.a111Registro A111**Registro A111 — Processo Referenciado**  
Este registro só será gerado se o lançamento declarado no registro A100 possuir algum processo referenciado. Esta informação pode ser associada na Guia — pasta Outros Dados — Processo judicial.a120Registro A120**Registro A120 — Informação Complementar — Operações de importação**  
Este registro só será gerado se o lançamento declarado no registro A100 estiver associado a um CFOP de serviço iniciado com 3. Os itens do lançamento deverão possuir os tributos PIS e COFINS Importação.a170Registro A170

**Registro A170 — Complemento do Documento — Itens do Documento**  
Neste registro é gerada uma linha para cada item do documento fiscal. A tributação do PIS e da COFINS deverá estar nos itens para que este registro seja corretamente gerado.  
Os valores de PIS COFINS deste registro são transportados para o detalhamento da apuração ao encerrar o período de apuração de PIS e COFINS. O sistema irá consistir o CST e alíquota do PIS COFINS para identificar se o tributo é cumulativo ou não cumulativo, com ou sem direito a crédito.

Imagema990Registro A990**Registro A990 — Encerramento do bloco A**  
Este registro é gerado automaticamente pela rotina com a quantidade de linhas do bloco A.
