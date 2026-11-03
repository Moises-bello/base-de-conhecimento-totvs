---
article_id: 14478100241047
category: IMPLANTAÇÃO
content_hash: 1fa55e800e0e34d9e92e6b3ee916ef522fa253e38cb40a1dd281575f0d6d12a1
fetched_at: '2026-06-28T22:44:33.349538+00:00'
product: protheus
section_id: 10299929290007
source: central-protheus
title: RH - Linha Protheus - Meu RH - Configuração da seção HTTP no appserver.ini,
  para acesso ao App Meu RH
type: support-article
updated_at: '2026-06-19T13:57:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/14478100241047-RH-Linha-Protheus-Meu-RH-Configura%C3%A7%C3%A3o-da-se%C3%A7%C3%A3o-HTTP-no-appserver-ini-para-acesso-ao-App-Meu-RH
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24442888209687) Tempo aproximado para leitura: **00:02:00**  
  
**Dúvida**  
Configuração da sessão HTTP, no appserver.ini, para acesso ao Meu RH?  
  
**Ambiente**  
TOTVS RH (Linha Protheus) - Meu RH – Todas as versões  
  
**Solução**  
Ao realizar a configuração do arquivo appserver.ini, **para a utilização e acesso ao App Meu RH**, é criada uma seção chamada **[HTTP]**. Esta seção contém informações de configuração do *Appserver* operando como **servidor HTTP**.  
  
Para utilização do App Meu RH, algumas *tags* dentro da seção [HTTP] são necessárias, exemplo:  
  
[HTTP]  
ENABLE=1  
PATH=C:\PROTHEUS\_1233\Protheus\_Data\web  
PORT=8088  
ENVIRONMENT=P1233 (exemplo de ambiente utilizado)  
COMPRESSION=1  
  
Abaixo, há explicação sobre cada uma das *tags*:  
- ***ENABLE***, basicamente diz ao Appserver que a **seção HTTP está habilitada**;  
- ***PATH***, é muito importante termos nela, **o caminho correto dos arquivos de portal Meu RH**.  
Por convenção, os arquivos de portal, ficarão numa sub-pasta da pasta *web*, que por sua vez, **ficará dentro da Protheus\_data**, porém no caminho da ***tag PATH*** é necessário indicar **somente até a pasta \web, ou seja, o diretório raiz dos arquivos de portal;**  
- ***PORT***refere-se à porta utilizada para **acesso ao Meu RH,** a mesma configurada na **URL de acesso;**  
- **ENVIRONMENT** contém as informações de configuração do **ambiente utilizado para o Meu RH**;  
- **COMPRESSION**, esta chave pode ser utilizada **para habilitar/desabilitar**, a compressão em um *host* específico, **caso um servidor HTTP, do Sistema, esteja em uso para mais de um** ***host***.  
  
Lembrando que, neste exemplo, há a configuração básica sobre a **seção HTTP e suas chaves obrigatórias**, para o correto funcionamento do App Meu RH.  
  
**Saiba Mais**  
[**CLIQUE AQUI** para acessar mais artigos e FAQs sobre o MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)  
[**CLIQUE AQUI** para acessar a documentação de referências sobre o MEU RH](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)
