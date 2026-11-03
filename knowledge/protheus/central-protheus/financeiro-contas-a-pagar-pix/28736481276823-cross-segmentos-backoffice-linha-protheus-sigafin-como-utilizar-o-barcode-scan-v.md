---
article_id: 28736481276823
category: Financeiro - Contas a Pagar - PIX
content_hash: 87436673de79d45979c0dca82bd12807ebf279705d4e5a50fb4b1293c89dd10a
fetched_at: '2026-06-28T22:38:11.326041+00:00'
product: protheus
section_id: 1500001550462
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Como utilizar o Barcode_Scan
  via WebApp?
type: support-article
updated_at: '2026-06-09T16:47:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28736481276823-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Como-utilizar-o-Barcode-Scan-via-WebApp
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28736481256087) Tempo aproximado para leitura: **00:08:00 min**  
  
**Dúvida**  
Como utilizar o BarCode\_scan via WebApp?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro – A partir da release 12.1.2410  
  
  
**Solução**  
Sim, é possível utilizar o **BarCode** no **WebApp** com o **WebAgent** habilitado. O funcionamento segue o mesmo conceito adotado no **SmartClient.**

No **SmartClient**, é necessário que o componente **BarcodeScan** esteja disponível na pasta da aplicação. Da mesma forma, no **WebApp**, o componente deve estar localizado na pasta utilizada pelo **WebAgent**, para que a leitura de código de barras funcione corretamente.  
  
**Documentação do webagent:**  
[TOTVS | WebAgent](https://tdn.totvs.com/display/tec/2.+WebApp+-+WebAgent)  
  
Após a instalação e habilitação do **WebAgent** na estação, é necessário copiar o arquivo **BARCODE\_SCAN.EXE** para o diretório de instalação do WebAgent.

Para localizar a pasta **AppData**, que por padrão é oculta no Windows, uma forma prática é utilizar o **Prompt de Comando (CMD)**.

Siga os passos abaixo para acessar o caminho:

**1.**Abra o **Prompt de Comando**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34983204341911)

**2.** Digite o comando abaixo e pressione **Enter**:

```
CD appdata e pressione Enter
```

**3.** Em seguida, digite o caminho do diretório.

```
C:\Users\%nomedousuariodamaquina%\AppData\
```

**4.** Dentro da pasta AppData localize a pasta Local\Programs\web-agent, na pasta de instalação do **Web-Agent** adicione o executável **BARCODE\_SCAN.EXE**.

Dessa forma, não é necessário habilitar a visualização de pastas ocultas para localizar o diretório de instalação do WebAgent.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/41090913703703)

**5.** Adicione também o arquivo **webagent.json**, conforme demonstrado na imagem acima.

Esse arquivo é responsável por informar a versão do **WebAgent** e os respectivos instaladores disponibilizados para cada sistema operacional.

É importante que o campo **version** seja atualizado com a versão correta do WebAgent que será distribuída aos usuários.

Exemplo:

```
{
    "version": "1.x.x",
    "windows_x86": "webagent\\web-agent-1.X.X-windows-x86-release.setup.exe",
    "windows_x64": "webagent\\web-agent-1.X.X-windows-x64-release.setup.exe",
    "darwin_universal": "20-10-10-p12_smartclient_web-agent_1.1.0_mac-universal.dmg",
    "linux_x64_deb": "webagent\\web-agent.deb",
    "linux_x64_rpm": "webagent\\web-agent.rpm"
}
```

> **Observação:** Substitua o valor do campo **version** pela versão efetivamente disponibilizada do WebAgent e valide se os nomes dos arquivos informados correspondem aos instaladores presentes no ambiente.

**6.**  No **AppServer**, configure também a versão do **WebAgent** na seção **[WebApp/webapp]**, informando a versão disponibilizada e o caminho do instalador correspondente.

Exemplo:

```
[WebApp/webapp]
MPP=
VERSION=1.1.0
Windows_x64=C:\totvs\files\web-agent-1.1.0-windows-x64.setup.exe
```

> **Importante:** O conteúdo informado na **VERSION** deve ser o mesmo configurado no arquivo **webagent.json**.

**Requisitos para o perfeito funcionamento da rotina:**

* Os binários do ambiente devem estar devidamente atualizados.
* O **WebAgent** deve estar na versão **1.0.19 ou superior**. Caso necessário, realize a atualização utilizando o link abaixo:

  [Download WEB-AGENT](https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/WEB-AGENT)
* O componente **Barcode Scan** também deve estar atualizado para a versão mais recente. Utilize o link abaixo para efetuar a atualização:

  [BARCODE SCAN](https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/BARCODE)

Acesse o **Protheus Web**. Ao iniciar a aplicação, será exibida a mensagem **"Deseja executar o WebAgent agora?"**.

Clique em **"Sim"** para permitir a execução do WebAgent e, em seguida, realize a leitura utilizando o **BarcodeScan** para validar o funcionamento da integração.
