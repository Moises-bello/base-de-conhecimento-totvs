---
article_id: 21511743751831
category: Originação de Grãos (OG)
content_hash: 782684b6c4495d6ab07eda9a0714663766a6d307515e16769a2cd9f114c0f8dd
fetched_at: '2026-06-28T22:45:45.145858+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Tabela Movimentação de Fardos - Atualizações
  do Compatibilizador
type: support-article
updated_at: '2025-07-16T13:11:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21511743751831-Agro-Linha-Protheus-AGR-Tabela-Movimenta%C3%A7%C3%A3o-de-Fardos-Atualiza%C3%A7%C3%B5es-do-Compatibilizador
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21511782496407) Tempo aproximado para leitura: **00:04:10 min****Dúvida**Para que serve as **Tabela Movimentação de Fardos**. Como realizar **Atualizações do Compatibilizador**?  
  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Solução**  
Para solucionar essa dúvida, realize os seguintes passos:

**1.** Faça a **Criação ou Alteração de** **Perguntas** no arquivo **SX1 – Cadastro de Perguntes**;

|  |  |
| --- | --- |
| **Pergunte** | *(X1\_PERGUNT)* |
| **Nome** |  |
| **Grupo** | *(X1\_GRUPO)* |
| **Ordem** | *(X1\_ORDEM)* |
| **Tipo** | *(X1\_TIPO)* |
| **Tamanho** | *(X1\_TAMANHO)* |

  

**2.** Realize a C**riação ou Alteração da tabela no arquivo** **SX2– Tabelas**;

|  |  |  |  |
| --- | --- | --- | --- |
| **Chave** | **Nome** | **Modo** | **PYME** |
| **N9D** | Movimentação de Fardos | E | N |
|  |  |  |  |

  
**3.** Faça a a **Criação ou Alteração das Tabelas Genéricas no arquivo** **SX5 – Tabelas Genéricas**;

|  |  |
| --- | --- |
| **Chave** | *K9* |
| **Descrição** | Tipo de movimentação de fardos |

**4.** Realize a **Criação ou Alteração dos Campos** no arquivo**SX3 – Campos****:**

* Tabela **N9D - Movimentação de Fardos**:

|  |  |
| --- | --- |
| **Campo** | *N9D\_FILIAL* |
| **Tipo** | *C* |
| **Tamanho** | *02* |
| **Decimal** | *(X3\_DECIMAL)* |
| **Formato** | *@!* |
| **Título** | *Filial* |
| **Descrição** | *Filial do Sistema* |
| **Nível** | *(X3\_NÍVEL)* |
| **Usado** | *Sim* |
| **Obrigatório** | *Não* |
| **Browse** | *Não* |
| **Opções** | *(X3\_CBOX)* |
| **When** | *(X3\_WHEN)* |
| **Relação** | *(X3\_RELACAO)* |
| **Val. Sistema** | *(X3\_VALID)* |
| **Help** | *Código que identifica a filial da empresa usuária do sistema.* |

|  |  |
| --- | --- |
| **Campo** | *N9D\_FARDO* |
| **Tipo** | *C* |
| Grupo | 033 |
| **Tamanho** | *06* |
| **Decimal** | *(X3\_DECIMAL)* |
| **Formato** | *@!* |
| **Título** | *Cod Fardo* |
| **Descrição** | *Código do Fardo* |
| **Nível** | *(X3\_NÍVEL)* |
| **Usado** | *Sim* |
| **Obrigatório** | *Sim* |
| **Browse** | *Sim* |
| **Opções** | *(X3\_CBOX)* |
| **When** | *(X3\_WHEN)* |
| **Relação** |  |
| **Val. Sistema** |  |
| **Help** | *Código identificador do fardo.* |

