---
article_id: 8220304109591
category: Portal de Gestão de Capital Humano
content_hash: 059f553bd1df121c86c960b7d476baedf3a41f3890c382514487b57e54b09056
fetched_at: '2026-06-28T22:42:59.085812+00:00'
product: protheus
section_id: 206960887
source: central-protheus
title: RH - Linha Protheus - PORTAL GCH - Ao consultar o banco de horas no portal
  é apresentado o erro "Rdmake EXTRABH não está compilado"
type: support-article
updated_at: '2022-08-17T12:01:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8220304109591-RH-Linha-Protheus-PORTAL-GCH-Ao-consultar-o-banco-de-horas-no-portal-%C3%A9-apresentado-o-erro-Rdmake-EXTRABH-n%C3%A3o-est%C3%A1-compilado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**Ao consultar o banco de horas no portal é apresentado o erro "Rdmake EXTRABH não está compilado"  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Portal Gestão do Capital Humano – Todas as versões  
  
**Solução**Ao consultar banco de horas no Portal GCH é apresentado o erro abaixo:  
  
"Rdmake EXTRABH não está compilado"  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8220749465623/mceclip1.png)  
  
Para a correção, é necessário compilar o **RDMAKE EXTRABH** no ambiente, o arquivo está disponível junto aos demais **RDMAKES** do RH disponíveis na Central de Downloads da TOTVS.   
Os arquivos podem ser baixados através do link abaixo específico para download dos **RDMAKES:**Link direto da Central de Downloads: **[RDMAKES RH](https://suporte.totvs.com/portal/p/10098/download#detail/947506)**Segue demonstração de como localizar os arquivos de **RDMAKE** na Central de Downloads da TOTVS. **![Download_IMPIRPF.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/5676292389271/Download_IMPIRPF.gif)**Na pasta baixada do RDMAKE é possível achar os arquivos na pasta **"Ponto Eletrônico"**. **![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8220561310103/mceclip0.png)****Outra opção:** Estes arquivos podem ser encontrados também ao baixar o Pacote **RH Expedição Contínua:**Link para baixar o RH Expedição Contínua: **[Pacote Acumulado RH](https://suporte.totvs.com/portal/p/10098/download#000006/all/all/search/RH_EXPEDICAO_CONTINUA)**  
![RH_Acumulado.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/5676527431191/RH_Acumulado.gif)  
  
**Observação:** Uma cópia desses arquivos **EXTRABH, includes (.CH) e os arquivos de tradução (.TRES)** está anexada no final deste artigo, se necessário, basta clicar no link disponível para realizar o download, porém é sempre importante verificar se na Central de Downloads não há uma versão mais recente.  
Colocar todos os arquivos dentro da mesma pasta (Include e Arquivos de Tradução junto com o RDMAKE EXTRABH) e compilar no ambiente.  
  
**Saiba Mais  
[RH - Linha Protheus - PORTAL GCH - Como Consultar Banco de Horas no Portal](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360055520534)**[CLIQUE AQUI para acessar mais artigos e FAQs sobre o Portal GCH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960887-RH-Portal-de-Gest%C3%A3o-de-Capital-Humano)
