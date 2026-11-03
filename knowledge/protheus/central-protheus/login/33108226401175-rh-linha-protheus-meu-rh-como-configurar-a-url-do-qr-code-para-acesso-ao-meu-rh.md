---
article_id: 33108226401175
category: LOGIN
content_hash: 3e00af76ecfdfc7239cf5dd0b86fc28060ee88f43a00de1d63478b6de01adcdb
fetched_at: '2026-06-28T22:44:40.372133+00:00'
product: protheus
section_id: 10299559916567
source: central-protheus
title: RH - Linha Protheus - MEU RH - Como configurar a URL do QR Code para acesso
  ao MEU RH
type: support-article
updated_at: '2025-12-16T11:36:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/33108226401175-RH-Linha-Protheus-MEU-RH-Como-configurar-a-URL-do-QR-Code-para-acesso-ao-MEU-RH
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33108186780055) Tempo aproximado para leitura: **00:03:00 min**  
  
**Dúvida**  
Como gerar o ***QRCode***de acesso ao Portal Meu RH via *App* e como extrair os dados para geração.  
  
**Ambiente**  
TOTVS RH (Linha Protheus) - Meu RH – todas as versões  
  
**Solução**:  
Para configurar o ***QRCode***de acesso ao aplicativo, basta seguir as orientações abaixo:  
  
Nos arquivos do Portal MEU RH existe um arquivo chamado ***qr-generator.html*** que pode ser utilizado para geração do ***QRCode*** de configuração do *APP* no celular.  
  
Segue exemplo de como a ***URL*** deve estar configurada para configurar o ambiente:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33557498086679)  
  
**Dicas sobre configuração das credenciais do app/Qrcode**  
  
Para o correto preenchimento devemos inicialmente encontrar os dados para incluir na configuração do QR Code  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33556356720151)  
  
**Campo*****URL***  
  
No campo **URL**, será preenchido com os dados de acesso Web do MEU RH e adicionar o conteudo "**/?restPort=**" + Porta do REST.  
  
**Importante sobre o Campo*****URL*****:**a palavra**/?restPort=** tem que ser exatamente como esta, se mudar qualquer letra de maiúscula para minúscula e vice versa pode interferir**.**  
  
Acesso Web do MEU RH, não copiar o "**/#/login**"  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33556347691287)  
  
Incluir a informação no Gerador de QR Code, Link de acesso Web + **/?restPort= +** Porta Rest (será adicionada após extração de dados do properties a seguir).  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33556347691799)  
  
**Campo*****Rest******URL***  
  
No Campo Rest URL, será preenchido com os dados de acesso ao REST que pode ser extraido do Properties.json  
  
Abrir o acesso web do MEU RH, clicar no **F12**, incluir um filtro com o nome **Properties**, após atualizar a pagina será apresentado o arquivo encontrado Properties.json.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33556356722071)  
  
Baixar o arquivo, ao clicar duas vezes no Properties.json, será direcionado para seleção de pasta para salvar.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33556356722327)  
  
Acessar a pasta onde foi baixado o arquivo e abrir o Properties.json  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33556356722967)  
  
Copiar a URL de acesso ao REST e verificar se está ativo, este passo é importante pois se o mesmo não estiver ativo não irá funcionar corretamente o App MEU RH.  
  
URL Rest ativa  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33556356725143)  
  
Incluir a URL do rest no configurador de QrCode, copiar a porta do **Rest URL** para a **URL**  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33556356726935)  
  
Concluir a geração do QR Code, Identificador e Ambiente o preenchimento é livre.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33556347696023)  
  
***How to*****de como gerar*****QRcode*****para acesso ao Meu RH:**  
<https://youtu.be/Flt-LKPEyBY>  
  
**Saiba Mais:**  
[RH - Linha Protheus - MEU RH - Como configurar o APPSERVER.INI e PROPERTIES.JSON para acesso ao MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044715514-RH-Linha-Protheus-MEU-RH-Como-configurar-o-APPSERVER-INI-e-PROPERTIES-JSON-para-acesso-ao-MEU-RH)  
[RH - Linha Protheus - MEU RH - Qual deve ser o conteúdo do arquivo PROPERTIES.JSON](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049493314-RH-Linha-Protheus-MEU-RH-Qual-deve-ser-o-conte%C3%BAdo-do-arquivo-PROPERTIES-JSON)  
[RH - Linha Protheus - MEU RH - Pacote de acumulado do RH no Portal de Cliente](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500007189282)  
[CLIQUE AQUI para acessar mais artigos e FAQs sobre o MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)  
[CLIQUE AQUI para acessar a documentação de referências sobre o MEU RH](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)
