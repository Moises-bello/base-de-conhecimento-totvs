---
article_id: 20199004434839
category: Financeiro - Consultas / Relatórios
content_hash: 6fb54df63682ac06e2e9f465253403c7011a39253d9b7c2f4a5ffcfb27b06f66
fetched_at: '2026-06-28T22:37:58.484498+00:00'
product: protheus
section_id: 1500001539561
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINR137 - Apresentar
  a posição dos títulos a receber por vendedor a partir de uma liquidação e baixa
  parcial
type: support-article
updated_at: '2023-12-29T18:48:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20199004434839-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINR137-Apresentar-a-posi%C3%A7%C3%A3o-dos-t%C3%ADtulos-a-receber-por-vendedor-a-partir-de-uma-liquida%C3%A7%C3%A3o-e-baixa-parcial
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20199004415511) Tempo aproximado para leitura: **00:05:00 min****Dúvida**Como apresentar a posição dos títulos a receber por vendedor a partir de uma liquidação e baixa parcial?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Solução**Para solucionar essa dúvida, realize os seguintes passos:

1. Inseri um título a receber, na **Aba Venda** selecione um vendedor cadastrado.  
2. Na rotina **Liquidação a receber** (**FINA460**) preencha os dados solicitados e o valor da parcela no campo **Val. Parcela** e **Confirmar.**  
3. Na rotina **Baixa a Receber** **(FINA070**) realize a baixa parcial do valor e **Salvar.**

4. Emitir o relatório **Posição dos títulos a Receber por Vendedor (FINR137)** com os parâmetros preenchidos

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20199004418839)

**Importante**  
Verifique na rotina de **Liquidação (FINA460)** e os parâmetros de envolve o cadastro de vendedor e comissão.  
![](https://totvssuporte.zendesk.com/attachments/token/TY6KLEBVwQrRMs2ZV58vWD4kh/?name=image.png)

**Saiba Mais:  
[FINA460 - Liquidação a receber - P12](https://tdn.totvs.com.br/pages/releaseview.action?pageId=545236275)  
[MV\_COMILIQ - Define o cálculo da comissão na liquidação de títulos a receber](https://tdn.totvs.com.br/pages/releaseview.action?pageId=126714060)**
