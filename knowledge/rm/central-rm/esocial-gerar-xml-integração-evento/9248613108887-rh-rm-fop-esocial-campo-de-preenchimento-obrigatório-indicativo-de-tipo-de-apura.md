---
article_id: 9248613108887
category: eSocial - Gerar XML/ Integração Evento
content_hash: d64094a1280726f3dff736f18af3d30542c5d906e28f1c213d2bf613b9564736
fetched_at: '2026-06-28T22:47:12.002312+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: 'RH - RM - FOP - eSocial - Campo de preenchimento obrigatório: Indicativo de
  tipo de apuração de IR'
type: support-article
updated_at: '2025-07-02T17:17:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9248613108887-RH-RM-FOP-eSocial-Campo-de-preenchimento-obrigat%C3%B3rio-Indicativo-de-tipo-de-apura%C3%A7%C3%A3o-de-IR
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24296765065623) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**Ao encaminhar o evento S-2299 é apresentado o erro de **Codigo da Ocorrência: 1 - Descrição : Campo de preenchimento obrigatorio: Indicativo de tipo de apuracao de IR.**  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as versões  
  
**Causa**O indicativo do tipo de apuração de IR foi uma *Tag* inserida no S-2299 a partir do leiaute S-1.0.

                          Leiaute S-1.0 *tag* indApurIR

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9318995547415)

Conforme leiaute do eSocial S-1.0 acima mencionado, o campo **indApurIR** é obrigatório caso o mês/ano de desligamento do funcionário seja maior ou igual à 07/2021.   
  
**Solução**Para solucionar essa ocorrência, realize as seguintes validações:  
1.  No parametrizador do eSocial em **Configurações | Parametrizador | Esocial | Configurações Gerais 1/7** e consulte se o Leiaute está vigente;  
2. Valide se no XML do RM e TAF gerou a *tag* automaticamente considerando a seguinte regra, conforme descrito no [Mapeamento do S-2299](https://tdn.totvs.com/display/public/LRM/Evento+S-2299), **Se for verba de IRRF RRA (códigos de cálculo 207, 211 ou 215) o valor será 1, caso contrário será 0.**'  
3. Se não existir apenas no XML, peço a gentileza de acionar o time de Suporte do TAF realizando a abertura de um novo Ticket para avaliação da equipe responsável pelo telefone (11) 4003-0015, Chat Online ou pelo Portal do Cliente.

4. Caso o XML do TAF também já conste corretamente a TAG para todos os registros, sugiro que seja feito contato diretamente com o [Governo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004050432-RH-RM-FOP-eSocial-Contato-com-o-Governo-para-d%C3%BAvidas-sobre-os-eventos-do-eSocial?source=search) para avaliação.
