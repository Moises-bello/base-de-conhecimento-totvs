---
article_id: 21657550069015
category: Originação de Grãos (OG)
content_hash: 60de533b10b4ab3f6e509488a75877b744de7b84a53bd722cd4be0365bb59ff5
fetched_at: '2026-06-28T22:45:39.351536+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Dicionário de Dados em Ágio e Deságio
type: support-article
updated_at: '2025-04-07T20:25:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21657550069015-Agro-Linha-Protheus-AGR-Dicion%C3%A1rio-de-Dados-em-%C3%81gio-e-Des%C3%A1gio
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21657550022423) Tempo aproximado para leitura: **00:03:20 min****Dúvida**  
Como realizar uma criação de Tabelas do Dicionário de Dados em Ágio e Deságio?  
  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12.1.23  
  
**Solução**  
Para solucionar essa dúvida, realize os seguintes passos:

**1.** Realize a Criação ou Alteração de **Perguntas** no arquivo **SX1 – Cadastro de Perguntas;**

|  |  |
| --- | --- |
| **Pergunte** | *(X1\_PERGUNT)* |
| **Nome** |  |
| **Grupo** | *(X1\_GRUPO)* |
| **Ordem** | *(X1\_ORDEM)* |
| **Tipo** | *(X1\_TIPO)* |
| **Tamanho** | *(X1\_TAMANHO)* |

**2.** Realize a Criação de tabela no arquivo **SX2– Tabelas;**

|  |  |  |  |
| --- | --- | --- | --- |
| **Chave** | **Nome** | **modo** | **PIMÉ** |
| **N78** | Regras de Ágio e Deságio | E | S |

|  |  |  |  |
| --- | --- | --- | --- |
| **Chave** | **Nome** | **modo** | **PIMÉ** |
| **N7F** | Regra HVI Agio Desagio | E | S |

|  |  |  |  |
| --- | --- | --- | --- |
| **Chave** | **Nome** | **modo** | **PIMÉ** |
| **N7G** | Cor Tipo Classif. Ágio/Deságio | E | S |

**3.** Faça a Criação de Tabelas Genéricas no arquivo **SX5 – Tabelas Genéricas;**

|  |  |
| --- | --- |
| **Chave** | K8 |
| **Descrição** | Cor tipo de Classificação |

**4.** Verifique a Criação de **Campos** no arquivo **SX3 – Campos****:**

* Tabela NJR - Contrato de Venda.

|  |  |
| --- | --- |
| **Campo** | NJR\_TIPPON |
| **Tipo** | CARACTERÍSTICA |
| **Tamanho** | 1 |
| **Decimal** | 0 |
| **Formato** | @! |
| **Título** | Pontuação |
| **Descrição** | Pontuação |
| **Nível** | 1 |
| **Usado** | Sim |
| **Obrigatório** | Não |
| **Navegar** | Não |
| **Opções** | 1=Individual;2=Grupo |
| **Quando** | M->NJR\_TIPCAL > "1" |
| **Relação** | 1 |
| **Val. Sistema** | Persistência("12") |
| **Ajuda** | Informa o tipo de pontuação. 1=Individual;2=Grupo |

|  |  |
| --- | --- |
| **Campo** | NJR\_HVIPON |
| **Tipo** | CARACTERÍSTICA |
| **Tamanho** | *1* |
| **Decimal** | *0* |
| **Formato** | @! |
| **Título** | Pontuação |
| **Descrição** | Pontuação |
| **Nível** | *1* |
| **Usado** | Sim |
| **Obrigatório** | Não |
| **Navegar** | Não |
| **Opções** | 1=Individual;2=Grupo |
| **Quando** | M->NJR\_TIPCAL > "1" |
| **Relação** | 1 |
| **Val. Sistema** | Persistência("12") |
| **Ajuda** | Informa o tipo de pontuação. 1=Individual;2=Grupo |

|  |  |
| --- | --- |
| **Campo** | NJR\_OUTPON |
| **Tipo** | CARACTERÍSTICA |
| **Tamanho** | *1* |
| **Decimal** | *0* |
| **Formato** | @! |
| **Título** | Pontuação |
| **Descrição** | Pontuação |
| **Nível** | *1* |
| **Usado** | Sim |
| **Obrigatório** | Não |
| **Navegar** | Não |
| **Opções** | 1=Individual;2=Grupo |
| **Quando** | M->NJR\_TIPCAL > "1" |
| **Relação** | 1 |
| **Val. Sistema** | Persistência("12") |
| **Ajuda** | Informa o tipo de pontuação. 1=Individual;2=Grupo |

