---
article_id: 27567119719319
category: Comércio Exterior - Easy Import Control - Financeiro
content_hash: 140d025a58c798ef9f5732d4da20191bd04dc82b5ebcf276c515bd3a7ff30c48
fetched_at: '2026-06-28T22:39:44.506366+00:00'
product: protheus
section_id: 1500001549642
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Configuração e
  Funcionalidade do Parâmetro MV_EIC0003?
type: support-article
updated_at: '2024-11-14T11:43:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/27567119719319-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Configura%C3%A7%C3%A3o-e-Funcionalidade-do-Par%C3%A2metro-MV-EIC0003
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27567126880151) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Qual é a Configuração e Funcionalidade do Parâmetro **MV\_EIC0003**?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – *Easy Import Control* – A partir da versão12.1.2210.  
  
**Solução**O parâmetro **MV\_EIC0003** tem por finalidade definir se o título provisório gerado através valor antecipado no processo de importação será ou não excluído em casos de liquidação.  
Ao gerar o Purchase Order **(EICPO400**) com condição de pagamento antecipada, o sistema gera títulos provisórios no Financeiro **(SIGAFIN)**, quando o adiantamento no Controle de Câmbio **(EICAP100)** é incluso, o sistema gera novamente um título provisório referente o adiantamento.

1. Se estiver configurado com o numeral um serão criados os títulos provisórios com as datas atualizadas de acordo com o câmbio e os títulos provisórios do *Purchase Order* não serão apagados.
2. Se estiver configurado com o numeral dois serão criados os títulos provisórios com as datas atualizadas de acordo com o câmbio e os títulos provisórios do *Purchase Order* serão apagados ao liquidar o pagamento antecipado.
3. Se estiver configurado com o numeral três serão criados os títulos provisórios com as datas atualizadas de acordo com o cambio e os títulos provisórios do *Purchase Order* serão apagados e criados conforme inclusão do câmbio.

**Saiba mais:**

**[Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - SIGAEIC - Título Provisório do Pagamento Antecipado](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025896392-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-SIGAEIC-T%C3%ADtulo-Provis%C3%B3rio-do-Pagamento-Antecipado)**

**[Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Tipo de Títulos SIGAEIC x SIGAFIN](https://centraldeatendimento.totvs.com/hc/pt-br/articles/115010175987-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Tipo-de-T%C3%ADtulos-SIGAEIC-x-SIGAFIN)**

**[MV\_EIC0003 igual a 2 está mantendo os títulos PR do PO, ao incluir o cambio de adiantamento do PO](https://tdn.totvs.com/pages/releaseview.action?pageId=877870790)**
