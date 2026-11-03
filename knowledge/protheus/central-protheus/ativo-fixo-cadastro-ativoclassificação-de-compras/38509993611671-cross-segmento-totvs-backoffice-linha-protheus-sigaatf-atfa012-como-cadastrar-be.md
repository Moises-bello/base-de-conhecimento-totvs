---
article_id: 38509993611671
category: Ativo Fixo - Cadastro Ativo/Classificação de Compras
content_hash: 9943760185bc341c97f42df7a5f1a27cf5ce161ec2edc5056e824f12847cb5a3
fetched_at: '2026-06-28T22:41:48.506820+00:00'
product: protheus
section_id: 1500001547662
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAATF - ATFA012 - Como
  cadastrar Bem em Construção
type: support-article
updated_at: '2026-02-19T20:26:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38509993611671-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAATF-ATFA012-Como-cadastrar-Bem-em-Constru%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38510014824215) Tempo aproximado para leitura: 15min  
  
**Dúvida**  
Como realizar o processo de cadastro, vinculação de componentes e finalização de um Bem em Construção no módulo Ativo Fixo (SIGAATF)?  
  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Ativo Fixo (SIGAATF) - a partir da versão 12.1.2210  
  
  
**Solução**  
O processo completo consiste em cadastrar o bem principal com valor zerado, dar entrada nos componentes via nota fiscal, vincular esses componentes ao bem em construção e, posteriormente, agrupá-los na rotina de transferência por aquisição (ATFA251) para gerar o bem final.  
  
A geração do bem final acumulará o saldo dos componentes amarrados a ele, atualizando o registro do bem em construção na tabela de Manutenção CIAP (SF9). Adicionalmente, o parâmetro MV\_ATFBMCT determina se será possível amarrar bens que não tenham CIAP ao bem principal.

**Passos:**

1. **Cadastro de Bens (ATFA012):**  
     
   Realize a inclusão de um bem selecionando o campo "Tipo do Bem" (N1\_BMCONTR) como "1-Bem em Construção".

   ![](https://tdn.totvs.com/download/attachments/567740807/image2021-3-2_17-7-10.png?version=1&modificationDate=1614715630183&api=v2)

   Este bem deve ser cadastrado com valor original zero na aba Saldos (permite valor R$ 0,00).  
     
   Ao término da inclusão, o status do bem (N1\_STATUS) será alterado automaticamente para "0-Pendente de Classificação" (esta informação não deve ser alterada em tela).
2. **Entrada de Nota Fiscal de Componentes (MATA103):**  
     
   Dê entrada nos componentes (bens do tipo 03) através de um documento de entrada  
     
   A TES utilizada deve estar configurada para gerar CIAP e desmembrar Ativo Fixo, contendo os campos:  
     
   **Atualiza Ativo (F4\_ATUATF)** = Sim   
   **Componente (F4\_COMPONE)** = Sim  
   **Livro Ciap (F4\_CIAP)** = Sim / Não (Verificar se deseja gerar CIAP)

   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/38509993599767)
3. **Classificação de Compras (ATFA240):**  
     
   Na rotina de classificação, vincule os componentes ao bem em construção.

   1. Realize a classificação dos componentes que deseja vincular ao bem em construção
   2. Na aba "Bem em Construção", utilize a Consulta Padrão (F3) no campo "Bem em Cons." (N1\_SLBMCON) para selecionar o bem principal, o que preencherá automaticamente o item.

      ![](https://centraldeatendimento.totvs.com/hc/article_attachments/38510014824727)

      A confirmação da classificação do primeiro componente ao bem principal gerará um registro na tabela SF9 e preencherá o campo N1\_CODCIAP do bem em construção. O código de baixa do componente será preenchido com o código do bem em construção.
4. **Aquisição por transferência (ATFA251):**

   1. Acesse a rotina e selecione a opção em Outras Ações: "Agr. bem em construc.".
   2. Selecione o bem em construção desejado via consulta (F3).
   3. A tela apresentará os componentes vinculados ao bem.

      ![](https://centraldeatendimento.totvs.com/hc/article_attachments/38510014824983)

   Ao confirmar o agrupamento, o sistema não gera um novo registro na tabela SF9, mas atualiza o registro do bem em construção com os saldos dos componentes referentes a ICMS do bem.

   Neste momento, o bem em construção virará um bem fiscal definitivo (tipo 01).

   **How To - Bens em construção**

**Saiba Mais:**   
[TDN - Bem em Construção](https://tdn.totvs.com/plugins/viewsource/viewpagesrc.action?pageId=567740807).