|  |  |
| --- | --- |
| **Campo** | *N9D\_TIPMOV* |
| **Tipo** | *C* |
| **Tamanho** | *2* |
| **Decimal** | *(X3\_DECIMAL)* |
| **Formato** | *@!* |
| **Título** | Tipo Mov |
| **Descrição** | *Tipo da Movimanetação* |
| **Nível** | *(X3\_NÍVEL)* |
| **Usado** | *Sim* |
| **Obrigatório** | *Sim* |
| **Browse** | *Sim* |
| **Opções** | *(X3\_CBOX)* |
| **When** | *(X3\_WHEN)* |
| **Relação** | *(X3\_RELAÇÃO)* |
| **Val. Sistema** | *(X3\_VALID)* |
| **Help** | *Tipo da Movimentação do Fardo* |

|  |  |
| --- | --- |
| **Campo** | *N9D\_IDMOV* |
| **Tipo** | *C* |
| **Tamanho** | *3* |
| **Decimal** | *(X3\_DECIMAL)* |
| **Formato** | *@!* |
| **Título** | ID Mov |
| **Descrição** | *Codigo Movimentação Fardo* |
| **Nível** | *(X3\_NÍVEL)* |
| **Usado** | *Sim* |
| **Obrigatório** | *Sim* |
| **Browse** | Não |
| **Opções** | *(X3\_CBOX)* |
| **When** | *(X3\_WHEN)* |
| **Relação** | *(X3\_RELAÇÃO)* |
| **Val. Sistema** | *(X3\_VALID)* |
| **Help** | Código sequencial de identificação da movimentação do fardo Código Sequencial da Movimentação Fardo |

|  |  |
| --- | --- |
| **Campo** | *N9D\_PESINI* |
| **Tipo** | *N* |
| **Tamanho** | *6* |
| **Decimal** | *2* |
| **Formato** | *@E 999.99* |
| **Título** | Peso Inicial |
| **Descrição** | *Peso Inicial do Fardo* |
| **Nível** | *(X3\_NÍVEL)* |
| **Usado** | *Sim* |
| **Obrigatório** | *Não* |
| **Browse** | Sim |
| **Opções** | *(X3\_CBOX)* |
| **When** | *(X3\_WHEN)* |
| **Relação** | *(X3\_RELAÇÃO)* |
| **Val. Sistema** | *Positivo()* |
| **Help** | Peso inicial do fardo na movimentação.  Peso antes de realizar a movimentação. |

|  |  |
| --- | --- |
| **Campo** | *N9D\_PESFIM* |
| **Tipo** | *N* |
| **Tamanho** | *6* |
| **Decimal** | *2* |
| **Formato** | *@E 999.99* |
| **Título** | Peso Final |
| **Descrição** | *Peso Final do Fardo* |
| **Nível** | *(X3\_NÍVEL)* |
| **Usado** | *Sim* |
| **Obrigatório** | *Não* |
| **Browse** | Sim |
| **Opções** | *(X3\_CBOX)* |
| **When** | *(X3\_WHEN)* |
| **Relação** | *(X3\_RELAÇÃO)* |
| **Val. Sistema** | *Positivo()* |
| **Help** | Peso final do fardo na movimentação.  Novo peso ajustado na movimentação. |

|  |  |
| --- | --- |
| **Campo** | *N9D\_PESDIF* |
| **Tipo** | *N* |
| **Tamanho** | *6* |
| **Decimal** | *2* |
| **Formato** | *@E 999.99* |
| **Título** | Dif. Peso |
| **Descrição** | *Diferença Peso* |
| **Nível** | *(X3\_NÍVEL)* |
| **Usado** | *Sim* |
| **Obrigatório** | *Nâo* |
| **Browse** | Sim |
| **Opções** | *(X3\_CBOX)* |
| **When** | *(X3\_WHEN)* |
| **Relação** | *(X3\_RELAÇÃO)* |
| **Val. Sistema** |  |
| **Help** | Valor da diferença de peso entre o peso inicial e final do fardo na movimentação. |

|  |  |
| --- | --- |
| **Campo** | *N9D\_LOCAL* |
| **Tipo** | *C* |
| **Tamanho** | *2* |
| **Decimal** | *0* |
| **Formato** | *@!* |
| **Título** | Local |
| **Descrição** | *Local/Armazem Fardo* |
| **Nível** | *(X3\_NÍVEL)* |
| **Usado** | *Sim* |
| **Obrigatório** | *Nâo* |
| **Browse** | Sim |
| **Opções** | *(X3\_CBOX)* |
| **When** | *(X3\_WHEN)* |
| **Relação** | *(X3\_RELAÇÃO)* |
| **Val. Sistema** |  |
| **Help** | Local/armazém de estoque do fardo |

