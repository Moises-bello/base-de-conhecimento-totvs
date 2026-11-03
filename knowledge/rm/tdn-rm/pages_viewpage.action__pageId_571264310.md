---
content_hash: 831d4aafafb16003c488bb671eb15a7c15e44cdf4d34b036d975d39278bbfc83
fetched_at: '2026-06-29T00:10:52.233007+00:00'
page_id: '571264310'
product: rm
source: tdn-rm
title: Contabilizar posteriormente (lançamento baixado)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=571264310
version: 2
---

**Introdução**

Para atender às demandas de mercado, o sistema permite que a contabilização da baixa seja realizada posteriormente oferecendo uma opção rápida e segura para o processo.

Para que esta contabilização seja realizada corretamente é essencial que a coligada esteja parametrizada para utilizar uma Tabela Default para Evento, pois é neste local que o sistema irá obter os dados necessários para a contabilização.

**Desenvolvimento/Procedimento**

Ao Baixar Lançamentos que sejam do “Tipo Contábil” igual a Baixa Contábil ou Contábil informando dados somente uma vez, é possível definir que a Contabilização de Baixa destes títulos será informada posteriormente. Para isso, basta marcar a opção Contabilizar Posteriormente que será apresentada na janela de Confirmação de Baixa, como no exemplo abaixo:

A opção de Contabilizar Posteriormente será ainda apresentada na janela dos seguintes processos:

* Retorno de Cobrança Registrada
* Retorno de Cobrança Não Registrada
* Retorno de Cobrança CNAB240
* Retorno de Pagamento
* Retorno de Pagamento CNAB240

Observações:

|  |
| --- |
| Ao realizar a Baixa de Lançamentos marcando tal opção, o Tipo Contábil dos Lançamentos envolvidos será alterado para “Contábil com Baixa a contabilizar” ou “Baixa a contabilizar”, de acordo com o Tipo Contábil anterior dos Lançamentos. O sistema fará consistência desta informação e só efetuará a contabilização se o Tipo Contábil dos Lançamentos selecionados for os citados acima.  Para Contabilizar os Lançamentos Baixados, selecione o(s) lançamento(s), acesse o Assistente de Implantação de Processos / Contabilidade / Contabilizar Lançamentos Baixados. O sistema efetuará a contabilização de baixa dos lançamentos selecionados usando o Evento Contábil associado à tabela Default para Evento. |

**Informações Adicionais**

A opção Contabilizar Posteriormente só será visualizada se o parâmetro “Usar Contabilização de Mútuo” estiver desmarcado no Assistente de Implantação de Processos do sistema / Integração contábil / Etapa Contabilização do Extrato de Caixa).

Caso não haja amarração do evento contábil a contabilização não será efetuada. Esta amarração deve ser feita conforme parâmetros da contabilidade, no Assistente de Implantação de Processos (menu Opções > Parâmetros > TOTVS Gestão Financeira > Integração Contábil > Contab. Financeiro > Opção: Tabela Default para Evento).
