---
article_id: 30648390781335
category: eSocial - Gerar XML/ Integração Evento
content_hash: 94f9870907624de5a191092cf88df144da2e5766a7be0886801e0290d277ae61
fetched_at: '2026-06-28T22:47:11.898180+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: 'RH - RM - FOP - eSocial - Ao enviar o evento S-1210 ocorre o Erro código 1955:
  O somatório de todas as rubricas de todos os demonstrativos referenciados nos grupos
  de Informações de Pagamento, cujos campos de Código de Incidência de IR ...'
type: support-article
updated_at: '2026-04-08T20:45:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/30648390781335-RH-RM-FOP-eSocial-Ao-enviar-o-evento-S-1210-ocorre-o-Erro-c%C3%B3digo-1955-O-somat%C3%B3rio-de-todas-as-rubricas-de-todos-os-demonstrativos-referenciados-nos-grupos-de-Informa%C3%A7%C3%B5es-de-Pagamento-cujos-campos-de-C%C3%B3digo-de-Incid%C3%AAncia-de-IR
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30648390742295) Tempo aproximado para leitura: **00:02:00 min**  
  
**Ocorrência**  
Ao enviar o evento S-1210 ocorre o **Erro código 1955**: O somatório de todas as rubricas de todos os demonstrativos referenciados nos grupos de Informações de Pagamento, cujos campos de Código de Incidência de IR nos eventos de Rubrica iguais a 31, 32, 33 e 34 e tipo de rubrica iguais a 2 e 4, devera ser maior ou igual ao somatório do valor das rubricas cujo tipo de rubrica sejam iguais a 1 e 3.   
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - A partir das versões 12.1.2402.245; 12.1.2406.185; 12.1.2410.121 e Superiores.  
  
**Causa**  
Conforme mensagem de erro, a inconsistência é apresentada quando o somatório dos descontos e bases dedutoras (tipos de rubrica 2 e 4) cujo código de incidência de IRRF e com incidências 31, 32, 33 e 34 está menor que o somatório dos proventos e bases informativas (tipo rubrica 1 e 3).

![](https://centraldeatendimento.totvs.com/hc/article_attachments/30648390743191)

O erro é acompanhado do valor negativo e incidência que foi identificado, conforme demonstrado abaixo:

**Erro código 1955**: O somatório de todas as rubricas de todos os demonstrativos referenciados nos grupos de Informações de Pagamento, cujos campos de Código de Incidência de IR nos eventos de Rubrica iguais a 31, 32, 33 e 34 e tipo de rubrica iguais a 2 e 4, devera ser maior ou igual ao somatório do valor das rubricas cujo tipo de rubrica sejam iguais a 1 e 3. **Incidências identificadas com inconsistências: Incidência 33, somatório -12.21**. Ação Sugerida: Verifique o resultado do somatório conforme os códigos de incidência e tipo de rubrica informados acima.  
  
**Solução**

Para solucionar essa ocorrência, é necessário acessar o XML S-1200 do funcionário (RM e TAF), dos períodos referenciados no XML S-1210 e, verificar se, para cada verba relacionada, o tipo de rubrica presente no cadastro da verba do governo corresponde ao tipo da verba no RM (**provento no RM como vencimento no Governo; desconto no RM como desconto no Governo; etc.**). Se necessário, ajuste o tipo da verba no produto, reencaminhando o S-1010.

No exemplo abaixo, iremos identificar o valor, ou a soma dos valores que chegam em R$ 12,21:

1. Foi identificado no XML S-1210 os períodos 1 - 11/2024 e 3 - 11/2024;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/30648406645143)

2. No XML S-1200 dos períodos supracitados, foi identificado uma rubrica com o valor de R$ 12,21, ao conferir no envelope, esse evento constava como Base de Cálculo;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/30648390744215)

2.1. No eSocial a rubrica também consta como Base de Cálculo;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/30648406647831)

2.2. Ao conferir o Código de Cálculo do evento no RM, foi identificado que é o CC61. De acordo com as configurações de Código de Cálculo, para este código é necessário que o evento seja do tipo Desconto e Valor. Ou seja, o evento está cadastrado incorretamente no envelope e no governo;  
3. Para correção será necessário:

* Alterar a configuração no RM;
* Enviar ao governo o S-1010 com competência igual ou anterior a 11/2024;
* Regerar o XML S-1200.

Importante  
Em caso de férias, é necessário validar também os envelopes das Configurações 6/7 e 7/7 conforme abaixo:

* [RH - RM - FOP - eSocial - Parametrizador eSocial: Configurações Gerais 6/7](https://centraldeatendimento.totvs.com/hc/pt-br/articles/17203402479255-RH-RM-FOP-eSocial-Parametrizador-eSocial-Configura%C3%A7%C3%B5es-Gerais-6-7);
* [RH - RM - FOP - eSocial - Parametrizador eSocial: Configurações Gerais 7/7](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6805437378455-RH-RM-FOP-eSocial-Parametrizador-eSocial-Configura%C3%A7%C3%B5es-Gerais-7-7?source=search)
