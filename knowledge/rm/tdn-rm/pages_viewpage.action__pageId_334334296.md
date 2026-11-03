---
content_hash: 0240effcc61e47481113eea508d327f4d587d523dddf8729273ce488255d5948
fetched_at: '2026-06-29T00:08:50.406808+00:00'
page_id: '334334296'
product: rm
source: tdn-rm
title: Como realizar a configuração da URL do TSS e onde informar o Certificado Digital
  para realizar a transmissão dos eventos do eSocial para o governo?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=334334296
version: 4
---

Segue abaixo as orientações de como realizar a configuração da URL do TSS para transmissão dos eventos do eSocial para o governo:

1.Acesse o caminho abaixo após concluir a instalação do TSS: C:\totvssped\bin\appserver

**OBS:** Verifique em qual diretório foi realizada a instalação, no exemplo instalamos no disco"C:".

**Manual de instalação do TSS:** <http://tdn.totvs.com/pages/releaseview.action?pageId=274324643>

2.Localize o arquivo **appserver.ini** e edite para localizar a chave "[localhost:8090]" que apresenta os dados da URL de Webservice de acordo com o servidor e a porta informada na instalação:

3.Teste a URL no seu navegador de internet para verificar se está conectando:

**OBS:** A informação do 1º print será utilizada para montar a URL do TSS que será informada no caminho exemplificado abaixo:

4.Acesse o TAF, clique em Atualizações/Configs TAF/Wizard de Config TSS:

5.Preencha os dados abaixo de acordo com o seu ambiente e informe a URL de acordo com os dados contidos no arquivo Appserver.ini:

6.Após preencher os dados do print anterior, avance e informe as configurações do Certificado Digital de acordo com as especificações do modelo da sua empresa:

**Dica!** [Procedimento de configuração de certificados modelo A3](http://tdn.totvs.com/display/public/TSS/TSS0042_Configurar_certificado_A3)

7.Configure uma conta de e-mail caso queira receber as notificações da transmissão:

8.Avance para concluir:

9.Acesse o menu de Monitoramento para realizar a transmissão dos Eventos:

10.Aplique os filtros:

11.Selecione os eventos e clique em **Transmitir ao Governo**:
