---
content_hash: c01ce958c7d51a32754a7f4b32f8462f95622451414d7fd1dd5bcef1a1d50cf0
fetched_at: '2026-06-29T00:10:59.652704+00:00'
page_id: '615129945'
product: rm
source: tdn-rm
title: TGM com Config Global
type: documentation
url: https://tdn.totvs.com/display/LRM/TGM+com+Config+Global
version: 5
---

## **ÍNDICE**

1. **Visão Geral**
2. **Exemplo de utilização**

**01. VISÃO GERAL**

O TOTVS Gateway Manager pode ser utilizado com o arquivo de configuração global. Para entender mais sobre esse formato e funcionamento da configuração, acesse  

Veja nos próximos tópicos como ficam os principais arquivos de configuração global para utilizar o TGM.

**02. EXEMPLO DE UTILIZAÇÃO**

Abaixo estão os principais pontos que devem ser alterados após configurar o  para ser utilizado com o TGM.

1) Para utilizar essa configuração é necessário ter o arquivo de configuração global (Global.config.json) dentro da pasta do TGM.

2) Nos arquivos de configuração do Host (service ou .exe) e RM, de cada estação, dentro de <appSettings>:

       • A tag ***CONFIGGLOBALADDRESS***deve apontar para o endpoint do TGM, no seguinte padrão: "[http://NomeServer:8040/api/globalconfig](http://BHN019401390:8040/api/globalconfig)", onde o NomeServer deve ser preenchido com o nome do servidor do TGM e a porta deve ser a porta do serviço do TGM.

Onde localizar a porta de configuração:

      Exemplos dos arquivos de configuração:

150 150150150

API para consulta de algum AppKey do config global com TGM: [http://servidor:porta/api/globalconfig/appconfig/AppKeyNome](http://bhd050101853:8040/api/globalconfig/appconfig/RM).

Onde o servidor e a porta são do serviço do TGM e o AppKeyNome deve ser o nome da chave dada no Config Global.  Exemplo: [http://bhd050101853:8040/api/globalconfig/appconfig/RM\_TGM](http://bhd050101853:8040/api/globalconfig/appconfig/RM)

Para mais informações sobre o TGM, como funcionamento, configuração, log de erros e outros, consulte:
