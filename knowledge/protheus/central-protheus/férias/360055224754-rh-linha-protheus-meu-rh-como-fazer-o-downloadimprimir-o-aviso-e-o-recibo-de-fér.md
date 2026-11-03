---
article_id: 360055224754
category: FÉRIAS
content_hash: 9eaf508e7b4a49d118375b90e0d9b2d2f339fb8c9fcfbc7a055c408684376ccf
fetched_at: '2026-06-28T22:44:34.591790+00:00'
product: protheus
section_id: 10299705719575
source: central-protheus
title: RH - Linha Protheus - MEU RH - Como fazer o download/imprimir o Aviso e o Recibo
  de Férias no MEU RH
type: support-article
updated_at: '2025-12-16T11:47:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360055224754-RH-Linha-Protheus-MEU-RH-Como-fazer-o-download-imprimir-o-Aviso-e-o-Recibo-de-F%C3%A9rias-no-MEU-RH
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30646825676055) Tempo aproximado para leitura: 00:03:00 min**  
  
**Dúvida**  
Como fazer o download/imprimir o Aviso e o Recibo de Férias no MEU RH?  
  
**Ambiente**  
TOTVS RH (Linha Protheus) - Meu RH – todas as versões  
  
**Solução**  
Para fazer o *download*/imprimir o  Aviso e o Recibo de Férias através do MEU RH é necessário:  
  
Ter o Protheus atualizado, conforme [**Roadmap do MEU RH - Protheus**](https://tdn.totvs.com/display/NPR/3.1.1+Funcionalidades+disponibilizadas)  
  
**O** ***RDMake RHNPMEURH***, foi **descontinuado** e criado outros dois, um para cada documento.  
Documentação sobre a descontinuação do *RHNPMEURH*:  
<https://tdn.totvs.com/display/NPR/Itens+Descontinuados>   
  
**Aviso de Férias: MRHAVIFE.PRW**  
**Recibo de Férias: MRHRECFE.PRW**  
Os dois estão disponíveis no pacote de Expedição Contínua do GPE, pasta *RDMakes*.  
<https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/RH_EXPEDICAO>   
  
Para saber como Compilar o RDMAKE no seu RPO acesse o artigo: [**Compilação de RDMakes**](https://tdn.totvs.com/pages/viewpage.action?pageId=73077498).  
  
Verifique no seu APPSERVER.INI onde está configurado o MEU RH se a tag *STARTPATH* está com o conteúdo SYSTEM entre duas barras invertidas, uma no começo e outra no final, conforme exemplo:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35986842212503)  
  
Verifique se o arquivo *printer* está gravado na pasta do APPSERVER onde está configurado o MEU RH, no artigo a seguir é demonstrado como realizar o download desse arquivo:  
[**Onde localizo o arquivo PRINTER?**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050119614)  
  
Quando você tem uma programação de Férias já aprovada basta acessar a rotina de Férias do MEU RH e aparecerá um botão de **Aviso de férias disponível** e ao pressioná-lo inicia o download do **Aviso de Férias** em formado '.PDF'.  
  
**![Aviso_de_F_rias.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360095609953)**  
  
Quando você tem uma Férias já calculada no SIGAGPE basta acessar a rotina de Férias do MEU RH, ao consultar o Recibo de Férias aparecerá um botão de ***download*** **do recibo de férias** e ao pressioná-lo inicia o download do **Recibo de Férias** em formado '.PDF'.  
  
**![Recibo_de_F_rias.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360093351714)**

**Observação:** Por se tratar de *RDMAKE* é possível customizar os relatórios, porém essas configuração é por conta em risco do operador do sistema em sua Empresa.  
  
**Saiba Mais**  
[CLIQUE AQUI para acessar mais artigos e FAQs sobre o MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)  
[CLIQUE AQUI para acessar a documentação de referências sobre o MEU RH](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)  
  
**Seguem os arquivos MRHAVIFE.PRW e MRHRECFE.PRW , juntamente com seus includes e os .tres**
