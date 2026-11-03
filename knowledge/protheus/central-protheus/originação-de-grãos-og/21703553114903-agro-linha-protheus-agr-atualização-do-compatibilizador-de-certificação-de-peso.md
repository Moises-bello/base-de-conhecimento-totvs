---
article_id: 21703553114903
category: Originação de Grãos (OG)
content_hash: 64543b259b2767a9f5165a08a0e886a8b86a56e4da7d3f136c99925b2a616c24
fetched_at: '2026-06-28T22:45:37.371710+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Atualização do Compatibilizador de Certificação
  de Peso
type: support-article
updated_at: '2025-06-25T12:46:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21703553114903-Agro-Linha-Protheus-AGR-Atualiza%C3%A7%C3%A3o-do-Compatibilizador-de-Certifica%C3%A7%C3%A3o-de-Peso
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21703538343319) Tempo aproximado para leitura: **00:03:35 min****Dúvida**  
Procedimento para realizar atualização do **Compatibilizador** em **Certificação de Peso**?  
  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12.1.23  
  
**Solução**  
Para solucionar essa dúvida, realize os seguinte passo:

**1.** Faça a **Criação ou Alteração de** **Perguntas** no arquivo **SX1 – Cadastro de Perguntes;**

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Pergunte** | **Nome** | **Grupo** | **Ordem** | **Tipo** | **Tamanho** |
| Arquivo de Modelo <ENTER> ? | *Arquivo de Modelo <ENTER> ?* | OGAR730 | 01 | C | 99 |
| Arquivo de Destino <ENTER> ? | *Arquivo de Destino <ENTER> ?* | OGAR730 | 02 | C | 99 |

**2.** Realize a **Criação de tabela** no arquivo **SX2– Tabelas;**

|  |  |  |  |
| --- | --- | --- | --- |
| **Chave** | **Nome** | **Modo** | **PYME** |
| **N91** | Contêineres da IE | C | N |
| **N98** | Processos de Aprovação | C | N |
| **N99** | Aprovadores do Processo | C | N |

**3.** Criação de Tabelas Genéricas no arquivo **SX5** – Tabelas Genéricas;

|  |  |
| --- | --- |
| **Chave** | K8 |
| **Descrição** | *Processos de Aprovação* |

**4.** Faça a Criação de **Campos** no arquivo **SX3 – Campos;**

* Tabela NJJ - Romaneios:

|  |  |
| --- | --- |
| **Campo** | NJJ\_DATCHE |
| **Tipo** | D |
| **Tamanho** | 8 |
| **Decimal** | 0 |
| **Formato** | @! |
| **Título** | Data Chegada |
| **Descrição** | Data de Chegada |
| **Nível** | 1 |
| **Usado** | Sim |
| **Obrigatório** | Não |
| **Browse** | Sim |
| **Opções** |  |
| **When** |  |
| **Relação** | ddatabase |
| **Val. Sistema** |  |
| **Help** | Data de Chegada do fardo no destino |

|  |  |
| --- | --- |
| **Campo** | NJJ\_HORCHE |
| **Tipo** | C |
| **Tamanho** | 5 |
| **Decimal** | 0 |
| **Formato** | 99:99 |
| **Título** | Hora Chegada |
| **Descrição** | Hora de chegada |
| **Nível** | 1 |
| **Usado** | Sim |
| **Obrigatório** | Não |
| **Browse** | Sim |
| **Opções** |  |
| **When** |  |
| **Relação** |  |
| **Val. Sistema** |  |
| **Help** | Horário de Chegada no destino |

* Tabela **DXI** - Fardos de algodão em pluma:

|  |  |
| --- | --- |
| **Campo** | DXI\_PESSAI |
| **Tipo** | N |
| **Tamanho** | 6 |
| **Decimal** | 2 |
| **Formato** | @E 999.99 |
| **Título** | Peso Saida |
| **Descrição** | Peso de Saida do Fardo |
| **Nível** |  |
| **Usado** | Sim |
| **Obrigatório** | Não |
| **Browse** | Sim |
| **Opções** |  |
| **When** |  |
| **Relação** |  |
| **Val. Sistema** |  |
| **Help** | Peso de Saida do fardo |

|  |  |
| --- | --- |
| **Campo** | DXI\_PESCHE |
| **Tipo** | N |
| **Tamanho** | 6 |
| **Decimal** | 2 |
| **Formato** | @E 999.99 |
| **Título** | Peso Chegada |
| **Descrição** | Peso de Chegada do Fardo |
| **Nível** |  |
| **Usado** | Sim |
| **Obrigatório** | Não |
| **Browse** | Sim |
| **Opções** |  |
| **When** |  |
| **Relação** |  |
| **Val. Sistema** |  |
| **Help** | Peso de Chegada do fardo no destino |

* Tabela N91 - Contêineres da IE:

|  |  |
| --- | --- |
| **Campo** | *N91\_FILIAL* |
| **Tipo** | *C* |
| **Tamanho** | *2* |
| **Decimal** | *0* |
| **Formato** | *@!* |
| **Título** | *Filial* |
| **Descrição** | *Filial* |
| **Nível** | *(X3\_NÍVEL)* |
| **Usado** | *Não* |
| **Obrigatório** | *Não* |
| **Browse** | *Não* |
| **Opções** | *(X3\_CBOX)* |
| **When** | *(X3\_WHEN)* |
| **C. Padrão SXB** | *(X3\_F3)* |
| **Val. Sistema** | *(X3\_VALID)* |
| **Help** | *Filial do Sistema* |

