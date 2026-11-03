---
article_id: 23284491550999
category: MDT - Atendimento Médico
content_hash: 5e52d3b77036abab5b127bc0dfbb884a743162faf950dc4432bdd624a2382730
fetched_at: '2026-06-28T22:44:20.534758+00:00'
product: protheus
section_id: 360010945694
source: central-protheus
title: 'RH - Linha Protheus - MDT - Ao tentar lançar data final do atestado é apresentado
  Erro de Predecessão: Não foi possível encontrar o registro predecessor'
type: support-article
updated_at: '2025-10-31T17:37:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23284491550999-RH-Linha-Protheus-MDT-Ao-tentar-lan%C3%A7ar-data-final-do-atestado-%C3%A9-apresentado-Erro-de-Predecess%C3%A3o-N%C3%A3o-foi-poss%C3%ADvel-encontrar-o-registro-predecessor
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23284491501847) Tempo aproximado para leitura: 00:02:00 min  
  
Ocorrência**Ao tentar lançar data final do atestado MDTA685 é apresentado Erro de Predecessão: Não foi possível encontrar o registro predecessor  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as Versões  
  
**Causa**O sistema tenta enviar ao SIGAGPE e SIGATAF a data final do afastamento, porem o inicio do afastamento não existe no TAF. isso pode ocorrer por problemas de integrações entre SIGAGPE x SIGATAF ou SIGAMDT x SIGAGPE:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23284480350743)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23284480353175)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23284491508375)  
  
**Solução  
1º** Validar se o afastamento foi lançado sem as integrações entre os módulos.

Valide se está desabilitado  os parâmetros **MV\_MDTGPE, MV\_NG2ESOC e MV\_RHTAF,** se sim será necessário refazer o atestado com os parâmetros habilitados.  
  
**2º**Validar se o afastamento está integrando com o GPE e com o campo de integração vazio:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23284491512983)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23284491516567)

**Obs:**Caso este campo esteja vazio, indica que a integração entre SIGAGPE x SIGATAF estava desabilitada.

Neste caso precisa ser refeito o atestado com a data inicial para integrar com o SIGATAF, habilitar os parâmetro **MV\_MDTGPE, MV\_NG2ESOC e MV\_RHTAF** caso estejam desabilitados e certifique-se que foi enviado ao **SIGATAF.**  
  
  
**Saiba Mais**  
[Artigos Atendimento Médico](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360010945694-MDT-Atendimento-M%C3%A9dico)  
[Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[ChatBot Carol](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022200991)
