---
article_id: 360015475591
category: Encargos
content_hash: 331520ac2f248f90f5646490b932c47652b6de3fcc70d624613c3f146a7b3c76
fetched_at: '2026-06-28T22:46:53.389674+00:00'
product: rm
section_id: 1500000834581
source: central-rm
title: 'RH - RM - FOP - SEFIP: FAP não está sendo considerado'
type: support-article
updated_at: '2025-03-13T11:25:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015475591-RH-RM-FOP-SEFIP-FAP-n%C3%A3o-est%C3%A1-sendo-considerado
---

**Dúvida**Por que o valor do FAP não está sendo considerado no programa da Sefip?  
   
 **Ambiente**  
RM - Folha de pagamento - Todas as versões  
   
**Solução**  
O layout da Sefip 8.4 não consta um campo para o FAP. Portanto, o arquivo gerado não leva as informações do FAP cadastrada na filial. Para que o programa da Sefip considere estes valores, deverá seguir uma das duas saídas de contorno abaixo:  
  
**01.** Marcando a opção **Gerar arquivo de Atualização do FAP**o sistema gera um arquivo para ser importado no programa da SEFIP para atualizar os valores do FAP por filial;  
  
​​![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360011192552/mceclip0.png)  
  
Após a geração do arquivo texto, será necessário importar as informações em programa específico da Caixa. Segue o [manual CAIXA](http://www.caixa.gov.br/Downloads/fgts-sefip-grf/Tutorial_Aplicativo_SEFIP_ATUALIZA_FAP.pdf) referente ao **SEFIP - Atualiza FAP**.  
  
Este parâmetroirá criar um arquivo texto para que seja importado com todos os FAP's cadastrados por filial. Importe dentro do programa **SEFIP - Atualiza FAP,** para que ele faça a importação das informações.  
  
**02.** Outra opção é inserir o FAP diretamente no programa da SEFIP. No programa, acesse **Ferramentas | Opções** e depois, na aba **Replicar FAP**, informe o código desejado:  
**![](https://totvssuporte.zendesk.com/attachments/token/03PwIa0h4R6q67BzAMu7CywRV/?name=inline-112342999.png)**