|  |  |
| --- | --- |
| **Campo** | *N91\_DESINE* |
| **Tipo** | *C* |
| **Tamanho** | *30* |
| **Decimal** | *0* |
| **Formato** | *@!* |
| **Título** | *Instr. Emb.* |
| **Descrição** | *Instrução de Embarque* |
| **Nível** | *(X3\_NÍVEL)* |
| **Usado** | *Sim* |
| **Obrigatório** | *Não* |
| **Browse** | Sim |
| **Opções** | *(X3\_CBOX)* |
| **When** | *(X3\_WHEN)* |
| **C. Padrão SXB** | *N7Q1* |
| **Val. Sistema** | *ExistCpo("N7Q")* |
| **Help** | *Descrição da Instrução de Embarque* |

|  |  |
| --- | --- |
| **Campo** | *N91\_CODINE* |
| **Tipo** | *C* |
| **Tamanho** | *30* |
| **Decimal** | *0* |
| **Formato** | *@!* |
| **Título** | *Instr. Emb.* |
| **Descrição** | *Código Instrução Embarque* |
| **Nível** | *(X3\_NÍVEL)* |
| **Usado** | *Sim* |
| **Obrigatório** | *Sim* |
| **Browse** | *Sim* |
| **Opções** | *(X3\_CBOX)* |
| **When** | *(X3\_WHEN)* |
| **C. Padrão SXB** | *N7Q* |
| **Val. Sistema** | *ExistCpo("N7Q") .And. ValQtCnt()* |
| **Help** | *Código Instrução de embarque.* |

|  |  |
| --- | --- |
| **Campo** | *N91\_CONTNR* |
| **Tipo** | *C* |
| **Tamanho** | *20* |
| **Decimal** | *0* |
| **Formato** | *@!* |
| **Título** | *No.Container* |
| **Descrição** | *Número do Container* |
| **Nível** | *(X3\_NÍVEL)* |
| **Usado** | *Sim* |
| **Obrigatório** | *Sim* |
| **Browse** | *Sim* |
| **Opções** | *(X3\_CBOX)* |
| **When** | *(X3\_WHEN)* |
| **C. Padrão SXB** | *(X3\_F3)* |
| **Val. Sistema** | *(X3\_VALID)* |
| **Help** | *Número do Container.* |

|  |  |
| --- | --- |
| **Campo** | *N91\_LACRE* |
| **Tipo** | *C* |
| **Tamanho** | *15* |
| **Decimal** | *0* |
| **Formato** | *@!* |
| **Título** | *Lacre* |
| **Descrição** | *Lacre* |
| **Nível** | *(X3\_NÍVEL)* |
| **Usado** | *Sim* |
| **Obrigatório** | *Sim* |
| **Browse** | *Sim* |
| **Opções** | *(X3\_CBOX)* |
| **When** | *(X3\_WHEN)* |
| **C. Padrão SXB** | *(X3\_F3)* |
| **Val. Sistema** | *(X3\_VALID)* |
| **Help** | *Código do Lacre do Container.* |

|  |  |
| --- | --- |
| **Campo** | *N91\_TARA* |
| **Tipo** | *N* |
| **Tamanho** | *10* |
| **Decimal** | *2* |
| **Formato** | *@E 9,999,999.99* |
| **Título** | *Tara Kg.* |
| **Descrição** | *Tara Kg.* |
| **Nível** | *(X3\_NÍVEL)* |
| **Usado** | *Sim* |
| **Obrigatório** | *Não* |
| **Browse** | *Sim* |
| **Opções** | *(X3\_CBOX)* |
| **When** | *(X3\_WHEN)* |
| **C. Padrão SXB** | *(X3\_F3)* |
| **Val. Sistema** | *(X3\_VALID)* |
| **Help** | *Tara do Container.* |

|  |  |
| --- | --- |
| **Campo** | *N91\_STATUS* |
| **Tipo** | *C* |
| **Tamanho** | *1* |
| **Decimal** | *0* |
| **Formato** | *@!* |
| **Título** | *Status* |
| **Descrição** | *Status do CNT* |
| **Nível** | *(X3\_NÍVEL)* |
| **Usado** | *Sim* |
| **Obrigatório** | *Não* |
| **Browse** | *Sim* |
| **Opções** | *1=Disponível;2=Em Estufagem;3=Estufado;4=Em Certificação;5=Certificado* |
| **When** | *(X3\_WHEN)* |
| **C. Padrão SXB** | *(X3\_F3)* |
| **Val. Sistema** | *Pertence('12345') .and. OGA730FST()* |
| **Help** | *Status do Container.* |

