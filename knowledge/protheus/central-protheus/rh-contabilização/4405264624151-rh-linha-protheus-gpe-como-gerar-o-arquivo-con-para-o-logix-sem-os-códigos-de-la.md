---
article_id: 4405264624151
category: RH - Contabilização
content_hash: cad7d05e1e684852100062ec2f0735bd7bdc2d667a6839d423286af8cc6d2e88
fetched_at: '2026-06-28T22:43:45.833421+00:00'
product: protheus
section_id: 360003109092
source: central-protheus
title: RH - Linha Protheus - GPE - Como gerar o arquivo CON para o Logix sem os códigos
  de Lançamentos Padrões do Protheus
type: support-article
updated_at: '2025-07-30T02:29:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4405264624151-RH-Linha-Protheus-GPE-Como-gerar-o-arquivo-CON-para-o-Logix-sem-os-c%C3%B3digos-de-Lan%C3%A7amentos-Padr%C3%B5es-do-Protheus
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33811065469975) Tempo aproximado para leitura: 00:01:00 min**

**Dúvida**Como gerar o arquivo CON para o Logix sem os códigos de Lançamentos Padrões do Protheus?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) -  GPE Gestão de Pessoal – Todas as versões.  
  
**Solução**Foi disponibilizado uma melhoria para o módulo Gestão de Pessoal possibilitando gerar na posição 10 do arquivo em formato de texto da contabilização os códigos do **Lançamento Padrão - CTBA080** atribuído a verba.  
Para que seja possivel gerar o arquivo **CON - Contábil Logix** sem  essa informação, ou seja, com 000 na posição 10 como era realizado anteriormente, após o processamento da **Contabilização** na etapa de geração do arquivo, é necessário que o campo campo **Código do Histórico Padrão** tenha seu conteúdo informado como **000** ou com o código aceito pelo módulo destino.  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4405264668823)  
  
Em seguida clique em Salvar, para que o arquivo seja gravado no diretório informado.   
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4405251935767)  
  
O arquivo será gerado com os LPs conforme demonstrado na imagem abaixo:  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4405265266327)  
  
**Saiba Mais**  
[Artigos Contabilização](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360003109092-RH-Contabiliza%C3%A7%C3%A3o)  
[11110103 DRHGCH-24144 DT Arquivo de Lote Contábil Para Integração Com LOGIX](https://tdn.totvs.com/pages/releaseview.action?pageId=590229085)  
[MP - GPE - Como realizar a integração da contabilização do módulo Gestão de Pessoal com o módulo CON do Logix por arquivo texto](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360062141273-MP-GPE-Como-realizar-a-integra%C3%A7%C3%A3o-da-contabiliza%C3%A7%C3%A3o-do-m%C3%B3dulo-Gest%C3%A3o-de-Pessoal-com-o-m%C3%B3dulo-CON-do-Logix-por-arquivo-texto)
