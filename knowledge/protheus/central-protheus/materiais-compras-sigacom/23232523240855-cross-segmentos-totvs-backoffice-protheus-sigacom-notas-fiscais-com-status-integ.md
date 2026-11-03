---
article_id: 23232523240855
category: Materiais - Compras (SIGACOM)
content_hash: 7461236b42c04ce9923bc8eed1609842c229f00208d01355b47bc6280f5afc4c
fetched_at: '2026-06-28T22:41:21.932315+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Notas fiscais com Status
  Integração ERP Exportadas não aparecem no Monitor do Importador XML
type: support-article
updated_at: '2024-05-13T13:20:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23232523240855-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Notas-fiscais-com-Status-Integra%C3%A7%C3%A3o-ERP-Exportadas-n%C3%A3o-aparecem-no-Monitor-do-Importador-XML
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23232523227927) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**O que fazer quando as notas fiscais estão com Status no campo Integração ERP Exportadas no TOTVS Transmite mas não aparecem no Monitor do importador XML?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Compras/GCT - Protheus Release 12.1.2210.  
  
**Solução**Quando o status do campo Integração ERP está como exportada significa que essa nota foi enviada com sucesso para o Importador XML do Protheus, porém por algumas razões essa nota não está disponivel no monitor do Importador XML para geração da Pré-Nota/Documento de Entrada. Abaixo listaremos alguns desses motivos:

**Paramêtros do monitor:**

- Ao abrir o monitor do importador XML será apresentado alguns parâmetros responsáveis por realizar um filtro na tela principal, certifique-se as datas e os conteudos desses parâmetros foram inseridos corretamente (Exemplo, Campos datas (INICIO/FIM));

**Erro de Integração:**

- Quando é realizado a integração do TOTVS Transmite com Importador XML pode ocorrer algumas rejeições que impedem a importação, essas rejeições podem ocorrer por varios motivos como: Fornecedor não cadastrado (Erro COM007), Falta de Amarração Produto x Fornecedor (Erro COM012) entre outros. Disponibilizo a documentação com todos códigos de erros: [Erros (Códigos)](https://tdn.totvs.com/pages/releaseview.action?pageId=485869227)

Para identificar esses códigos de erros, você deve **acessar** o **monitor** do importador XML > Clicar em **Reprocessar** > **Localizar** a nota fiscal > **Identificar** o código de **erro** > **Tratar** o **erro** (Exemplo, cadastrar o fornecedor) > **Selecionar** **a nota** > Clicar em 'Ok'

![gif (2).gif](https://centraldeatendimento.totvs.com/hc/article_attachments/23233189540503)

**Caso a nota não esteja aparecendo no Reprocessar:**

**Falha no agendamento SCHEDCOMCOL:**

- Verique se o agendamento SCHEDCOMCOL está ativo no schedule, caso o agendamento não esteja sendo executado, realize a execução manualmente via menu do módulo compras: [Como executar as funções de carga SEM utilizar o Schedule](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360040549593-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Importador-XML-ou-Totvs-Colabora%C3%A7%C3%A3o-Como-executar-as-fun%C3%A7%C3%B5es-de-carga-SEM-utilizar-o-Schedule)

Após esse procedimento, valide se as notas serão listadas no monitor ou na opção Reprocessar.

**Persistindo:**

- Verifique se existe algum filtro na opção F10 do monitor, caso exista, remova e refaça os testes:

![recording-2024-01-09-10-52-37 (online-video-cutter.com) (1).gif](https://centraldeatendimento.totvs.com/hc/article_attachments/23233179067159)

- Valide se o paramêtro **MV\_IMPXML** está .T., caso esteja como .F. o XML não será lido pelo Importador XML devido o campo CKO\_CODEDI ter sido gravado com um conteudo diferente de 109,319,214 ou 273. Neste caso, é necessario ativar o parâmetro > Importar novamente o XML para que o CKO\_CODEDI seja gravado corretamente.

Mais detalhes em: [O que fazer quando o documento está com o CKO\_FLAG = "0"](https://centraldeatendimento.totvs.com/hc/pt-br/articles/22967620309399-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-O-que-fazer-quando-o-documento-est%C3%A1-com-o-CKO-FLAG-0)

***Saiba Mais:***

* [Importador XML - Guia de Referencia (SIGACOM)](https://tdn.totvs.com/pages/releaseview.action?pageId=485858148)
* [Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Importador XML - Os documentos não estão aparecendo na rotina do REPROCESSAR dentro monitor.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/20435997213591)
* [IX10 - Integração Importador XML x TOTVS Transmite](https://tdn.totvs.com/x/m1tyK)
* [Pontos de Entrada disponíveis nas funções](http://tdn.totvs.com/display/public/PROT/IX02+-+Pontos+de+Entrada)
* [Parâmetros Envolvidos](http://tdn.totvs.com/pages/releaseview.action?pageId=485869217)
* [Tabelas e rotinas](http://tdn.totvs.com/pages/releaseview.action?pageId=485869224)
* [Códigos de Erros](http://tdn.totvs.com/pages/releaseview.action?pageId=485869227)
* [Importador XML ou Totvs Colaboração: Como executar as funções de carga SEM utilizar o schedule](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360040549593-MP-SIGACOM-Importador-XML-ou-Totvs-Colabora%C3%A7%C3%A3o-Como-executar-as-fun%C3%A7%C3%B5es-de-carga-SEM-utilizar-o-schedule)
* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
* [TOTVS Transmite](https://tdn.totvs.com/pages/releaseview.action?pageId=678583195)