|  |  |
| --- | --- |
| **Campo** | *N91\_TIPCON* |
| **Tipo** | *C* |
| **Tamanho** | *0* |
| **Decimal** | *0* |
| **Formato** | *@!* |
| **Título** | *Tp.Container* |
| **Descrição** | *Tipo de Container* |
| **Nível** | *(X3\_NÍVEL)* |
| **Usado** | *Sim* |
| **Obrigatório** | *Não* |
| **Browse** | *Sim* |
| **Opções** | *(X3\_CBOX)* |
| **When** | *(X3\_WHEN)* |
| **C. Padrão SXB** | *C3* |
| **Val. Sistema** | *ExistCpo('SX5','C3'+M->N91\_TIPCON)* |
| **Help** | *Tipo do Container.* |

|  |  |
| --- | --- |
| **Campo** | *N91\_VM\_OBS* |
| **Tipo** | *M* |
| **Tamanho** | *60* |
| **Decimal** | *0* |
| **Formato** | *@!* |
| **Título** | *Observação* |
| **Descrição** | *Observação* |
| **Nível** | *(X3\_NÍVEL)* |
| **Usado** | *Sim* |
| **Obrigatório** | *Não* |
| **Browse** | *Sim* |
| **Opções** | *(X3\_CBOX)* |
| **When** | *(X3\_WHEN)* |
| **C. Padrão SXB** | *(X3\_F3)* |
| **Val. Sistema** | *(X3\_VALID)* |
| **Help** | *Observação.* |

|  |  |
| --- | --- |
| **Campo** | *N91\_DTRETI* |
| **Tipo** | *D* |
| **Tamanho** | *8* |
| **Decimal** | *0* |
| **Formato** | *@!* |
| **Título** | *Dt.Retirada* |
| **Descrição** | *Data de Retirada* |
| **Nível** | *(X3\_NÍVEL)* |
| **Usado** | *Sim* |
| **Obrigatório** | *Não* |
| **Browse** | *Sim* |
| **Opções** | *(X3\_CBOX)* |
| **When** | *(X3\_WHEN)* |
| **C. Padrão SXB** | *(X3\_F3)* |
| **Val. Sistema** | *(X3\_VALID)* |
| **Help** | *Data de Retirada.* |

|  |  |
| --- | --- |
| **Campo** | *N91\_DTPREV* |
| **Tipo** | *D* |
| **Tamanho** | *8* |
| **Decimal** | *0* |
| **Formato** | *@!* |
| **Título** | *Dt.Prev.Devo* |
| **Descrição** | *Dt prevista devolução* |
| **Nível** | *(X3\_NÍVEL)* |
| **Usado** | *Sim* |
| **Obrigatório** | *Não* |
| **Browse** | *Sim* |
| **Opções** | *(X3\_CBOX)* |
| **When** | *(X3\_WHEN)* |
| **C. Padrão SXB** | *(X3\_F3)* |
| **Val. Sistema** | *(X3\_VALID)* |
| **Help** | *Data prevista para devolução* |

|  |  |
| --- | --- |
| **Campo** | *N91\_DTDEVO* |
| **Tipo** | *D* |
| **Tamanho** | *8* |
| **Decimal** | *0* |
| **Formato** | *@!* |
| **Título** | *Dt.Devolucao* |
| **Descrição** | *Data de devolução* |
| **Nível** | *(X3\_NÍVEL)* |
| **Usado** | *Sim* |
| **Obrigatório** | *Não* |
| **Browse** | *Sim* |
| **Opções** | *(X3\_CBOX)* |
| **When** | *(X3\_WHEN)* |
| **C. Padrão SXB** | *(X3\_F3)* |
| **Val. Sistema** | *(X3\_VALID)* |
| **Help** | *Data de devolução.* |

|  |  |
| --- | --- |
| **Campo** | *N91\_CSIRIN* |
| **Tipo** | *C* |
| **Tamanho** | *6* |
| **Decimal** | *0* |
| **Formato** | *@!* |
| **Título** | *Cod.Com.Rota* |
| **Descrição** | *Cod.Memo Coment. Rota* |
| **Nível** | *(X3\_NÍVEL)* |
| **Usado** | *Sim* |
| **Obrigatório** | *Não* |
| **Browse** | *Sim* |
| **Opções** | *(X3\_CBOX)* |
| **When** | *(X3\_WHEN)* |
| **C. Padrão SXB** | *(X3\_F3)* |
| **Val. Sistema** | *(X3\_VALID)* |
| **Help** | *Cod.Memo Coment. Rota.* |

|  |  |
| --- | --- |
| **Campo** | *N91\_INFOSI* |
| **Tipo** | *C* |
| **Tamanho** | *1* |
| **Decimal** | *0* |
| **Formato** | *@!* |
| **Título** | *Info. SI?* |
| **Descrição** | *Origem de Info. para SI?* |
| **Nível** | *(X3\_NÍVEL)* |
| **Usado** | *Sim* |
| **Obrigatório** | *Não* |
| **Browse** | *Sim* |
| **Opções** | *1=Sim; 2=Não* |
| **When** | *(X3\_WHEN)* |
| **C. Padrão SXB** | *(X3\_F3)* |
| **Val. Sistema** | *Pertence('12')* |
| **Help** | *Origem de Info. para SI?* |

