---
article_id: 40384662978071
category: Comércio Exterior - Easy Import Control - Solic. de Importação
content_hash: 324f6a25259c6be6cc9729c86ab2c3d02083f4f3fca0331f8c5d4ff9599bae87
fetched_at: '2026-06-28T22:39:46.705361+00:00'
product: protheus
section_id: 1500001538401
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice (Linha Protheus) - Easy Import Control -
  Help: SI_NODEL Existem itens com importação em andamento'
type: support-article
updated_at: '2026-05-12T21:51:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40384662978071-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-Easy-Import-Control-Help-SI-NODEL-Existem-itens-com-importa%C3%A7%C3%A3o-em-andamento
---

Ao tentar excluir uma Solicitação de Importação no TOTVS Backoffice (SIGAEIC), o sistema bloqueia a operação se houver Purchase Order (P.O.) vinculado, pois o saldo da S.I. foi consumido. Para excluir, é necessário estornar o P.O. associado, liberando o saldo da S.I. e permitindo a exclusão sem bloqueios.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40384705951767) Tempo aproximado para leitura: **00:03:00 min**  
  
**Dúvida**  
Ao tentar excluir uma Solicitação de Importação na rotina, o sistema bloqueia a operação e exibe a seguinte mensagem de validação em tela:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/40384662946967)  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Easy Import Control (SIGAEIC) - Todas as versões  
  
**Solução**  
O Help "**SI\_NODEL**" ocorre porque a Solicitação de Importação (S.I.) selecionada para exclusão já possui seus itens vinculados a um Purchase Order (P.O.) gerado. Quando o P.O. é incluído, o sistema consome o saldo da S.I. (campo Saldo Qtde) e bloqueia a exclusão do registro original para garantir a integridade do processo de importação em andamento.

Para que a exclusão da Solicitação de Importação seja permitida, é necessário primeiramente realizar o estorno do Purchase Order associado. Isso fará com que o saldo retorne para a S.I., liberando-a para a exclusão.  
  
**Passos:**  
- Acesse o módulo "**Easy Import Control (SIGAEIC)**" e abra a rotina de Purchase Order;

- Localize e posicione no Purchase Order (P.O.) que consumiu os itens da Solicitação de Importação que deseja excluir;

- Clique em "**Outras Ações**" e selecione a opção "**Estornar**";

- Confirme a operação e aguarde a mensagem de conclusão do estorno;

- Retorne para a rotina de Solicitação de Importação (EICSI400);

- Posicione na S.I. desejada. Caso queira validar, clique em "**Visualizar**" e verifique que o campo "**Saldo Qtde**" retornou ao seu valor total;

- Com a S.I. selecionada, clique em "**Outras Ações**" e escolha a opção "**Excluir**".

- Confirme a exclusão. O processo será concluído com sucesso sem apresentar o bloqueio.  
  
**Saiba mais:**  
[**Exclusão da Solicitação de Importação**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360040201053-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Exclus%C3%A3o-da-Solicita%C3%A7%C3%A3o-de-Importa%C3%A7%C3%A3o)  
[**Estorno da Purchase Order**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360040201053-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Exclus%C3%A3o-da-Solicita%C3%A7%C3%A3o-de-Importa%C3%A7%C3%A3o)
