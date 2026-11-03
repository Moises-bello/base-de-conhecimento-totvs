---
content_hash: 3aee4566d5e9e410090e0a8361b97c741fc43cf8e723eb026381e2252c440d18
fetched_at: '2026-07-02T19:24:27.761423+00:00'
page_id: '680246280'
product: protheus
source: tdn-tec
title: SCPing
type: documentation
url: https://tdn.totvs.com/display/tec/SCPing
version: 6
---

A partir da versão 20.3.1.0 do Smartclient e Appserver, uma nova ferramenta de análise de rede estará disponível.

Assim que um certo tempo (configurável, por padrão, acima de 100ms) de resposta entre o Appserver e o Smartclient for detectado um aviso será exibido no "tray" do sistema operacional, informando um possível problema de infraestrutura/rede:

Clicar nessa mensagem irá mostrar um gráfico com as informações de latência coletadas:

Também nessa tela, é possível verificar o uso de CPU e da memória RAM do Sistema Operacional:

Nessa tela já é possível Salvar os arquivos logs diretamente através do botão "Salvar Log".

Caso isso aconteça, ao finalizar o Smartclient dois arquivos de log serão gerados no diretório Temporário da máquina:

* totvssmartclient\_nettest.log: Contendo informações de Data/hora e Ping (em ms)
* totvssmartclient\_nettest\_cpuram.log: Contendo informações de Data/hora e uso de CPU/RAM.

Alerta

O alerta só será exibido uma vez por execução do Smartclient, isto é, só na primeira vez que o problema de latência ocorrer (de acordo com os parâmetros configurados). Após isso, mesmo que o problema volte a ocorrer o alerta não será mais exibido até o Smartclient ser reiniciado.

Para ajustes finos do comportamento, veja as configurações no appserver.ini .