|  |  |
| --- | --- |
| **Campo** | NJR\_TIPUM |
| **Tipo** | CARACTERÍSTICA |
| **Tamanho** | *3* |
| **Decimal** | *0* |
| **Formato** | @! |
| **Título** | UM |
| **Descrição** | Unidade de Medida |
| **Nível** | *1* |
| **Usado** | Sim |
| **Obrigatório** | Não |
| **Navegar** | Não |
| **F3** | SAH |
| **Quando** | M->NJR\_TIPCAL > "1" |
| **Relação** | 1 |
| **Val. Sistema** | vazio() .ou. existeCpo("SAH") |
| **Ajuda** | Informa a Unidade de Medida. |

|  |  |
| --- | --- |
| **Campo** | NJR\_HVIUM |
| **Tipo** | CARACTERÍSTICA |
| **Tamanho** | *3* |
| **Decimal** | *0* |
| **Formato** | @! |
| **Título** | UM |
| **Descrição** | Unidade de Medida |
| **Nível** | *1* |
| **Usado** | Sim |
| **Obrigatório** | Não |
| **Navegar** | Não |
| **F3** | SAH |
| **Quando** | M->NJR\_TIPCAL > "1" |
| **Relação** | 1 |
| **Val. Sistema** | vazio() .ou. existeCpo("SAH") |
| **Ajuda** | Informa a Unidade de Medida. |

|  |  |
| --- | --- |
| **Campo** | NJR\_OUTUM |
| **Tipo** | CARACTERÍSTICA |
| **Tamanho** | *3* |
| **Decimal** | *0* |
| **Formato** | @! |
| **Título** | UM |
| **Descrição** | Unidade de Medida |
| **Nível** | *1* |
| **Usado** | Sim |
| **Obrigatório** | Não |
| **Navegar** | Não |
| **F3** | SAH |
| **Quando** | M->NJR\_TIPCAL > "1" |
| **Relação** | 1 |
| **Val. Sistema** | vazio() .ou. existeCpo("SAH") |
| **Ajuda** | Informa a Unidade de Medida. |

|  |  |
| --- | --- |
| **Campo** | NJR\_TIPCAL |
| **Tipo** | CARACTERÍSTICA |
| **Tamanho** | *1* |
| **Decimal** | *0* |
| **Formato** | @! |
| **Título** | Para. Cálculo |
| **Descrição** | Fórmula de Cálculo |
| **Nível** | *1* |
| **Usado** | Sim |
| **Obrigatório** | Não |
| **Navegar** | Não |
| **Opções** | 1=Nenhum;2=Valor;3=Porcentagem;4=Pontuação; . |
| **Relação** | 1 |
| **Val. Sistema** | Pertence("1234") .AND. OGA290VGE('NJR\_TIPCAL') |
| **Ajuda** | Informa a Fórmula de Cálculo 1=Nenhum;2=Valor;3=Percentagem;4=Pontuação; |

|  |  |
| --- | --- |
| **Campo** | NJR\_HVICAL |
| **Tipo** | CARACTERÍSTICA |
| **Tamanho** | *1* |
| **Decimal** | *0* |
| **Formato** | @! |
| **Título** | Para. Cálculo |
| **Descrição** | Fórmula de Cálculo |
| **Nível** | *1* |
| **Usado** | Sim |
| **Obrigatório** | Não |
| **Navegar** | Não |
| **Opções** | 1=Nenhum;2=Valor;3=Porcentagem;4=Pontuação; |
| **Relação** | 1 |
| **Val. Sistema** | Pertence("1234") .AND. OGA290VGE('NJR\_TIPCAL') |
| **Ajuda** | Informa a Fórmula de Cálculo 1=Nenhum;2=Valor;3=Percentagem;4=Pontuação; |

|  |  |
| --- | --- |
| **Campo** | NJR\_OUTCAL |
| **Tipo** | CARACTERÍSTICA |
| **Tamanho** | *1* |
| **Decimal** | *0* |
| **Formato** | @! |
| **Título** | Para. Cálculo |
| **Descrição** | Fórmula de Cálculo |
| **Nível** | *1* |
| **Usado** | Sim |
| **Obrigatório** | Não |
| **Navegar** | Não |
| **Opções** | 1=Nenhum;2=Valor;3=Porcentagem;4=Pontuação; |
| **Relação** | 1 |
| **Val. Sistema** | Pertence("1234") .AND. OGA290VGE('NJR\_TIPCAL') |
| **Ajuda** | Informa a Fórmula de Cálculo 1=Nenhum;2=Valor;3=Percentagem;4=Pontuação; |

