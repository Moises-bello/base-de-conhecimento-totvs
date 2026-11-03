---
article_id: 360043729034
category: ATUALIZAÇÕES
content_hash: a30a5d3600e7cdd32114d4282c386569b87458441453073ce7f8a9a4143a6a4e
fetched_at: '2026-06-28T22:44:32.672031+00:00'
product: protheus
section_id: 10325349771415
source: central-protheus
title: RH - Linha Protheus - MEU RH - Onde baixo a versão mais recente e como atualizar
  os arquivos do Portal Meu RH
type: support-article
updated_at: '2026-04-16T11:19:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043729034-RH-Linha-Protheus-MEU-RH-Onde-baixo-a-vers%C3%A3o-mais-recente-e-como-atualizar-os-arquivos-do-Portal-Meu-RH
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22226906684055) Tempo aproximado para leitura: 00:05:00 min****Dúvida**  
Onde baixo a versão mais recente e como atualizar os arquivos do Portal Meu RH?  
  
**Ambiente**TOTVS RH (Linha Protheus) - Meu RH – todas as versões  
  
**Solução**Segue abaixo passo de como baixar e atualizar os arquivos do Portal MEU RH: **![chrome_20cj7Sg7zo.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/5431462203287)**  
Segue **abaixo**, ***link*** para *download*:  
**<https://suporte.totvs.com/portal/p/10098/download?e=696055>**  
\*\* Cabe ressaltar que, **os arquivos de portal** Meu RH, **não possuem *release*** do Protheus, portanto, poderão ser utilizado para qualquer versão deste ERP.  
Após **baixar** os arquivos e **descompactar** a pasta, será obtida a seguinte estrutura de arquivos (imagem abaixo):  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/14597158571287)  
  
Dentro desse arquivo será encontrada a pasta "**PortalMeuRH**", contendo os WebFiles, essa pasta deve ser descompactada no diretório ***web*** no mesmo caminho informado na tag **RootPath** no appserver.ini do ambiente utilizado, ou seja, dentro do **ProtheusData**.  
  
Exemplo do appserver.ini do ambiente do MEU RH:  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8389890916119)  
  
**C:\Ambiente\_33\protheus\_data\web\PortalMeuRH**  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8389888612631)

O caminho criado será posteriormente utilizado na chave *Path* das seções **HTTP** e auxiliar do Meu RH dentro do appserver.ini.  
Em casos de ambiente com unidade de rede mapeada, segue-se o mesmo conceito listado acima, ambos precisam estar no mesmo caminho/diretório.  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8389953729175)  
  
**ATENÇÃO**: Ao baixar os arquivos do Portal MEU RH, dentro da pasta virá um arquivo **PROPERTIES.JSON em BRANCO**, ou seja, ao substituir os arquivos do ambiente pelos arquivos novos cuidado para não sobrepor este arquivo, caso contrário, não conseguirá acessar o MEU RH.  
![Arquivos_MEU_RH.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/8390132881047)  
  
**Dica de atualização:**  
Dentro do diretório atual, delete todos os arquivos existentes, **menos o properties.json**, assim a pasta terá somente os arquivos atualizados.  
  
Ao baixar os arquivos do Portal MEU RH, dentro da pasta virá um **arquivo PROPERTIES.JSON como exemplo**, ou seja, ao substituir os arquivos do ambiente pelos arquivos novos, atenção para **não sobrepor este arquivo**, caso contrário, **não conseguirá acessar o MEU RH.**  
  
No artigo abaixo explicamos o preenchimento do referido arquivo:  
[**RH - Linha Protheus - MEU RH - Qual deve ser o conteúdo do arquivo PROPERTIES.JSON?**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049493314)  
  
**Documentação de referência:** [Atualizando os arquivos](https://tdn.totvs.com/display/public/NPR/Passo+1%3A+Atualizando+os+arquivos)  
  
Veja no *link* abaixo, um *How-To* criado de como realizar corretamente a atualização dos arquivos.  
[**https://www.youtube.com/watch?v=DWIVCMJDFWk**](https://www.youtube.com/watch?v=DWIVCMJDFWk)  
  
**Saiba Mais:**  
[**RH - Linha Protheus - MEU RH - O que devo configurar para acessar o MEU RH?**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050243093)  
[**RH - Linha Protheus - MEU RH - Como configurar o APPSERVER.INI, PROPERTIES.JSON e URL do QRCODE para acesso ao MEU RH?**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044715514)  
[**CLIQUE AQUI** para acessar mais artigos e FAQs sobre o MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)  
[**CLIQUE AQUI** para acessar a documentação de referências sobre o MEU RH](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)
