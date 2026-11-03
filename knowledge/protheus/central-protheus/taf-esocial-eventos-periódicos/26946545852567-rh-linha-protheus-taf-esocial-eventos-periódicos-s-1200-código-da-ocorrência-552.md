---
article_id: 26946545852567
category: TAF - eSocial - Eventos Periódicos
content_hash: f0100463e60dd9735e3ccdc465354dd589f51d01a9774be2c7191d57edc2f955
fetched_at: '2026-06-28T22:45:19.177575+00:00'
product: protheus
section_id: 1500001536901
source: central-protheus
title: 'RH - Linha Protheus - TAF - eSocial - Eventos Periódicos - S-1200 - Código
  da Ocorrência 552: Quantidade de casas decimais invalida'
type: support-article
updated_at: '2026-06-25T12:22:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/26946545852567-RH-Linha-Protheus-TAF-eSocial-Eventos-Peri%C3%B3dicos-S-1200-C%C3%B3digo-da-Ocorr%C3%AAncia-552-Quantidade-de-casas-decimais-invalida
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26946570519703) Tempo aproximado para leitura: **00:03:00 min****Ocorrência**No módulo do TAF, ao tentar realizar a transmissão do evento S-1200 (Remuneração de Trabalhador vinculado ao Regime Geral de Previd. Social) é apresentada a seguinte rejeição:  
  
**Sequência: 000001 - Tipo: Erro - Codigo da ocorrência: 552**   
**Localização: /eSocial/evtRemun/omDev[2]/infoPerApur/iceEstabLot/remunPerApur/itensRemun[1]/qto Rubr**   
**Descrição: Quantidade de casas decimais invalida.**  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - eSocial - TAF - Todas as versões.  
  
**Causa**Essa inconsistência ocorre, pois o tamanho e/ou decimal do campo C9M\_QTDRUB estão incorretos.  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
**1.** Verifique o **Tamanho** e **Decimal** do campo no **Configurador**.  
**Caminho**: Base de Dados > Dicionário > Base de Dados:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26946570520343)  
  
**2.** Caso estejam diferentes de **Tamanho = 12 e Decimal = 2**, realize o ajuste para ficar de acordo com a regra do eSocial:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26946545828631)  
<https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-1-2-versao-s-1-2-nt-04-2024/index.html#1202_dmDev_infoPerApur_ideEstab_remunPerApur_itensRemun>  
  
**3.** Exclua o evento **S-1200** no TAF e gere/integre novamente a partir do seu **ERP**;  
  
**4.** Tente transmitir novamente e verifique se o erro foi solucionado.  
  
**Saiba Mais**Para saber mais consulte os links abaixo:   
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)  
  
Para conhecimento dos eventos futuros, acessa a nossa página [**TOTVS Informa**](https://informa.totvs.com/)selecione em categorias a área e pesquise por "**Eventos**"  
  
Essa documentação também pode ser acessada 24h por dia e pelo Protheus, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