|  |  |
| --- | --- |
| **Campo** | *N91\_QTDBL* |
| **Tipo** | *N* |
| **Tamanho** | *2* |
| **Decimal** | *0* |
| **Formato** | *99* |
| **Título** | *Quant.  BL* |
| **Descrição** | *Quantidade de B/L* |
| **Nível** | *(X3\_NÍVEL)* |
| **Usado** | *Sim* |
| **Obrigatório** | *Não* |
| **Browse** | *Sim* |
| **Opções** | *(X3\_CBOX)* |
| **When** | *(X3\_WHEN)* |
| **C. Padrão SXB** | *(X3\_F3)* |
| **Val. Sistema** | *Positivo()* |
| **Help** | *Quantidade de B/L* |

|  |  |
| --- | --- |
| **Campo** | *N91\_QTDBLC* |
| **Tipo** | *N* |
| **Tamanho** | *2* |
| **Decimal** | *0* |
| **Formato** | *99* |
| **Título** | *Qtd Copia BL* |
| **Descrição** | *Quant. de Copias de B/L* |
| **Nível** | *(X3\_NÍVEL)* |
| **Usado** | *Sim* |
| **Obrigatório** | *Não* |
| **Browse** | *Sim* |
| **Opções** | *(X3\_CBOX)* |
| **When** | *(X3\_WHEN)* |
| **C. Padrão SXB** | *(X3\_F3)* |
| **Val. Sistema** | *Positivo()* |
| **Help** | *Quant. de Copias de B/L* |

|  |  |
| --- | --- |
| **Campo** | *N91\_SEQSI* |
| **Tipo** | *C* |
| **Tamanho** | *3* |
| **Decimal** | *0* |
| **Formato** | @! |
| **Título** | *Seq. SI* |
| **Descrição** | *Sequência SI* |
| **Nível** | *(X3\_NÍVEL)* |
| **Usado** | *Sim* |
| **Obrigatório** | *Não* |
| **Browse** | *Sim* |
| **Opções** | *(X3\_CBOX)* |
| **When** | *(X3\_WHEN)* |
| **C. Padrão SXB** | *(X3\_F3)* |
| **Val. Sistema** | *(X3\_VALID)* |
| **Help** | *Sequência SI* |

|  |  |
| --- | --- |
| **Campo** | *N91\_SICOM* |
| **Tipo** | *M* |
| **Tamanho** | *60* |
| **Decimal** | *0* |
| **Formato** | @! |
| **Título** | *Coment. SI* |
| **Descrição** | *Comentários para SI* |
| **Nível** | *(X3\_NÍVEL)* |
| **Usado** | *Sim* |
| **Obrigatório** | *Não* |
| **Browse** | *Sim* |
| **Opções** | *(X3\_CBOX)* |
| **When** | *(X3\_WHEN)* |
| **C. Padrão SXB** | *(X3\_F3)* |
| **Val. Sistema** | *(X3\_VALID)* |
| **Help** | *Comentários para SI.* |

|  |  |
| --- | --- |
| **Campo** | *N91\_SINUM* |
| **Tipo** | *C* |
| **Tamanho** | *35* |
| **Decimal** | *0* |
| **Formato** | @! |
| **Título** | *Num. SI* |
| **Descrição** | *Número da SI* |
| **Nível** | *(X3\_NÍVEL)* |
| **Usado** | *Sim* |
| **Obrigatório** | *Não* |
| **Browse** | *Sim* |
| **Opções** | *(X3\_CBOX)* |
| **When** | *(X3\_WHEN)* |
| **C. Padrão SXB** | *(X3\_F3)* |
| **Val. Sistema** | *(X3\_VALID)* |
| **Help** | *Número da SI.* |

|  |  |
| --- | --- |
| **Campo** | *N91\_SIRINS* |
| **Tipo** | *M* |
| **Tamanho** | *60* |
| **Decimal** | *0* |
| **Formato** | @! |
| **Título** | *Coment. Rota* |
| **Descrição** | *Coment. Instrução de Rota* |
| **Nível** | *(X3\_NÍVEL)* |
| **Usado** | *Sim* |
| **Obrigatório** | *Não* |
| **Browse** | *Sim* |
| **Opções** | *(X3\_CBOX)* |
| **When** | *(X3\_WHEN)* |
| **C. Padrão SXB** | *(X3\_F3)* |
| **Val. Sistema** | *(X3\_VALID)* |
| **Help** | *Coment. Instrução de Rota.* |

|  |  |
| --- | --- |
| **Campo** | *N91\_TIPOBL* |
| **Tipo** | *C* |
| **Tamanho** | *1* |
| **Decimal** | *0* |
| **Formato** | @! |
| **Título** | *Tipo do B/L* |
| **Descrição** | *Tipo do B/L* |
| **Nível** | *(X3\_NÍVEL)* |
| **Usado** | *Sim* |
| **Obrigatório** | *Não* |
| **Browse** | *Sim* |
| **Opções** | *1=BillOfLanding; 2=SeaWayBill* |
| **When** | *(X3\_WHEN)* |
| **C. Padrão SXB** | *(X3\_F3)* |
| **Val. Sistema** | *Pertence('12')* |
| **Help** | *Tipo do Bl.* |