|  |  |
| --- | --- |
| **Campo** | *N9D\_ENTLOC* |
| **Tipo** | *C* |
| Grupo | 001 |
| **Tamanho** | *6* |
| **Decimal** | *0* |
| **Formato** | *@!* |
| **Título** | Entidade Loc |
| **Descrição** | *Entidade do Local/Armazem* |
| **Nível** | *(X3\_NÍVEL)* |
| **Usado** | *Sim* |
| **Obrigatório** | *Nâo* |
| **Browse** | Sim |
| **Opções** | *(X3\_CBOX)* |
| **When** | *(X3\_WHEN)* |
| **Relação** | *(X3\_RELAÇÃO)* |
| **Val. Sistema** |  |
| **Help** | Código da Entidade do Local/Armazém do Fardo |

|  |  |
| --- | --- |
| **Campo** | *N9D\_LOJLOC* |
| **Tipo** | *C* |
| Grupo | 002 |
| **Tamanho** | *2* |
| **Decimal** | *0* |
| **Formato** | *@!* |
| **Título** | Loja Ent.Loc |
| **Descrição** | *Loja Entidade Local/Armaz* |
| **Nível** | *(X3\_NÍVEL)* |
| **Usado** | *Sim* |
| **Obrigatório** | *Nâo* |
| **Browse** | Sim |
| **Opções** | *(X3\_CBOX)* |
| **When** | *(X3\_WHEN)* |
| **Relação** | *(X3\_RELAÇÃO)* |
| **Val. Sistema** |  |
| **Help** | Loja do Local/Armazém de Estoque |

|  |  |
| --- | --- |
| **Campo** | *N9D\_DATA* |
| **Tipo** | *D* |
| **Tamanho** | *8* |
| **Decimal** | *0* |
| **Formato** |  |
| **Título** | Data Mov. |
| **Descrição** | *Data Movimentação* |
| **Nível** | *(X3\_NÍVEL)* |
| **Usado** | *Sim* |
| **Obrigatório** | *Nâo* |
| **Browse** | Sim |
| **Opções** | *(X3\_CBOX)* |
| **When** | *(X3\_WHEN)* |
| **Relação** | *(X3\_RELAÇÃO)* |
| **Val. Sistema** |  |
| **Help** | Data da Movimentação do Fardo |

|  |  |
| --- | --- |
| **Campo** | *N9D\_STATUS* |
| **Tipo** | *C* |
| **Tamanho** | *1* |
| **Decimal** | *(X3\_DECIMAL)* |
| **Formato** | *@!* |
| **Título** | *Status* |
| **Descrição** | *Status Movimentação* |
| **Nível** | *(X3\_NÍVEL)* |
| **Usado** | *Sim* |
| **Obrigatório** | *Não* |
| **Browse** | *Sim* |
| **Opções** | *(X3\_CBOX)* |
| **When** | *(X3\_WHEN)* |
| **Relação** | *(X3\_RELACAO)* |
| **Val. Sistema** | *Pertence("123")* |
| Ini. Padrâo | "2" |
| Cbox Port | 1=Previsto;2=Ativo;3=Inativo |
| **Help** | Status da Movimentação do Fardo  1=Previsto  2=Ativo  3=Inativo |

|  |  |
| --- | --- |
| **Campo** | *N9A\_CODROM* |
| **Tipo** | *C* |
| **Tamanho** | *10* |
| **Decimal** | *(X3\_DECIMAL)* |
| **Formato** | *@!* |
| **Título** | *Cod.Romaneio* |
| **Descrição** | *Codigo do Romaneio* |
| **Nível** | *(X3\_NÍVEL)* |
| **Usado** | *Sim* |
| **Obrigatório** | *Não* |
| **Browse** | *Sim* |
| **Opções** | *(X3\_CBOX)* |
| **When** | *(X3\_WHEN)* |
| **Relação** | *(X3\_RELACAO)* |
| **Val. Sistema** | *(X3\_VALID)* |
| **Help** | Codigo do Romaneio |

