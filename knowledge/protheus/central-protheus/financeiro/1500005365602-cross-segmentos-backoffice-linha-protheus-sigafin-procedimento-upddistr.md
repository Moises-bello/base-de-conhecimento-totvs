---
article_id: 1500005365602
category: Financeiro
content_hash: 4ac6e9aa71c0aad6a6a226173bf66762e048268541469ce544c47b27ff8178cd
fetched_at: '2026-06-28T22:38:03.423848+00:00'
product: protheus
section_id: 1500001550522
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Procedimento UPDDISTR
type: support-article
updated_at: '2022-06-15T00:52:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500005365602-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Procedimento-UPDDISTR
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:00 min**  
**Dúvida**Qual procedimento para executar  o compatibilizador  UPDDISTR para as atualizações que demanda esse processo?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões

**Solução**

**Procedimento para executar o UPDDISTR.**

**1. Limpeza das Pastas**  
- Exclua os arquivos **\*.DBF**e**\*.DTC** da pasta SYSTEMLOAD  
- Exclua os arquivos **\*.IDX** da pasta SYSTEMLOAD  
- Exclua os arquivos **\*.LOG** da pasta SYSTEM  
- Exclua os arquivos **TOTVSP\*.\*** da pasta SYSTEM  
- Exclua os arquivos **\*.TSK** e .**LOG** da pasta APPSERVER  
  
  
**2. Executando o compatibilizador de Upgrade de Release**  
- Abra o Smartclient, e no Programa Inicial, digite: **UPDDISTR***\* Maiores detalhes sobre a funcionalidade do UPDDISTR podem ser encontrados neste link: [Atualizador de dicionário e base de dados - UPDDISTR](https://tdn.totvs.com/pages/viewpage.action?pageId=181965468)*  
![](https://tdn.totvs.com/download/attachments/286020348/2017-08-07_15-31-45.png?version=1&modificationDate=1502287639000&api=v2)

Selecione a(s) empresa(s) que deseja fazer o Upgrade de Release e clique em **OK**.  
![](https://tdn.totvs.com/download/attachments/286020348/2017-08-07_15-33-01.png?version=1&modificationDate=1502287639000&api=v2)  
  
- Após selecionar a(s) empresa(s), será exibida uma tela com as recomendações de **backup** e **espaço livre**. Clique em **Avançar**.  
![](https://tdn.totvs.com/download/attachments/286020348/2017-09-22_028.png?version=1&modificationDate=1506089085000&api=v2)  
  
- Em seguida, serão exibidas as telas do **Termo de Aceite** que é **necessário** para o prosseguimento do processo. Leia atentamente, **marque** os **aceites**, e vá **avançando**.  
![](https://tdn.totvs.com/download/attachments/286020348/2017-09-22_029.png?version=1&modificationDate=1506089085000&api=v2)  
![](https://tdn.totvs.com/download/attachments/286020348/2017-09-22_030.png?version=1&modificationDate=1506089086000&api=v2)  
![](https://tdn.totvs.com/download/attachments/286020348/2017-09-22_031.png?version=1&modificationDate=1506089086000&api=v2)  
![](https://tdn.totvs.com/download/attachments/286020348/2017-09-22_032.png?version=1&modificationDate=1506089087000&api=v2)  
![](https://tdn.totvs.com/download/attachments/286020348/2017-09-22_033.png?version=1&modificationDate=1506089087000&api=v2)  
  
- Na tela seguinte, digite a senha do **Admin** e clique em **Avançar**.  
![](https://tdn.totvs.com/download/attachments/286020348/2017-08-07_15-34-08.png?version=1&modificationDate=1502287639000&api=v2)  
  
- Em seguida, a opção padrão para o **Diretório de Dados** e a pasta **\DATA\**. Clique em **Avançar**.  
![](https://tdn.totvs.com/download/attachments/286020348/2017-08-07_15-34-44.png?version=1&modificationDate=1502287639000&api=v2)  
  
- Na tela Configuração, é recomendável deixar marcadas apenas as opções obrigatórias e a opção **Corrigir erros automaticamente**. Clique em **Avançar** e depois em **Avançar** novamente.  
![](https://tdn.totvs.com/download/attachments/286020348/2017-08-07_15-35-56.png?version=1&modificationDate=1502287639000&api=v2)  
  
- O Upgrade será iniciado.  
- Caso o Upgrade possua erros, será exibida uma janela com os logs dos erros, que devem ser corrigidos na base antes de continuar. Segue abaixo link com as correções de erros mais comuns em Migrações/Upgrades:  
[Erros críticos mais comuns em migrações](http://tdn.totvs.com/pages/viewpage.action?pageId=271414000)  
- Caso o erro não esteja listado, é necessário abrir um ticket para o Suporte Framework através do Portal do Cliente.  
- Ao final do Upgrade, será exibida uma janela com a informação "O processo de atualização foi finalizado com sucesso."  
![](https://tdn.totvs.com/download/attachments/286020348/2017-08-08_15-42-24.png?version=1&modificationDate=1502287639000&api=v2)  
  
- Para confirmar, acesse o Configurador, tecle Shift+F6, e confira a "**Release do RPO**"  
![](https://tdn.totvs.com/download/attachments/286020348/2017-08-08_15-43-43.png?version=1&modificationDate=1502287639000&api=v2)  
  
Informações adicionais:  
[Upgrade de Release do Protheus 12](https://tdn.totvs.com/pages/releaseview.action?pageId=286020348)
