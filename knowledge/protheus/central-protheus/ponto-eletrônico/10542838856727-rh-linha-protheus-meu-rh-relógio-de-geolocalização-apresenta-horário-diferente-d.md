---
article_id: 10542838856727
category: PONTO ELETRÔNICO
content_hash: 07aa6efcd69d1eedd191340b6d56f8dd2070e09e388fe63bc6c96cd1bb476b7a
fetched_at: '2026-06-28T22:44:36.635279+00:00'
product: protheus
section_id: 10299685322391
source: central-protheus
title: RH - Linha Protheus - MEU RH - Relógio de Geolocalização apresenta horário
  diferente da hora atual
type: support-article
updated_at: '2026-06-16T18:56:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10542838856727-RH-Linha-Protheus-MEU-RH-Rel%C3%B3gio-de-Geolocaliza%C3%A7%C3%A3o-apresenta-hor%C3%A1rio-diferente-da-hora-atual
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30646274336663) Tempo aproximado para leitura: **00:02:00 min****Dúvida**Ao acessar a opção de **Relógio** no Meu RH, a **hora apresentada** no Relógio da Marcação é **diferente** da **hora** atual do **servidor**  
  
**Ambiente**TOTVS RH (Linha Protheus) - Meu RH – todas as versões  
  
**Solução**O **horário** desta funcionalidade é carregado de acordo com o **horário do servidor**, somado aos **arquivos complementares** do aplicativo, deste modo qualquer divergência entre os arquivos do Portal, pode causar este erro.  
  
**Para correção** deste tipo de ocorrência, necessário seguir com os seguintes procedimentos:  
**1. Limpeza** dos arquivos de ***cache*** do dispositivo que está acessando o Meu RH:  
[RH - Linha Protheus - MEU RH - Como limpar o Cache do MEU RH no APP ou Navegador](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058396533) **2. Parar** os serviços ***REST*** e ***HTTP***;  
 **3. Aplicar os Arquivos do Portal** mais recentes (mesmo que já tenha sido aplicado, necessário sobrepor os arquivos atuais):  
[RH - Linha Protheus - MEU RH - Onde baixo a versão mais recente e como atualizar os arquivos do Portal Meu RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043729034) **4. Reiniciar** os serviços do ***REST*** e ***HTTP***.  
 **Obs:** Caso seu ambiente esteja em nosso *cloud*, realize o procedimento da limpeza de *cache* de seus dispositivos (passo 1) e solicite à equipe *cloud,* para realizar o processo de sobreposição dos Arquivos do Portal. **Saiba Mais****[RH - Linha Protheus - MEU RH - Aprenda sobre o MEU RH e como fazer a implantação](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036164214)  
[CLIQUE AQUI para acessar mais artigos e FAQs sobre o MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)  
[CLIQUE AQUI para acessar a documentação de referência sobre o MEU RH](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)**
