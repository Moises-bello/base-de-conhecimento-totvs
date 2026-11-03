---
article_id: 360028853991
category: DEMONSTRATIVOS
content_hash: ba0ce903a95b674309ef09531924c6307f5654893c52323c70ac3d90b4db2a97
fetched_at: '2026-06-28T22:44:38.477000+00:00'
product: protheus
section_id: 10299629664279
source: central-protheus
title: RH - Linha Protheus - MEU RH - Como consultar e fazer download do Informe de
  Rendimento
type: support-article
updated_at: '2026-06-19T14:16:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028853991-RH-Linha-Protheus-MEU-RH-Como-consultar-e-fazer-download-do-Informe-de-Rendimento
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22226346181399) Tempo aproximado para leitura: 00:05:00 min**  
  
**Dúvida**  
Como consultar e fazer download do Informe de Rendimento?  
  
**Ambiente**  
TOTVS RH (Linha Protheus) - MEU RH - Todas às versões  
  
**Solução**  
Para consultar o **Informe de Rendimento** acesse o MEU RH no menu **Pagamento** - **Informe de Rendimentos** e clique no botão **Download** ao lado direito do ano que deseja consultar para baixar o arquivo em formato **.PDF** conforme demonstrado abaixo:  
![MEURH_Informe.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/8744796727831)  
  
**Dúvidas Frequentes:**  
**O que faço quando não vejo no Menu a opção 'Informe de Rendimentos'?**  
Acesse o artigo abaixo e veja como liberar essa opção para o Usuário do Portal.  
[**Configuração de permissão de acesso as funcionalidades e menu do MEU RH**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033892693)  
  
**Como faço para liberar o acesso do Usuário ao Informe de Rendimento de um ano específico e a partir de qual momento ele vai ver essa informação?**  
Acesse o artigo abaixo e veja como configurar essas informações.  
[**Como habilitar a consulta do Informe de Rendimento de um ano específico**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050192114)  
  
**O que faço quando pressiono o botão para imprimir o Informe de Rendimento e é apresentado a mensagem '*****Internal Error*****'?**  
Isso normalmente ocorre porque não foi compilado o *RDMAKE* do Informe de Rendimento no RPO do MEU RH.  
  
**O que faço quando é gerado o arquivo '.PDF' porém ele não abre ou o seu conteúdo é uma mensagem de erro?**  
**1º** Verifique se consegue imprimir o Informe de Rendimento desse Trabalhador no Gestão de Pessoal, módulo '07 - SIGAGPE';  
  
**2º** Verifique no seu APPSERVER.INI onde está configurado o MEU RH se tag STARTPATH está com o conteúdo SYSTEM entre duas barras invertidas, uma no começo e outra no final, conforme exemplo:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360077627053)  
  
**3º** Verifique se o arquivo *printer* está gravado na pasta do *APPSERVER* onde está configurado o MEU RH (Se usar balance ou broker para o meu rh, deve ser colado o printer.exe em todas pastas appserver de cada serviço), no artigo abaixo é demonstrado como realizar o Download desse arquivo;  
[**Onde localizo o arquivo PRINTER**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050119614)  
  
**4º** Verifique se o seu RDMAKE IMPIRPF.PRX do Informe de Rendimento está atualizado e compilado:  
  
**Para saber como achar esse RDMAKE acesse o artigo abaixo:**  
[**Onde localizar o Include IMPIRPF.CH**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050106234)  
  
**Para saber como Compilar o RDMAKE no seu RPO acesse o artigo abaixo:**  
[**Compilação de RDMakes**](https://tdn.totvs.com/pages/viewpage.action?pageId=73077498)  
  
**Caso o erro persista**, abra um Ticket ao Suporte, porém para uma análise assertiva é importante que descreva corretamente seu cenário e encaminhe evidências, segue abaixo informações que auxiliam na análise:

1. [Arquivo com a data de suas rotinas do RPO do MEU RH](https://tdn.totvs.com/x/nYPxF);
2. [Data dos arquivos do portal MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059194334);
3. Arquivo APPSERVER.INI;
4. [Arquivo Console.log do momento da geração do arquivo '.PDF'](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035487834/);
5. Print do local de gravação do arquivo PRINTER;
6. Cópia do Informe de Rendimento desse Trabalhador gerado no Gestão de Pessoal, módulo '07 - SIGAPE'.
7. console.log de todos os serviços appserver

**ATENÇÃO:** Certifique-se sempre de estar com seu ambiente atualizado, pois são disponibilizados periodicamente atualizações com melhorias e correções no MEU RH.  
[**RH - Linha Protheus - MEU RH - Onde baixo a versão mais recente e como atualizar os arquivos do Portal Meu RH**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043729034)  
[**RH - Linha Protheus - MEU RH - Pacote de acumulado do RH no Portal de Cliente**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500007189282)  
  
**Saiba Mais**  
Acesse o link a seguir para verificar mais documentos sobre a DIRF 2020:  
[**Central de Atendimento TOTVS Protheus RH – DIRF**](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000030307-RH-DIRF)  
[**RH - Linha Protheus - GPE - RDMAKE e Includes para informe de rendimento DIRF**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360023194891)