|  |  |
| --- | --- |
| **Campo** | NJR\_TIPFAT |
| **Tipo** | NÚMERO |
| **Tamanho** | *12* |
| **Decimal** | *2* |
| **Formato** | @E 999.999.999,99 |
| **Título** | Fator |
| **Descrição** | Fator |
| **Nível** | *1* |
| **Usado** | Sim |
| **Obrigatório** | Não |
| **Navegar** | Não |
| **Quando** | M->NJR\_TIPCAL = "4" |
| **Relação** | 1 |
| **Val. Sistema** | Positivo() |
| **Ajuda** | Informa o Fator para cálculo. |

|  |  |
| --- | --- |
| **Campo** | NJR\_OUTFAT |
| **Tipo** | NÚMERO |
| **Tamanho** | *12* |
| **Decimal** | *2* |
| **Formato** | @E 999.999.999,99 |
| **Título** | Fator |
| **Descrição** | Fator |
| **Nível** | *1* |
| **Usado** | Sim |
| **Obrigatório** | Não |
| **Navegar** | Não |
| **Quando** | M->NJR\_TIPCAL = "4" |
| **Relação** | 1 |
| **Val. Sistema** | Positivo() |
| **Ajuda** | Informa o Fator para cálculo. |

|  |  |
| --- | --- |
| **Campo** | NJR\_HVIFAT |
| **Tipo** | NÚMERO |
| **Tamanho** | *12* |
| **Decimal** | *2* |
| **Formato** | @E 999.999.999,99 |
| **Título** | Fator |
| **Descrição** | Fator |
| **Nível** | *1* |
| **Usado** | Sim |
| **Obrigatório** | Não |
| **Navegar** | Não |
| **Quando** | M->NJR\_TIPCAL = "4" |
| **Relação** | 1 |
| **Val. Sistema** | Positivo() |
| **Ajuda** | Informa o Fator para cálculo. |

|  |  |
| --- | --- |
| **Campo** | NJR\_OUTTOL |
| **Tipo** | NÚMERO |
| **Tamanho** | *3* |
| **Decimal** | *0* |
| **Formato** | @E 999 |
| **Título** | Tolerância |
| **Descrição** | Tolerância Ágio e Deságio |
| **Nível** | *1* |
| **Usado** | Sim |
| **Obrigatório** | Não |
| **Navegar** | Não |
| **Quando** | M->NJR\_OUTCAL > "1" |
| **Relação** | 1 |
| **Val. Sistema** | Positivo() |
| **Ajuda** | Informa a Tolerância de Ágio e Deságio. |

|  |  |
| --- | --- |
| **Campo** | NJR\_TIPTOL |
| **Tipo** | NÚMERO |
| **Tamanho** | *3* |
| **Decimal** | *0* |
| **Formato** | @E 999 |
| **Título** | Tolerância |
| **Descrição** | Tolerância Ágio e Deságio |
| **Nível** | *1* |
| **Usado** | Sim |
| **Obrigatório** | Não |
| **Navegar** | Não |
| **Quando** | M->NJR\_OUTCAL > "1" |
| **Relação** | 1 |
| **Val. Sistema** | Positivo() |
| **Ajuda** | Informa a Tolerância de Ágio e Deságio. |

|  |  |
| --- | --- |
| **Campo** | NJR\_HVITOL |
| **Tipo** | NÚMERO |
| **Tamanho** | *3* |
| **Decimal** | *0* |
| **Formato** | @E 999 |
| **Título** | Tolerância |
| **Descrição** | Tolerância Ágio e Deságio |
| **Nível** | *1* |
| **Usado** | Sim |
| **Obrigatório** | Não |
| **Navegar** | Não |
| **Quando** | M->NJR\_OUTCAL > "1" |
| **Relação** | 1 |
| **Val. Sistema** | Positivo() |
| **Ajuda** | Informa a Tolerância de Ágio e Deságio. |

