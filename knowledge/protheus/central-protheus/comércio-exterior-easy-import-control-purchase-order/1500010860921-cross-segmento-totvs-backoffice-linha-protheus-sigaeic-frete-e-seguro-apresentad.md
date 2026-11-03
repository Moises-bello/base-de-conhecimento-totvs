---
article_id: 1500010860921
category: Comércio Exterior - Easy Import Control - Purchase - Order
content_hash: 0f113dac90fa0cc624eb65cde2c62a8ae2c94be24cc60d3f1118dd198e54520a
fetched_at: '2026-06-28T22:39:41.162514+00:00'
product: protheus
section_id: 1500001538481
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Frete e Seguro
  apresentados indevidamente ao Classificar a Nota Fiscal do EIC no Documento de Entrada
  do Compras
type: support-article
updated_at: '2025-03-21T18:21:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500010860921-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Frete-e-Seguro-apresentados-indevidamente-ao-Classificar-a-Nota-Fiscal-do-EIC-no-Documento-de-Entrada-do-Compras
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24398610444183)Tempo aproximado para leitura: **00:03:00 min**

**Ocorrência**Após finalizar o Recebimento de Importação dentro do SIGAEIC, com todas as informações corretas da Nota Fiscal e iniciar a Classificação da mesma dentro do Documento de Entrada no SIGACOM, é apresentado de forma incorreta os valores de Frete e Seguro. Neste caso, de acordo com a normativa CAT 06/2015, tais valores não devem ser apresentados, pois já estão inseridos nos produtos.  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Import Control* – Todas versões.  
  
**Causa**Em alguns casos, os valores de Frete e Seguro podem ser apresentados de forma indevida, no momento de Classificar a Nota Fiscal dentro do SIGACOM quando o campo "**C7\_SEQUEN"** não estiver preenchido.  
  
**Solução**Neste caso, será necessário verificar se o campo "**C7\_SEQUEN"**está preenchido de acordo com o conteúdo "**W3\_POSICAO"**. Se o mesmo não estiver, verificar se o parâmetro "**MV\_EXECCOM" está Habilitado "T"** e se o campo "**C7\_SEQUEN"**está como **"Usado por todos os módulos"**.  
Ao preencher o conteúdo do campo "**C7\_SEQUEN"** de acordo com "**W3\_POSICAO",** gerar novamente a Nota Fiscal e verificar que o Frete e Seguro não serão apresentados.  
  
**Saiba mais:**  
**[MV\_EXECCOM - Utiliza o execauto do MATA120 na integração com o EIC.](https://tdn.totvs.com/pages/viewpage.action?pageId=838684287)**
