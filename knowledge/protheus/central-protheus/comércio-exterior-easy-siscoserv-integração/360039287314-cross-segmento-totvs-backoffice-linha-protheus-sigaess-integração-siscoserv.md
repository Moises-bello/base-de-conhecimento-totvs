---
article_id: 360039287314
category: Comércio Exterior - Easy Siscoserv - Integração
content_hash: ba8e95e1f78ee6259a05634bb8fa525e90a0092be7ed5f00623e5c0a06429398
fetched_at: '2026-06-28T22:39:38.289332+00:00'
product: protheus
section_id: 1500001549462
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAESS - Integração Siscoserv
type: support-article
updated_at: '2022-04-25T19:28:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360039287314-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAESS-Integra%C3%A7%C3%A3o-Siscoserv
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:04:00 min  
  
Dúvida**Como configurar a integração com o Siscoserv através do arquivo 'tr-sw-web-solution-siscoserv.jar'?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – Easy Siscoserv – A partir da versão 12.1.17  
  
**Solução**Execute as verificações:

1. Cancele o lote gerado.
2. MV\_AVG0222, deve estar com o conteúdo em branco.
3. MV\_AVG0221, deve estar com o conteúdo INI.
4. As permissões para gravação na pasta temp\siscoserv, devem estar liberadas para realizar a gravação e leitura.
5. O parâmetro MV\_ESS0027 = 10 ou superior.
6. Na rotina Int. Siscoserv, na ação configurações, informe o caminho do JAVA.EXE caso tenha instalado na máquina mais de um java.  
   ![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360051712074/mceclip0.png)  
   É necessário ter o arquivo '**tr-sw-web-solution-siscoserv.jar'** na pasta smartclient local, este encontra-se disponível no pacote acumulado: [Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Pacote Acumulado Comex](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047332793)
7. Rotina **ESSCI103** atualizada: 12.1.25:<https://suporte.totvs.com/portal/p/10098/download?e=766082> ; 12.1.23:<https://suporte.totvs.com/portal/p/10098/download?e=766081> ; 12.1.17:<https://suporte.totvs.com/portal/p/10098/download?e=766080> ;

**Saiba mais**  
[Dúvidas SISCOSERV Manual 10](http://tdn.totvs.com/pages/releaseview.action;jsessionid=E9511790E10D7A101D8D46732988A37D?pageId=240295216)