|  |  |
| --- | --- |
| **Campo** | NJR\_TIPGRU |
| **Tipo** | NÚMERO |
| **Tamanho** | *12* |
| **Decimal** | *2* |
| **Formato** | @E 999.999.999,99 |
| **Título** | P.Grupo |
| **Descrição** | Pontos por Grupo |
| **Nível** | *1* |
| **Usado** | Sim |
| **Obrigatório** | Não |
| **Navegar** | Não |
| **Quando** | M->NJR\_TIPCAL> "1" .AND. M->NJR\_TIPPON = "2" |
| **Relação** | 1 |
| **Val. Sistema** | Positivo() |
| **Ajuda** | Informações dos Pontos por Grupo. |

|  |  |
| --- | --- |
| **Campo** | NJR\_HVIGRU |
| **Tipo** | NÚMERO |
| **Tamanho** | *12* |
| **Decimal** | *2* |
| **Formato** | @E 999.999.999,99 |
| **Título** | P.Grupo |
| **Descrição** | Pontos por Grupo |
| **Nível** | *1* |
| **Usado** | Sim |
| **Obrigatório** | Não |
| **Navegar** | Não |
| **Quando** | M->NJR\_TIPCAL> "1" .AND. M->NJR\_TIPPON = "2" |
| **Relação** | 1 |
| **Val. Sistema** | Positivo() |
| **Ajuda** | Informações dos Pontos por Grupo. |

|  |  |
| --- | --- |
| **Campo** | NJR\_OUTGRU |
| **Tipo** | NÚMERO |
| **Tamanho** | *12* |
| **Decimal** | *2* |
| **Formato** | @E 999.999.999,99 |
| **Título** | P.Grupo |
| **Descrição** | Pontos por Grupo |
| **Nível** | *1* |
| **Usado** | Sim |
| **Obrigatório** | Não |
| **Navegar** | Não |
| **Quando** | M->NJR\_TIPCAL> "1" .AND. M->NJR\_TIPPON = "2" |
| **Relação** | 1 |
| **Val. Sistema** | Positivo() |
| **Ajuda** | Informações dos Pontos por Grupo. |

**5.** Observe a Tabela N78 - Regras do Ágio e Deságio;

|  |  |
| --- | --- |
| **Campo** | N78\_FILIAL |
| **Tipo** | CARACTERÍSTICA |
| **Tamanho** | *2* |
| **Decimal** | *0* |
| **Formato** | @! |
| **Título** | Filial |
| **Descrição** | Filial do Sistema |
| **Nível** | *1* |
| **Usado** | Não |
| **Obrigatório** | Não |
| **Navegar** | Não |
| **Ajuda** | Filial do Sistema |

|  |  |
| --- | --- |
| **Campo** | N78\_CODCTR |
| **Tipo** | CARACTERÍSTICA |
| **Tamanho** | *6* |
| **Decimal** | *0* |
| **Formato** | @! |
| **Título** | Bacalhau. Contrato |
| **Descrição** | Código do Contrato |
| **Nível** | *1* |
| **Usado** | Sim |
| **Obrigatório** | Sim |
| **Navegar** | Não |
| **Val. Sistema** | ExistCpo('NJR') |
| **Ajuda** | Informa o código do contrato. |

|  |  |
| --- | --- |
| **Campo** | N78\_APLICA |
| **Tipo** | CARACTERÍSTICA |
| **Tamanho** | *1* |
| **Decimal** | *2* |
| **Formato** | @! |
| **Título** | Aplicação |
| **Descrição** | Tipo de aplicação |
| **Nível** | *1* |
| **Usado** | Sim |
| **Obrigatório** | Sim |
| **Navegar** | Não |
| **Opções** | 1=Tipo/Cor;2=IVS;3=Outros; |
| **Val. Sistema** | Persistência("123") |
| **Ajuda** | Informações sobre o tipo de aplicação.  1 = Tipo/Cor;  2 = IVS;  3 = Outros. |

|  |  |
| --- | --- |
| **Campo** | N78\_SEQUEM |
| **Tipo** | CARACTERÍSTICA |
| **Tamanho** | *4* |
| **Decimal** | *0* |
| **Formato** | @! |
| **Título** | Sequencial |
| **Descrição** | Sequencial |
| **Nível** | *1* |
| **Usado** | Sim |
| **Obrigatório** | Sim |
| **Navegar** | Não |
| **Ajuda** | Informa o sequencial do tipo de aplicação. |

