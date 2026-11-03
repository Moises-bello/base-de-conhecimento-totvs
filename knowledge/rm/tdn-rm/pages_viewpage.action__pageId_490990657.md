---
content_hash: d03c7e8bd1a7a53129854e756e3ef34a910ca770c83159db46835f5fcc11934b
fetched_at: '2026-06-29T00:10:21.661430+00:00'
page_id: '490990657'
product: rm
source: tdn-rm
title: Meu Imóvel - Boletos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=490990657
version: 35
---

Nesta página o usuário terá à disposição informações dos boletos associados aos seu contratos, tanto de vendas, quanto de aluguel ou ambos, caso existam.

Somente boletos em aberto e registrados ou registrados online (CNABSTATUS IN ('2','5')) na instituição bancária, serão mostrados no aplicativo Meu Imóvel.Novidade!

A partir do Release 12.1.2502 é possível de visualizar os Boletos em aberto para:

* Condomínio;
* Fundo de promoção;
* Evento Financeiro (avulso); e
* Aluguel complementar.

Reforçando que em Releases anteriores o sistema já exibia os boletos dos contratos de locação.

As funcionalidades da tela de boletos, quando acessada via aplicativo Meu Imóvel, são:

* **Copiar Código de Barras:** Copia o número do código de barras para a área de transferência do dispositivo, permitindo que seja usado posteriormente para envio via outro aplicativo ou pagamento direto no APP de seu banco.
* **Enviar boleto por:** Efetua o download do PDF e permite compartilhar / salvar este arquivo em seu aplicativo de preferência. Por exemplo, enviá-lo por um e-mail via app do Gmail, ou compartilhar com outro contato, através do Whatsapp ou Telegram.

Importante!Caso não exista um relatório específico para segunda via de boleto associado ao convênio bancário, ou associado na tabela de defaults de banco (Integração Protheus) o Meu Imóvel somente irá permitir a cópia do código de barras e não exibirá o menu "Enviar boleto por".**Observação**: Selecionando um boleto (tocando na linha de Unidade e valor), abrirá uma nova tela que irá exibir, além dos dados da tela anterior, detalhes da parcela (somatório), como valor de juros, correção monetária e multa. Outros componentes da parcela que gerem outros valores de integração, serão exibidos com a descrição "Outros", assim como é exibido no relatório Ficha Financeira.

Para boletos que agrupem vários lançamentos, são exibidas informações resumidas da origem de cada lançamento indicando se ele corresponde a parcela de contrato de financiamento habitacional, parcela de contrato de locação ou parcela de despesa.

Na tela de detalhes do boleto, estará disponibilizada a opção "**Baixar PDF**". ao tocar nesta opção o usuário terá a visualização do boleto em formato .pdf, possibilitando que o mesmo seja também salvo na memória do seu telefone.

Caso não existam boletos em aberto e registrados (CNABSTATUS <> 2 e CNABSTATUS <> 5) na instituição bancária, será exibido a tela abaixo:
