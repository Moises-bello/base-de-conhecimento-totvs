---
article_id: 13618422681367
category: Suricato
content_hash: 6c7e611057ace5e24089728a3909c1fbada235c5226f45ec15ace1f88ff3efdd
fetched_at: '2026-06-28T22:46:26.386870+00:00'
product: rm
section_id: 28312167464215
source: central-rm
title: RH - RM - PTO - Importação de batidas via API de integração com Suricato
type: support-article
updated_at: '2025-09-04T15:28:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/13618422681367-RH-RM-PTO-Importa%C3%A7%C3%A3o-de-batidas-via-API-de-integra%C3%A7%C3%A3o-com-Suricato
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19408788377495) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**Como configurar a importação das batidas integradas via API pelo Suricato  
  
**Ambiente**RH - RH (Linha RM) - TOTVS Automação de Ponto - A partir da versão 12.1.2205  
  
**Solução**

A configuração básica para utilização da importação de batidas integradas via API, consiste em informar no parametrizador, que o sistema irá utilizar a integração.

Para isso, basta acessar o menu **Configurações | Parametrizador**, no processo 08.01 - Iniciais, avance até a Etapa 5 - Integração-Integração Carol/TSA e selecionar o parâmetro **"Utilizar integração com o TSA".**

Ao confirmar a integração o parâmetro **"Importar batidas integradas via API",** será habilitado. Marque esse parâmetro caso queira realizar a importação de batidas via API.

**![](https://tdn.totvs.com/download/attachments/682054374/image2022-4-20_18-31-33.png?version=1&modificationDate=1650490293983&api=v2)**

Para realizar a importação de batidas acesse o menu **Entrada de Dados | Importar.** Na tela de importação, ao configurar o parametrizador da forma demonstrada acima, irá habilitar o parâmetro **"Utilizar integração com o TSA".**

![](https://tdn.totvs.com/download/attachments/682054374/image2022-4-20_18-31-56.png?version=1&modificationDate=1650490317120&api=v2)

Ao marcar este parâmetro, as seguintes opções serão desabilitadas:

* Arquivo para importação;
* Layout do Relógio;
* Terminal de Coleta para Histórico;
* Considera última linha importada;

**Importante:**

1. O usuário poderá definir se a importação das batidas irá considerar as informações armazenadas na tabela MSA\_CONTROL\_MARCAC ou na tabela AINTEGRACAOBATIDAS. Não sendo possível considerar ambas as tabelas simultaneamente.
   1. Marque apenas o parâmetro "Utilizar integração com o TSA ", caso queira importar as informações armazenadas na tabela MSA\_CONTROL\_MARCAC,
   2. Marque também o parâmetro "Importar batidas integradas via API" e com isso as informações importadas serão da tabela AINTEGRACAOBATIDAS
2. É necessário fornecer ao time da Telemática a URL da API e do TOKEN para que o Suricato posso ser configurado de forma a enviar as marcações para a tabela AINTEGRACAOBATIDAS
   1. URL API: http://SERVIDOR:APIPORT/api/rh/v1/recordClockMarkings/integracaobatidas  
      Exemplo: http://192.168.01.01:8051/api/rh/v1/recordClockMarkings/integracaobatidas
   2. TOKEN: http(s)://SERVIDOR:APIPORT/api/connect/token/  
      Exemplo: http://192.168.01.01:8051/api/connect/token/
3. Também é preciso informar ao time da Telemática um usuário e senha do RM que tenha acesso aos módulos Automação de Ponto e Folha de Pagamento.

**Saiba mais:**[DT API recordValidatedVersion](https://tdn.totvs.com/display/LRM/DT+API+recordValidatedVersion)

[DT API recordClockMarkings](https://tdn.totvs.com/display/public/LRM/DT+API+recordClockMarkings)
