---
article_id: 4428231795735
category: BI - Business Intelligence - Crystal-Reports
content_hash: a78d2c719fe87ced5126fc21cb517c754bb7e3aa5358435bf280a03f665e643f
fetched_at: '2026-06-28T22:40:29.036949+00:00'
product: protheus
section_id: 1500001548282
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice Linha Protheus - BI - Relatórios crystal
  não funcionam após migração '
type: support-article
updated_at: '2022-02-18T12:30:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4428231795735-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-BI-Relat%C3%B3rios-crystal-n%C3%A3o-funcionam-ap%C3%B3s-migra%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:05:00 min****Dúvida**Após migrar da release 12.1.25 ou anterior, meus relatórios *Crystal* não funcionam na release 12.1.27, como resolver?   
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – Crystal – até o release 12.1.27.  
  
**Solução**Favor migrar para o **TReports** uma nova ferramenta de relatórios que vem para substituir o ***Crystal Reports***, como já deve ter sido informado(a) o ***Crystal Reports*** foi descontinuado e não sofrerá mais manutenção de produto, sendo assim **a partir do release 12.1.33 não há suporte para o uso da ferramenta**.  
  
Para a configuração Crystal na **versão 12.1.27** seguir os passos abaixo:  
1 - No diretório do appserver, anexe os arquivos crysini.ini, crwini, protheus\_crystal\_integration.msi, protheus\_crystal\_integration\_without\_bde.msi, as dlls( apapi.dll, apapi64.dll e apconn.dll), SGCRYS32.exe;  
2 - Configure corretamente os caminhos CrwStartPath e CRWINSTALLPATH no appserver.ini e crysini.ini conforme exemplo abaixo:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4429282846359/mceclip0.png)  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4429322129303/mceclip4.png)  
  
3 - Configure no arquivo crwini.ini as chaves SX1 e SX2 com os valores "1";  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4429332372631/mceclip5.png)  
  
4- Crie o ODBC na versão de 32bits com a versão de driver "*SQL Server Native Client 11*", tanto para usuários quanto para sistema:  
![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4429354730263/mceclip6.png)​  
  
Tenha certeza de ter a mesma configuração de usuário ODBC criada nos relatórios Crystal:  
![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4429341691287/mceclip7.png)​  
  
5 - Verifique a chamada do seu programa **Callcrys** no menu Protheus;  
6 - Valide todos estes passos e após isso execute a instalação primeiro do arquivo **protheus\_crystal\_integration.msi**, possivelmente acusará um erro na conclusão, porém pode seguir com o processo. Após isto execute o **protheus\_crystal\_integration\_without\_bde.msi** , ambos no diretório do appserver.  
  
**Observação:** Como procedimento **exclusivo** para as releases acima da 25, é necessário executar o **CrysConfig** para criptografar os dados do banco de dados utilizados na geração dos relatórios do ***Crystal Reports***. Siga o procedimento abaixo:  
1 - Para executá-lo, basta chamar no campo **Programa inicial** do smartclient a função **Crysconfig**;  
  
![](https://totvssuporte.zendesk.com/attachments/token/7p3MJypRBDYN1oYIV2Clubnsk/?name=inline-2124921838.png)​  
2- Adicionar a seguir as informações de usuário/senha do Protheus e do Banco de dados:  
![](https://totvssuporte.zendesk.com/attachments/token/TKksHoY3RIlQGnOYTAqDAaM0r/?name=inline2064744608.png)​

Banco de dados:  
![](https://totvssuporte.zendesk.com/attachments/token/ApDvCwCab8QZjMbSP6fG2fjrs/?name=inline1883519378.png)​  
  
**Importante:** Caso tenha atualizado o fonte de dados ODBC do banco/Protheus, deve-se atualizar os mesmos dados no relatório do *Crystal* selecionando **Especialista em banco de dados** na aba **Banco de Dados** do relatório *Crystal*.  
**![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4429413198487/mceclip8.png)  
  
Saiba mais**[Descontinuação: Crystal Reports](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360061924433)  
[TOTVS TReports](https://tdn.totvs.com/display/framework/TOTVS+TReports#TOTVSTReports-02.INSTALA%C3%87%C3%83ODOTREPORTS)
