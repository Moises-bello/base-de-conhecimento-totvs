---
article_id: 360022286212
category: GPE - eSocial - Periódicos
content_hash: 9b0ff87397feed7316f2b1ea345310961d063c6532cfbfaac49a57ee660993dd
fetched_at: '2026-06-28T22:45:09.040727+00:00'
product: protheus
section_id: 360005445793
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-1299 - Como gerar o evento S-1299 (fechamento
  periódicos) para transmitir ao RET
type: support-article
updated_at: '2025-07-22T17:12:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022286212-RH-Linha-Protheus-GPE-eSocial-S-1299-Como-gerar-o-evento-S-1299-fechamento-peri%C3%B3dicos-para-transmitir-ao-RET
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19460669242519) Tempo aproximado para leitura: **00:02:00min  
  
Dúvida**Como gerar o evento S-1299 (fechamento periódicos) para transmitir ao RET?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as Versões  
  
**Solução**O evento S-1299 pode ser gerado através do modulo **SIGAGPE** ou **SIGATAF** em um dos caminhos abaixo.  
  
**SIGAGPE:** Miscelânea > eSocial >Fechamento S-1299  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19460669257111)  
  
Preencher a **competência** e selecionar a **filial.** O campo 'Ref. 13' deve manter como NÃO para que seja gerado o S-1299 mensal. Após confirmar o evento será integrado e ficará disponível para transmissão.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27323856063895)

**SIGATAF**: Atualizações > Eventos eSocial > Periódicos > Fechamento Periódicos.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19460643349399)  
  
No TAF os campos devem ser preenchidos pelo usuário, abaixo a descrição dos campos:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19460669266839)

Campos TAF  S-1299 x Tags S-1299 eSocial  
  
**Campo Ind.Per.Apur. = tag indApuracao**  
Descrição: Indicativo de período de apuração: 1 - Mensal; 2 - Anual (13° salário).   
  
**Campo Per.Apur = tag perApur**  
Informar o mês/ano (formato AAAA-MM) de referência das informações, se indApuracao for igual a [1], ou apenas o ano (formato AAAA), se indApuracao for igual a [2].  
**Validação:** Deve ser um mês/ano ou ano válido, igual ou posterior ao início da obrigatoriedade dos eventos periódicos para o empregador.  
  
**Campo Remuneração = tag evtRemun**  
Descrição: Possui informações relativas remuneração de trabalhadores no período de apuração? S - Sim; N - Não. Validação: Se for igual a [S], deve existir evento de remuneração (S-1200, S-2299 ou S-2399) enviado para o período de apuração. Caso contrário, não deve existir evento de remuneração para o período de apuração.   
  
**Campo Pag. Per Apu = tag evtPgtos**  
Descrição: Possui informações de pagamento de rendimentos do trabalho no período de apuração? Validação: Se for igual a [S], deve existir o evento S-1210 enviado para o período de apuração. Caso contrário, não deve existir o evento.   
  
**Campo Com.Produção = tag evtComProd**  
Descrição: Possui informações de comercialização de produção? S - Sim; N - Não. Validação: Se for igual a [S], deve existir o evento S-1260 no período de apuração. Caso contrário, não deve existir o evento   
  
**Campo Cont.NaoPort = tag evtContratAvNP**  
Descrição: Contratou, por intermédio de sindicato, serviços de trabalhadores avulsos não portuários? S - Sim; N - Não.  Validação: Se for igual a [S], deve existir evento transmitido para o período de apuração, relativo a "contratação de avulsos não portuários" (S-1270). Caso contrário o evento não deve existir.  
  
**Campo InfoComplPer = tag evtInfoComplPer**  
Descrição: Possui informações de desoneração de folha de pagamento ou, sendo empresa enquadrada no Simples, possui informações sobre a receita obtida em atividades cuja contribuição previdenciária incidente sobre a folha de pagamento é concomitantemente substituída e também não substituída? Validação: Se for igual a [S], deve existir o evento S-1280 para o mesmo período de apuração. Caso contrário, não deve existir o evento.  
  
**OBS:** Após gerar o evento o usuário deve fazer a transmissão através do TAF.  
  
**Artigos Relacionados:**

* [S-1200 - Tenho uma empresa sem movimento, mas as filiais têm movimento. Neste caso, como faço a informação?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004771032)
* [S-1299 - Temos uma filial sem movimento. Como devo enviar esta situação](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036913273)
* [S-1299 - Como funciona este evento de fechamento? Necessário enviar após enviar todos os periódicos?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004476032)

**Saiba Mais**Para saber mais consulte os links abaixo:   
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes)  
  
*Para conhecimento dos eventos futuros, acessa a nossa página*[***TOTVS Informa***](https://informa.totvs.com/)*selecione em categorias a área e**pesquise**por "****Eventos****"  
Quer receber em primeira mão sobre artigos publicados? Participe da nossa [**Comunidade****WhatsApp**](https://chat.whatsapp.com/DJCIHJOMrC65a262mwAIEI?utm_source=whatsapp&utm_medium=-&utm_campaign=backoffice&utm_term=gsp&utm_content=-)*Essa documentação também pode ser acessada 24h por dia e pelo Protheus, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
