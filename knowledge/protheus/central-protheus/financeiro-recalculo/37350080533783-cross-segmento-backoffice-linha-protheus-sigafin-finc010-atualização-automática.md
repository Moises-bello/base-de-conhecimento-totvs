---
article_id: 37350080533783
category: Financeiro - Recalculo
content_hash: 8c50b3b88351df3533dd9ed4bb46cccfd920d32fff4e23dc5a427f801c30d799
fetched_at: '2026-06-28T22:37:27.644356+00:00'
product: protheus
section_id: 35058632967831
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINC010 - Atualização
  automática dos dados do cliente
type: support-article
updated_at: '2026-02-13T12:42:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37350080533783-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINC010-Atualiza%C3%A7%C3%A3o-autom%C3%A1tica-dos-dados-do-cliente
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37350080508439) Tempo aproximado para leitura: **00:04 min**

**Dúvida:**  
Por que a posição do cliente não está atualizando o histórico financeiro e outros dados de saldo automaticamente no cadastro?  
  
**Ambiente:**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Financeiro - 12.1.33 e superiores.

**Solução:**

A atualização dos campos de saldo e histórico no cadastro de clientes (como o campo **A1\_SALDUP**) é controlada pelo parâmetro **MV\_ATUSA1**. Por padrão, este parâmetro é configurado como **.F.** (Falso), o que desativa a atualização em tempo real para otimizar a performance do sistema durante a gravação de títulos.

Quando o parâmetro está desativado, os valores só são atualizados mediante a execução manual da rotina de reprocessamento.

Para que o sistema realize a atualização automática ao final do lançamento dos títulos, siga os passos abaixo:

1. Acesse o módulo **Configurador (SIGACFG)**;
2. Vá em **Dicionário > Base de Dados > Parâmetros**;
3. Localize o parâmetro **MV\_ATUSA1**;
4. Altere o conteúdo para **.T.** (Verdadeiro);
5. Confirme a alteração.

**Observação:** Caso opte por manter o parâmetro como **.F.**, para atualizar os saldos acumulados, deve-se executar periodicamente a rotina **FINA410 (Recálculo de Saldo)**.
