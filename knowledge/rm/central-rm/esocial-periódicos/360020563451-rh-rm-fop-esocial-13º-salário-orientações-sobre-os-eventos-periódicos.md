---
article_id: 360020563451
category: esocial - Periódicos
content_hash: d7ca6bfdbf89302354bbbb6a5bb42127fe675245391888d400b8d9a2b2bb3b76
fetched_at: '2026-06-28T22:47:09.118086+00:00'
product: rm
section_id: 1500000860982
source: central-rm
title: 'RH - RM - FOP - eSocial - 13º Salário: Orientações sobre os eventos periódicos'
type: support-article
updated_at: '2024-10-23T10:57:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020563451-RH-RM-FOP-eSocial-13%C2%BA-Sal%C3%A1rio-Orienta%C3%A7%C3%B5es-sobre-os-eventos-peri%C3%B3dicos
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22836604462231) Tempo aproximado para leitura: 00:03:00 min  
  
Dúvida**Como gerar os eventos periódicos relativos ao pagamento do 13º Salário?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - eSocial - A partir da versão 12.1.25  
  
**Solução**O 13º salário é concedido anualmente, em duas parcelas. Porém, é possível realizar o pagamento do adiantamento do 13º salário integral antes do mês de dezembro. Caso o empregador decida pagar o benefício em duas parcelas, a primeira parcela (adiantamento do 13º salário) deve ser paga ao trabalhador entre os meses de fevereiro e novembro (até o dia 30/11). Já a segunda parcela deve ser paga até o dia 20 de dezembro, considerando o valor da remuneração de dezembro e descontando o adiantamento recebido durante o ano corrente.

Quanto aos encargos, devem ser observadas as seguintes regras de incidência:

**FGTS** – incide quando é pago qualquer valor referente ao 13º salário, no adiantamento ou na quitação do 13º salário através da 2ª parcela. O recolhimento é realizado na guia da competência de pagamento.  
**Contribuição Previdenciária** – incide sobre o valor total do 13º salário. O recolhimento é realizado na guia exclusiva de 13º salário em dezembro, quando refere-se a 2ª. parcela. Em caso de rescisão o recolhimento é realizado na guia da competência de pagamento.  
**IRRF** – incide sobre o total do 13º salário. O recolhimento é realizado juntamente com a guia da competência de pagamento.

Em relação à geração dos XML, observa-se:

• Pagamento em **duas parcelas** (adiantamento da 1ª parcela do 13º)  
Será gerado **um único S-1200** no **período de apuração corrente**, incluindo o pagamento da folha e o adiantamento do 13º conforme seus períodos de lançamento (ideDmDev).   
Para a Folha calculada em Dezembro, serão gerados **dois S-1200** sendo, um com o pagamento da **Folha Mensal** (período de apuração '12') e outro com o pagamento do **13º** (período de apuração 'Anual').   
O S-1210 é único para Folha e 13º.

**Exemplo**: Adiantamento do 13º feito no mês de Novembro/2021.   
Em Novembro, período de apuração '11-2020', será gerado um único S-1200 contendo as verbas da folha e do adiantamento do 13º. O evento S-1200 gerado deverá ser enviado até o dia 15/Dez.  
Em Dezembro, será gerado um S-1200 com a Folha no período de apuração '12-2021' (Mensal) e outro S-1200 com o 13º no período de apuração '2021' (Anual). O evento S-1200 Mensal deve ser enviado até o dia 15/Jan, e o S-1200 Anual até o dia 20/Dez.

• Pagamento em **parcela única** (sem adiantamento)  
Serão gerados **dois S-1200** sendo, um com o pagamento da Folha Mensal (período de apuração '12') e outro com o pagamento do 13º (período de apuração 'Anual').  
O S-1210 é único para Folha e 13º.

**Exemplo**: Pagamento integral realizado em Dezembro/2021.  
Em Dezembro, será gerado um S-1200 com a Folha no período de apuração '12-2021' (Mensal) e outro S-1200 com o 13º no período de apuração '2021' (Anual). O evento S-1200 Mensal deve ser enviado até o dia 15/Jan, e o S-1200 Anual até o dia 20/Dez.

**Importante**  
Para o sistema manter o período aquisitivo de férias e os avos do 13º salário para funcionários que tiveram [Suspensão Temporária de Contrato](https://tdn.totvs.com/pages/releaseview.action?pageId=545621865), deverá marcar os parâmetros localizados em **Configurações | Parametrizador | Folha normal | Afastamento 2/2**.

**![euuuuu.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360098374534)**

**Importante**Cabe destacar que os eventos S-1200 e S-1299 referentes ao período de apuração anual devem ser enviados entre os dias **01 e 20 de dezembro** . É importante lembrar que não há período de apuração anual para o evento S-1210, ou seja, no evento de pagamento (S-1210) referente a um período anual, o mês em que é efetuado o pagamento deve ser indicado no campo {perApur} e o prazo para seu envio segue a regra geral, ou seja, deve ser enviado até o dia 07 do mês seguinte ou até o fechamento da folha deste mês, o que ocorrer primeiro. No evento S-1210, quando se tratar de pagamento de folha anual, apenas a indicação do período de referência {perRef} deve ser informada no formado AAAA e não AAAA-MM.

**Saiba mais**  
Para verificar o processo de geração dos eventos vinculados ao 13º salário, acesse:   
      • [Orientações para realizar o pagamento do 13º Salário - eSocial](http://tdn.totvs.com/pages/releaseview.action?pageId=439363960)
