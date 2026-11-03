---
article_id: 360025168831
category: eSocial - Gerar XML/ Integração Evento
content_hash: 769b207e925bcf452916b761326fec823bcc725b46e3da59cbf5086b73b4635d
fetched_at: '2026-06-28T22:47:13.179924+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: RH - RM - FOP - eSocial - Validação dos erros 724 e/ou 726 no envio do evento
  S-1210
type: support-article
updated_at: '2025-12-29T14:51:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025168831-RH-RM-FOP-eSocial-Valida%C3%A7%C3%A3o-dos-erros-724-e-ou-726-no-envio-do-evento-S-1210
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18579683975191)**Tempo aproximado para leitura: **00:01:00 min**  
  
**Dúvida**  
Quais as possíveis causas para a exibição dos erros 724 (**Não foi localizado um evento de remuneração do trabalhador para o período e com mesmo demonstrativo de pagamento**) e 726 (**Não foi localizado um evento de rescisão contratual para o trabalhador com mesmo recibo de pagamento**) no envio do S-1210?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as versões  
  
**Solução**  
O erro **724** é apresentado no envio do S-1210 com a seguinte mensagem:

Não foi localizado um **evento de remuneração** do trabalhador para o período e com mesmo demonstrativo de pagamento. Ação Sugerida: Deve ser um valor atribuído pela fonte pagadora em S-1200, S-1202 ou S-1206 no campo "Identificador de Recibo de Pagamento", obedecendo a relação: Se Tipo de Pagamento = [1], em S-1200; Se Tipo de Pagamento = [5], em S-1202; Se Tipo de Pagamento = [7], em S-1206.

Já o erro **726** é apresentado no envio do S-1210 com a seguinte mensagem:

Não foi localizado um **evento de rescisão contratual** para o trabalhador com mesmo recibo de pagamento. Ação Sugerida: Deve ser um identificador de recibo de pagamento atribuído pela empresa em um dos eventos rescisórios (S-2299 ou S-2399), no campo "Identificador de recibo de pagamento". Se Tipo de Pagamento = [2] deve ser um valor atribuído pela empresa em S-2299; Se Tipo de Pagamento = [3], deve ser um valor atribuído pela empresa em S-2399.

Notem que os erros são bem semelhantes, alterando apenas o **evento** de remuneração de referência.   
As validações para o caso dos erros são:

**• Regime COMPETÊNCIA**  
Deve-se validar no XML (RM e TAF) se a *tag* **tpPgto** (tipo de pagamento) está sendo gerada corretamente relacionando o evento de remuneração (S-1200). Deve-se verificar também se todas as verbas estão corretamente relacionadas ao **perRef** (mês de referência do pagamento) do evento S-1200.

**• Regime CAIXA**  
Neste caso deve-se verificar se a *tag* **tpPgto** está com o tipo de pagamento**9 - Pagamento relativo a competências anteriores**. O evento S-1210, para funcionários admitidos posteriormente ao início da obrigatoriedade dos eventos não periódicos, só será gerado no próximo período de apuração. Isto porque as verbas pagas no mês de admissão terão datas de pagamento para o próximo mês.   
A *tag***nrRecArq** é preenchida pelo TAF com o número do recibo do arquivo que contém as informações da rescisão contratual que originou o pagamento. Assim, deve-se validar se o XML gerado pelo TAF apresenta corretamente esta informação.

Assista nossos **vídeos How To** sobre o tema:

*Parte 1/2*

*Parte 2/2*

**Saiba mais**  
Para mais informações sobre as validações, acesse:  
      • [Como validar os erros 724 e 726 apresentados no S-1210?](https://tdn.totvs.com/pages/releaseview.action?pageId=464966473)
