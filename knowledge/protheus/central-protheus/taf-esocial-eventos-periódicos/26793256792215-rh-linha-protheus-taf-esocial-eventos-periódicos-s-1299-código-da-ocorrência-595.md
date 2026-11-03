---
article_id: 26793256792215
category: TAF - eSocial - Eventos Periódicos
content_hash: c3befe7cb5c16d5175504c6e294ccd5f77f6126dc9ede0871e1ba3f5fb0ae2d0
fetched_at: '2026-06-28T22:45:19.088104+00:00'
product: protheus
section_id: 1500001536901
source: central-protheus
title: 'RH - Linha Protheus - TAF - eSocial - Eventos Periódicos - S-1299 - Código
  da Ocorrência 595: Preencha com Sim quando existir informação de contratação de
  trabalhadores avulsos não portuários no período e Não quando não existir'
type: support-article
updated_at: '2026-06-23T20:50:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/26793256792215-RH-Linha-Protheus-TAF-eSocial-Eventos-Peri%C3%B3dicos-S-1299-C%C3%B3digo-da-Ocorr%C3%AAncia-595-Preencha-com-Sim-quando-existir-informa%C3%A7%C3%A3o-de-contrata%C3%A7%C3%A3o-de-trabalhadores-avulsos-n%C3%A3o-portu%C3%A1rios-no-per%C3%ADodo-e-N%C3%A3o-quando-n%C3%A3o-existir
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26793213416599) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**No módulo do TAF, ao tentar realizar a transmissão do evento S-1299 (Fechamento dos Eventos Periódicos) é apresentada a seguinte rejeição:  
  
**Sequência: 000001 - Tipo: Erro - Código da ocorrência: 595  
Localização: /eSocial/evtFechaEvPer/infoFech/evtContratAvNP  
Descrição: Preencha com Sim quando existir informação de contratação de trabalhadores avulsos não portuários no período e Não quando não existir.  
  
Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - eSocial - TAF - Todas as versões.  
  
**Causa**Essa inconsistência ocorre, pois os campos **Tipo de Guia** (CUO\_TPGUIA) e **Cont.NaoPort** (CUO\_COAVNP) estão preenchido incorretamente.  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
**1.** Acesse a rotina de Fechamento de Período (S-1299) no TAF.   
Caminho: Atualizações > Eventos eSocial > Periódicos > Fechamento Periódicos:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26793213421463)  
  
**2.** Após acessar a rotina, localize o S-1299 com erro, entre como **Alterar** e ajuste os campos **Tipo de Guia** e **Cont.NaoPort** do evento conforme a realidade da sua Empresa e a regra do eSocial:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26793256743191)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26793213430551)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26793213438615)  
<https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-1-2-versao-s-1-2-nt-04-2024/index.html#1299_infoFech>  
  
**3.** Confirme as alterações e tente transmitir o evento novamente.  
  
**Saiba Mais**Para saber mais consulte os links abaixo:   
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)  
  
Para conhecimento dos eventos futuros, acessa a nossa página [**TOTVS Informa**](https://informa.totvs.com/)selecione em categorias a área e pesquise por "**Eventos**"  
  
Essa documentação também pode ser acessada 24h por dia e pelo Protheus, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
