---
article_id: 1500011508142
category: Faturamento - Cadastros
content_hash: bdb6871a27605d684659063d290c4a227a4308d1895739ccc03bc2bbf05a987f
fetched_at: '2026-06-28T22:38:35.310674+00:00'
product: protheus
section_id: 1500001539221
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice (Linha Protheus) - Sigafat - Help Regnois
  - Problema: Não existe registro relacionado a chave informada no alias CC3, ordenação
  1.'
type: support-article
updated_at: '2022-07-27T18:58:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500011508142-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-Sigafat-Help-Regnois-Problema-N%C3%A3o-existe-registro-relacionado-a-chave-informada-no-alias-CC3-ordena%C3%A7%C3%A3o-1
---

**Ocorrência**

Após a implementação da API Carol, ao tentar informar o CPF ou CGC está gerando a mensagem:

Help Regnois - Problema: Não existe registro relacionado a chave informada no alias CC3, ordenação 1.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500018550702/mceclip0.png)  
  
**Causa**

Além da mensagem de Regnois, dentro do processo poderão ser gerados outras duas mensagens:

Erro de preenchimento do cnae do cliente:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500018827201/mceclip1.png)

Atenção:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500018552762/mceclip2.png)

O problema ocorre devido a validação do campo **A1\_CNAE** para o tratamento de integração com a API Carol.

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Sigafat - a partir da release 12.1.27.  
  
**Solução**

Para solucionar:

1- Aplique o pacote de expedição contínua no módulo que já contém a correção em questão, via Vs-code, para a release em vigência:

12.1.33: <https://suporte.totvs.com/portal/p/10098/download?e=1039091>

1-a Para as releases expiradas seguem os pacotes disponíveis:

12.1.17:<https://r.totvs.io/p/1021956> (garantia estendida);

12.1.23:<https://r.totvs.io/p/1021957> ;

12.1.25:<https://r.totvs.io/p/1021958> ;

12.1.27:<https://suporte.totvs.com/portal/p/10098/download?e=954520>;

2-Valide se a validação do A1\_CNAE está igual a  **A30VldCnae()** . Caso não esteja, aplique o dicionário diferencial de Faturamento que se encontra no pacote de expedição contínua: **[SIGAFAT](https://tdn.totvs.com/pages/releaseview.action?pageId=521997859)**

E execute o **upddistr** para os ajustes de dicionário.

**Observação**: Para aplicação de pacote e atualização de dicionários, requer que o analista tenha pelos conhecimentos de estrutura Protheus.
