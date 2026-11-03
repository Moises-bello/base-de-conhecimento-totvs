---
article_id: 40065181147927
category: Contabilidade Gerencial - Movimentos, Lançamentos contábeis automáticos,
  lançamentos manuais e contabilização
content_hash: 60d97fcf2a403e091445c730ec4868f24b3ae0a9f22315a31cfec3a12dea7495
fetched_at: '2026-06-28T22:40:32.600867+00:00'
product: protheus
section_id: 1500001537961
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGACTB - CTBA105 - Ao
  contabilizar apresenta help: "Informar a Atividade Complementar..."'
type: support-article
updated_at: '2026-06-09T20:47:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40065181147927-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGACTB-CTBA105-Ao-contabilizar-apresenta-help-Informar-a-Atividade-Complementar
---

Durante a contabilização, mensagens de help sobre obrigatoriedade de Atividades Complementares aparecem devido à parametrização da conta contábil. Para inibir essas mensagens, deve-se acessar a rotina Plano de Contas (CTBA020), localizar a conta, alterar a aba Atividades e ajustar para "Não" a obrigatoriedade da atividade correspondente, salvando a alteração.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40065181137303) Tempo aproximado para leitura: **5 min**  
  
**Ocorrência**  
Durante o processo de contabilização, mensagens de Help referentes à obrigatoriedade de Atividades Complementares (como CT2\_AT02DB, CT2\_AT02CR, CT2\_AT03DB, CT2\_AT03CR, CT2\_AT04DB e CT2\_AT04CR) são apresentadas repetidas vezes. Qual procedimento deve ser realizado para inibir essa mensagem?

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40065181137943)

**Ambiente**  
Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Contabilidade Gerencial (SIGACTB) - a partir de versão 12  
  
  
**Causa**  
Esta mensagem de obrigatoriedade ocorre porque o cadastro da conta contábil envolvida na operação está parametrizado para obrigar a passagem da informação de atividades complementares. Para inibir a apresentação do help, é necessário alterar o cadastro da conta e retirar a obrigatoriedade da respectiva atividade.  
  
  
**Solução**

1. Acesse a rotina Plano de Contas (CTBA020).

   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/40065218834455)
2. Localize a conta contábil que apresenta o help durante o processo e selecione a opção Alterar.

   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/40065218835095)
3. Navegue até a aba Atividades.

   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/40065284188439)
4. Localize o campo correspondente à atividade apresentada na mensagem de help (exemplo: Ativ 02. Ob, Ativ 03. Ob ou Ativ 04. Ob) e ajuste o conteúdo para "Não".

   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/40065284189079)
5. Confirme a alteração para salvar o cadastro.

**Saiba mais:**  
[CTBA020 - Como cadastrar um plano de contas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500011068541-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA020-Como-cadastrar-um-plano-de-contas)
