---
article_id: 360050353553
category: IMPLANTAÇÃO
content_hash: 17cfe5f98f81856e9a21139af2bc05e9200e1f7fca5892c218effec5bb9f465c
fetched_at: '2026-06-28T22:44:33.399061+00:00'
product: protheus
section_id: 10299929290007
source: central-protheus
title: RH - Linha Protheus - MEU RH - Como configurar um endereço para cada um dos
  diferentes Grupos de Empresas
type: support-article
updated_at: '2026-06-22T18:17:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050353553-RH-Linha-Protheus-MEU-RH-Como-configurar-um-endere%C3%A7o-para-cada-um-dos-diferentes-Grupos-de-Empresas
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24762680484503) Tempo aproximado para leitura: 00:05:00 min****Dúvida**Como configurar um endereço para cada um dos diferentes Grupos de Empresas?  
  
**Ambiente**TOTVS RH (Linha Protheus) - Meu RH – todas as versões  
  
**Solução**A configuração adequada está descritas passo a passo na **[Documentação de referências sobre o MEU RH](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)**, essa FAQ foi criada para auxiliar aqueles com problema na configuração indicando como realizar a manutenção diretamente no arquivo informado.  
  
No artigo **[Informações Relevantes sobre HTTP/REST no Meu RH](https://tdn.totvs.com/pages/releaseview.action?pageId=550327736)** temos explicações técnicas mais aprofundadas sobre essa configuração.  
Abaixo demonstraremos um exemplo da configuração mais indicada onde é utilizado um endereço/link de acesso para o MEU RH para cada um dos diferentes Grupos de Empresa do mesmo SIGAMAT utilizando o mesmo **appserver.ini**, mas é altamente recomendado ter um server para cada serviço *REST*.  
  
**IMPORTANTE:** Quando menciono "Grupo de Empresa", me refiro a divisão do SIGAMAT do Protheus, no meu caso, a configuração desse artigo é para cada um dos Grupos, ou seja, todas Empresas, Unidades de Negócio e Filiais dentro desses Grupos terão acesso ao MEU RH, mas cada Grupo com seu próprio endereço/link de acesso, nesta situação é necessário um diretório com os arquivos do Portal Meu RH para cada endereço/link de acesso.  
  
![xjUzXgDcN9.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4407201398295)  
  
Segue abaixo um modelo do **appserver.ini** dessa configuração, neste caso é necessário se atentar que:

1. É utilizado um diretório com os arquivos do portal MEU RH para cada Grupo onde cada um terá seu próprio **properties.json** apontando o endereço/link específico do Grupo;
2. O endereço de acesso será conforme o Grupo, ou seja, o Grupo **01** vai usar o endereço/link de acesso "**192.168.0.4:8088/01**", o Grupo **02**vai usar o endereço/link de acesso "**192.168.0.4:8088/02**" e assim sucessivamente, veremos mais a frente que cada um terá sua própria chave "**PrepareIn**";  
     
   ![je9Xp274w1.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4407207939735)
3. Nesse exemplo utilizo uma única porta REST para todos endereços, mas tenho que criar diferentes chaves "**[HTTPENV]**" para cada Grupo e apontar a chave "**PrepareIn**" para cada Grupo específico;  
     
   ![yBofNvkYce.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4407215360407)

Segue abaixo um modelo do **properties.json**dessa configuração, neste caso é necessário se atentar que o conteúdo da chave "**rootcontext**" deve ter "**//**" (duas barras) e no meio deve conter o conteúdo da chave "**PrepareIn**", lembrando que teremos um **properties.json** para cada Grupo de Empresa, conforme "**PATH**" configurado.  
  
![ZImZZ8KZCE.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4407215418263)  
  
**Obs.: Segue em anexo ao final deste artigo uma cópia do arquivo properties.json**  
  
Segue abaixo um modelo da configuração do **QRCode** dessa cenário, ele é utilizado para configuração do APP MEU RH nos aparelhos celulares. Neste caso também será necessário um **QRCode** para cada Grupo de Empresa apontando para um endereço/link específico. Neste cenário é necessário se atentar que a URL deve ter aquelas "**//**" (duas barras), porém no meio vai o conteúdo da chave "**PrepareIn**" de cada Grupo.  
  
Segue exemplo da configuração do **QRCode** de como irá ficar do Grupo **01** e grupo **02**  
  
![VurcpMBfMS.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4407215494807)  
  
Para mais detalhes sobre essa configuração acesse o artigo abaixo:  
**[RH - Linha Protheus - MEU RH - O que devo configurar para acessar o MEU RH?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050243093)**  
  
**ATENÇÃO:** Certifique-se sempre de estar com seu ambiente atualizado, pois são disponibilizados periodicamente atualizações com melhorias e correções no MEU RH.  
**[RH - Linha Protheus - MEU RH - Como Atualizar os arquivos do Portal Meu RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043729034)**  
**[RH - Linha Protheus - MEU RH - Pacote de acumulado do RH no Portal de Cliente](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500007189282)****Saiba Mais:  
[RH - Linha Protheus - MEU RH - Como configurar o APPSERVER.INI, PROPERTIES.JSON e URL do QRCODE para acesso ao MEU RH?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044715514)  
[RH - Linha Protheus - MEU RH - Qual deve ser o conteúdo do arquivo PROPERTIES.JSON](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049493314)**  
[**CLIQUE AQUI** para acessar mais artigos e FAQs sobre o MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)  
[**CLIQUE AQUI** para acessar a documentação de referências sobre o MEU RH](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)