|  |  |
| --- | --- |
| **Campo** | N78\_TCRTIP |
| **Tipo** | CARACTERÍSTICA |
| **Tamanho** | *2* |
| **Decimal** | *0* |
| **Formato** | @! |
| **Título** | Tipo |
| **Descrição** | Tipo de algodão |
| **Nível** | *1* |
| **Usado** | Sim |
| **Obrigatório** | Não |
| **Navegar** | Não |
| **F3** | DXAN78 |
| **Ajuda** | Informa o tipo de classificação do algodão. |

|  |  |
| --- | --- |
| **Campo** | N78\_TCRFOL |
| **Tipo** | CARACTERÍSTICA |
| **Tamanho** | *1* |
| **Decimal** | *0* |
| **Formato** | @! |
| **Título** | Tipo |
| **Descrição** | Tipo de algodão |
| **Nível** | *1* |
| **Usado** | Sim |
| **Obrigatório** | Não |
| **Navegar** | Não |
| **Val. Sistema** | Persistência("12345678") |
| **Ajuda** | Informa a folha do tipo de classificação do algodão. |

|  |  |
| --- | --- |
| **Campo** | N78\_TCRPON |
| **Tipo** | NÚMERO |
| **Tamanho** | *12* |
| **Decimal** | *2* |
| **Formato** | @E 999.999.999,99 |
| **Título** | Vlr. Cálculo |
| **Descrição** | Valor do Cálculo |
| **Nível** | *1* |
| **Usado** | Sim |
| **Obrigatório** | Não |
| **Navegar** | Sim |
| **Ajuda** | Informa o valor para cálculo de ágio e deságio.  Esse campo poderá ser por valor, pontuação ou porcentagem. |

|  |  |
| --- | --- |
| **Campo** | N78\_TCRTOL |
| **Tipo** | NÚMERO |
| **Tamanho** | *3* |
| **Decimal** | *0* |
| **Formato** | @E 999 |
| **Título** | Tolerância |
| **Descrição** | Tolerância de Ágio e Deságio |
| **Nível** | *1* |
| **Usado** | Sim |
| **Obrigatório** | Não |
| **Navegar** | Sim |
| **Val. Sistema** | Positivo() |
| **Ajuda** | Informa o percentual de tolerância para o cálculo do ágio e deságio. |

|  |  |
| --- | --- |
| **Campo** | N78\_HVIDES |
| **Tipo** | CARACTERÍSTICA |
| **Tamanho** | *20* |
| **Decimal** | *0* |
| **Formato** | @! |
| **Título** | Exame HVI |
| **Descrição** | Descrição Exame HVI |
| **Nível** | *1* |
| **Usado** | Sim |
| **Obrigatório** | Não |
| **Navegar** | Sim |
| **Ajuda** | Informa a descrição do exame de IVS do algodão. |

|  |  |
| --- | --- |
| **Campo** | N78\_HVIFDE |
| **Tipo** | NÚMERO |
| **Tamanho** | *3* |
| **Decimal** | *0* |
| **Formato** | @E 999 |
| **Título** | Faixa Inicial |
| **Descrição** | Faixa Inicial |
| **Nível** | *1* |
| **Usado** | Sim |
| **Obrigatório** | Não |
| **Navegar** | Sim |
| **Ajuda** | Informar a faixa inicial para tratar incidentes. |

|  |  |
| --- | --- |
| **Campo** | N78\_HVIFAT |
| **Tipo** | NÚMERO |
| **Tamanho** | *3* |
| **Decimal** | *0* |
| **Formato** | @E 999 |
| **Título** | Faixa Fim |
| **Descrição** | Final da Faixa |
| **Nível** | *1* |
| **Usado** | Sim |
| **Obrigatório** | Não |
| **Navegar** | Sim |
| **Ajuda** | Informa a faixa final para tratar desconto. |

|  |  |
| --- | --- |
| **Campo** | N78\_HVIPON |
| **Tipo** | NÚMERO |
| **Tamanho** | *12* |
| **Decimal** | *2* |
| **Formato** | @E 999.999.999,99 |
| **Título** | Vlr. Cálculo |
| **Descrição** | Valor do Cálculo |
| **Nível** | *1* |
| **Usado** | Sim |
| **Obrigatório** | Não |
| **Navegar** | Sim |
| **Ajuda** | Informa o valor para cálculo de ágio e deságio.  Esse campo poderá ser por valor, pontuação ou porcentagem. |