|  |  |
| --- | --- |
| **Campo** | *N91\_BLNUM* |
| **Tipo** | *C* |
| **Tamanho** | *25* |
| **Decimal** | *0* |
| **Formato** | @! |
| **Título** | *Num. B/L* |
| **Descrição** | *Número do B/L* |
| **Nível** | *(X3\_NÍVEL)* |
| **Usado** | *Sim* |
| **Obrigatório** | *Não* |
| **Browse** | *Sim* |
| **Opções** | *(X3\_CBOX)* |
| **When** | *(X3\_WHEN)* |
| **C. Padrão SXB** | *(X3\_F3)* |
| **Val. Sistema** | *(X3\_VALID)* |
| **Help** | *Número do B/L.* |

|  |  |
| --- | --- |
| **Campo** | *N91\_CUBAGE* |
| **Tipo** | *N* |
| **Tamanho** | *16* |
| **Decimal** | *3* |
| **Formato** | @E 999,999,999,999.999 |
| **Título** | *Cubagem (m3)* |
| **Descrição** | *Cubagem (m3)* |
| **Nível** | *(X3\_NÍVEL)* |
| **Usado** | *Sim* |
| **Obrigatório** | *Não* |
| **Browse** | *Sim* |
| **Opções** | *(X3\_CBOX)* |
| **When** | *(X3\_WHEN)* |
| **C. Padrão SXB** | *(X3\_F3)* |
| **Val. Sistema** | *(X3\_VALID)* |
| **Help** | *Cubagem (m3)* |

|  |  |
| --- | --- |
| **Campo** | *N91\_DTCERT* |
| **Tipo** | *D* |
| **Tamanho** | *8* |
| **Decimal** | *0* |
| **Formato** |  |
| **Título** | *Dt Certifica* |
| **Descrição** | *Data da Certificação* |
| **Nível** | *(X3\_NÍVEL)* |
| **Usado** | *Sim* |
| **Obrigatório** | *Não* |
| **Browse** | *Sim* |
| **Opções** | *(X3\_CBOX)* |
| **When** | *(X3\_WHEN)* |
| **C. Padrão SXB** | *(X3\_F3)* |
| **Val. Sistema** | *(X3\_VALID)* |
| **Help** | *Data da Certificação do Container* |

|  |  |
| --- | --- |
| **Campo** | *N91\_QTDANT* |
| **Tipo** | *N* |
| **Tamanho** | *16* |
| **Decimal** | *4* |
| **Formato** | *@E 99,999,999,999.9999* |
| **Título** | *Qtd. Antecip* |
| **Descrição** | *Qtd. Antecipada* |
| **Nível** | *(X3\_NÍVEL)* |
| **Usado** | *Sim* |
| **Obrigatório** | *Não* |
| **Browse** | Sim |
| **Opções** | *(X3\_CBOX)* |
| **When** | *(X3\_WHEN)* |
| **C. Padrão SXB** | *(X3\_F3)* |
| **Val. Sistema** | *(X3\_VALID)* |
| **Help** | *Quantidade Antecipada.* |

|  |  |
| --- | --- |
| **Campo** | *N91\_STUFIN* |
| **Tipo** | *C* |
| **Tamanho** | *1* |
| **Decimal** | *0* |
| **Formato** | *@!* |
| **Título** | *Stuf. Fin.* |
| **Descrição** | *Estufagem Finalizada?* |
| **Nível** | *(X3\_NÍVEL)* |
| **Usado** | *Sim* |
| **Obrigatório** | *Não* |
| **Browse** | *Sim* |
| **Opções** | *1=Sim;2=Não* |
| **When** | *M->N91\_STATUS $ "2|3|4"* |
| **C. Padrão SXB** | *(X3\_F3)* |
| **Val. Sistema** | *Pertence('12') .and. OGA730FST()* |
| **Help** | *Status do Container.* |

* Tabela **N98** - Processos de Aprovação:

|  |  |
| --- | --- |
| **Campo** | *N98\_FILIAL* |
| **Tipo** | *C* |
| **Tamanho** | *02* |
| **Decimal** | *0* |
| **Formato** | @! |
| **Título** | *Filial* |
| **Descrição** | *Filial do Sistema* |
| **Nível** | *(X3\_NÍVEL)* |
| **Usado** | *Sim* |
| **Obrigatório** | *Não* |
| **Browse** | *Não* |
| **Opções** | *(X3\_CBOX)* |
| **When** | *(X3\_WHEN)* |
| **C. Padrão SXB** | *(X3\_F3)* |
| **Val. Sistema** | *(X3\_VALID)* |
| **Help** | *Filial do Sistema* |

|  |  |
| --- | --- |
| **Campo** | *N98\_CODPRO* |
| **Tipo** | *C* |
| **Tamanho** | *06* |
| **Decimal** | *0* |
| **Formato** | @! |
| **Título** | *Cód. Process* |
| **Descrição** | *Cód. Processo Aprovação* |
| **Nível** | *(X3\_NÍVEL)* |
| **Usado** | *Sim* |
| **Obrigatório** | *Sim* |
| **Browse** | *Sim* |
| **Opções** | *(X3\_CBOX)* |
| **When** | *(X3\_WHEN)* |
| **C. Padrão SXB** | *(X3\_F3)* |
| **Val. Sistema** | *(X3\_VALID)* |
| **Help** | *Código do Processo de Aprovação.* |

