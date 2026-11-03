---
content_hash: 6c87472b642797dfb93f15a508d9500e8d0918281e06469e59080dd4d4cdde57
fetched_at: '2026-06-29T00:09:50.837200+00:00'
page_id: '436275389'
product: rm
source: tdn-rm
title: Novidades 12.1.23 - TOTVS Construção Gestão de Imóveis
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=436275389
version: 16
---

* **Vendas**
  + **[Menus Financeiros no TOTVS Incorporação](http://tdn.totvs.com/pages/viewpage.action?pageId=438279829):**Menus de Recebíveis do Financeiros incorporados no TOTVS Incorporação:

* + - Banco
    - Conta Caixa
    - Bancos / Agências
    - Conta Corrente
    - Convênio
    - Financeiro
    - Lançamentos
    - Boletos
    - Posição Financeira
    - Baixas
    - Integração Bancárias
    - Cadastros bancários
    - Cobrança
    - Débito Automático
    - Processo em lote
    - Registro online
    - Remessa de Cobrança
    - Remessa de Débito Automático

* **Retirada de parâmetros de reajuste:**Alguns parâmetros de reajuste serão retirados do sistema a partir da versão 12.1.23. Caso esses parâmetros estiverem habilitados, ao executar um reajuste, aparecerá no log do processo uma mensagem de aviso, informando quais parâmetros serão descontinuados do TIN. São eles:

* + - Utiliza data vencimento para definir se a correção será com índice antes ou após.
    - Calcula Correção Monetária sobre o Saldo Devedor Total Amortizado.
    - Calcula Juros de Contrato sobre o Saldo Devedor Total Amortizado.
    - Valores calculados na correção serão arredondados mês a mês.

* **Aluguel**

* + **[Campos Complementares Tipo de Despesa e Despesa](http://tdn.totvs.com/display/LRM/Controle+de+Despesa+-+Tipo+de+Despesa):**Foram criados Campos Complementares para os cadastros de Tipo de Despesa e Despesa;
  + **[Pesquisa de CEP](http://tdn.totvs.com/pages/viewpage.action?pageId=435105278):**Para facilitar o cadastro de endereço o sistema passa a carregá-lo automaticamente, através do CEP no cadastro de imóveis. O usuário também poderá fazer uma pesquisa por logradouros, bairros, cidades e UF;
  + **[Alteração no processo de Importação de Medição de Faturamento](http://tdn.totvs.com/pages/viewpage.action?pageId=435105012)[:](http://tdn.totvs.com/pages/viewpage.action?pageId=435105012)** Foi implementado no **Contrato de Locação / Processo de Importação de Medição de Faturamento** o campo Número do Contrato de Locação, sendo que esta implementação facilita no momento de informar os contratos a serem buscados. Com isso, o sistema possibilita realizar a busca dos contratos de outra forma;
  + **[Escalonamento com Prioridade](http://tdn.totvs.com/display/LRM/DT+Aluguel+-+Prioridade+de+Escalonamento)**: Inclusão do campo **Prioridade** no cadastro de escalonamento do contrato de locação. Este campo deve ser utilizado pelo usuário para informar a prioridade de um determinado escalonamento quando ocorre conflito de períodos entre escalonamentos. Este campo é numérico e o maior valor tem a maior prioridade;
  + **[Módulo de Condomínio](http://tdn.totvs.com/pages/viewpage.action?pageId=438279824)**: Disponíveis os menus [Manutenção de empreendimentos](http://tdn.totvs.com/pages/viewpage.action?pageId=435105380), [Básicos](http://tdn.totvs.com/pages/viewpage.action?pageId=435105228) e [Fechamento do Condomínio](http://tdn.totvs.com/pages/viewpage.action?pageId=435104834), que controlam os cadastros e processos pertinentes ao módulo de condomínio;
  + **[Controle de Seguro](http://tdn.totvs.com/pages/viewpage.action?pageId=435104862)**: Disponíveis os menus [Seguro](http://tdn.totvs.com/display/LRM/Outros+-+Controle+de+Seguro+-+Seguro), [Modalidade de Seguros](http://tdn.totvs.com/display/LRM/Outros+-+Controle+de+Seguro+-+Modalidade+de+Seguros) e [Campos Complementares](http://tdn.totvs.com/display/LRM/Outros+-+Controle+de+Seguro+-+Campos+Complementares+de+Seguro), que controlam os cadastros e processos pertinentes ao módulo de seguro.

Para maiores informações a respeito das novidades da **release 12.1.23**, acesse aqui a [página dos nossos documentos técnicos](http://tdn.totvs.com/pages/viewpage.action?pageId=415710061).
