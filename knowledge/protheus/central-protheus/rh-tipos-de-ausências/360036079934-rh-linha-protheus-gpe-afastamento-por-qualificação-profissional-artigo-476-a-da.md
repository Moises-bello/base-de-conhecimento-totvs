---
article_id: 360036079934
category: RH - Tipos de Ausências
content_hash: 1e8680c4a25e37d45a43953b632c3a2d5f102db09cd0f8272bdcdcc819da4ca7
fetched_at: '2026-06-28T22:43:21.057288+00:00'
product: protheus
section_id: 360011967353
source: central-protheus
title: RH - Linha Protheus - GPE - Afastamento por Qualificação Profissional (Artigo
  476-A da CLT)
type: support-article
updated_at: '2025-08-06T19:49:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036079934-RH-Linha-Protheus-GPE-Afastamento-por-Qualifica%C3%A7%C3%A3o-Profissional-Artigo-476-A-da-CLT
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33997079941399) Tempo aproximado para leitura: 00:05:00 min**

**Dúvida**Como parametrizar o Afastamento por Qualificação Profissional conforme Artigo 476-A da CLT

**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**O empregado poderá se afastar por um período de dois a cinco meses, para participar de curso ou programa de qualificação profissional.  
A suspensão do contrato de trabalho poderá ocorrer em duas situações, por instrumento coletivo de trabalho e concordância do empregado.  
Quando a suspensão ocorrer por ocasião a acordo ou a convenção coletiva de trabalho, não será admitido somente o acordo individual e sim um acordo coletivo.  
Caso da suspensão ocorrer a pedido do empregado, deverá manifestar sua concordância de modo formal por escrito.  
  
**>Cadastro do Afastamento**Em **Atualizações/ Definições de Calculo/ Tipos de Ausência,** deve ser criado um afastamento motivo **27 - Qualificação -** Afastamento por suspensão de contrato de acordo com ART 476-A;

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360047183094)

O período que o contrato permanecer suspenso, **não entra para contagem de 13° e Férias.**  
  
**Código de Ausência SEFIP:**  
Conforme manual da Sefip código = X (Licença sem vencimentos)  
Código de Retorno = Z5 (Outros retornos de afastamento temporário e/ou licença)  
  
**Código de ausência RAIS:**  
Conforme manual da RAIS = 70 (Licença sem vencimentos, remuneração);  
  
**Código Homolognet:**  
Código = X2 (Licença sem percepção de salário);  
Código de Retorno = Z10 (Retorno de licença sem percepção de salário, informado pela movimentação X2);  
  
**>Lançamento do Afastamento e Integração com o TAF**

Em**Atualizações/ Lançamentos/ Ausências**, deve ser informado o afastamento com **data inicio em fim.**

Esse afastamento só deve ser integrado se o afastamento for superior a 30 dias.

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360048068033)

**>Cadastro de Verba para pagamento da Bolsa Qualificação Profissional**

A verba de pagamento da Bolsa Qualificação deve ser tipo Provento, sem incidências;

  
**>Como fazer para que a verba apareça na folha e pagamento?**

O afastamento pode durar de dois a cinco meses, para que não seja necessário lançar mensalmente a verba para pagamento, orientamos que o lançamento desta verba seja feito na rotina de valores futuros.

Exemplo: Afastamento 01/07/2019 a 31/08/2019 - O colaborador receberá auxilio por 2 meses.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360048067833)  
  
**>Folha de pagamento**

Na folha de pagamento será demonstrada a verba de Bolsa Qualificação, sem incidência de FGTS, INSS e IRRF.

A verba Salário Base ID 0318 será demonstrada normalmente assim como em qualquer afastamento.

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360048068913)

Para mais informações, acesse: [Consultoria de Segmentos](https://tdn.totvs.com/pages/releaseview.action?pageId=126718725)

****Saiba Mais****  
[RH - Linha Protheus - GPE - Como cadastrar verbas no Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411677253783-RH-Linha-Protheus-GPE-Como-cadastrar-verbas-no-Protheus)[RH - Linha Protheus - GPE - Cadastro tipos de ausência](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360029174591-RH-Linha-Protheus-GPE-Cadastro-tipos-de-aus%C3%AAncia)