|  |  |
| --- | --- |
| **Campo** | N9D\_CODINE |
| **Tipo** | *C* |
| **Tamanho** | *30* |
| **Decimal** | *(X3\_DECIMAL)* |
| **Formato** | *@!* |
| **Título** | *Instr.Embarq* |
| **Descrição** | *Instrução de Embarque* |
| **Nível** | *(X3\_NÍVEL)* |
| **Usado** | *Sim* |
| **Obrigatório** | *Não* |
| **Browse** | *Sim* |
| **Opções** | *(X3\_CBOX)* |
| **When** | *(X3\_WHEN)* |
| **Relação** | *(X3\_RELACAO)* |
| **Val. Sistema** | *(X3\_VALID)* |
| **Help** | Código interno da instrução de embarque |

|  |  |
| --- | --- |
| **Campo** | *N9D\_CODCTR* |
| **Tipo** | *C* |
| **Tamanho** | *06* |
| **Decimal** | *(X3\_DECIMAL)* |
| **Formato** | *@!* |
| **Título** | *Contrato* |
| **Descrição** | *Codigo do Contrato* |
| **Nível** | *(X3\_NÍVEL)* |
| **Usado** | *Sim* |
| **Obrigatório** | *Não* |
| **Browse** | *Sim* |
| **Opções** | *(X3\_CBOX)* |
| **When** | *(X3\_WHEN)* |
| **Relação** | *(X3\_RELACAO)* |
| **Val. Sistema** | *(X3\_VALID)* |
| **Help** | Código do contrato |

|  |  |
| --- | --- |
| **Campo** | *N9D\_CODRES* |
| **Tipo** | *C* |
| **Tamanho** | *06* |
| **Decimal** | *(X3\_DECIMAL)* |
| **Formato** | *@!* |
| **Título** | *Reserva* |
| **Descrição** | *Codigo da Reserva* |
| **Nível** | *(X3\_NÍVEL)* |
| **Usado** | *Sim* |
| **Obrigatório** | *Não* |
| **Browse** | *Sim* |
| **Opções** | *(X3\_CBOX)* |
| **When** | *(X3\_WHEN)* |
| **Relação** | *(X3\_RELAÇÃO)* |
| **Val. Sistema** | *(X3\_VALID)* |
| **Help** | Codigo da Reserva do Contrato |

|  |  |
| --- | --- |
| **Campo** | *N9D\_ITERES* |
| **Tipo** | *C* |
| **Tamanho** | *02* |
| **Decimal** | *(X3\_DECIMAL)* |
| **Formato** | *@!* |
| **Título** | *Item Reserva* |
| **Descrição** | *Item da Reserva Contrato* |
| **Nível** | *(X3\_NÍVEL)* |
| **Usado** | *Sim* |
| **Obrigatório** | *Não* |
| **Browse** | *Sim* |
| **Opções** | *(X3\_CBOX)* |
| **When** | *(X3\_WHEN)* |
| **Relação** | *(X3\_RELAÇÃO)* |
| **Val. Sistema** | *(X3\_VALID)* |
| **Help** | Item da Reserva do Fardo |

|  |  |
| --- | --- |
| **Campo** | *N9D\_ITEREF* |
| **Tipo** | *C* |
| **Tamanho** | *03* |
| **Decimal** | *(X3\_DECIMAL)* |
| **Formato** | *@!* |
| **Título** | Item Reg.Fis |
| **Descrição** | *Item da Regra Fiscal* |
| **Nível** | *(X3\_NÍVEL)* |
| **Usado** | *Sim* |
| **Obrigatório** | Não |
| **Browse** | *Sim* |
| **Opções** | *(X3\_CBOX)* |
| **When** | *(X3\_WHEN)* |
| **Relação** | *(X3\_RELAÇÃO)* |
| **Val. Sistema** | *(X3\_VALID)* |
| **Help** | Item da Regra Fiscal do Item de Entrega do Contrato |