|  |  |
| --- | --- |
| **Campo** | *N98\_DESPRO* |
| **Tipo** | *C* |
| **Tamanho** | *30* |
| **Decimal** | *0* |
| **Formato** | @! |
| **Título** | *Desc. Proces* |
| **Descrição** | *Desc. Processo Aprovação* |
| **Nível** | *(X3\_NÍVEL)* |
| **Usado** | *Sim* |
| **Obrigatório** | *Sim* |
| **Browse** | *Sim* |
| **Opções** | *(X3\_CBOX)* |
| **When** | *(X3\_WHEN)* |
| **C. Padrão SXB** | *(X3\_F3)* |
| **Val. Sistema** | *(X3\_VALID)* |
| **Help** | *Descrição do Processo de Aprovação.* |

* Tabela **N99** - Aprovadores do Processo:

|  |  |
| --- | --- |
| **Campo** | *N99\_FILIAL* |
| **Tipo** | *C* |
| **Tamanho** | *02* |
| **Decimal** | *0* |
| **Formato** | @! |
| **Título** | *Filial* |
| **Descrição** | *Filial do Sistema* |
| **Nível** | *(X3\_NÍVEL)* |
| **Usado** | *Sim* |
| **Obrigatório** | *Sim* |
| **Browse** | *Sim* |
| **Opções** | *(X3\_CBOX)* |
| **When** | *(X3\_WHEN)* |
| **C. Padrão SXB** | *(X3\_F3)* |
| **Val. Sistema** | *(X3\_VALID)* |
| **Help** | *Filial do Sistema.* |

|  |  |
| --- | --- |
| **Campo** | *N99\_CODPRO* |
| **Tipo** | *C* |
| **Tamanho** | *06* |
| **Decimal** | *0* |
| **Formato** | @! |
| **Título** | *Cod. Process* |
| **Descrição** | *Cód. Processo Aprovação* |
| **Nível** | *(X3\_NÍVEL)* |
| **Usado** | *Sim* |
| **Obrigatório** | *Sim* |
| **Browse** | *Sim* |
| **Opções** | *(X3\_CBOX)* |
| **When** | *(X3\_WHEN)* |
| **C. Padrão SXB** | *(X3\_F3)* |
| **Val. Sistema** | *ExistCpo('N98')* |
| **Help** | *Código do Processo de Aprovação.* |

|  |  |
| --- | --- |
| **Campo** | *N99\_CODUSU* |
| **Tipo** | *C* |
| **Tamanho** | *06* |
| **Decimal** | *0* |
| **Formato** | @! |
| **Título** | *Cod. Usuário* |
| **Descrição** | *Codigo do Usuário* |
| **Nível** | *(X3\_NÍVEL)* |
| **Usado** | *Sim* |
| **Obrigatório** | *Não* |
| **Browse** | *Sim* |
| **Opções** | *(X3\_CBOX)* |
| **When** | *(X3\_WHEN)* |
| **C. Padrão SXB** | *USR* |
| **Val. Sistema** | *UsrExist (M→N99\_CODUSU) .OR. Vazio()* |
| **Help** | *Codigo do Usuário* |

|  |  |
| --- | --- |
| **Campo** | *N99\_NOMUSU* |
| **Tipo** | *C* |
| **Tamanho** | *50* |
| **Decimal** | *0* |
| **Formato** | @! |
| **Título** | *Nom. Usuário* |
| **Descrição** | *Nome do Usuário* |
| **Nível** | *(X3\_NÍVEL)* |
| **Usado** | *Sim* |
| **Obrigatório** | *Não* |
| **Browse** | *Sim* |
| **Opções** | *(X3\_CBOX)* |
| **When** | *(X3\_WHEN)* |
| **C. Padrão SXB** | *(X3\_F3)* |
| **Val. Sistema** | *(X3\_VALID)* |
| **Help** | *Nome do Usuário.* |

|  |  |
| --- | --- |
| **Campo** | *N99\_GRPUSU* |
| **Tipo** | *C* |
| **Tamanho** | *50* |
| **Decimal** | *0* |
| **Formato** | @! |
| **Título** | *Grup.Usuário* |
| **Descrição** | *Grupo de Usuários* |
| **Nível** | *(X3\_NÍVEL)* |
| **Usado** | *Sim* |
| **Obrigatório** | *Não* |
| **Browse** | *Sim* |
| **Opções** | *(X3\_CBOX)* |
| **When** | *(X3\_WHEN)* |
| **C. Padrão SXB** | *AGRGRU* |
| **Val. Sistema** | *(X3\_VALID)* |
| **Help** | *Grupo de Usuários.* |

|  |  |
| --- | --- |
| **Campo** | *N99\_DGRUSU* |
| **Tipo** | *C* |
| **Tamanho** | *30* |
| **Decimal** | *0* |
| **Formato** | @! |
| **Título** | *Desc.Gr.Usua* |
| **Descrição** | *Desc. Gru. Usuários* |
| **Nível** | *(X3\_NÍVEL)* |
| **Usado** | *Sim* |
| **Obrigatório** | *Não* |
| **Browse** | *Sim* |
| **Opções** | *(X3\_CBOX)* |
| **When** | *(X3\_WHEN)* |
| **C. Padrão SXB** | *(X3\_F3)* |
| **Val. Sistema** | *(X3\_VALID)* |
| **Help** | *Descrição do Grupo de Usuários* |

