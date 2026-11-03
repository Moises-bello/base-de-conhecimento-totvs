---
article_id: 37068075172375
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 97829a8fef4bce5f872fd95fb207ba77cfe5d06df902d008ef39ff02978d2793
fetched_at: '2026-06-28T22:38:29.829797+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - SIGAFAT - InterFunctionCall: cannot
  find function CBOTPCOMPL'
type: support-article
updated_at: '2026-01-02T13:35:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37068075172375-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-InterFunctionCall-cannot-find-function-CBOTPCOMPL
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37068075150359) Tempo aproximado para leitura: **00:02:00 min**  
  
**Ocorrência**  
Como corrigir os erros InterFunctionCall: cannot find function CBOTPCOMPL e Help:NOFUNCW - Opção não disponível no Protheus Função: CBOTCOMPL Called By X3CBOX?  
  
**Ambiente**  
Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões.

**Causa**  
O erro ocorre devido a ausência de uma função presente no fonte MATA600.PRW (Nota de Débito), para corrigir é necessário aplicar o pacote de expedição contínua abaixo:

**Obs.:** Caso já tenha aplicado o pacote e ainda ocorra o erro, isso significa que houve algum erro na atualização, será necessário reaplicar o pacote atualizando novamente os fonte e rodando o UPDDISTR.

**Solução**

Segue passo a passo:

**1 -** Aplique o pacote de 'Expedição Contínua' de **dezembro/2025** conforme sua release: [Pacotes de Atualização - Faturamento](https://tdn.totvs.com/x/Iw4dHw)

Exemplo:   
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/37069382298391)**  
  
**2 -** Atualize os fontes e aplique o dicionário contido na pasta "sdf": **Abra a pasta SDF > Abra a pasta "bra" > Copie todas as pastas e cole (substituindo) dentro da pasta "" do ambiente Protheus "protheus > protheus\_data > systemload".**  
  
**3 -** Rode o UPDDISTR para compatibilizar os dicionários e as tabelas necessárias.

**Observações**  
Caso o ambiente seja Cloud, recomendamos seguir o processo presente na documentação da equipe: [**CLOUD - MP - Aplicar Pacote (Patch)**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024948533-CLOUD-MP-Aplicar-Pacote-Patch). Se surgir alguma dúvida/impeditivo sobre o processo documentado, recomendamos abrir um chat/ticket com o time Cloud para auxiliarem na aplicação do pacote.
