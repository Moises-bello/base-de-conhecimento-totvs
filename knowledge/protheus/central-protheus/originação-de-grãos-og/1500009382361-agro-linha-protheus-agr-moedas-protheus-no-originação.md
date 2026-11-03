---
article_id: 1500009382361
category: Originação de Grãos (OG)
content_hash: 89c47583891a8f77bc3f263d00dcaf42cf98d366ab6855c717084cd116008d66
fetched_at: '2026-06-28T22:45:41.047585+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Moedas Protheus no Originação
type: support-article
updated_at: '2025-06-23T15:51:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500009382361-Agro-Linha-Protheus-AGR-Moedas-Protheus-no-Origina%C3%A7%C3%A3o
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16621037848471)***Tempo aproximado para leitura:**00:01:45 min**  
**Dúvida**Como realizar uma configuração de moedas no Originação de Grãos?  
  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Solução**Ao alterar o parâmetro **MV\_MOEDA2 - Título da moeda 2** de **dólar** para **peso**, ao abrir a tela **Moedas Protheus x Externo OGA011** o Sistema irá atualizar a tabela **Moedas Protheus x Externas -** **NJ7** campo **NJ7\_DESCRI - Descrição**de **dólar** para **peso** e limpar os dados dos campos **NJ7\_IDEXT1 - Cod Atual** e **NJ7\_IDEXT2 - Cod Futuro** relacionados ao campo **Cod Protheus - NJ7\_CODPRO = 2**.

![ORIG.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7108571805975)

Inicialmente o Sistema realiza a carga na tabela conforme as moedas do **Protheus** e mostra os dados na tela possibilitando a edição.

![ORIG1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7108616474263)

Para vincular uma moeda de um Sistema externo com a **moeda** do **Protheus** selecione-a na lista e clique em **Alterar**.

![ORIG2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7108617411735)

Informe os campos **Cod Atual** e  **Cod Futuro** e clique em **Confirmar,**o Sistema valida para que esses valores não sejam repetidos.

![ORIG3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7108618422295)

**Saiba mais**Pata mais informações sobre **moedas** do **Protheus** acesse o artigo: [Agro - Linha Protheus - AGR - Moedas Protheus versos Integrações](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500009260562-Agro-Linha-Protheus-AGR-Moedas-Protheus-versos-Integra%C3%A7%C3%B5es)
