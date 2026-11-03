---
article_id: 20687093055639
category: SIGAEST - MOVIMENTAÇÕES
content_hash: d94cb3627a114ce662a3615494fa3dd64c1efabe55e3c61f619d52992dbdea86
fetched_at: '2026-06-28T22:38:56.934771+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA241 - Como configurar
  a rotina movimentação multipla via Mile?
type: support-article
updated_at: '2025-07-17T22:20:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20687093055639-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA241-Como-configurar-a-rotina-movimenta%C3%A7%C3%A3o-multipla-via-Mile
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20687092994967)  Tempo estimado para leitura: **00:01:40 min****Dúvida**Como configurar a rotina através do Mile para movimentações? E como corrigir o erro: argument error in function Len() on MATA241(MATA241.PRX)?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Protheus Release 12.1.33 ou Superior.  
  
**Solução**A rotina MATA241, por se tratar de movimentação múltipla, possui um cabeçalho para a digitação dos itens:

**Com as variáveis denominadas:**

* CDOCUMENTO(D3\_DOC) - Número do Documento
* CTM(D3\_TM) - TM
* CCC(D3\_CC) - Centro de Custos
* DA241Data(D3\_EMISSAO) - Emissão

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20687130345751)

Para realizar a configuração através do Mile, não se deve utilizar o Modelo 1, pois este não contempla o cabeçalho no Canal. Caso este modelo de importação seja utilizado, o seguinte erro será gerado:

**argument error in function Len() on MATA241(MATA241.PRX)**

Para configurar corretamente a rotina MATA241 para utilização no Mile, utilize o modelo:

(2=**Modelo 2** (1 Tabela com cabeçalho/itens)

Atenção aos campos obrigatórios e adicionais a critério do cliente.

![mile241.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/20687093000087)

**Atenção**  ao preenchimento dos campos **D3\_QUANT** e **D3\_CUSTO1**, conforme a configuração de sua TM.

Exemplo do arquivo utilizado no gif para importação:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20687130352407)

Movimento efetivado:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20687130357655)

Caso seja necessário o uso de variáveis na importação, sugerimos a utilização do execauto da rotina em si:

<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022031372-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Execauto-rotina-MATA241-Movimentacao-Multipla>

**Mapeamento em casos de HELP = AJUDA:REGNOIS**

- **Cenário mapeado**: Verificar se a configuração do seu campo "Ocorrência" ou demais campos obrigatórios estão devidamente configurados para a ação de utilização do arquivo a ser importado.

Por exemplo: ao utilizar o Mile na rotina MATA241, a opção de ocorrências deve ser configurada com o conteúdo N, uma vez que o canal receberá várias informações em sequência.

* N= Várias – O canal ocorre várias vezes para cada unidade de informação.

Documentação completa para utilização do Mile:

[MP - FRAME - MILE: Model Integrator Layout Engine](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028814432-MP-FRAME-MILE-Model-Integrator-Layout-Engine)

**Saiba mais:**

[MP - SIGAEST - MATA241 - Movimentações Múltiplas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026614194-MP-SIGAEST-MATA241-Movimenta%C3%A7%C3%B5es-M%C3%BAltiplas-)

[Clique aqui e veja mais artigos sobre Movimentações no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000033422-SIGAEST-MOVIMENTA%C3%87%C3%95ES)
