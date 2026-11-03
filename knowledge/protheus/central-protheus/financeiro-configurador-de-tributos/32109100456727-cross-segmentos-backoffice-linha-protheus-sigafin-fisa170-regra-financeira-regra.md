---
article_id: 32109100456727
category: Financeiro - Configurador de Tributos
content_hash: c2fa903aac7ce06ec3dc850820248ff7cb720150906ff6d5fb11d42053a5824c
fetched_at: '2026-06-28T22:37:46.132796+00:00'
product: protheus
section_id: 30946086151959
source: central-protheus
title: Cross Segmentos Backoffice Linha Protheus - SIGAFIN - FISA170 - Regra financeira
  - Regra de Título
type: support-article
updated_at: '2025-09-18T18:22:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/32109100456727-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FISA170-Regra-financeira-Regra-de-T%C3%ADtulo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32109093542295) Tempo aproximado para leitura: **00:08 min** **Dúvida**

Como cadastrar uma regra de título?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - A partir da versão 12

**Solução**

Para realizar o cadastro de uma regra de título:

* Clique na opção Regra Financeira:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32109093543063)

* Ao expandir, clique na opção Regra de Título:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32109093543831)

* Clique no botão incluir:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32109093544471)

Para este cenário, crie a regra de título considerando os campos indicados a seguir:

**Código** - Código da regra de geração de títulos de impostos.

* Informe um código identificador para a regra de títulos de impostos.

**Descrição** - Descrição da regra de geração de títulos de impostos.

* Informe uma descrição que ajude na identificação da regra de título de impostos.

**Tp. Movto**. - Tipo de movimento que deverá ocorrer no ato da geração do título de imposto: Abatimento ou Imposto.

* Define qual o tipo de movimento deverá ocorrer no ato da geração do título de imposto:  
  1 - Abatimento  
  2 - Imposto

**Participante -** Define o tipo de participante para o qual será gerado o título de imposto

* Define o cadastro do sistema responsável pelo movimento (se um fornecedor ou um cliente).  
  Obrigatório o preenchimento do campo devido às validações posteriores, como Código do Participante e Carteira (Pagar ou Receber), as quais a regra terá efeito.

**Cód. Particip**. - Código do participante

* Código do participante (fornecedor ou cliente) para o qual que será gerado um título destacado.

**Loja** - Loja do participante

* Loja do participante (fornecedor ou cliente) para o qual será gerado um título destacado.

**Carteira** - Define a carteira onde será gerado o título de imposto.

* Indica em qual carteira será gerada a movimentação:  
  1 - Pagar: será gerado um título na carteira a pagar  
  2 - Receber: será gerado um título na carteira receber

**Natureza** - Tipo do título a ser gerado para o imposto.

* Preencha com o tipo de título a ser gerado para o imposto.

  Observação:  
  Consulta F3 disponível: já filtrando com os tipos considerados como impostos.

**Tipo Titulo** - Tipo do título a ser gerado para o imposto.

* Preencha com o tipo de título a ser gerado para o imposto.

  Observação:  
  Consulta F3 disponível: filtrará com os tipos considerados como impostos.

**Prefixo** - Informe o prefixo do título de imposto

* Prefixo a ser atribuído ao título de recolhimento.  
  Para ser considerado como título de recolhimento, a regra financeira não deve possuir uma regra de retenção atrelada.  
  Caso a regra financeira possua uma regra de retenção atrelada, sempre será considerado como prefixo do título de tributo, o mesmo prefixo do título principal.

Exemplo do cadastro preenchido:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32109093545367)

Após preencher as informações, clique em salvar.

Dessa forma, está pronto o seu primeiro cadastro, onde é possível realizar as ações de alteração, exclusão, cópia e impressão do browser.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32109100434839)
