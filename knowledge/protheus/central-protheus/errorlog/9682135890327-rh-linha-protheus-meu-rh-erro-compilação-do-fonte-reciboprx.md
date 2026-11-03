---
article_id: 9682135890327
category: ERRORLOG
content_hash: 871c19ac5719b845dd9b88b619474b103c72216e9f57e17afb77309cb76a8a50
fetched_at: '2026-06-28T22:44:39.464242+00:00'
product: protheus
section_id: 10299583475863
source: central-protheus
title: RH - Linha Protheus - MEU RH - Erro compilação do fonte recibo.prx
type: support-article
updated_at: '2026-06-18T19:55:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9682135890327-RH-Linha-Protheus-MEU-RH-Erro-compila%C3%A7%C3%A3o-do-fonte-recibo-prx
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19282435320087) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**RH - Linha Protheus - MEU RH - Erro compilação do fonte ***recibo.prx***  
  
**Ambiente**TOTVS RH (Linha Protheus) - Meu RH – todas as versões  
  
**Solução**Ao compilar o **RDMAKE recibo.prx**, via VS Code, temos o seguinte erro:  
**"constant STR0237 compile Ln 5220, Col1"**  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9681605719063)  
  
Este erro ocorre pois, o **RDMAKE** em questão, utiliza o *include* do **gper1030.ch** e, não mais, o **recibo.ch**  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9681569095831)  
  
Por isso, ao compilar o ***RDMAKE recibo.prx***, certifique-se que o *include* correto esteja referenciado.  
  
Outra possibilidade, é realizar o download na [Central de *Downloads* da TOTVS](https://suporte.totvs.com/portal/p/10098/download#company/).  
Segue demonstração de como localizar os arquivos de *RDMAKE*   
Na busca procurar: **RDMAKES\_RECURSOS\_HUMANOS**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19282435325719)  
  
Outra opção: Estes arquivos podem ser encontrados também ao baixar o **Pacote RH Expedição Contínua:***Link* para baixar o RH Expedição Contínua  
[Pacote Acumulado RH](https://suporte.totvs.com/portal/p/10098/download#000006/all/all/search/RH_EXPEDICAO_CONTINUA)  
  
Também poderá acessar a Central e realizar a seguinte busca:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19282441037591)  
  
**Observação:** Uma cópia desses arquivos **RECIBO**está anexada no final deste artigo, se necessário, basta clicar no link disponível para realizar o download, porém é sempre importante verificar se na Central de Downloads não há uma versão mais recente.  
  
**Saiba Mais:**  
[**CLIQUE AQUI** para acessar mais artigos e FAQs sobre o MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)  
[**CLIQUE AQUI** para acessar a documentação de referências sobre o MEU RH](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)  
  
**Seguem os arquivos RECIBO.CH e RECIBO.PRW:**
