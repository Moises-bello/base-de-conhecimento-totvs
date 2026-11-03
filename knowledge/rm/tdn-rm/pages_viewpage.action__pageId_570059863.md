---
content_hash: 44c94174ad7d8806dbf5d1c5e9c124ad8c0e2d422b1415bd71958f606d5f9125
fetched_at: '2026-06-29T00:10:52.100282+00:00'
page_id: '570059863'
product: rm
source: tdn-rm
title: Propostas - Comissão
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=570059863
version: 12
---

#FF9000Cálculo de comissão do gerente

Quando o empreendimento possui um [gerente](https://tdn.totvs.com/display/LRM/PVI+-+Backend+-+Empreendimentos) definido em seu cadastro e esse gerente possui um percentual de comissão preenchido no empreendimento, O Portal de Imóveis automaticamente irá aplicar este percentual subtraindo diretamente do percentual da comissão do corretor.

Exemplo: Se o Empreendimento/Usuário/Imobiliária/Grupo tem 5% de comissão e o empreendimento tem definido como comissão do Gerente 0,5% de comissão, quando a proposta for salva, nas informações da comissão da proposta, teremos 4,5% definidos como comissão do Corretor e 0,5% como comissão do Gerente.

Lembrando que a comissão do gerente somente será calculada se o campo "Percentual de comissão do gerente" estiver cadastrado no empreendimento em questão.

Importante: Quando existe percentual de comissão do gerente cadastrada para um empreendimento o Portal de Imóveis irá sempre considerar este percentual de comissão para o gerente, independente se a comissão estipulada ao corretor foi zerada.

Veja a figura abaixo o exemplo deste cálculo, na proposta já salva:

**Importante:** Não será possível alterar o percentual de comissão definido para o corretor para valores acima do calculado através da meta de comissão deste empreendimento.

**Exemplo**:

Empreendimento com uma meta de comissão com uma faixa de retirada de 2% para Propostas com descontos entre 0,01% e 5.00%

Um corretor com um percentual de comissão de 10%, ao gerar uma proposta com desconto na faixa acima, terá uma comissão calculada de 8%.

Neste exemplo, não será possível alterar este percentual de 8% para um maior percentual, visto que ultrapassa a meta.

#FF9000Cálculo de comissão do diretor

A comissão do diretor será também calculada ao salvar uma proposta. Para que isso aconteça, devemos primeiro definir o diretor e o seu percentual de comissão dentro do

A comissão do diretor não tem vínculos com a comissão do corretor / gerente exemplificada acima.

Importante: Devido ao parâmetro **Identificação do vendedor enviado para backoffice no instante do envio da venda o PVI irá se comportar da forma abaixo ao enviar os vendedores ao RM: o Portal de Imóveis tem o seguinte comportamento ao enviar a Venda ao RM:**

* Caso a comissão possua distribuição para o Diretor de acordo com os parâmetros do Empreendimento e este Diretor possua CPF / CNPJ cadastrado no RM, ao enviar a venda o Diretor será enviado como Vendedor, independente do parâmetro.
* Caso a comissão possua distribuição para o Gerente de acordo com os parâmetros do Empreendimento e este Gerente possua CPF / CNPJ cadastrado no RM, ao enviar a venda o Gerente será enviado como Vendedor, independente do parâmetro.
* Caso o Corretor não tenha CPF / CNPJ cadastrado no RM, não será enviado o Vendedor para o RM.

Caso o parâmetro "**Identificação do vendedor enviado..."**seja:

* **Imobiliária:** Somente será levado como Vendedor caso o Corretor possua em seu cadastro uma Imobiliária. A Imobiliária deve possuir CPF / CNPJ cadastrado no banco RM.
* **Corretor / imobiliária:** Caso o Corretor possua em seu cadastro uma Imobiliária, serão enviados como vendedores tanto o Corretor quanto a Imobiliária. Para que sejam enviados ao RM, eles devem possuir CPF / CNPJ cadastrado no banco RM.
#FF9000Nova Comissão - Portal Imóveis e TCGI

Com o uso da nova Comissão, toda a parametrização das Comissões passa a ser realizado e controlado no TCGI.

Para mais detalhes sobre esta funcionalidade consulte a documentação **[TOTVS Construção Gestão de Imóveis - Comissão](https://tdn.totvs.com/pages/viewpage.action?pageId=665033766)**