|  |  |
| --- | --- |
| **Campo** | *N99\_COPROD* |
| **Tipo** | *C* |
| **Tamanho** | *15* |
| **Decimal** | *0* |
| **Formato** | @! |
| **Título** | *Cód. Produto* |
| **Descrição** | *Código do Produto* |
| **Nível** | *(X3\_NÍVEL)* |
| **Usado** | *Sim* |
| **Obrigatório** | *Não* |
| **Browse** | *Sim* |
| **Opções** | *(X3\_CBOX)* |
| **When** | *(X3\_WHEN)* |
| **C. Padrão SXB** | *SB1* |
| **Val. Sistema** | *ExistCpo('SB1') .And. OGA760ValUser()* |
| **Help** | *Código do Produto.* |

|  |  |
| --- | --- |
| **Campo** | *N99\_DEPROD* |
| **Tipo** | *C* |
| **Tamanho** | *30* |
| **Decimal** | *0* |
| **Formato** | @! |
| **Título** | *Desc.Produto* |
| **Descrição** | *Descição do Produto* |
| **Nível** | *(X3\_NÍVEL)* |
| **Usado** | *Sim* |
| **Obrigatório** | *Não* |
| **Browse** | *Sim* |
| **Opções** | *(X3\_CBOX)* |
| **When** | *(X3\_WHEN)* |
| **C. Padrão SXB** | *(X3\_F3)* |
| **Val. Sistema** | *(X3\_VALID)* |
| **Help** | *Descição do Produto.* |

|  |  |
| --- | --- |
| **Campo** | *N99\_GRPROD* |
| **Tipo** | *C* |
| **Tamanho** | *04* |
| **Decimal** | *0* |
| **Formato** | @! |
| **Título** | *Grp. Produto* |
| **Descrição** | *Grupo de Produto* |
| **Nível** | *(X3\_NÍVEL)* |
| **Usado** | *Sim* |
| **Obrigatório** | *Não* |
| **Browse** | *Sim* |
| **Opções** | *(X3\_CBOX)* |
| **When** | *(X3\_WHEN)* |
| **C. Padrão SXB** | *SBM* |
| **Val. Sistema** | ExistCPO("SBM") .And. OGA760ValUser() |
| **Help** | *Grupo de Produto.* |

|  |  |
| --- | --- |
| **Campo** | *N99\_DGRPRO* |
| **Tipo** | *C* |
| **Tamanho** | *30* |
| **Decimal** | *0* |
| **Formato** | @! |
| **Título** | *Desc.Gr.Prod* |
| **Descrição** | *Desc. Grupo Produto* |
| **Nível** | *(X3\_NÍVEL)* |
| **Usado** | *Sim* |
| **Obrigatório** | *Não* |
| **Browse** | *Sim* |
| **Opções** | *(X3\_CBOX)* |
| **When** | *(X3\_WHEN)* |
| **C. Padrão SXB** | *SBM* |
| **Val. Sistema** | *(X3\_VALID)* |
| **Help** | *Descrição do Grupo de Produto.* |

|  |  |
| --- | --- |
| **Campo** | *N99\_PERINI* |
| **Tipo** | *N* |
| **Tamanho** | *07* |
| **Decimal** | *2* |
| **Formato** | *@E 99.99* |
| **Título** | *Per. Inicial* |
| **Descrição** | *% inicial de Aprovação* |
| **Nível** | *(X3\_NÍVEL)* |
| **Usado** | *Sim* |
| **Obrigatório** | *Não* |
| **Browse** | *Sim* |
| **Opções** | *(X3\_CBOX)* |
| **When** | *(X3\_WHEN)* |
| **C. Padrão SXB** | *(X3\_F3)* |
| **Val. Sistema** | *(X3\_VALID)* |
| **Help** | *Percentual Inicial de Aprovação.* |

|  |  |
| --- | --- |
| **Campo** | *N99\_PERFIN* |
| **Tipo** | *N* |
| **Tamanho** | *07* |
| **Decimal** | *2* |
| **Formato** | *@E 99.99* |
| **Título** | *Per. Final* |
| **Descrição** | *% Final de Aprovação* |
| **Nível** | *(X3\_NÍVEL)* |
| **Usado** | *Sim* |
| **Obrigatório** | *Não* |
| **Browse** | *Sim* |
| **Opções** | *(X3\_CBOX)* |
| **When** | *(X3\_WHEN)* |
| **C. Padrão SXB** | *(X3\_F3)* |
| **Val. Sistema** | *(X3\_VALID)* |
| **Help** | *Percentual Final de Aprovação.* |

* Tabela **NJJ** - Romaneio C/ Pesagem:

|  |  |
| --- | --- |
| **Campo** | *NJJ\_ROMSAI* |
| **Tipo** | *C* |
| **Tamanho** | *30* |
| **Decimal** | *0* |
| **Formato** | *@!* |
| **Título** | *Instr. Emb.* |
| **Descrição** | Código Instrução Embarque |
| **Nível** | *(X3\_NÍVEL)* |
| **Usado** | *Sim* |
| **Obrigatório** | *Não* |
| **Browse** | *Não* |
| **Opções** | *(X3\_CBOX)* |
| **When** | *(X3\_WHEN)* |
| **C. Padrão SXB** | NJJN7Q |
| **Val. Sistema** | *Vazio() .or. ExistCpo("N7Q")* |
| **Help** | *Código da Instrução de Embarque* |

