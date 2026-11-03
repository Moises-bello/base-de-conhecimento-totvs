---
article_id: 29737338195863
category: Financeiro - Contas a Pagar
content_hash: 0d34e4201c074a0dde9ba1e9dd7140c940e0069401b66330372167ab4bcd35ca
fetched_at: '2026-06-28T22:38:07.127346+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA290 - Rotina não
  filtra os títulos quando a Origem é da rotina FINA677
type: support-article
updated_at: '2025-02-04T11:47:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/29737338195863-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA290-Rotina-n%C3%A3o-filtra-os-t%C3%ADtulos-quando-a-Origem-%C3%A9-da-rotina-FINA677
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29737387539479) Tempo aproximado para leitura: **00****:03 min** **Dúvida**Rotina FINA290 ou FINA565 não apresenta títulos oriundos da rotina FINA677.  
  
**Ambiente**Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Todas as versões  
  
  
**Solução**Foi aberto um ticket junto a equipe do produto para o cenário, e o desenvolvimento bloqueou processos de liquidação **FINA565** e **FINA290** para o **E2\_ORIGEM = FINA677** que é o processo padrão da rotina.  
  
Neste caso, títulos gerados pela Prestação de contas não podem ser usados pelas rotinas de **(liquidação e/ou faturas a pagar)** no padrão.   
  
Para trazer na tela de faturas títulos oriundos da **FINA677**, existe o ponto de entrada **F290CHK - Ponto de entrada que permite substituir filtro padrão para seleção de títulos.**  
Para mais informações, consulte: [FCHK - Substitui filtro padrão para seleção de títulos](https://tdn.totvs.com/pages/releaseview.action?pageId=641456743)  
  
Porém, ressaltamos que alteração da **Query**, não surtira efeito na **FINA677** - **Prestação de Contas** para mudar o status para fechado da viagem, ficara com status **"7 - Em Avaliação do Financeiro"** e não será finalizada.

**Saiba mais**

[FINA677 - Não fecha a Prestação de Contas, quando o titulo gerado no Financeiro é liquidado e baixado](https://tdn.totvs.com/pages/releaseview.action?pageId=814542040)
