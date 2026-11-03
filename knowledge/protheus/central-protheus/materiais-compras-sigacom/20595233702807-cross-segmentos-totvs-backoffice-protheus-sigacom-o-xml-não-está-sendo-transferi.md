---
article_id: 20595233702807
category: Materiais - Compras (SIGACOM)
content_hash: 618cc6e74af366c1de92013859da7370bc2555d86701374d3b8891b37f733e57
fetched_at: '2026-06-28T22:41:22.010514+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - O XML NÃO está sendo
  transferido da pasta IN para LIDOS no Importador XML.
type: support-article
updated_at: '2024-04-02T18:43:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20595233702807-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-O-XML-N%C3%83O-est%C3%A1-sendo-transferido-da-pasta-IN-para-LIDOS-no-Importador-XML
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20595228838295) Tempo aproximado para leitura: **00:03:00 min****Dúvida**O XML NÃO está sendo transferido da pasta IN para LIDOS.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS COMPRAS - A partir da Versão 12  
  
**Solução**

Realizar um teste com as rotinas diretamente no menu:

**Passo 1:** Parar os serviços do Schedule

* Acesse o sistema e pare os serviços do Schedule para garantir que as rotinas não sejam executadas automaticamente durante o teste.

**Passo 2:** Executar as rotinas **COLAUTOREAD** e **SCHEDCOMCOL** manualmente no menu.

* Acesse o Menu de Compras seguindo as instruções fornecidas na documentação (SIGACFG > Ambiente > Cadastros > Menus > Compras).
* Dentro do menu de Compras, localize e execute as rotinas **COLAUTOREAD** e **SCHEDCOMCOL** manualmente, nesta ordem.

**Passo 3:** Verificar a movimentação dos XMLs

* Após a execução das rotinas, verifique se os arquivos XML saem da pasta **IN** para a pasta **LIDOS** conforme o esperado.
* Certifique-se de conferir tanto a pasta de origem (**IN**) quanto a pasta de destino (**LIDOS**) para garantir que os arquivos estejam sendo movidos corretamente.

**Passo 4:** Conferir os parâmetros de diretório

* Acesse os parâmetros relevantes para as pastas **INN**, **LIDOS** e **OUT**, conforme definido na configuração do sistema.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22512193939991)

* Verifique se os diretórios estão corretamente configurados de acordo com o exemplo fornecido na documentação.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20595481531927)

**Passo 5:** Análise de resultados

* Após executar as rotinas verifique se o arquivo XML foi transferido da pasta **IN** para a pasta **LIDOS**.

**IMPORTANTE:** Caso tenha gerado algum erro ou inconsistência, pedimos que seja aberto um ticket para a equipe do compras estar investigando a causa e tomar as medidas necessárias para corrigir o problema.

***Saiba Mais:***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