* Tabela DXI - Fardos:

|  |  |
| --- | --- |
| **Campo** | *DXI\_ROMFLO* |
| **Tipo** | *C* |
| **Tamanho** | *10* |
| **Decimal** | *0* |
| **Formato** | *@!* |
| **Título** | Rom. Lote |
| **Descrição** | Romaneio Formação de Lote |
| **Nível** | *(X3\_NÍVEL)* |
| **Usado** | *Sim* |
| **Obrigatório** | *Não* |
| **Browse** | *Não* |
| **Opções** | *(X3\_CBOX)* |
| **When** | *(X3\_WHEN)* |
| **C. Padrão SXB** |  |
| **Val. Sistema** |  |
| **Help** | *Romaneio Formação de Lote* |

* Tabela **N7Q** - Instrução de Embarque:

|  |  |
| --- | --- |
| **Campo** | *N7Q\_NFDEVOL* |
| **Tipo** | *C* |
| **Tamanho** | *1* |
| **Decimal** | *0* |
| **Formato** | *9* |
| **Título** | NF Devol.? |
| **Descrição** | NF de Devolução |
| **Nível** | *1* |
| **Usado** | *Sim* |
| **Obrigatório** | *Não* |
| **Browse** | *Sim* |
| **Opções** | *1=Sim;2=Nao* |
| **When** | *(X3\_WHEN)* |
| **C. Padrão SXB** |  |
| **Val. Sistema** | *Pertence("12")* |
| **Help** | *NF de Devolução de Expotação:*  *1- Sim*  *2- Não* |

* Tabela **NKM** - Movimentações

|  |  |
| --- | --- |
| **Campo** | *NKM\_CODINE* |
| **Tipo** | *C* |
| **Tamanho** | *30* |
| **Decimal** | *0* |
| **Formato** | *9* |
| **Título** | Instr. Emba |
| **Descrição** | Codigo Instr Embarque |
| **Nível** | *1* |
| **Usado** | *Sim* |
| **Obrigatório** | *Não* |
| **Browse** | *Sim* |
| **Help** | *Código da Instrução de Embarque* |

**5.** Realize a **Criação de** **Consulta Padrão** no arquivo **SXB – Consulta Padrão;**

Pesquisa **N7Q**:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Alias** | ***Tipo*** | **Sequência** | **Coluna** | **Descrição** | **Contém** |
| *N7Q* | *C* | *01* | *N7Q\_CODINE+N7Q\_DESINE* | *Código* | *(XB\_CONTEM)* |
| *AGRGRU* | *C* | *01* | *Id+Nome* | *Id+Nome* | *(XB\_CONTEM)* |

**6.** Faça a **Criação de** **Índices** no arquivo **SIX – Índices;**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Índice** | ***Ordem*** | **Chave** | **Descrição** | **Proprietário** |
| N91 | 01 | *N91\_FILIAL+N91\_CODINE+N91\_CONTNR* | *Instr. Emb. + No.Container* | S |
| N98 | *01* | *N98\_FILIAL+N98\_CODPRO* | *Cod. Process* | S |
| N99 | *01* | *N99\_FILIAL+N99\_CODPRO+N99\_CODUSU+N99\_GRPUSU+N99\_COPROD+N99\_GRPROD* | *Cod. Process + Cod. Usuário + Grupo Usuário + Cod. Produto + Grupo Produto* | S |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Índice** | ***Ordem*** | **Chave** | **Descrição** | **Proprietário** |
| DXI | 09 | *DXI\_FILIAL+DXI\_ROMFLO+DXI\_ITROMS* | *Romaneio Formação de Lote. + Itens do Romaneio* | S |

**7.** Faça a **Criação ou Alteração** **de** **Parâmetros** no arquivo **SX6 – Parâmetros;**

|  |  |
| --- | --- |
| **Nome da Variável** | *(X6\_VAR)* |
| **Tipo** | *(X6\_TIPO)* |
| **Descrição** | *(X6\_DESCRIC + X6\_DESC1 + X6\_DESC2)* |
| **Valor Padrão** | *(X6\_CONTEUD)* |

**8.** Realize a **Criação ou Alteração** (mantenha somente a instrução correspondente) de **Gatilhos** no arquivo **SX7 – Gatilhos.**

Tabela ***BD5 – Contas Médicas***:

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Campo** | ***Sequência*** | **Campo Domínio** | **Tipo** | **Regra** | **Posiciona?** | **Chave** | **Condição** | **Proprietário** |
| *N99\_COPROD* | *001* | *N99\_DEPROD* | *Primário* | *SB1->B1\_DESC* | *Sim* | *xFilial('SB1')+M->N99\_COPROD* | *X7\_CONDIC* | *X7\_PROPRI* |
| *N99\_GRPROD* | *001* | *N99\_DGRPRO* | *Primário* | *SBM->BM\_DESC* | *Sim* | *xFilial('SBM')+M->N99\_GRPROD* | *X7\_CONDIC* | *X7\_PROPRI* |
