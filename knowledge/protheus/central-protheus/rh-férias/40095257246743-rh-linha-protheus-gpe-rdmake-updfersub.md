---
article_id: 40095257246743
category: RH - Férias
content_hash: dafd18ca9794f1377cbd58e4d94a35425b183d5a562a595a29e3f3cc554ee42f
fetched_at: '2026-06-28T22:43:59.175479+00:00'
product: protheus
section_id: 360001597291
source: central-protheus
title: RH - Linha Protheus - GPE - Rdmake UPDFERSUB
type: support-article
updated_at: '2026-04-29T18:15:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40095257246743-RH-Linha-Protheus-GPE-Rdmake-UPDFERSUB
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40095257238807) Tempo aproximado para leitura: **00:01:30 min**  
  
**Dúvida**  
Para que serve o rdmake UPDFERSUB?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**  
Implementada a criação do rdmake **UPDFERSUB** para efetuar a gravação das verbas de substituição no campo **"Vb.Subs.Fer" (RR\_FERSUB, RGB\_FERSUB, RC\_FERSUB, RD\_FERSUB)** nas verbas de férias, que tem configuração de verbas substitutas nos campos **"Vb Fer Mes"(RV\_FERXML) e "Vb Fer Mes A"(RV\_FERAXML)**.

Essa rotina deve ser executada somente para casos que foram **calculada as férias sem a atualização** referente a Nota Técnica S-1.3 nº 04/2025 do eSocial, deixando de gravar o campo "Vb.Subs.Fer" (RR\_FERSUB) e consequentemente os demais envolvidos, e que não possam ser recalculadas.

Para executar o rdmake **UPDFERSUB** siga os passos abaixo:

1. Compile o rdmake **UPDFERSUB** no ambiente. O rdmake está disponível no pacote do expedição continua do RH a partir de 13/02/2026 (pasta rdmake).  
🔸12.1.2310:<https://suporte.totvs.com/portal/p/10098/download?e=1123885>(**SOMENTE COM GARANTIA ESTENDIDA**)  
🔸12.1.2410:<https://suporte.totvs.com/portal/p/10098/download?e=1170810>  
🔸12.1.2510:<https://suporte.totvs.com/portal/p/10098/download?e=1221795>

2. Inclua a rotina no menu do módulo SIGAGPE: [RH - Linha Protheus - GPE - Como incluir a rotina UPDFERSUB no menu](https://centraldeatendimento.totvs.com/hc/pt-br/articles/40101037691287-RH-Linha-Protheus-GPE-Como-incluir-a-rotina-UPDFERSUB-no-menu)

3. Ao abrir a rotina/rdmake **UPDFERSUB**, será exibido a tela abaixo:

![](https://tdn.totvs.com/download/attachments/1014630057/image-2026-2-3_16-18-13.png?version=1&modificationDate=1770146293637&api=v2)

O botão "**Abrir**" irá abrir a documentação técnica no navegador do usuário.

O botão "**Param**" irá abrir a tela para preenchimento do filtro de processamento da rotina.

* Na tela para preenchimento de parâmetros é obrigatório que seja preenchido o **filtro de período**, **os demais não são obrigatórios** e caso não esteja preenchido será apresenta apenas um alerta informando se deseja prosseguir.
* Caso não seja realizado o preenchimento dos filtros e efetue direto o processamento, será encerrada a rotina com informativo de preenchimento do período obrigatório.
* No filtro caso precise processar mais de uma Filial, Matricula ou Processo, basta deixar vazio o filtro. **Não é possivel realizar filtros por range.**

![](https://tdn.totvs.com/download/attachments/1014630057/image-2026-2-3_16-19-53.png?version=1&modificationDate=1770146393980&api=v2)

O botão "**Ok**" irá iniciar o processamento após a confirmação do usuário em algumas mensagens de aviso.  
Ao executar, será emitido alguns avisos perguntando se foi realizado o backup da base de dados e se deseja continuar, **é importante que tenha feito o backup da base.**

![](https://tdn.totvs.com/download/attachments/1014630057/image-2026-2-3_16-21-41.png?version=1&modificationDate=1770146501597&api=v2)  
  
Após confirmação, será iniciado o processo do ajuste das verbas e poderá ser acompanhado o status pela barra de progresso:

![](https://tdn.totvs.com/download/attachments/1014630057/image-2026-2-3_16-27-58.png?version=1&modificationDate=1770146878713&api=v2)

Ao finalizar, será aberto o log de ocorrência para validação dos registros processados:

![](https://tdn.totvs.com/download/attachments/1014630057/image-2026-2-3_16-30-5.png?version=1&modificationDate=1770147005597&api=v2)

Caso não tenha verbas com o campo "**Vb.Subs.Fer**" **(RR\_FERSUB)**vazio, não será processado nenhum registro, pois entendemos que já esta correta as informações nos campos:

![](https://tdn.totvs.com/download/attachments/1014630057/image-2026-2-3_16-32-56.png?version=1&modificationDate=1770147176923&api=v2)

**Observações:**

* O RDMake irá processar registros que estão com os campos **Vb.Subs.Fer (RR\_FERSUB, RGB\_FERSUB, RC\_FERSUB, RD\_FERSUB)** vazios.
* Se for identificado verbas que não tem configuração de verbas substitutas nos campos **RV\_FERXML** ou **RV\_FERAXML**, será informado no log de ocorrência, nesse caso deve ser ajustado e processar novamente.
* Se as verbas estiverem configuradas com as substitutas, será apresentado no log de ocorrência qual é a verba substituta gravada.

**Saiba Mais**  
[Substituir verbas de Férias](https://tdn.totvs.com/pages/viewpage.action?pageId=1014630057#body-body2)  
[RH - Férias](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597291-RH-F%C3%A9rias)
