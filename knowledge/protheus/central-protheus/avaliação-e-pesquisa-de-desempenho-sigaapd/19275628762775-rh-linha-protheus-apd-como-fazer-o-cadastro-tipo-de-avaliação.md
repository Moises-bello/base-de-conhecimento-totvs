---
article_id: 19275628762775
category: Avaliação e Pesquisa de Desempenho (SIGAAPD)
content_hash: b4cafdaf02f33ba2dfe5645d24bb0983d74c0da075ffece22d1d8ceefe833b76
fetched_at: '2026-06-28T22:42:53.800530+00:00'
product: protheus
section_id: 206956088
source: central-protheus
title: RH - Linha Protheus - APD - Como fazer o cadastro Tipo de Avaliação?
type: support-article
updated_at: '2023-11-23T14:10:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19275628762775-RH-Linha-Protheus-APD-Como-fazer-o-cadastro-Tipo-de-Avalia%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19275586715799) Tempo aproximado para leitura: **00:02:00 min****Dúvida**Como fazer o cadastro de Tipo de Avaliação?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Avaliação Pesquisa e Desempenho – Todas as versões  
  
**Solução**O cadastro Tipo de Avaliação é utilizado **para definir os tipos de avaliações e suas características principais**, permitindo configurar: **o tipo da avaliação** (avaliação ou pesquisa), **se o colaborador deve se identificar durante a avaliação**, **as redes de relacionamento**, **os níveis hierárquicos das redes**, **quantidade de participantes**, **permissão da autoavaliação do colaborador**, **possibilidade de um consenso final**, etc.  
  
Exemplos:

|  |  |
| --- | --- |
| • | Avaliação Up Down |

|  |  |
| --- | --- |
| • | Avaliação Down Up |

|  |  |
| --- | --- |
| • | Avaliação 360 Graus |

|  |  |
| --- | --- |
| • | Avaliação 180 Graus |

  
Cada avaliação de competência é vinculada a um tipo de avaliação que, por sua vez, é vinculada a uma rede de relacionamento. Essas avaliações são apresentadas no **Portal de Gestão do Capital Humano**, divididas em seções, cujos títulos são padrão do Sistema.  
  
Por exemplo:  
Visualização permitida ao Diretor:

|  |  |
| --- | --- |
| Seção | >> Minhas Avaliações |
| >> Minha Equipe |
| >> Pares |

  
Para permitir que esses títulos apresentem a descrição informada no Cadastro de Redes, deve-se configurar o **parâmetro [MV\_APDREDE](https://interno.totvs.com/mktfiles/tdiportais/helponlineprotheus/p12/portuguese/apda040_parametros.htm), que habilita a definição desses títulos.**  
  
Por exemplo:  
Suponha o Tipo de Avaliação 360° - Avaliação de competências profissionais, cuja rede vinculada seja Autoavaliação, Superiores e Cliente Interno.  
  
Essa rede é descrita no portal como os títulos das seções.  
Quando o parâmetro [MV\_APDREDE](https://interno.totvs.com/mktfiles/tdiportais/helponlineprotheus/p12/portuguese/apda040_parametros.htm) está configurado como .T. (true - verdadeiro), as seções no Portal apresentam como títulos, os itens informados no Cadastro de Redes:

|  |  |  |
| --- | --- | --- |
| Seção | Anterior (padrão) | Atual (Cadastro de Redes) |
| >> Minhas Avaliações | >> Autoavaliação |
| >> Minha Equipe | >> Superiores |
| >> Pares | >> Cliente Interno |

  
Caso contrário, se configurado como .F. (false - falso) ou " " (espaço em branco), as seções no Portal apresentam os títulos padrão do Sistema.

|  |
| --- |
| Help_buttonObservação:  O conteúdo padrão do parâmetro [MV\_APDREDE](https://interno.totvs.com/mktfiles/tdiportais/helponlineprotheus/p12/portuguese/apda040_parametros.htm) é F, que desabilita a apresentação da descrição da rede. |

**Para cadastrar habilidades acesse o módulo 53 - SIGAAPD > Clique no menu Atualizações > Cadastros > Tipo de Avaliação > Clique em Incluir e preencha os dados:  
![Tipos de Avaliação.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/19275639312535)**

**Saiba Mais**Para saber mais consulte os links abaixo:   
[CLIQUE AQUI para acessar mais artigos e FAQs sobre o Portal GCH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960887-RH-Portal-de-Gest%C3%A3o-de-Capital-Humano)
