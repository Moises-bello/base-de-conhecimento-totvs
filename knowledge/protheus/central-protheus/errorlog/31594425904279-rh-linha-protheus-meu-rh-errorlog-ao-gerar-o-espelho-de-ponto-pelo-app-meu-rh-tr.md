---
article_id: 31594425904279
category: ERRORLOG
content_hash: b3d7e060da56b6dea8ffc65289eb5bc10af4566bc8ffedd3bf20afc2f615cfea
fetched_at: '2026-06-28T22:44:39.411472+00:00'
product: protheus
section_id: 10299583475863
source: central-protheus
title: RH - Linha Protheus - Meu RH - Errorlog ao gerar o Espelho de Ponto pelo App
  Meu RH - Traduzir fonte IMPESP_pt-br.TRes não disponível
type: support-article
updated_at: '2026-06-23T21:12:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/31594425904279-RH-Linha-Protheus-Meu-RH-Errorlog-ao-gerar-o-Espelho-de-Ponto-pelo-App-Meu-RH-Traduzir-fonte-IMPESP-pt-br-TRes-n%C3%A3o-dispon%C3%ADvel
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31594425895447) Tempo aproximado para leitura: **00:02:00 min** **Dúvida***Errorlog* ao gerar o Espelho de Ponto pelo App Meu RH - Traduzir fonte IMPESP\_pt-br.TRes não disponível  
  
**Ambiente**TOTVS RH (Linha Protheus) - Meu RH – todas as versões  
  
**Causa**Ao gerar o Espelho de Ponto no App Meu RH, é trazido o seguinte *errorlog* no *console.log*:  
  
**THREAD ERROR ([14748], TP|HTTPREST|ENV18@18|FALSE, 510B0CAACE7B284BAD2A95402D4AFEAA) 22/04/2025 13:21:37**

**Saída no final: Traduzir fonteIMPESP\_pt-br.TRes não disponível!**  
**on FINAL(MSFINAL.PRW) 11/04/2025 09:24:37 line : 269**

**Solução**Este *errorlog* traz referência à **falta de compilação dos tradutores *.tres* no RPO do Meu RH.**  
Por vezes, é configurado um RPO apartado para o Meu RH do Protheus, nesse caso, o ***RDMake IMPESP,*** responsável pela geração do Espelho de Ponto no Meu RH, está compilado nele, **porém os tradutores .tres não estão.**  
  
Para solucionar, será necessário que a Equipe de TI compile o *RDMake IMPESP* mais recente, assim como todos os tradutores .tres no RPO.  
  
Abaixo, os arquivos de deverão ser compilados:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31607735228695)  
  
**Para saber como baixar o *include*, *RDMake* e os .tres do *IMPESP*, [clique aqui.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/19276300373655)  
  
Saiba Mais:  
[CLIQUE AQUI para acessar mais artigos e FAQs sobre o MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)  
[CLIQUE AQUI para acessar a documentação de referências sobre o MEU RH](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)**
