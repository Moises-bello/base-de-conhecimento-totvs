---
article_id: 1500002658202
category: Financeiro - Contas a Pagar
content_hash: 98ba475c8c5df707429912fc6d5d42afacf317c48de7e3886fab2d4e04df508d
fetched_at: '2026-06-28T22:38:07.292629+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINA050 - BANCO NÃO
  APARECE NA INCLUSÃO DO PA '
type: support-article
updated_at: '2022-09-13T18:47:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500002658202-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA050-BANCO-N%C3%83O-APARECE-NA-INCLUS%C3%83O-DO-PA
---

**Ocorrência**No módulo Financeiro, ao acessar a rotina de Contas a Pagar e incluir um PA, não habilita a opção de informações bancárias do titulo.   
  
**Ambiente**Microsiga Protheus - Financeiro - FNA050- A partir da versão 11.80  
  
**Causa**

1- Um dos motivos que ocorre este erro é referente ao rotina **Tipos de títulos (FINA015 - SIGAFIN)** podendo ter registros na tabela **SES** para tratamento dos tipos de títulos de Mercado Internacional (Outros países).

2-  Caso não seja a situação acima , esse incidente pode ocorrer também , pois a parametrização de validação do campo **E2\_TIPO** pode estar incorreta.

**Solução**

1- Realize o processo primeiramente base de homologação.  
Identificar se na **ES\_TIPORIG** contém o tipo PA inserido, desabilite o registro e inclua novamente o PA no Contas a Pagar.   
  
![KCS.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360101309294/KCS.png)

2 - Caso não seja a situação acima verifique a Validação do campo E2\_TIPO  
 A validação precisar estar desta forma - E2\_TIPO -> **FA050Tipo**() .and. **FA050Num**() .and. **FA050Natur**()

**Importante**Ações de análise de base, alterações, customizações ou treinamentos não fazem parte do nosso escopo de atendimento, sendo necessário ser avaliado pelo desenvolvedor responsável ou através de um analista in loco previamente agendado.

**Saiba mais:**[Utilizacao\_rotina\_tipos\_de\_titulos\_FINA015](https://tdn.totvs.com/display/public/PROT/FIN0004_Utilizacao_rotina_tipos_de_titulos_FINA015)  
[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA340 - HELP: NOTITSEL](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021352991-MP-SIGAFIN-FINA340-HELP-NOTITSEL)
