---
article_id: 360052402093
category: PONTO ELETRÔNICO
content_hash: 37aa29e32d70d179798f9afed50f7b71bd549e1819724293b31d5685f6f69c7d
fetched_at: '2026-06-28T22:44:36.754205+00:00'
product: protheus
section_id: 10299685322391
source: central-protheus
title: RH - Linha Protheus - MEU RH - Demonstração de saldo de banco de horas em "Horas
  valorizadas"
type: support-article
updated_at: '2026-06-19T14:41:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052402093-RH-Linha-Protheus-MEU-RH-Demonstra%C3%A7%C3%A3o-de-saldo-de-banco-de-horas-em-Horas-valorizadas
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20142125774615)Tempo aproximado para leitura: 02:00 min**  
  
**Dúvida**  
Como demonstrar o saldo de banco de horas no MEU RH como **"Horas valorizadas"**  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Meu RH – todas as versões  
  
**Solução**  
O MEU RH disponibiliza a possibilidade de visualização do saldo de banco de horas como "Horas valorizadas". Para isto, siga as instruções da documentação abaixo:  
  
[**Saldo do banco de horas apresentando horas reais ou valorizadas**](https://tdn.totvs.com/display/public/NPR/Saldo+do+banco+de+horas+apresentando+horas+reais+ou+valorizadas)  
  
Caso o parâmetro mencionado no documento não exista em seu ambiente, será necessário cria-lo manualmente.  
A demonstração das Horas Valorizadas no **Saldo de Banco de Horas via aplicativo Meu RH** é controlado pelo parâmetro **MV\_TCFBHVL**  
  
**No relatório de Espelho de Ponto, por utilizar a funcionalidade** ***RDMake*** **IMPESP e o INCLUDE impesp\_pt-br.tres** , é possível utilizar o *RDMake* contido no link abaixo, no pacote de Expedição Contínua do RH, no diretório *rdmake*, o fonte de nome **IMPESP.PRX** e alterar o conteúdo da variável **lImpHrVal** com .F. e realizar a compilação deste RDMake e do include **impesp\_pt-br.tres** no Repositório do Portal:  
[RH - Linha Protheus - GPE - Como fazer o download (baixar) do pacote de expedição contínua (acumulado) do RH Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus?source=search)

![](https://totvssuporte.zendesk.com/attachments/token/QpRMqybuy1Wi7AWa5RlJn8Sui/?name=image.png)

Abaixo, o local da atribuição às variáveis utilizadas para impressão do relatório.   
A **lImpHrVal**, especificamente para impressão de Horas Valorizadas ou não:![](https://totvssuporte.zendesk.com/attachments/token/B3sVrtHLamsQ6y3qRFYlPd5U5/?name=image.png)

**Obs.: Sem esta funcionalidade, não é possível alterar o conteúdo desta pergunta ao extrair via aplicativo e o relatório SEMPRE irá exibir as Horas Valorizadas.**  
  
**ATENÇÃO:** Certifique-se sempre de estar com seu ambiente atualizado, pois são disponibilizados periodicamente atualizações com melhorias e correções no MEU RH.  
[**MP - MEU RH - Como Atualizar os arquivos do Portal Meu RH?**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043729034)  
  
Anexo a este artigo, segue o ***RDMake IMPESP*** com seu *include*, para customização e, um vídeo explicativo.  
  
**Saiba Mais:**  
[**CLIQUE AQUI** para acessar mais artigos e FAQs sobre o MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)  
[**CLIQUE AQUI** para acessar a documentação de referências sobre o MEU RH](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)
