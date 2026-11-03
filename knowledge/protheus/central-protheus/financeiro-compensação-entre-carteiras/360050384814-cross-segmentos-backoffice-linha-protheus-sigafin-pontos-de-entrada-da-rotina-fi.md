---
article_id: 360050384814
category: Financeiro - Compensação entre Carteiras
content_hash: f7a5ae4c961c818340be5e5859c13a2ee4097803c4b7074de31ed3b38670fb2a
fetched_at: '2026-06-28T22:37:27.014654+00:00'
product: protheus
section_id: 35058659965079
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Pontos de entrada da
  rotina FINA450
type: support-article
updated_at: '2025-11-26T20:41:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050384814-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Pontos-de-entrada-da-rotina-FINA450
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25937480496919)** Tempo aproximado para leitura: **00:10:00 min**  
  
**Dúvida**  
Quais são os pontos de entrada da rotina FINA450?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas versões  
  
**Solução**  
Seguem abaixo uma relação de pontos de entrada da rotina **FINA450**

**F450BROW:** Ponto de entrada que permite manipular o conteúdo dos campos, e quais campos irão compor o *browser* na rotina de compensação entre carteiras.   
Documentação: <https://tdn.totvs.com/pages/releaseview.action?pageId=528453462>  
  
**lFA450BU:** Criação de botão.  
Documentação: <https://tdn.totvs.com/pages/releaseview.action?pageId=6071571>  
  
**F450ValCon:**Permite a validação após a seleção de títulos.   
Documentação: <https://tdn.totvs.com/pages/releaseview.action?pageId=6071685>  
  
**F450SE5:**Executado após a compensação de todos os títulos selecionados na tela.   
Documentação:[https://tdn.totvs.com/pages/releaseview.action?pageId=6071066](https://tdn.totvs.com/pages/viewpage.action?pageId=645893891)  
  
  
**F450FIL:**Realiza a customização do filtro da *IndRegua* em ambientes *TopConect.*  
 Documentação: <https://tdn.totvs.com/pages/releaseview.action?pageId=645892013>  
  
**F450OWN1:** Monta a expressão de filtro adicional.   
Documentação: <https://tdn.totvs.com/display/PROT/F450OWN1+-+Filtro+da+tabela+SE2>  
  
  
**F450ORDEM:**Permite a alteração da ordem dos títulos apresentados para seleção, no momento de realizar a compensação entre carteiras. Deve retornar a nova chave para a *Indregua.* O retorno deve ser sempre do tipo **Caracter**.  
Documentação:<https://tdn.totvs.com/pages/releaseview.action?pageId=6071392>  
  
**F450GRAVA:** O PE permite manipular os dados temporários da tabela "**TRB"**.   
Documentação:<https://tdn.totvs.com/pages/releaseview.action?pageId=653141268>  
  
**F450Conf:**O PE tem como finalidade validar a marcação do título para compensação. Documentação: <https://tdn.totvs.com/pages/releaseview.action?pageId=6071061>  
  
**F450valid:** Permite a validação de informações da tela de compensação.   
Documentação: <https://tdn.totvs.com/pages/releaseview.action?pageId=6071689>  
  
**F450CAES:**Utilizado para validar ou executar algum procedimento após o usuário confirmar o Cancelamento/Estorno da compensação entre carteiras.   
Documentação: <https://tdn.totvs.com/display/public/mp/F450CAES+-+Valida+procedimento+--+11800>  
  
**F450SE1C:**Grava dados complementares.   
Documentação: <https://tdn.totvs.com/display/public/mp/F450SE1C+-+Grava+dados+complementares+--+11804>  
  
**F450SE2C:**Gava dados complementares no arquivo **SE2**.  
Documentação: <https://tdn.totvs.com/display/public/mp/F450SE2C+-+Grava+dados+complementares+--+11805>

**F450FCA:**Seleção dos registros pesquisados no cancelamento de compensação entre carteiras. Documentação: <https://tdn.totvs.com/pages/viewpage.action?pageId=645890948>  
  
**FA450BUT:**Inclusão de opções na barra de ferramentas.   
Documentação:<https://tdn.totvs.com/pages/releaseview.action?pageId=6071229>  
  
**FILEMOT:**PE utilizado para leitura do arquivo de texto de motivos de baixa de **Contas a Receber**. Documentação:<https://tdn.totvs.com/display/public/PROT/DT_FILEMOT_Motivo_Baixas>

**Saiba Mais**  
<https://tdn.totvs.com/display/public/PROT/FIN0106_CPAG_FINA450_PONTOS+DE+ENTRADA>
