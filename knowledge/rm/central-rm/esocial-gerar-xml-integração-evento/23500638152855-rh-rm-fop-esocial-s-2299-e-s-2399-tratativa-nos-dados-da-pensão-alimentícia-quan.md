---
article_id: 23500638152855
category: eSocial - Gerar XML/ Integração Evento
content_hash: f7411ca15c18470fb3e4ed55eba59479edd237f9aa50d620eeed9917d3c148cf
fetched_at: '2026-06-28T22:47:13.164613+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: RH - RM - FOP - eSocial - S-2299 e S-2399 - Tratativa nos dados da Pensão Alimentícia
  quando possui retenção no FGTS
type: support-article
updated_at: '2026-06-01T16:07:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23500638152855-RH-RM-FOP-eSocial-S-2299-e-S-2399-Tratativa-nos-dados-da-Pens%C3%A3o-Aliment%C3%ADcia-quando-possui-reten%C3%A7%C3%A3o-no-FGTS
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23500638138007) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
Como realizar o Indicativo de pensão alimentícia para fins de retenção de FGTS na geração do evento S-2299 e S-2399 ?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as versões  
  
**Solução**  
Na geração dos eventos S-2299 e S-2399, as tags abaixo deverão ser geradas com base nas informações e parâmetro "Possui Retenção FGTS" do cadastro de dependentes dos dados da pensão.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23500638138775)

Implementado o parâmetro **Possui Retenção FGTS** no cadastro de dependentes. Ao ativá-lo, o sistema passará a gerar automaticamente as tags de informação sobre pensão alimentícia, de acordo com os dados cadastrados.

Esse parâmetro deve ser marcado apenas quando houver decisão judicial que estabeleça que um percentual do saque do FGTS seja destinado ao beneficiário da pensão alimentícia.

1) Acesse o menu Funcionários | Anexos Dependentes | Aba Dados da Pensão e marque o campo conforme demonstração abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23500638140439)

2) Ao gerar o XML do evento S-2299 ou S-2399 a tag será preenchida conforme demonstrado abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23500638141335)

**Saiba mais**  
[DT - S-2299 e S-2399 - Tratativa nos dados da Pensão Alimentícia quando possui retenção no FGTS](https://tdn.totvs.com/pages/viewpage.action?pageId=841178815)
