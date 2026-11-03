---
article_id: 360050631613
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 400460b0624633549070b9e194b118566001e55f063a8ab9d5ce62a759bc26db
fetched_at: '2026-06-28T22:39:58.607837+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSe - TSS: WSCERRINT
  / invalid property ACCESS_TOKEN (Florianópolis)'
type: support-article
updated_at: '2021-10-06T19:08:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050631613-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSe-TSS-WSCERRINT-invalid-property-ACCESS-TOKEN-Florian%C3%B3polis
---

**Ocorrência**Ao realizar a transmissão de um RPS para Florianópolis a nota fica com *STATUS = 2 (Aguardando Transmissão do Lote)* e apresenta o erro *WSCERRINT / invalid property ACCESS\_TOKEN* no console do TSS.  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.  
  
**Causa**Esse problema ocorre por conta do TOKEN de comunicação Web Services (o qual envolve várias informações reunidas) estar incorreto, causando falha de comunicação.  
  
Geralmente isso ocorre por dois principais motivos:  
  
1. Os parâmetros de autenticação Web Services **não estão sendo passados por completo ou corretamente** dentro do Wizard.cfg na rotina FISA022.   
Detalhes dos parâmetros: [clique aqui.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044297654-MP-NFSE-FLORIANOPOLIS-Mensagem-de-Envio-Token-Vazio)  
  
2. Os parâmetros estão corretos e populados na SPED000 dessa entidade, **porém essas credencias estão habilitadas apenas para um ambiente específico** (Produção ou Homologação).  
  
**Solução**1. Revisar os dados informados dentro do Wizard.cfg (o qual todos devem ser disponibilizados pela própria prefeitura).  
2. Verificar com a prefeitura para qual ambiente poderá ser utilizada essas credenciais e se possível realizar a liberação para ambos (Produção e Homologação).
