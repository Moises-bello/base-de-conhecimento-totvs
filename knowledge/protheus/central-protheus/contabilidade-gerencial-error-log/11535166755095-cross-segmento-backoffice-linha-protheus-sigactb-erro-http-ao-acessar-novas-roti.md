---
article_id: 11535166755095
category: Contabilidade Gerencial - Error log
content_hash: 78bcaf670eab64fbde9905f31fdf65eb889da165e3fc992d28d1ff231580919c
fetched_at: '2026-06-28T22:40:52.019869+00:00'
product: protheus
section_id: 1500001537581
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGACTB - Erro HTTP ao acessar
  novas rotinas PO-UI '
type: support-article
updated_at: '2023-11-13T15:37:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11535166755095-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-Erro-HTTP-ao-acessar-novas-rotinas-PO-UI
---

**Ocorrência**

Ao acessar as novas rotinas PO-UI é apresentado erro: Não possível Acessar este Site **![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11535027500055)****Ambiente**  
Cross Segmento - Backoffice Linha Protheus - Controladoria Gerencial - A partir da release 12.1.33  
  
**Causa**Falta de parametrizações no Appserver.Ini do Protheus.

**Solução**Para corrigir o erro, veja os passos abaixo:

Confira se as Tags abaixo estão configuradas corretamente no Appserver.Ini em seu ambiente:

Para a utilização da nova funcionalidade Conciliador Contábil e Validador ECD/ECF por exemplo, é necessária a ativação da porta multi-protocolo no appserver.ini do seu ambiente Protheus.

* + Na seção GENERAL, deve-se incluir a chave “**App\_Environment”**, cujo valor deve ser o nome do ambiente que os serviços PO-UI rodarão.
  + Na seção DRIVERS,  deve-se habilitar a porta **multiprotocolo** na chave “**MultiProtocolPort”** com o valor = **1.**
  + Por padrão a conexão **SSL** está ativa na porta **multiprotocolo**, os detalhes das configurações estão disponíveis na documentação [Application Server - Porta Multiprotocolo](https://tdn.totvs.com/x/jIUoI). Para desabilitar a conexão por SSL é necessário informar a chave “**MultiProtocolPortSecure = 0”**

Para mais informações sobre essa configuração acesse a página [Application Server - Porta Multiprotocolo](https://tdn.totvs.com/x/jIUoI).

Exemplo:  
  
![](https://tdn.totvs.com.br/download/attachments/648811255/image2022-8-17_15-45-8.png?version=1&modificationDate=1660761909113&api=v2)

![](https://tdn.totvs.com.br/download/thumbnails/648811255/image2022-12-1_16-12-12.png?version=1&modificationDate=1669921932577&api=v2)

**Obs:**Caso tenha balanceamento de carga nos AppServer, é necessário que tanto o Master quanto os Slaves possuam a configuração das Tags no arquivo Ini. 

Após Configuração das Tags, realizar o procedimento abaixo:

**01.**Acesse **c:\totvs\Protheus\_Data\FrameHTML;  
02.** Renomeie a pasta Http-Root;

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11534785277591)

**03.**Após aplicar as alterações, reinicie os serviços do  Appserver e tente novamente o acesso via Desktop.

**Saiba Mais**

[Conciliador Backoffice - CTBA940 - P12 - Contabilidade Gerencial](https://tdn.totvs.com.br/display/public/PROT/Conciliador+Backoffice+-+CTBA940+-+P12+-+Contabilidade+Gerencial)

[Validador ECD / ECF](https://tdn.totvs.com/pages/releaseview.action?pageId=665275974)

[Chave App\_Environment](https://tdninterno.totvs.com/pages/viewpage.action?pageId=556382089)

[Balanceamento de carga](https://tdn.totvs.com/display/tec/Balanceamento+de+carga)
