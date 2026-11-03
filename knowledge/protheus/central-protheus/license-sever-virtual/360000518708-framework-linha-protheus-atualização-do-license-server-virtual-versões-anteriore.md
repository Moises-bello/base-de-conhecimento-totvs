---
article_id: 360000518708
category: License Sever Virtual
content_hash: 4442069f24dd9efbd1f4270681eef67a1d9422d085b1497ac62db00bf036325b
fetched_at: '2026-06-28T22:42:20.010405+00:00'
product: protheus
section_id: 360000075428
source: central-protheus
title: Framework - Linha Protheus - Atualização do License Server Virtual versões
  anteriores 3.5.0
type: support-article
updated_at: '2024-05-09T11:19:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000518708-Framework-Linha-Protheus-Atualiza%C3%A7%C3%A3o-do-License-Server-Virtual-vers%C3%B5es-anteriores-3-5-0
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17888048890775) Tempo aproximado para leitura: **00:02:16 min  
  
Dúvida**Como atualizar o **License Server Virtual versões anteriores a 3.5.0**  
  
**Ambiente**  
Protheus – Servidor de Licenças - Todas as versões  
  
**Solução**Realize os seguintes passos:  
  
1. Baixe o instalador conforme sistema operacional utilizado através dos *links*:

**Windows** - <https://suporte.totvs.com/portal/p/10098/download?e=1137545>

**Linux** - <https://suporte.totvs.com/portal/p/10098/download?e=1137544>

2. Pare o serviço da atual instalação do **License Server**;  
  
3. Para desativar a instalação atual do **License Server** para utilização da nova, existem 2 opções:  
  
     3.1. Faça um *backup* da pasta atual, e então desinstale o **License Server**, pelo **Painel de Controle** do **S.O. -sistema operacional**ou pelo ***Uninstaller***da pasta **\TOTVS\TOTVSLicense2014\uninstall\**  
      3.2. Mantenha a pasta, e no respectivo serviço, troque o **Tipo de Inicialização** de **Automático** para **Manual** ou **Desativado**, para que esse serviço não volte a inicializar;  
  
4. Execute o **novo** instalador;  
  
5. Durante a instalação, utilize as **mesmas portas** que eram utilizadas na instalação anterior. Caso tenha dúvidas, consulte as portas no arquivo **appserver.ini** da instalação anterior;  
  
6. Ao término da instalação, quando abrir o *Wizard* de configuração, clique em **Cancelar**;  
  
7. Abra os serviços do **Windows** e pare o serviço do **TOTVS | License Server Virtual**;  
  
8. Na pasta onde foi instalado, acesse a pasta **\TOTVS\TOTVSLicenseVirtual\bin\appserver** e renomeie o arquivo **licenseserver.ini**;  
  
9. Copie o arquivo **licenseserver.ini** da instalação original, e cole nesta pasta;  
  
10. Acesse a pasta **\TOTVS\TOTVSLicenseVirtual\data\db\_sys** da sua instalação original;  
  
11. Se sua instalação original não possui um arquivo chamado **SYSTEM.DB** ou então não possui essa pasta, pule o passo seguinte;  
  
12. Mova o arquivo **SYSTEM.DB** da instalação original para a pasta **\TOTVS\TOTVSLicenseVirtual\data\db\_sys**, caso exista um arquivo **SYSTEM.DB** nessa pasta, apague o mesmo antes de executar a mudança;  
  
13. Reinicie o serviço do **TOTVS | License Server Virtual**;  
14. Abra o **Monitor de Licenças;**15. No primeiro acesso, as licenças ainda não vão aparecer. Clique no ícone de **atualização manual**  - ícone em forma de antena, aguarde sincronizar, e após a sincronização, clique no ícone de **atualizar a tela**. As licenças serão exibidas.