|  |  |
| --- | --- |
| **Campo** | N78\_HVIREG |
| **Tipo** | CARACTERÍSTICA |
| **Tamanho** | *3* |
| **Decimal** | *0* |
| **Formato** | @! |
| **Título** | Regra HVI |
| **Descrição** | Regra do Exame HVI |
| **Nível** | *1* |
| **Usado** | Sim |
| **Obrigatório** | Não |
| **Navegar** | Sim |
| **Ajuda** | Informa a regra para o cálculo de ágio e deságio. |

|  |  |
| --- | --- |
| **Campo** | N78\_HVITOL |
| **Tipo** | NÚMERO |
| **Tamanho** | *3* |
| **Decimal** | *0* |
| **Formato** | @E 999 |
| **Título** | Tolerância |
| **Descrição** | Tolerância Ágio e Deságio |
| **Nível** | *1* |
| **Usado** | Sim |
| **Obrigatório** | Não |
| **Navegar** | Sim |
| **Val. Sistema** | Positivo() |
| **Ajuda** | Informa o percentual de tolerância para o cálculo do ágio e deságio. |

|  |  |
| --- | --- |
| **Campo** | N78\_OUTDES |
| **Tipo** | CARACTERÍSTICA |
| **Tamanho** | *20* |
| **Decimal** | *0* |
| **Formato** | @! |
| **Título** | Descrição |
| **Descrição** | Descrição do Ágio/Deságio |
| **Nível** | *1* |
| **Usado** | Sim |
| **Obrigatório** | Não |
| **Navegar** | Sim |
| **Ajuda** | Informa a descrição do ágio ou deságio.  Campo livre para descrição. |

|  |  |
| --- | --- |
| **Campo** | N78\_OUTPON |
| **Tipo** | NÚMERO |
| **Tamanho** | *12* |
| **Decimal** | *2* |
| **Formato** | @E 999.999.999,99 |
| **Título** | Vlr. Cálculo |
| **Descrição** | Valor do Cálculo |
| **Nível** | *1* |
| **Usado** | Sim |
| **Obrigatório** | Não |
| **Navegar** | Sim |
| **Ajuda** | Informa o valor para cálculo de ágio e deságio.  Esse campo poderá ser por valor, pontuação ou porcentagem. |

|  |  |
| --- | --- |
| **Campo** | N78\_OUTREG |
| **Tipo** | CARACTERÍSTICA |
| **Tamanho** | *3* |
| **Decimal** | *0* |
| **Formato** | @! |
| **Título** | Regra |
| **Descrição** | Regra de Aplicação |
| **Nível** | *1* |
| **Usado** | Sim |
| **Obrigatório** | Não |
| **Navegar** | Sim |
| **Ajuda** | Informa a regra para o cálculo de ágio e deságio. |

**6.** Observe a Tabela N7F - Regra HVI Ágio Deságio;

|  |  |
| --- | --- |
| **Campo** | N7F\_FILIAL |
| **Tipo** | CARACTERÍSTICA |
| **Tamanho** | *8* |
| **Decimal** | *0* |
| **Formato** | @! |
| **Título** | Filial |
| **Descrição** | Filial |
| **Nível** | *1* |
| **Usado** | Não |
| **Obrigatório** | Não |
| **Navegar** | Não |
| **Ajuda** | Filial |

|  |  |
| --- | --- |
| **Campo** | N7F\_CODCTR |
| **Tipo** | CARACTERÍSTICA |
| **Tamanho** | *6* |
| **Decimal** | *0* |
| **Formato** | @! |
| **Título** | Bacalhau. Contrato |
| **Descrição** | Código do Contrato |
| **Nível** | *1* |
| **Usado** | Sim |
| **Obrigatório** | Sim |
| **Navegar** | Não |
| **Ajuda** | Informa o Código do Contrato. |

|  |  |
| --- | --- |
| **Campo** | N7F\_ITEM |
| **Tipo** | CARACTERÍSTICA |
| **Tamanho** | *3* |
| **Decimal** | *0* |
| **Formato** | @! |
| **Título** | Item |
| **Descrição** | Item |
| **Nível** | *1* |
| **Usado** | Sim |
| **Obrigatório** | Sim |
| **Navegar** | Sim |
| **Ajuda** | Informação do Item. |

