---
article_id: 26790302703383
category: TAF - eSocial - Eventos Periódicos
content_hash: 7ac0d65560199490875a2af7326da74196d4d87061eec3d58cd3e12006560aa5
fetched_at: '2026-06-28T22:45:19.083001+00:00'
product: protheus
section_id: 1500001536901
source: central-protheus
title: 'RH - Linha Protheus - TAF - eSocial - Eventos Periódicos - S-1299 - Código
  da Ocorrência 588: Preencha com Sim quando existir remuneração no período e Não
  quando não existir'
type: support-article
updated_at: '2026-06-23T20:52:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/26790302703383-RH-Linha-Protheus-TAF-eSocial-Eventos-Peri%C3%B3dicos-S-1299-C%C3%B3digo-da-Ocorr%C3%AAncia-588-Preencha-com-Sim-quando-existir-remunera%C3%A7%C3%A3o-no-per%C3%ADodo-e-N%C3%A3o-quando-n%C3%A3o-existir
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26790340945943) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**No módulo do TAF, ao tentar realizar a transmissão do evento S-1299 (Fechamento dos Eventos Periódicos) é apresentada a seguinte rejeição:  
  
**Sequência: 000001 - Tipo: Erro - Codigo da ocorrência: 588  
Localização: /eSocial/evtFechaEvPer/infoFech/evtRemun  
Descrição: Preencha com Sim quando existir remuneração no período e Não quando não existir.  
  
Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - eSocial - TAF - Todas as versões.  
  
**Causa**Essa inconsistência ocorre, pois o campo Remuneração (**CUO\_REMUN**) está preenchido incorretamente.  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
**1.** Acesse a rotina de Fechamento de Período (S-1299) no TAF.   
Caminho: Atualizações > Eventos eSocial > Periódicos > Fechamento Periódicos:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26790302682647)  
  
**2.** Após acessar a rotina, localize o S-1299 com erro, entre como **Alterar** e ajuste o campo **Remuneração** do evento conforme a realidade da sua Empresa e a regra do eSocial:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26790302683543)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26790302684823)  
<https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-1-2-versao-s-1-2-nt-04-2024/index.html#1299_infoFech>  
  
**3.** Confirme as alterações e tente transmitir o evento novamente.  
  
**Saiba Mais**Para saber mais consulte os links abaixo:   
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)  
  
Para conhecimento dos eventos futuros, acessa a nossa página [**TOTVS Informa**](https://informa.totvs.com/)selecione em categorias a área e pesquise por "**Eventos**"  
  
Essa documentação também pode ser acessada 24h por dia e pelo Protheus, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
