---
article_id: 360025128033
category: RH - Leitura e Apontamento
content_hash: ee9a65d299a7ce9453ed81858f8e50a2b5ec2a0efe24b682bfb65956f953ba5c
fetched_at: '2026-06-28T22:44:45.880878+00:00'
product: protheus
section_id: 32419281460119
source: central-protheus
title: RH - Linha Protheus - PON - Ao filtrar a filial na rotina Leitura e Apontamento
  de Marcações ocorre o Help PONM010VALPAR
type: support-article
updated_at: '2025-06-13T18:44:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025128033-RH-Linha-Protheus-PON-Ao-filtrar-a-filial-na-rotina-Leitura-e-Apontamento-de-Marca%C3%A7%C3%B5es-ocorre-o-Help-PONM010VALPAR
---

**Ocorrência**Ao filtrar a filial na rotina Leitura e Apontamento de Marcações ocorre o *Help* PONM010VALPAR  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**Esse incidente ocorre por conta do Compartilhamento da tabela de Relógios - SP0, e por falta de atualização do *Help* de Campos.  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360039310553/mceclip0.png)  
  
Por padrão, sempre que o cadastro de relógios for compartilhado, não é possível fazer a leitura filtrando apenas uma filial, deve fazer a leitura com parâmetro de branco até ZZZZZ.  
  
Em Relação a mensagem em Branco, deverá atualizar o Help de Campo.  
Passo a passo para atualizar o help:   
1 - Descompacte os arquivos .txt dentro da pasta Systemload do Protheus;  
2 - Pare o serviço do Protheus, acesse a pasta System e;

**Para o help de campos em português, apague o arquivo sigahlp.hlp**  
**Para o help de campos em inglês, apague o arquivo sigahle.hle**  
**Para o help de campos em espanhol, apague o arquivo sigahls.hls**

3 - Reinicie o serviço do Protheus;   
4 - Acesse o sistema, o help será recriado a partir do .txt descompactado anteriormente. Uma imagem de alerta será exibida durante a atualização dos arquivos.  
 [![](http://tdn.totvs.com/download/attachments/271414846/Help_Campos.png?version=1&modificationDate=1486573706000&api=v2)](https://suporte.totvs.com/portal/p/10098/download#detail/737329)
