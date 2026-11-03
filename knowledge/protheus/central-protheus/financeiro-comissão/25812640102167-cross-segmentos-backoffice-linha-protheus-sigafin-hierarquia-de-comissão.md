---
article_id: 25812640102167
category: Financeiro - Comissão
content_hash: 7db96b98b93ff6436f21ec9d67973b221c63da93f892955398920f92e986d659
fetched_at: '2026-06-28T22:37:50.817931+00:00'
product: protheus
section_id: 26655771327895
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Hierarquia de Comissão
type: support-article
updated_at: '2026-02-10T19:19:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/25812640102167-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Hierarquia-de-Comiss%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25827526183447) Tempo aproximado para leitura: **00:05 min**

**Dúvida**  
O que fazer quando a porcentagem está errada na comissão gerada?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões.

**Solução**

O sistema buscará o percentual de comissão a ser exibido no pedido de vendas conforme a validação a seguir. Se um percentual de comissão for encontrado em um dos campos, os campos subsequentes serão desconsiderados.

**1º** Campo de **Comissão** da Linha do Item do **Pedido de Venda (MATA410)**: "**Comissao 1**" (**C6\_COMIS1**). Caso o sistema identifique este campo preenchido, ignora os demais.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38301796193559)

**2º** Campo de **Comissão** no **Cadastro do Produto (MATA010)**: **"% Comissao**" (**B1\_COMIS**). Caso os campos da **SC6** não sejam preenchidos, o sistema carrega a **comissão do cadastro do produto**. (O sistema não valida as comissões por grade de produtos caso utilize)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38301811812631)

**3º** Campo de **Comissão** no **Cabeçalho do Pedido de Venda (MATA410**): "**Comissao 1**" (**C5\_COMIS1**). Caso os campos anteriores estejam vazios, o sistema considera o que estiver preenchido neste campo.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38301796205463)

**4º** Campo de **Comissão** no **Cadastro do Cliente (CRMA980)**: "**% Comissao**" (**A1\_COMIS**). Caso os campos anteriores estejam vazios, o sistema considera o que estiver preenchido neste campo.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38301796209047)

**5º** Campo de **Comissão** no **Cadastro do Vendedor (MATA040)**: "**Comissao**" (**A3\_COMIS**). Caso os campos anteriores estejam vazios, o sistema considera o que estiver preenchido neste campo.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38301796213783)

**Exemplo:**

Quando o percentual de comissão do vendedor estiver definido em 5% no cadastro e, no pedido de venda, for informado o percentual de 3% no campo **C6\_COMIS1**, o sistema irá considerar **3%** para o cálculo da comissão na rotina **MATA490**.

Isso ocorre porque o sistema segue a hierarquia de definição de comissões mencionada acima, na qual o campo **C6\_COMIS1** possui prioridade sobre os demais. O percentual cadastrado para o vendedor é considerado apenas como última opção, sendo utilizado somente quando não houver comissão informada nas demais origens.

**Importante**

Caso possua alguma particularidade no negócio e deseje tratar a comissão de forma personalizada, podem ser utilizados os pontos de entrada:

[M410LIOK - Validação de linha de pedido](https://tdn.totvs.com/pages/releaseview.action?pageId=6784149)

**Saiba mais**  
[Hierarquia de priorização de busca da Comissão pelo Pedido de Vendas](https://tdn.totvs.com/pages/releaseview.action?pageId=232818579)