|  |  |
| --- | --- |
| **Campo** | *N9D\_ITEFIX* |
| **Tipo** | *C* |
| **Tamanho** | *03* |
| **Decimal** | *(X3\_DECIMAL)* |
| **Formato** | *@!* |
| **Título** | *Item fixação* |
| **Descrição** | *Item da Fixação Contrato* |
| **Nível** | *(X3\_NÍVEL)* |
| **Usado** | *Sim* |
| **Obrigatório** | *Não* |
| **Browse** | *Sim* |
| **Opções** | *(X3\_CBOX)* |
| **When** | *(X3\_WHEN)* |
| **Relação** |  |
| **Val. Sistema** | *(X3\_VALID)* |
| **Help** | Item da Fixação do Contrato |

|  |  |
| --- | --- |
| **Campo** | *N9D\_FILORG* |
| **Tipo** | *C* |
| Grupo | 033 |
| **Tamanho** | *02* |
| **Decimal** | *(X3\_DECIMAL)* |
| **Formato** | *@!* |
| **Título** | *Filial Orig* |
| **Descrição** | *Filial Origem Fardo* |
| **Nível** | *(X3\_NÍVEL)* |
| **Usado** | *Sim* |
| **Obrigatório** | *Não* |
| **Browse** | *Sim* |
| **Opções** | *(X3\_CBOX)* |
| **When** | *(X3\_WHEN)* |
| **Relação** |  |
| **Val. Sistema** | *. (X3\_VALID)* |
| **Help** | Filial de Origem do Fardo |

**Importante:**

O tamanho dos campos que possuem grupo pode variar conforme ambiente em uso.

**5.** Realize a **Criação ou Alteração de** **Consulta Padrão** no arquivo **SXB – Consulta Padrão**:

* Pesquisa **B05LS**:

|  |  |
| --- | --- |
| **Alias** | *(XB\_ALIAS)* |
| **Tipo** | *(XB\_TIPO)* |
| **Sequência** | *(XB\_SEQ)* |
| **Coluna** | *(XB\_COLUNA)* |
| **Descrição** | *(XB\_DESCRI)* |
| **Contém** | *(XB\_CONTEM)* |

  
**6.** Realize a Criação ou Alteração de **Índices** no arquivo **SIX – Índices**:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Índice** | **Ordem** | **Chave** | **Descrição** | **Proprietário** |
| N9D | 001 | N9D\_FILIAL+N9D\_FARDO+N9D\_TIPMOV+N9D\_IDMOV |  | S |

**7.** Faça a **Criação ou Alteração de Parâmetros** no arquivo **SX6 – Parâmetros**:

|  |  |
| --- | --- |
| **Nome da Variável** | *(X6\_VAR)* |
| **Tipo** | *(X6\_TIPO)* |
| **Descrição** | *(X6\_DESCRIC + X6\_DESC1 + X6\_DESC2)* |
| **Valor Padrão** | *(X6\_CONTEUD)* |

  
**8.** Realize a **Criação ou Alteração de** **Gatilhos** no arquivo **SX7 – Gatilhos**:

* Tabela **BD5 – Contas Médicas**:

|  |  |
| --- | --- |
| **Campo** | *Informe o conteúdo do (X7\_CAMPO)* |
| **Sequência** | *Informe o conteúdo do (X7\_SEQUENC)* |
| **Campo Domínio** | *Informe o conteúdo do (X7\_CDOMIN)* |
| **Tipo** | *Informe o conteúdo do (X7\_TIPO)* |
| **Regra** | *Informe o conteúdo do (X7\_REGRA)* |
| **Posiciona?** | *Informe o conteúdo do (X7\_SEEK)* |
| **Chave** | *Informe o conteúdo do (X7\_CHAVE)* |
| **Condição** | *Informe o conteúdo do (X7\_CONDIC)* |
| **Proprietário** | *Informe o conteúdo do (X7\_PROPRI)* |
