---
article_id: 36426959563415
category: Materiais - Compras (SIGACOM)
content_hash: 1a442ae79624293a67e56994a7ec66ecacc4dd17fff875d4c11cabbe2c19cd5f
fetched_at: '2026-06-28T22:41:21.912498+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - NFC - type mismatch
  on JSTOADVPL(PGCA010.PRW)
type: support-article
updated_at: '2025-11-19T11:26:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36426959563415-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-NFC-type-mismatch-on-JSTOADVPL-PGCA010-PRW
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36426966819479) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
Ao acessar a rotina do Novo Fluxo de Compras, sistema gera o errorlog ***type mismatch on JSTOADVPL(PGCA010.PRW)***  
  
**Ambiente**  
Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Gestão de Compras - Protheus Release 12.1.2310  
  
**Solução**  
O errorlog ***type mismatch on*** indica que uma variável do fonte está preparada para receber um tipo (por exemplo caractere) mas invés disso recebe um valor lógico.

Para solucionar o errorlog em questão, abra o módulo Configurador SIGACFG. Busque pelo parâmetro **MV\_NFCDTRE** e verifique com qual tipo ele está cadastrado. Esse parâmetro **deve estar cadastrado com** **tipo Lógico.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36426966821271)

Com o objetivo de permitir a alteração da **data de recebimento da cotação**, foi implementado o parâmetro:

**MV\_NFCDTRE –*****Permite alterar o prazo de recebimento da cotação***

* + `.T.` = Ativado
  + `.F.` = Desativado

Quando o parâmetro estiver **ativado** (`.T.`), será exibido o botão **"Alterar Recebimento"** na **tela de edição da cotação**, permitindo a modificação do prazo de recebimento.

![](https://tdn.totvs.com/download/attachments/960013217/image-2025-7-21_15-19-13.png?version=1&modificationDate=1753121953127&api=v2)

**Importante:**

* Apenas o status da cotação **Finalizada**, não pode ter a Data de Recebimento alterada.
* Para o funcionamento correto da solução, cadastrar o parâmetro via **Configurador (SIGACFG),**conforme as orientações abaixo:
  + **Aba Informações:**
    - **Nome de Var:** MV\_NFCDTRE
    - **Tipo: 3 - Lógico**
    - Em uso: Sim
    - Cont. Por: .T.
    - Cont. Ing: .T.
    - Cont. Esp: .T.
  + **Aba Descrição:**
    - **Descrição:**Permite alterar o prazo de recebimento da cotacao
    - Cont.Descriç: .T. = Ativado; .F. = Desativado.
    - Desc. Esp: Permite modificar la fecha limite de recepcion de la cotizacion
    - Cont.Descriç: .T. = Activado; .F. = Desactivado.
    - Desc. Ingles: Allows changing the quotation receipt deadline
    - Cont.Descriç: .T.  = Enabled; .F. = Disabled.

***Saiba Mais:***

[DT NFC | Implementação integração com o PCO e Alteração da Data de Recebimento](https://tdn.totvs.com/pages/viewpage.action?pageId=960013217)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)

[Novo Fluxo de Compras: Guia de Referência](https://tdn.totvs.com.br/pages/releaseview.action?pageId=680260500)
