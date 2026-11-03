---
article_id: 38730052974743
category: Financeiro - Configurador de Tributos
content_hash: 21bc9e468a0d3f2fd5bf8bb59998dbb6d6dcd6c23fb7b4a83c0a69f72ea0f4e7
fetched_at: '2026-06-28T22:37:46.034046+00:00'
product: protheus
section_id: 30946086151959
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FISA170 - É possível
  alterar uma regra financeira adicionando um novo tributo ?
type: support-article
updated_at: '2026-03-02T12:26:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38730052974743-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FISA170-%C3%89-poss%C3%ADvel-alterar-uma-regra-financeira-adicionando-um-novo-tributo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38730036690455) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
É possível alterar uma **Regra Financeira** adicionando um novo tributo?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro (SIGAFIN) - **FISA170** - A partir da versão 12

**Solução**

É possível alterar as informações e o comportamento de uma regra financeira existente (como fato gerador, carteira, regras de vencimento, etc.) criando uma nova versão de vigência. **No entanto, não é possível alterar, excluir ou adicionar um novo tributo em uma regra financeira já existente.** Para incluir um novo tributo, é necessário incluir uma **nova** regra financeira no sistema.

Caso o objetivo seja alterar as informações gerais de uma regra financeira existente, é necessário primeiro ajustar a vigência atual e, em seguida, gerar uma nova versão.

Para alterar uma regra financeira existente (dados gerais e de cálculo):

1. Acesse a rotina de **Regras Financeiras**.
2. Selecione a regra que deseja modificar e clique em **Outras Ações > Ajustar Vigência**.
3. Altere a data final da vigência atual para encerrar o período da regra (ex: `31/12/2025`) e clique em **Confirmar**.
4. Selecione a mesma regra novamente e clique em **Outras Ações > Alterar**. O sistema criará uma nova versão.
5. Ajuste a data inicial da nova versão (ex: `01/01/2026`) e informe a nova data final.
6. A partir deste momento, os campos das abas **Dados Gerais**, **Regras Gerais** e **Contábil** estarão liberados para alteração. *(Lembrando: o campo de Tributo permanecerá bloqueado)*.
7. Após realizar os ajustes necessários, clique em **Confirmar** para salvar.

No exemplo a seguir veja a demonstração do processo:

![Gravar #7.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/38730052966551)

**Saiba mais**

* [Configurador de Tributos - Financeiro](https://centraldeatendimento.totvs.com/hc/pt-br/sections/30946086151959-Financeiro-Configurador-de-Tributos?page=2#articles)
* [FISA170 - Regras Financeiras](https://tdn.totvs.com.br/display/public/PROT/Configurador+de+Tributos+-+Regras+Financeiras)

###
