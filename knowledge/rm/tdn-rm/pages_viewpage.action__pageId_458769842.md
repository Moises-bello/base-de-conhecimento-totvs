---
content_hash: ef118c967484150e7537f619f100e8007b3223fd70dbce813a515156ec280744
fetched_at: '2026-06-29T00:10:13.915565+00:00'
page_id: '458769842'
product: rm
source: tdn-rm
title: TOTVS Construção Gestão de Imóveis - Acordo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=458769842
version: 16
---

### Introdução

---

Com o intuito de flexibilizar o parcelamento e pagamentos de débitos de contratos de locação e vendas, foi disponibilizada a opção de geração de acordo para lançamentos provenientes do TOTVS Construção Gestão de Imóveis.  
As regras para geração do acordo seguirão os padrões que devem primeiro ser definidos no TOTVS Gestão Financeira. Consulte a documentação abaixo para maiores detalhes da rotina de acordo:



### Procedimentos  para realização do acordo

---

**Permissões | Template**

Para iniciar a utilização do Acordo, certifique-se que estão habilitadas, através do *Perfil de Usuário* no TOTVS Gestão Financeira, em Serviços Globais as permissões para: *Incluir | Editar | Aprovar e Excluir* acordos.

**Configuração da interface de Acordo | Template**

Após liberação de permissão deve-se acessar o processo através do menu *Contas a Pagar | Receber - Operações Financeiras | Acordo.*

Neste momento será possível definir regras de interface criando [templates](http://tdn.totvs.com/display/LRM/Template+de+Acordo) para a tela de geração de acordo.

**Gerando o acordo no TOTVS Construção Gestão de Imóveis**

falseImportante:

* Para os **contratos de venda** é preciso informar um componente padrão que será utilizado para as novas parcelas que forem criadas, o mesmo será informado no parâmetro ***Código do componente a ser gerado no acordo de venda (Somente Principal),*** disponível em: *Parâmetros | TOTVS Construção Gestão de Imóveis | Integração Financeira | Financeiro.*

Para gerar um acordo no TOTVS Construção Gestão de Imóveis, basta selecionar o Contrato de Venda / Aluguel, acessar a visão de lançamentos gerados (Anexos | Lançamento Financeiro) e ir em Processos | Gerar Acordo:

Durante o processo, pode-se selecionar o template cadastrado ao usuário, bem como outros dados e valores pertinentes ao acordo.

Estes lançamentos, após a realização do acordo, serão considerados como baixados por acordo. O usuário deverá então baixar as novas parcelas geradas, com seus respectivos novos valores de juros, multa, descontos e etc.

* As parcelas geradas (de origem **Contrato de Locação**) via acordo financeiro serão exibidas em *Anexos | Lançamentos Financeiros* da visão de Contratos de Locação e também na visão de Lançamentos de Shopping. (Menu: *Shopping. Agrupador: Financeiro | Lançamentos)*
* As parcelas geradas (de origem **Condomínio**) via acordo financeiro serão exibidas em *Anexos | Lançamentos Financeiros* na visão de Fechamento de Condomínio e também na visão de Lançamentos de Shopping. (Menu: *Shopping. Agrupador: Financeiro | Lançamentos)*
* As parcelas geradas (de origem **Fundo Promocional**) via acordo financeiro serão exibidas diretamente na visão de Lançamentos de Shopping. (Menu: *Shopping. Agrupador: Financeiro | Lançamentos)*
* Nos contratos de venda, para que se visualize as parcelas e faça a posterior baixa das mesmas, deve-se ir diretamente no módulo TOTVS Gestão Financeira, ou então, acessar as parcelas via rastreabilidade, selecionando o lançamento que participou do acordo.
* Os lançamentos gerados por acordo quando são de Fundo Promocional ou de Locação, irão compor os eventos financeiros já registrados para essas origens.
* Os lançamentos gerados por acordo quando são de Condomínio, não irão compor evento financeiro, visto que o processo de geração de financeiro no condomínio não gera evento.

**Cancelamento do acordo.**

É permitido cancelar um Acordo, desde que nenhum lançamento gerado esteja incluído em uma das categorias que restringem o cancelamento do Lançamento gerado por Acordo.

Ao cancelar um Acordo, a baixa dos lançamentos geradores será automaticamente cancelada e os Lançamentos gerados serão também cancelados.