|  |  |
| --- | --- |
| **Campo** | N7F\_CAMPO |
| **Tipo** | CARACTERÍSTICA |
| **Tamanho** | *10* |
| **Decimal** | *0* |
| **Formato** | @! |
| **Título** | Campo HVI |
| **Descrição** | Campo do Layout HVI |
| **Nível** | *1* |
| **Usado** | Sim |
| **Obrigatório** | Sim |
| **Navegar** | Sim |
| **F3** | SX3DX7 |
| **Val. Sistema** | ExistCpo( 'SX3', M->N7F\_CAMPO , 2 ) |
| **Ajuda** | Informa o Campo do Layout HVI. |

|  |  |
| --- | --- |
| **Campo** | N7F\_HVIDES |
| **Tipo** | CARACTERÍSTICA |
| **Tamanho** | *20* |
| **Decimal** | *0* |
| **Formato** | @! |
| **Título** | Descrição HVI |
| **Descrição** | Descrição HVI |
| **Nível** | *1* |
| **Usado** | Sim |
| **Obrigatório** | Não |
| **Navegar** | Sim |
| **Relação** | iif (Inclui,' ',AGRTITULO(N7F->N7F\_CAMPO) ) |
| **F3** | SX3DX7 |
| **Val. Sistema** | ExistCpo( 'SX3', M->N7F\_CAMPO , 2 ) |
| **Ajuda** | Informa a Descrição HVI. |

|  |  |
| --- | --- |
| **Campo** | N7F\_VLRINI |
| **Tipo** | CARACTERÍSTICA |
| **Tamanho** | *6* |
| **Decimal** | *0* |
| **Formato** |  |
| **Título** | De |
| **Descrição** | Valor Inicial |
| **Nível** | *1* |
| **Usado** | Sim |
| **Obrigatório** | Não |
| **Navegar** | Sim |
| **Ajuda** | Informação o Valor Inicial. |

|  |  |
| --- | --- |
| **Campo** | N7F\_VLRFIM |
| **Tipo** | CARACTERÍSTICA |
| **Tamanho** | *6* |
| **Decimal** | *0* |
| **Formato** | @! |
| **Título** | Comeu |
| **Descrição** | Valor Final |
| **Nível** | *1* |
| **Usado** | Sim |
| **Obrigatório** | Não |
| **Navegar** | Sim |
| **Ajuda** | Informação o Valor Final. |

|  |  |
| --- | --- |
| **Campo** | N7F\_REGRA |
| **Tipo** | CARACTERÍSTICA |
| **Tamanho** | *1* |
| **Decimal** | *0* |
| **Formato** | @! |
| **Título** | Regra |
| **Descrição** | Regra para Aplicação |
| **Nível** | *1* |
| **Usado** | Sim |
| **Obrigatório** | Não |
| **Navegar** | Sim |
| **Relação** | 1=E;2=OU |
| **Ajuda** | Informa a Regra de Aplicação. |

**7.** Observe a Tabela N7G - Cor Tipo Classif. Ágio/Deságio

|  |  |
| --- | --- |
| **Campo** | N7G\_FILIAL |
| **Tipo** | CARACTERÍSTICA |
| **Tamanho** | *1* |
| **Decimal** | *0* |
| **Formato** | @! |
| **Título** | Filial |
| **Descrição** | Filial do Sistema |
| **Nível** | *1* |
| **Usado** | Sim |
| **Obrigatório** | Não |
| **Navegar** | Não |
| **Ajuda** | Filial do Sistema |

|  |  |
| --- | --- |
| **Campo** | N7G\_CODCTR |
| **Tipo** | CARACTERÍSTICA |
| **Tamanho** | *6* |
| **Decimal** | *0* |
| **Formato** | @! |
| **Título** | Contrato |
| **Descrição** | Contrato |
| **Nível** | *1* |
| **Usado** | Sim |
| **Obrigatório** | Não |
| **Navegar** | Não |
| **Val.Sistema** | ExistCpo('NJR') |
| **Ajuda** | Informa o contrato que se refere aos núcleos do agio/desagio. |

|  |  |
| --- | --- |
| **Campo** | N7G\_CODCOR |
| **Tipo** | CARACTERÍSTICA |
| **Tamanho** | *1* |
| **Decimal** | *0* |
| **Formato** | @! |
| **Título** | Bacalhau. Cor |
| **Descrição** | Código da Cor |
| **Nível** | *1* |
| **Usado** | Sim |
| **Obrigatório** | Não |
| **Navegar** | Sim |
| **F3** | SX5 |
| **Val.Sistema** | Existchav('N7G').AND.ExistCpo("SX5","K8"+M->N7G\_CODCOR) |
| **Ajuda** | Informa o código de cor para ágio/deságio do contrato. |

