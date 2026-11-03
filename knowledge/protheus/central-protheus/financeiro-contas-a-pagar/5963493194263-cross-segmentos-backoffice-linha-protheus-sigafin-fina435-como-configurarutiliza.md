---
article_id: 5963493194263
category: Financeiro - Contas a Pagar
content_hash: 92cf0c0e498ece5bc621d61fdef00bee4b1e7392a4b0e727960e18bc8c39bb9e
fetched_at: '2026-06-28T22:38:09.697731+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA435 - Como configurar/utilizar
  a rotina Baixa Retorno Automático
type: support-article
updated_at: '2022-05-10T12:43:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5963493194263-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA435-Como-configurar-utilizar-a-rotina-Baixa-Retorno-Autom%C3%A1tico
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00****Dúvida**Como configurar/utilizar a rotina FINA435 - Baixa Retorno Automático via Schedule

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - FINA435 - Todas as versões  
  
**Solução**Para utilização da rotina de **Baixa Retorno Automático via Schedule FINA435**, siga os passos abaixo:

1° Na rotina **FINA130** além da configuração padrão dos parâmetros de banco na aba "**Cadastros**",  ajuste a aba "**Retorno Automático**" para o tipo de carteira "**Recebimento**","**Pagamento**" ou "**Ambos**"

![FINA435.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5963288231447/FINA435.png)

**Ret.Automat?** Carteira que será realizado o processo de retorno.  
**Dir.Imp.Pag.** Diretorio de importação dos arquivos  
**Dir.Bkp.Pag.** Diretorio que após a importação, será gravados os arquivos de backup  
**Arq.Cfg.Pag.** Arquivo de retorno ( Deve estar salvo dentro da pasta system )   
**CNAB Pagto.?** Modelo de Pagamento Modelo 1, Modelo 2  
**Proc Filial?** Filial de processamento dos arquivos

2° Adicione a configuração do Schedule para o processo de retorno automático via **SIGACFG  - Configurador** em **Ambientes >> Schedule >> Agendamento >> Cadastros**

![RETORNO_AUTOMATICO.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5963419707415/RETORNO_AUTOMATICO.png)

**Saiba mais:**  
[Schedule - Como agendar a execução de rotinas](https://tdn.totvs.com/pages/viewpage.action?pageId=271167961)

[Parâmetros de Bancos - FINA130](https://tdn.totvs.com.br/pages/releaseview.action?pageId=624116777)

[How to | SIGAFIN | CNAB via Schedule](https://www.youtube.com/watch?v=LXAVSKV7lxM)
