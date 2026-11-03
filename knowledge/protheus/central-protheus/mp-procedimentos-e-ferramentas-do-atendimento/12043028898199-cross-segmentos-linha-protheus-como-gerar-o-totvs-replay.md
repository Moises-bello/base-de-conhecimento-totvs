---
article_id: 12043028898199
category: MP - Procedimentos e Ferramentas do Atendimento
content_hash: 962ab816cf2ba044a91bf28659a6a72227a21db4e70b80d97ff5b8f657b9a4ce
fetched_at: '2026-06-28T22:36:36.745771+00:00'
product: protheus
section_id: 360011719313
source: central-protheus
title: ' Cross Segmentos - Linha Protheus - Como gerar o TOTVS Replay'
type: support-article
updated_at: '2023-07-21T20:22:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/12043028898199--Cross-Segmentos-Linha-Protheus-Como-gerar-o-TOTVS-Replay
---

**Dúvida**Como gerar o **TOTVS Replay**?  
  
**Ambiente** Cross Segmentos - Linha Protheus - A partir da versão 12.1.25  
  
**Solução**Para geração do **TOTVS Replay** é necessário que o ambiente conste as atualizações de pré-requisito abaixo:  
  
**Protheus 12.1.25 com binário - appserver 17.3.0.20 ou superior****Windows -**[Clique aqui para download do appserver para Windows](https://suporte.totvs.com/portal/p/10098/download#detail/737297)**Linux -**[Clique aqui para download do appserver para Linux](https://suporte.totvs.com/portal/p/10098/download#detail/737298)  
  
**Protheus 12.1.27 com binário - appserver 19.3.0.2 ou superior****Windows -**[Clique aqui para download do appserver para Windows](https://suporte.totvs.com/portal/p/10098/download#detail/947528)**Linux -**[Clique aqui para download do appserver para Linux](https://suporte.totvs.com/portal/p/10098/download#detail/947509)  
  
**Lib com data maior ou igual a 20200727**[Clique aqui para download da LIB](https://suporte.totvs.com/portal/p/10098/download#detail/989259)  
  
Para gerar o **TOTVS Replay**, acesse a rotina que estiver apresentando a inconsistência e clicar em **SHIFT+F6**. Navegue até a quinta aba eclique em **Iniciar** e em seguida **Concluir**.

![Captura_de_tela_2021-05-24_173617.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16203807705111)

Execute o processo até que seja reproduzido o incidente, clique em **SHIFT+F6** e navegue até a quinta aba, clique em **Finalizar** e em seguida **Concluir.**Ao finalizar, será apresentado a tela abaixo informado o diretório onde será salvo o arquivo que por padrão é sempre a pasta do **smartclient**.

![3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16203807707671)

Localizar o arquivo e enviar via **ticket** para que o analista da **TOTVS** analisar o conteúdo gerado.

**Importante**O arquivo a ser gerado deve possuir a extensão **.trplay**. Se gerar como **.trparam**, será necessário aplicar as atualizações de **BUILD** e **LIB** listadas na documentação. **Saiba mais**Para mais informações sobre **TOTVS Replay**, acesse o link: [TDS Replay](https://github.com/totvs/tds-vscode/wiki/TDS-Replay)

**Exemplo:**