|  |  |
| --- | --- |
| **Campo** | N7G\_DESCOR |
| **Tipo** | CARACTERÍSTICA |
| **Tamanho** | *30* |
| **Decimal** | *0* |
| **Formato** | @! |
| **Título** | Desc. Cor |
| **Descrição** | Descrição da Cor |
| **Nível** | *1* |
| **Usado** | Sim |
| **Obrigatório** | Não |
| **Navegar** | Sim |
| **Relação** | If(! INCLUI, Posicione( "SX5", 1, xFilial( "SX5" ) + "K8" + N7G->N7G\_CODCOR, "X5\_DESCRI" ), ' ') |
| **F3** | SX5 |
| **Val.Sistema** | Existchav('N7G').AND.ExistCpo("SX5","K8"+M->N7G\_CODCOR) |
| **Ajuda** | Informa a descrição do cor do tipo de classificação selecionada. |

|  |  |
| --- | --- |
| **Campo** | N7G\_PONTUA |
| **Tipo** | NÚMERO |
| **Tamanho** | *12* |
| **Decimal** | *2* |
| **Formato** | @E 999.999.999,99 |
| **Título** | Vlr. Cálculo |
| **Descrição** | Valor de Cálculo |
| **Nível** | *1* |
| **Usado** | Sim |
| **Obrigatório** | Não |
| **Navegar** | Sim |
| **Ajuda** | Informa o valor para cálculo do ágio/deságio sobre o tipo de cor informado. |

**Importante:**

**O tamanho dos campos que possuem grupo pode variar de acordo com o ambiente de uso.****8.** Veja a Criação   de **Consulta Padrão** no arquivo **SXB – Consulta Padrão;**

* Pesquisa DXAN78:

|  |  |
| --- | --- |
| **Alias** | DXA |
| **Tipo** | 5 |
| **Sequência** | 01 |
| **Coluna** | 01 |
| **Descrição** | CÓDIGO |
| **Contém** | DXA\_CODIGO |

**9.** Verifique a *Criação*  de **Índices** no arquivo **SIX – Índices;**

|  |  |
| --- | --- |
| **Índice** | N78 |
| **Ordem** | 1 |
| **Chave** | N78\_FILIAL+N78\_CODCTR+N78\_APLICA+N78\_SEQUEN |
| **Descrição** | Cód.contrato + Aplicação + Sequencial |
| **Proprietário** | S |

|  |  |
| --- | --- |
| **Índice** | N7F |
| **Ordem** | 1 |
| **Chave** | N7F\_FILIAL+N7F\_CODCTR+N7F\_ITEM |
| **Descrição** | Código Contrato + Item |
| **Proprietário** | S |

|  |  |
| --- | --- |
| **Índice** | N7G |
| **Ordem** | 1 |
| **Chave** | N7G\_FILIAL+N7G\_CODCTR+N7G\_CODCOR |
| **Descrição** | Contrato + Código Cor |
| **Proprietário** | S |

**10.** Veja a Criação de **Parâmetros** no arquivo **SX6 – Parâmetros;**

|  |  |
| --- | --- |
| **Nome da Variável** | MV\_AGRO005 |
| **Tipo** | Lógico |
| **Descrição** | Utilize Ágio Deságio |
| **Valor Padrão** | *.*T. *\_* |

**11.** Verifique e realize a Criação de **Gatilhos** no arquivo **SX7 – Gatilhos.**

* Tabela N7F ***– Regra HVI Ágio Deságio*** :

|  |  |
| --- | --- |
| **Campo** | N7F\_CAMPO |
| **Sequência** | 001 |
| **Campo Domínio** | N7F\_HVIDES |
| **Tipo** | X |
| **Regra** | AGRTITULO(M->N7F\_CAMPO) |
| **Posição?** | N |
| **Proprietário** | S |

* Tabela N7G ***– Cor Tipo Classif. Ágio/Deságio*** :

|  |  |
| --- | --- |
| **Campo** | N7G\_CODCOR |
| **Sequência** | 001 |
| **Campo Domínio** | N7G\_DESCOR |
| **Tipo** | P |
| **Regra** | SX5->X5\_DESCRI |
| **Posição?** | N |
| **Chave** | xFilial("SX5")+ "K8" + M->N7G\_CODCOR |
| **Proprietário** | S |
