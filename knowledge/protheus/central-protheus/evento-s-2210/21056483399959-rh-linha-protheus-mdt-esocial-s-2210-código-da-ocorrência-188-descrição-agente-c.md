---
article_id: 21056483399959
category: Evento S-2210
content_hash: 327688ea06209bb1c84872da9e57a498fafd813ea9a944a93536cabc5246cabb
fetched_at: '2026-06-28T22:45:24.403470+00:00'
product: protheus
section_id: 8260521640983
source: central-protheus
title: RH - Linha Protheus - MDT - eSocial - S-2210 - Código da ocorrência 188 Descrição
  Agente causador invalido
type: support-article
updated_at: '2024-02-02T13:34:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21056483399959-RH-Linha-Protheus-MDT-eSocial-S-2210-C%C3%B3digo-da-ocorr%C3%AAncia-188-Descri%C3%A7%C3%A3o-Agente-causador-invalido
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21056505891479) Tempo aproximado para leitura: **00:02:00min****Ocorrência**Código da ocorrência: 188 Descrição: Agente causador invalido, o que deve avaliar?  
  
![Image-3213.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21056483355927) **Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as versões  
  
**Causa**Mudança referente ao agente causador no leiaute do eSocial S-1.2 que passou a vigorar no dia **22/01/2024.**  
  
![ag.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21056505894807)  
  
Para mais informações, consulte: [Leiaute eSocial S-1.2](https://www.gov.br/esocial/pt-br/noticias/publicacao-da-versao-s-1-2-do-leiaute-do-esocial)  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
1. Verifique se seu ambiente esta atualizado e configurado com o leiaute S-1.2, conforme documentação a seguir: [Configuração Leiaute S-1.2](https://centraldeatendimento.totvs.com/hc/pt-br/articles/20828974337559)  
2. Verifique se as tabelas auto contidas do TAF estão atualizadas: [Atualização das tabelas auto contidas do TAF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034479973-Automa%C3%A7%C3%A3o-Fiscal-CONFIGURA%C3%87%C3%83O-Atualiza%C3%A7%C3%A3o-das-tabelas-autocontidas)  
3. No módulo de **Medicina e Segurança do Trabalho**. Acessar a rotina de **Acidentes** através do caminho, **Atualizações > Acidente de Trabalho > Acidentes**. Para acidentes cadastrados com data igual ou posterior ao dia **22/01/2024** e que tiverem a indicação do tipo de acidente **1 - Acidente Típico** ou **3 - Doença do trabalho**, o agente causador deve ser um código valido, presente na **tabela 14** (Códigos iniciados com numeral **3**), conforme imagem abaixo:  
  
![1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21056505898135)  
  
Para acidentes cadastrados com data inferior ao dia **22/01/2024** ou que tiverem a indicação do tipo de acidente **2 - Acidente de Trajeto**. O agente causador deve ser um código valido, presente na **tabela** **14** (Códigos iniciados com numeral 3) ou na **tabela 15** (Códigos iniciados com numeral 2). Conforme imagem abaixo:  
  
![2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21056505900951)  
  
Ao realizar a inserção do código correto informado no Passo 3, clicar em **Confirmar**. Será gerado um evento S-2210:  
  
![3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21056505902615)  
  
O evento gerado irá gravar a informação do agente causador no XML na tag **<codAgntCausador>**, para mais informações de como gerar XML da CAT, consulte: [Como gerar o XML do eventoS-2210](https://centraldeatendimento.totvs.com/hc/pt-br/articles/5754090383383) **![xm.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21068387109271)**  
O evento S-2210 no qual ocorreu o erro de transmissão será retificado no TAF com a nova informação. Realize novamente a transmissão do evento ao governo:  
  
![4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21056505904279)  
  
**Saiba Mais**[Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT)  
[Artigos centralizados MDT - Acidente de Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360012070513-MDT-Acidente-de-Trabalho)  
[Artigos centralizados MDT - eSocial - S-2210](https://centraldeatendimento.totvs.com/hc/pt-br/sections/8260521640983-Evento-S-2210)
