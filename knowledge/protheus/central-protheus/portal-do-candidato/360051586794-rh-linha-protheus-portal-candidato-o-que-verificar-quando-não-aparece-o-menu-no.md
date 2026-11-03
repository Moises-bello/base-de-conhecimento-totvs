---
article_id: 360051586794
category: Portal do Candidato
content_hash: 10d4387f85a6c7dbb43389f3ac4c10e9a8c555c4fdd06e690f85e7386a8ac886
fetched_at: '2026-06-28T22:42:57.754944+00:00'
product: protheus
section_id: 360005048093
source: central-protheus
title: RH - Linha Protheus - PORTAL CANDIDATO - O que verificar quando não aparece
  o Menu no Portal do Candidato
type: support-article
updated_at: '2025-05-05T11:36:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051586794-RH-Linha-Protheus-PORTAL-CANDIDATO-O-que-verificar-quando-n%C3%A3o-aparece-o-Menu-no-Portal-do-Candidato
---

**Dúvida**O que verificar quando não aparece o Menu no Portal do Candidato?  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360081623014)  
  
**Ambiente**TOTVS RH (Linha Protheus) - Portal do Candidato – Todas as versões  
  
**Solução**Deverá realizar atualização do Web Files e extrair dentro da pasta Systemload, verifique o link abaixo:  
**[MP - PORTAL GCH - Como Atualizar os arquivos do Portal](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044250613)**

Após atualização, deverá acessar o SRVWIZARD, no item Módulo Web e editar as instancias WS e PC, avance todas telas será apresentado mensagem "Deseja descompactar o arquivo http na pasta especificada?", clique em SIM para atualizar os novos arquivos.  
  
**Importante:** Sempre será necessário configurar um **web service** para cada empresa/filial e para acesso ao portal existem licenças específicas que necessitam da contratação do cliente.  
Para mais informações, verifique o artigo: **[MP - PORTAL CANDIDATO - Como Instalar e Configurar o Portal do Candidato](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360029084072-MP-PORTAL-CANDIDATO-Como-Instalar-e-Configurar-o-Portal-do-Candidato)**  
  
- Limpe os *cookies* do navegador e também a pasta temporária do Windows.  
  
- Verifique o compartilhamento das tabelas AI7, AI8 e AI9 se estão iguais, conforme abaixo, oriento que estas 3 tabelas, sejam criadas como TOTALMENTE COMPARTILHADA, ou seja, C C C.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19458856659607)

As vezes é necessário recriar as tabelas AI7, AI8 e AI9 e depois refazer os passos abaixo:  
\* Entre no módulo SIGATCF (18) e acesse o menu *Atualizações >Configurações > Web Services.*\* Ao entrar na rotina, clique em "Outras Ações" e Automático:  
\* Depois, acesse o menu *Atualizações > Configurações > Menus*:  
**\* Observação:** Não é necessário efetuar nenhuma manutenção nos menus, apenas entrar na rotina e sair para carregar as informações.

- Certifique-se que o ambiente está com último Acumulado RH aplicado:   
**[MP - GPE - Pacote de acumulado do RH no Portal de Cliente](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)**  
- Certifique-se que a tag Security=0 foi adicionada na seção HTTP e no JOB do WS do seu appserver.ini, conforme exemplo abaixo:  
  
[HTTP]  
ENABLE=1  
PORT=85  
PATH=C:\PROTHEUS\_12\MICROSIGA\Protheus\_Data\_ctree\_2310\web  
ENVIRONMENT=2310\_PERF\_EEUUFFFFF  
**SECURITY=0**[localhost:85/ws33perfeeuufffff]  
ENABLE=1  
PATH=C:\PROTHEUS\_12\Microsiga\Protheus\_Data\_ctree\_2310\web\WS\_33\_PERF\_EEUUFFFFF  
ENVIRONMENT=2310\_PERF\_EEUUFFFFF  
INSTANCENAME=WS\_33\_PERF\_EEUUFFFFF  
RESPONSEJOB=JOB\_WS\_33\_PERF\_EEUUFFFFF\_01010100001  
DEFAULTPAGE=wsindex.apw  
  
[JOB\_WS\_33\_PERF\_EEUUFFFFF\_01010100001]  
TYPE=WEBEX  
ENVIRONMENT=2310\_PERF\_EEUUFFFFF  
INSTANCES=1,2  
SIGAWEB=WS  
INSTANCENAME=WS\_33\_PERF\_EEUUFFFFF  
ONSTART=\_\_WSSTART  
ONCONNECT=\_\_WSCONNECT  
PREPAREIN=01,010100001  
**SECURITY=0  
  
Verifique que, a *tag PrepareIn* está com conteúdo GRUPO DE EMPRESA,FILIAL**  
Para o Portal do Candidato, que é desenvolvido em *SOAP*, **os *Web Services* precisam ser carregadas em todas as filiais**, ou seja, para preparar o ambiente, o *PrepareIn* é **obrigatório** que esteja com essa configuração.  
  
Se o *PrepareIn* estiver *ALL* ou somente com o código do Grupo de Empresa, **os menus não serão demonstrados.**  
  
IMPORTANTE   
**SECURITY=0** conforme sugestões acima são aplicadas da versão 2310 pra baixo.   
Para versão 2410 em diante é obrigatório o uso do **SECURITY=1.**Deve ser configurado conforme acima mas com **SECURITY=1.  
  
Para versão 2410** em diante é obrigatório aplicar a documentação abaixo:  
[Configuração portais GCH com autenticação **SECURITY=1**](https://tdn.totvs.com/pages/releaseview.action?pageId=563435668)

**Saiba Mais**[Artigos Portal Candidato](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048093-Portal-do-Candidato)  
[Artigos Recrutamento e Seleção](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960907-Recrutamento-e-Sele%C3%A7%C3%A3o-de-Pessoas-SIGARSP-)  
[Informações adicionais sobre a Tag Security](https://tdn.totvs.com/pages/viewpage.action?pageId=185747842)
