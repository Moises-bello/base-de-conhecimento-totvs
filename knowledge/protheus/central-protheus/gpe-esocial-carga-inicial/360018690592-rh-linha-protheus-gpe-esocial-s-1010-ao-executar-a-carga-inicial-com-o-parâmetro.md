---
article_id: 360018690592
category: GPE - eSocial - Carga Inicial
content_hash: a893079a03cac301ed03cdce9f589dc131d0ba882eca633e6f8a565386e29fbf
fetched_at: '2026-06-28T22:45:03.232639+00:00'
product: protheus
section_id: 360005445833
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-1010 - Ao executar a carga inicial
  com o parâmetro MV_XMLGPE habilitado o sistema não gera o arquivo XML das rubricas
  (verbas)
type: support-article
updated_at: '2024-12-04T18:28:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018690592-RH-Linha-Protheus-GPE-eSocial-S-1010-Ao-executar-a-carga-inicial-com-o-par%C3%A2metro-MV-XMLGPE-habilitado-o-sistema-n%C3%A3o-gera-o-arquivo-XML-das-rubricas-verbas
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28278059112599)**Tempo aproximado para leitura: **00:02:00 min**

**Ocorrência**S-1010 - Ao executar a carga inicial com o parâmetro **MV\_XMLGPE** habilitado o sistema não gera o arquivo XML das rubricas (verbas).  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Causa**Na rotina carga inicial quando o parâmetro **MV\_XMLGPE** está habilitado o sistema gera o arquivo XML na pasta system ou no diretório informado para todos os eventos com exceção do evento S-1010 (rubricas), devido a quantidade de registro que esse evento processa.  
  
**Solução**Só é possível gerar o XML do S-1010 através da rotina cadastro de verbas. Para gerar o arquivo XML do evento S-1010 efetue os seguintes passos:  
1. Deixe o parâmetro MV\_XMLGPE como .T. ;  
  
2. Ao efetuar uma alteração ou inclusão de verbas através do cadastro de verbas (GPEA040) o sistema vai gerar o XML na pasta system ou no diretório informado.  
[MP - GPE - eSocial - Como alterar o diretório onde serão gravados os arquivos XML's do SIGAGPE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035286913)Observação: O arquivo XML contém TAGs da integração do GPE com o TAF utilizado apenas para análise em caso de erros.  
  
**Saiba Mais**  
Para saber mais consulte os links abaixo:   
[Artigos S-1010](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051971613)  
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)   
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes)
