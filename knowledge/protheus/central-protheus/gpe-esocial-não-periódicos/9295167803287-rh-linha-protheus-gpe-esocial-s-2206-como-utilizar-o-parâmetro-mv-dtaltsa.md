---
article_id: 9295167803287
category: GPE - eSocial - Não Periódicos
content_hash: 36e9baefce2d5dc8eb57858e13dfde3e7a52c88c61188b835e828c6646c5bd62
fetched_at: '2026-06-28T22:45:04.707066+00:00'
product: protheus
section_id: 360005445813
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-2206 - Como utilizar o parâmetro MV_DTALTSA
type: support-article
updated_at: '2023-08-22T16:43:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9295167803287-RH-Linha-Protheus-GPE-eSocial-S-2206-Como-utilizar-o-par%C3%A2metro-MV-DTALTSA
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16946380955415) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**Como utilizar o parâmetro c?  
  
**Ambiente**TOTVS RH - (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**O parâmetro foi criado para permitir definir se, ao gerar a tag **dtAlteracao** do evento **S-2206**, o sistema deve considerar a **data da alteração salarial** ou a **data base**.

Disponibilizado o parâmetro MV\_DTALTSA para que seja feita essa parametrização.

* .T. - Utiliza a data base (padrão)
* .F. - Utiliza a data da alteração salarial (R3\_DATA)

Abaixo informações técnicas sobre o parâmetro.

|  |  |
| --- | --- |
| **Tabela** | SX6 |
| **Nome** | MV\_DTALTSA |
| **Tipo** | Lógico |
| **Descrição** | Considera a database na Alteração Salarial (S-2206) |
| **Conteúdo** | .T. - Utiliza a database (padrão) |  .F. - Utiliza a data da alteração salarial(R3\_DATA) |

Exemplo de utilização do parâmetro **MV\_DTALTSA = .T.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/16945601847319)**Evento S-2206 no TAF **![](https://centraldeatendimento.totvs.com/hc/article_attachments/16945815517207)  
  
Atenção:** Com o parâmetro MV\_DTALTSA = .T. o evento S-2206 será integrado com a data base do Windows, deste modo, o ideal é que o [Job/Schedule](https://centraldeatendimento.totvs.com/hc/pt-br/articles/5220215589527-RH-Linha-Protheus-GPE-eSocial-S-2206-S-2230-Como-configurar-o-job-schedule-GPEM026B) seja executado na mesma data do calculo do Dissidio RetroativoExemplo de utilização do parâmetro **MV\_DTALTSA = .F.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/16945703308695)**Evento S-2206 no TAF **![](https://centraldeatendimento.totvs.com/hc/article_attachments/16945971100695)  
  
Atenção:** A data da alteração e a data efeito busca a informação do mesmo campo (R3\_DATA), deste modo, quando se tratar de alteração salarial a partir do calculo do Dissidio Retroativo, o ideal é que o parâmetro MV\_DTALTSA seja configurado = .T. Caso não encontre em seu banco de dados, será necessário atualizar o dicionário de acordo com o release.  
*Link* para baixar o pacote expedição continua RH: <https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/rh_expedicao_continua>  
  
  
**Saiba Mais**Para saber mais consulte os *links* abaixo:   
[Artigos S-2206](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360055237854)  
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica)
